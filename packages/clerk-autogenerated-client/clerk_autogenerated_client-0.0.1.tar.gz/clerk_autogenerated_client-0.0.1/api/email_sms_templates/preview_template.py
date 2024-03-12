from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.preview_template_json_body import PreviewTemplateJsonBody
from ...models.preview_template_response_200 import PreviewTemplateResponse200
from ...livtypes import Response


def _get_kwargs(
    template_type: str,
    slug: str,
    *,
    client: Client,
    json_body: PreviewTemplateJsonBody,
) -> Dict[str, Any]:
    url = "{}/templates/{template_type}/{slug}/preview".format(client.base_url, template_type=template_type, slug=slug)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, PreviewTemplateResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PreviewTemplateResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = cast(Any, None)
        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, PreviewTemplateResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    template_type: str,
    slug: str,
    *,
    client: Client,
    json_body: PreviewTemplateJsonBody,
) -> Response[Union[Any, PreviewTemplateResponse200]]:
    """Preview changes to a template

     Returns a preview of a template for a given template_type, slug and body

    Args:
        template_type (str):
        slug (str):
        json_body (PreviewTemplateJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PreviewTemplateResponse200]]
    """

    kwargs = _get_kwargs(
        template_type=template_type,
        slug=slug,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    template_type: str,
    slug: str,
    *,
    client: Client,
    json_body: PreviewTemplateJsonBody,
) -> Optional[Union[Any, PreviewTemplateResponse200]]:
    """Preview changes to a template

     Returns a preview of a template for a given template_type, slug and body

    Args:
        template_type (str):
        slug (str):
        json_body (PreviewTemplateJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PreviewTemplateResponse200]
    """

    return sync_detailed(
        template_type=template_type,
        slug=slug,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    template_type: str,
    slug: str,
    *,
    client: Client,
    json_body: PreviewTemplateJsonBody,
) -> Response[Union[Any, PreviewTemplateResponse200]]:
    """Preview changes to a template

     Returns a preview of a template for a given template_type, slug and body

    Args:
        template_type (str):
        slug (str):
        json_body (PreviewTemplateJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PreviewTemplateResponse200]]
    """

    kwargs = _get_kwargs(
        template_type=template_type,
        slug=slug,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    template_type: str,
    slug: str,
    *,
    client: Client,
    json_body: PreviewTemplateJsonBody,
) -> Optional[Union[Any, PreviewTemplateResponse200]]:
    """Preview changes to a template

     Returns a preview of a template for a given template_type, slug and body

    Args:
        template_type (str):
        slug (str):
        json_body (PreviewTemplateJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PreviewTemplateResponse200]
    """

    return (
        await asyncio_detailed(
            template_type=template_type,
            slug=slug,
            client=client,
            json_body=json_body,
        )
    ).parsed
