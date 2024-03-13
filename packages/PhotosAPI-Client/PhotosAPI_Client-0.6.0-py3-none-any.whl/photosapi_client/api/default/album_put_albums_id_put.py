from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.album_modified import AlbumModified
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response


def _get_kwargs(
    id: str,
    *,
    name: str,
    title: str,
    cover: str,
) -> Dict[str, Any]:

    params: Dict[str, Any] = {}

    params["name"] = name

    params["title"] = title

    params["cover"] = cover

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/albums/{id}".format(
            id=id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AlbumModified, Any, HTTPValidationError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AlbumModified.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.NOT_ACCEPTABLE:
        response_406 = cast(Any, None)
        return response_406
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AlbumModified, Any, HTTPValidationError]]:
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
    name: str,
    title: str,
    cover: str,
) -> Response[Union[AlbumModified, Any, HTTPValidationError]]:
    """Album Put

     Modify album's name and title by id

    Args:
        id (str):
        name (str):
        title (str):
        cover (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AlbumModified, Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        id=id,
        name=name,
        title=title,
        cover=cover,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    name: str,
    title: str,
    cover: str,
) -> Optional[Union[AlbumModified, Any, HTTPValidationError]]:
    """Album Put

     Modify album's name and title by id

    Args:
        id (str):
        name (str):
        title (str):
        cover (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AlbumModified, Any, HTTPValidationError]
    """

    return sync_detailed(
        id=id,
        client=client,
        name=name,
        title=title,
        cover=cover,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    name: str,
    title: str,
    cover: str,
) -> Response[Union[AlbumModified, Any, HTTPValidationError]]:
    """Album Put

     Modify album's name and title by id

    Args:
        id (str):
        name (str):
        title (str):
        cover (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AlbumModified, Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        id=id,
        name=name,
        title=title,
        cover=cover,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    name: str,
    title: str,
    cover: str,
) -> Optional[Union[AlbumModified, Any, HTTPValidationError]]:
    """Album Put

     Modify album's name and title by id

    Args:
        id (str):
        name (str):
        title (str):
        cover (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AlbumModified, Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            name=name,
            title=title,
            cover=cover,
        )
    ).parsed
