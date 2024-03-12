from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.change_production_instance_domain_json_body import ChangeProductionInstanceDomainJsonBody
from ...livtypes import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: ChangeProductionInstanceDomainJsonBody,
) -> Dict[str, Any]:
    url = "{}/instance/change_domain".format(client.base_url)

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
    if response.status_code == HTTPStatus.ACCEPTED:
        return None
    if response.status_code == HTTPStatus.BAD_REQUEST:
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
    json_body: ChangeProductionInstanceDomainJsonBody,
) -> Response[Any]:
    """Update production instance domain

     Change the domain of a production instance.

    Changing the domain requires updating the [DNS
    records](https://clerk.com/docs/deployments/overview#dns-records) accordingly, deploying new [SSL
    certificates](https://clerk.com/docs/deployments/overview#deploy), updating your Social Connection's
    redirect URLs and setting the new keys in your code.

    WARNING: Changing your domain will invalidate all current user sessions (i.e. users will be logged
    out). Also, while your application is being deployed, a small downtime is expected to occur.

    Args:
        json_body (ChangeProductionInstanceDomainJsonBody):

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
    json_body: ChangeProductionInstanceDomainJsonBody,
) -> Response[Any]:
    """Update production instance domain

     Change the domain of a production instance.

    Changing the domain requires updating the [DNS
    records](https://clerk.com/docs/deployments/overview#dns-records) accordingly, deploying new [SSL
    certificates](https://clerk.com/docs/deployments/overview#deploy), updating your Social Connection's
    redirect URLs and setting the new keys in your code.

    WARNING: Changing your domain will invalidate all current user sessions (i.e. users will be logged
    out). Also, while your application is being deployed, a small downtime is expected to occur.

    Args:
        json_body (ChangeProductionInstanceDomainJsonBody):

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
