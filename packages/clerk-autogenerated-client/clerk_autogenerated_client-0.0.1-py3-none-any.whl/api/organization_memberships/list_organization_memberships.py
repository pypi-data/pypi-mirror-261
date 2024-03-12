from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...livtypes import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    *,
    client: Client,
    limit: Union[Unset, None, int] = 10,
    offset: Union[Unset, None, int] = 0,
    order_by: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/organizations/{organization_id}/memberships".format(client.base_url, organization_id=organization_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["limit"] = limit

    params["offset"] = offset

    params["order_by"] = order_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if response.status_code == HTTPStatus.UNAUTHORIZED:
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
    organization_id: str,
    *,
    client: Client,
    limit: Union[Unset, None, int] = 10,
    offset: Union[Unset, None, int] = 0,
    order_by: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Get a list of all members of an organization

     Retrieves all user memberships for the given organization

    Args:
        organization_id (str):
        limit (Union[Unset, None, float]):  Default: 10.0.
        offset (Union[Unset, None, float]):
        order_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        client=client,
        limit=limit,
        offset=offset,
        order_by=order_by,
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
    limit: Union[Unset, None, int] = 10,
    offset: Union[Unset, None, int] = 0,
    order_by: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Get a list of all members of an organization

     Retrieves all user memberships for the given organization

    Args:
        organization_id (str):
        limit (Union[Unset, None, float]):  Default: 10.0.
        offset (Union[Unset, None, float]):
        order_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        client=client,
        limit=limit,
        offset=offset,
        order_by=order_by,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
