from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...livtypes import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    email_address: Union[Unset, None, List[str]] = UNSET,
    phone_number: Union[Unset, None, List[str]] = UNSET,
    external_id: Union[Unset, None, List[str]] = UNSET,
    username: Union[Unset, None, List[str]] = UNSET,
    web3_wallet: Union[Unset, None, List[str]] = UNSET,
    user_id: Union[Unset, None, List[str]] = UNSET,
    organization_id: Union[Unset, None, List[str]] = UNSET,
    query: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 10,
    offset: Union[Unset, None, int] = 0,
    order_by: Union[Unset, None, str] = "-created_at",
) -> Dict[str, Any]:
    url = "{}/users".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_email_address: Union[Unset, None, List[str]] = UNSET
    if not isinstance(email_address, Unset):
        if email_address is None:
            json_email_address = None
        else:
            json_email_address = email_address

    params["email_address"] = json_email_address

    json_phone_number: Union[Unset, None, List[str]] = UNSET
    if not isinstance(phone_number, Unset):
        if phone_number is None:
            json_phone_number = None
        else:
            json_phone_number = phone_number

    params["phone_number"] = json_phone_number

    json_external_id: Union[Unset, None, List[str]] = UNSET
    if not isinstance(external_id, Unset):
        if external_id is None:
            json_external_id = None
        else:
            json_external_id = external_id

    params["external_id"] = json_external_id

    json_username: Union[Unset, None, List[str]] = UNSET
    if not isinstance(username, Unset):
        if username is None:
            json_username = None
        else:
            json_username = username

    params["username"] = json_username

    json_web3_wallet: Union[Unset, None, List[str]] = UNSET
    if not isinstance(web3_wallet, Unset):
        if web3_wallet is None:
            json_web3_wallet = None
        else:
            json_web3_wallet = web3_wallet

    params["web3_wallet"] = json_web3_wallet

    json_user_id: Union[Unset, None, List[str]] = UNSET
    if not isinstance(user_id, Unset):
        if user_id is None:
            json_user_id = None
        else:
            json_user_id = user_id

    params["user_id"] = json_user_id

    json_organization_id: Union[Unset, None, List[str]] = UNSET
    if not isinstance(organization_id, Unset):
        if organization_id is None:
            json_organization_id = None
        else:
            json_organization_id = organization_id

    params["organization_id"] = json_organization_id

    params["query"] = query

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
    email_address: Union[Unset, None, List[str]] = UNSET,
    phone_number: Union[Unset, None, List[str]] = UNSET,
    external_id: Union[Unset, None, List[str]] = UNSET,
    username: Union[Unset, None, List[str]] = UNSET,
    web3_wallet: Union[Unset, None, List[str]] = UNSET,
    user_id: Union[Unset, None, List[str]] = UNSET,
    organization_id: Union[Unset, None, List[str]] = UNSET,
    query: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 10,
    offset: Union[Unset, None, int] = 0,
    order_by: Union[Unset, None, str] = "-created_at",
) -> Response[Any]:
    """List all users

     Returns a list of all users.
    The users are returned sorted by creation date, with the newest users appearing first.

    Args:
        email_address (Union[Unset, None, List[str]]):
        phone_number (Union[Unset, None, List[str]]):
        external_id (Union[Unset, None, List[str]]):
        username (Union[Unset, None, List[str]]):
        web3_wallet (Union[Unset, None, List[str]]):
        user_id (Union[Unset, None, List[str]]):
        organization_id (Union[Unset, None, List[str]]):
        query (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):  Default: 10.0.
        offset (Union[Unset, None, float]):
        order_by (Union[Unset, None, str]):  Default: '-created_at'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        email_address=email_address,
        phone_number=phone_number,
        external_id=external_id,
        username=username,
        web3_wallet=web3_wallet,
        user_id=user_id,
        organization_id=organization_id,
        query=query,
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
    *,
    client: Client,
    email_address: Union[Unset, None, List[str]] = UNSET,
    phone_number: Union[Unset, None, List[str]] = UNSET,
    external_id: Union[Unset, None, List[str]] = UNSET,
    username: Union[Unset, None, List[str]] = UNSET,
    web3_wallet: Union[Unset, None, List[str]] = UNSET,
    user_id: Union[Unset, None, List[str]] = UNSET,
    organization_id: Union[Unset, None, List[str]] = UNSET,
    query: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 10,
    offset: Union[Unset, None, int] = 0,
    order_by: Union[Unset, None, str] = "-created_at",
) -> Response[Any]:
    """List all users

     Returns a list of all users.
    The users are returned sorted by creation date, with the newest users appearing first.

    Args:
        email_address (Union[Unset, None, List[str]]):
        phone_number (Union[Unset, None, List[str]]):
        external_id (Union[Unset, None, List[str]]):
        username (Union[Unset, None, List[str]]):
        web3_wallet (Union[Unset, None, List[str]]):
        user_id (Union[Unset, None, List[str]]):
        organization_id (Union[Unset, None, List[str]]):
        query (Union[Unset, None, str]):
        limit (Union[Unset, None, float]):  Default: 10.0.
        offset (Union[Unset, None, float]):
        order_by (Union[Unset, None, str]):  Default: '-created_at'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        email_address=email_address,
        phone_number=phone_number,
        external_id=external_id,
        username=username,
        web3_wallet=web3_wallet,
        user_id=user_id,
        organization_id=organization_id,
        query=query,
        limit=limit,
        offset=offset,
        order_by=order_by,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
