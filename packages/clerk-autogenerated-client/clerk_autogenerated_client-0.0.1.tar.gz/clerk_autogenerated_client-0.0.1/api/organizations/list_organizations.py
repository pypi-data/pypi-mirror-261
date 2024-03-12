from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...livtypes import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    limit: Union[Unset, None, int] = 10,
    offset: Union[Unset, None, int] = 0,
    include_members_count: Union[Unset, None, bool] = UNSET,
    query: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = "-created_at",
) -> Dict[str, Any]:
    url = "{}/organizations".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["limit"] = limit

    params["offset"] = offset

    params["include_members_count"] = include_members_count

    params["query"] = query

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
    limit: Union[Unset, None, int] = 10,
    offset: Union[Unset, None, int] = 0,
    include_members_count: Union[Unset, None, bool] = UNSET,
    query: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = "-created_at",
) -> Response[Any]:
    """Get a list of organizations for an instance

     This request returns the list of organizations for an instance.
    Results can be paginated using the optional `limit` and `offset` query parameters.
    The organizations are ordered by descending creation date.
    Most recent organizations will be returned first.

    Args:
        limit (Union[Unset, None, float]):  Default: 10.0.
        offset (Union[Unset, None, float]):
        include_members_count (Union[Unset, None, bool]):
        query (Union[Unset, None, str]):
        order_by (Union[Unset, None, str]):  Default: '-created_at'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        limit=limit,
        offset=offset,
        include_members_count=include_members_count,
        query=query,
        order_by=order_by,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Client,
    limit: Union[Unset, None, int] = 10,
    offset: Union[Unset, None, int] = 0,
    include_members_count: Union[Unset, None, bool] = UNSET,
    query: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = "-created_at",
) -> Response[Any]:
    """Get a list of organizations for an instance

     This request returns the list of organizations for an instance.
    Results can be paginated using the optional `limit` and `offset` query parameters.
    The organizations are ordered by descending creation date.
    Most recent organizations will be returned first.

    Args:
        limit (Union[Unset, None, float]):  Default: 10.0.
        offset (Union[Unset, None, float]):
        include_members_count (Union[Unset, None, bool]):
        query (Union[Unset, None, str]):
        order_by (Union[Unset, None, str]):  Default: '-created_at'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        limit=limit,
        offset=offset,
        include_members_count=include_members_count,
        query=query,
        order_by=order_by,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
