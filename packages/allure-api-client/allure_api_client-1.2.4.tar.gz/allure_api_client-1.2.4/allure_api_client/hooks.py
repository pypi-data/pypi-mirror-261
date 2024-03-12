import allure
from httpx import Response, Request


def request_hook(request: Request) -> None:
    """
    This hook function is designed to be used with the httpx.Client event hooks for requests.
    It captures and logs the outgoing request details, including the method, URL, headers, and body.
    The request is formatted as a cURL command and attached to the Allure test report for easier debugging and reproduction.

    Args:
        request (Request): The httpx.Request object representing the outgoing HTTP request.

    Example:
        # To use this hook, attach it to a httpx.Client instance's event_hooks for requests
        client = httpx.Client(event_hooks={'request': [request_hook]})
    """
    with allure.step(title=f'Request: [{request.method}] --> {request.url}'):
        headers = []
        for header in request.headers:
            headers.append(f'-H "{header}: {request.headers[header]}"')
        body = '' if request.content == b'' \
            else f" --data '{request.content if isinstance(request.content, str) else request.content.decode()}'"
        curl = f"curl --location '{request.url}' {' '.join(headers)}{body}"
        print(curl)
        allure.attach(curl, 'request', allure.attachment_type.TEXT)
    return


def response_hook(response: Response) -> None:
    """
    This hook function is designed to be used with the httpx.Client event hooks for responses.
    It captures and logs the details of the incoming response, including the request method, request URL, status code,
    and response content. The response details are attached to the Allure test report for documentation and analysis.

    Args:
        response (Response): The httpx.Response object representing the incoming HTTP response.

    Example:
        # To use this hook, attach it to a httpx.Client instance's event_hooks for responses
        client = httpx.Client(event_hooks={'response': [response_hook]})
    """
    with allure.step(title=f'Response: [{response.request.method}] --> {response.request.url}'):
        response.read()
        resp_message = f'status_code: {response.status_code} \n  Content: \n {response.text}'
        print(resp_message)
        allure.attach(resp_message, 'response', allure.attachment_type.TEXT)
    return
