from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.create_organization_json_body import CreateOrganizationJsonBody
from ...livtypes import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: CreateOrganizationJsonBody,
) -> Dict[str, Any]:
    url = "{}/organizations".format(client.base_url)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return None
    if response.status_code == HTTPStatus.FORBIDDEN:
        return None
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
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
    *,
    client: Client,
    json_body: CreateOrganizationJsonBody,
) -> Response[Any]:
    r"""Create an organization

     Creates a new organization with the given name for an instance.
    In order to successfully create an organization you need to provide the ID of the User who will
    become the organization administrator.
    You can specify an optional slug for the new organization.
    If provided, the organization slug can contain only lowercase alphanumeric characters (letters and
    digits) and the dash \"-\".
    Organization slugs must be unique for the instance.
    You can provide additional metadata for the organization and set any custom attribute you want.
    Organizations support private and public metadata.
    Private metadata can only be accessed from the Backend API.
    Public metadata can be accessed from the Backend API, and are read-only from the Frontend API.

    Args:
        json_body (CreateOrganizationJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Client,
    json_body: CreateOrganizationJsonBody,
) -> Response[Any]:
    r"""Create an organization

     Creates a new organization with the given name for an instance.
    In order to successfully create an organization you need to provide the ID of the User who will
    become the organization administrator.
    You can specify an optional slug for the new organization.
    If provided, the organization slug can contain only lowercase alphanumeric characters (letters and
    digits) and the dash \"-\".
    Organization slugs must be unique for the instance.
    You can provide additional metadata for the organization and set any custom attribute you want.
    Organizations support private and public metadata.
    Private metadata can only be accessed from the Backend API.
    Public metadata can be accessed from the Backend API, and are read-only from the Frontend API.

    Args:
        json_body (CreateOrganizationJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
