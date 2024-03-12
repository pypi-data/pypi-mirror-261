from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.get_session_list_status import GetSessionListStatus
from ...livtypes import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    client_id: Union[Unset, None, str] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, GetSessionListStatus] = UNSET,
    limit: Union[Unset, None, int] = 10,
    offset: Union[Unset, None, int] = 0,
) -> Dict[str, Any]:
    url = "{}/sessions".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["client_id"] = client_id

    params["user_id"] = user_id

    json_status: Union[Unset, None, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value if status else None

    params["status"] = json_status

    params["limit"] = limit

    params["offset"] = offset

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
    *,
    client: Client,
    client_id: Union[Unset, None, str] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, GetSessionListStatus] = UNSET,
    limit: Union[Unset, None, int] = 10,
    offset: Union[Unset, None, int] = 0,
) -> Response[Any]:
    """List all sessions

     Returns a list of all sessions.
    The sessions are returned sorted by creation date, with the newest sessions appearing first.

    Args:
        client_id (Union[Unset, None, str]):
        user_id (Union[Unset, None, str]):
        status (Union[Unset, None, GetSessionListStatus]):
        limit (Union[Unset, None, float]):  Default: 10.0.
        offset (Union[Unset, None, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        client_id=client_id,
        user_id=user_id,
        status=status,
        limit=limit,
        offset=offset,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Client,
    client_id: Union[Unset, None, str] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, GetSessionListStatus] = UNSET,
    limit: Union[Unset, None, int] = 10,
    offset: Union[Unset, None, int] = 0,
) -> Response[Any]:
    """List all sessions

     Returns a list of all sessions.
    The sessions are returned sorted by creation date, with the newest sessions appearing first.

    Args:
        client_id (Union[Unset, None, str]):
        user_id (Union[Unset, None, str]):
        status (Union[Unset, None, GetSessionListStatus]):
        limit (Union[Unset, None, float]):  Default: 10.0.
        offset (Union[Unset, None, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        client_id=client_id,
        user_id=user_id,
        status=status,
        limit=limit,
        offset=offset,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
