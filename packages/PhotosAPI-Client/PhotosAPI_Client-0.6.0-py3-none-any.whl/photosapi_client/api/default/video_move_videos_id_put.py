from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.video_public import VideoPublic
from ...types import UNSET, Response


def _get_kwargs(
    id: str,
    *,
    album: str,
) -> Dict[str, Any]:

    params: Dict[str, Any] = {}

    params["album"] = album

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/videos/{id}".format(
            id=id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, VideoPublic]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = VideoPublic.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, HTTPValidationError, VideoPublic]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    album: str,
) -> Response[Union[Any, HTTPValidationError, VideoPublic]]:
    """Video Move

     Move a video into another album

    Args:
        id (str):
        album (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, VideoPublic]]
    """

    kwargs = _get_kwargs(
        id=id,
        album=album,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    album: str,
) -> Optional[Union[Any, HTTPValidationError, VideoPublic]]:
    """Video Move

     Move a video into another album

    Args:
        id (str):
        album (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, VideoPublic]
    """

    return sync_detailed(
        id=id,
        client=client,
        album=album,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    album: str,
) -> Response[Union[Any, HTTPValidationError, VideoPublic]]:
    """Video Move

     Move a video into another album

    Args:
        id (str):
        album (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, VideoPublic]]
    """

    kwargs = _get_kwargs(
        id=id,
        album=album,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    album: str,
) -> Optional[Union[Any, HTTPValidationError, VideoPublic]]:
    """Video Move

     Move a video into another album

    Args:
        id (str):
        album (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, VideoPublic]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            album=album,
        )
    ).parsed
