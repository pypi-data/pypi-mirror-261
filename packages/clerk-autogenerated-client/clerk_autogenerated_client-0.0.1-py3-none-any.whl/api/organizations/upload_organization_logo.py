from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.upload_organization_logo_multipart_data import UploadOrganizationLogoMultipartData
from ...livtypes import Response


def _get_kwargs(
    organization_id: str,
    *,
    client: Client,
    multipart_data: UploadOrganizationLogoMultipartData,
) -> Dict[str, Any]:
    url = "{}/organizations/{organization_id}/logo".format(client.base_url, organization_id=organization_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "files": multipart_multipart_data,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return None
    if response.status_code == HTTPStatus.FORBIDDEN:
        return None
    if response.status_code == HTTPStatus.NOT_FOUND:
        return None
    if response.status_code == HTTPStatus.REQUEST_ENTITY_TOO_LARGE:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    *,
    client: Client,
    multipart_data: UploadOrganizationLogoMultipartData,
) -> Response[Any]:
    r"""Upload a logo for the organization

     Set or replace an organization's logo, by uploading an image file.
    This endpoint uses the `multipart/form-data` request content type and accepts a file of image type.
    The file size cannot exceed 10MB.
    Only the following file content types are supported: `image/jpeg`, `image/png`, `image/gif`,
    `image/webp`, `image/x-icon`, `image/vnd.microsoft.icon`.
    Only \"admin\" members can upload an organization logo.

    Args:
        organization_id (str):
        multipart_data (UploadOrganizationLogoMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        client=client,
        multipart_data=multipart_data,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    organization_id: str,
    *,
    client: Client,
    multipart_data: UploadOrganizationLogoMultipartData,
) -> Response[Any]:
    r"""Upload a logo for the organization

     Set or replace an organization's logo, by uploading an image file.
    This endpoint uses the `multipart/form-data` request content type and accepts a file of image type.
    The file size cannot exceed 10MB.
    Only the following file content types are supported: `image/jpeg`, `image/png`, `image/gif`,
    `image/webp`, `image/x-icon`, `image/vnd.microsoft.icon`.
    Only \"admin\" members can upload an organization logo.

    Args:
        organization_id (str):
        multipart_data (UploadOrganizationLogoMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        client=client,
        multipart_data=multipart_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
