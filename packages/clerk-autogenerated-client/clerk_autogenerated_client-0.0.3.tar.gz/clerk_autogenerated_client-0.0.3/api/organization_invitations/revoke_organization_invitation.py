from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.revoke_organization_invitation_json_body import RevokeOrganizationInvitationJsonBody
from ...livtypes import Response


def _get_kwargs(
    organization_id: str,
    invitation_id: str,
    *,
    client: Client,
    json_body: RevokeOrganizationInvitationJsonBody,
) -> Dict[str, Any]:
    url = "{}/organizations/{organization_id}/invitations/{invitation_id}/revoke".format(
        client.base_url, organization_id=organization_id, invitation_id=invitation_id
    )

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
    if response.status_code == HTTPStatus.NOT_FOUND:
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
    invitation_id: str,
    *,
    client: Client,
    json_body: RevokeOrganizationInvitationJsonBody,
) -> Response[Any]:
    r"""Revoke a pending organization invitation

     Use this request to revoke a previously issued organization invitation.
    Revoking an organization invitation makes it invalid; the invited user will no longer be able to
    join the organization with the revoked invitation.
    Only organization invitations with \"pending\" status can be revoked.
    The request needs the `requesting_user_id` parameter to specify the user which revokes the
    invitation.
    Only users with \"admin\" role can revoke invitations.

    Args:
        organization_id (str):
        invitation_id (str):
        json_body (RevokeOrganizationInvitationJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        invitation_id=invitation_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    organization_id: str,
    invitation_id: str,
    *,
    client: Client,
    json_body: RevokeOrganizationInvitationJsonBody,
) -> Response[Any]:
    r"""Revoke a pending organization invitation

     Use this request to revoke a previously issued organization invitation.
    Revoking an organization invitation makes it invalid; the invited user will no longer be able to
    join the organization with the revoked invitation.
    Only organization invitations with \"pending\" status can be revoked.
    The request needs the `requesting_user_id` parameter to specify the user which revokes the
    invitation.
    Only users with \"admin\" role can revoke invitations.

    Args:
        organization_id (str):
        invitation_id (str):
        json_body (RevokeOrganizationInvitationJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        invitation_id=invitation_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
