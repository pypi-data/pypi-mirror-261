from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.create_organization_invitation_json_body import CreateOrganizationInvitationJsonBody
from ...livtypes import Response


def _get_kwargs(
    organization_id: str,
    *,
    client: Client,
    json_body: CreateOrganizationInvitationJsonBody,
) -> Dict[str, Any]:
    url = "{}/organizations/{organization_id}/invitations".format(client.base_url, organization_id=organization_id)

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
    json_body: CreateOrganizationInvitationJsonBody,
) -> Response[Any]:
    r"""Create and send an organization invitation

     Creates a new organization invitation and sends an email to the provided `email_address` with a link
    to accept the invitation and join the organization.
    You can specify the `role` for the invited organization member.

    New organization invitations get a \"pending\" status until they are revoked by an organization
    administrator or accepted by the invitee.

    The request body supports passing an optional `redirect_url` parameter.
    When the invited user clicks the link to accept the invitation, they will be redirected to the URL
    provided.
    Use this parameter to implement a custom invitation acceptance flow.

    You must specify the ID of the user that will send the invitation with the `inviter_user_id`
    parameter.
    That user must be a member with administrator privileges in the organization.
    Only \"admin\" members can create organization invitations.

    You can optionally provide public and private metadata for the organization invitation.
    The public metadata are visible by both the Frontend and the Backend whereas the private ones only
    by the Backend.
    When the organization invitation is accepted, the metadata will be transferred to the newly created
    organization membership.

    Args:
        organization_id (str):
        json_body (CreateOrganizationInvitationJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
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
    *,
    client: Client,
    json_body: CreateOrganizationInvitationJsonBody,
) -> Response[Any]:
    r"""Create and send an organization invitation

     Creates a new organization invitation and sends an email to the provided `email_address` with a link
    to accept the invitation and join the organization.
    You can specify the `role` for the invited organization member.

    New organization invitations get a \"pending\" status until they are revoked by an organization
    administrator or accepted by the invitee.

    The request body supports passing an optional `redirect_url` parameter.
    When the invited user clicks the link to accept the invitation, they will be redirected to the URL
    provided.
    Use this parameter to implement a custom invitation acceptance flow.

    You must specify the ID of the user that will send the invitation with the `inviter_user_id`
    parameter.
    That user must be a member with administrator privileges in the organization.
    Only \"admin\" members can create organization invitations.

    You can optionally provide public and private metadata for the organization invitation.
    The public metadata are visible by both the Frontend and the Backend whereas the private ones only
    by the Backend.
    When the organization invitation is accepted, the metadata will be transferred to the newly created
    organization membership.

    Args:
        organization_id (str):
        json_body (CreateOrganizationInvitationJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
