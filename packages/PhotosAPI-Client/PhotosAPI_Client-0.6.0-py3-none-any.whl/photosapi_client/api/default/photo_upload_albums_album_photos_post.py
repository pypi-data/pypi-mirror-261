from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_photo_upload_albums_album_photos_post import BodyPhotoUploadAlbumsAlbumPhotosPost
from ...models.http_validation_error import HTTPValidationError
from ...models.photo import Photo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    album: str,
    *,
    body: BodyPhotoUploadAlbumsAlbumPhotosPost,
    ignore_duplicates: Union[Unset, bool] = False,
    compress: Union[Unset, bool] = True,
    caption: Union[None, Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["ignore_duplicates"] = ignore_duplicates

    params["compress"] = compress

    json_caption: Union[None, Unset, str]
    if isinstance(caption, Unset):
        json_caption = UNSET
    else:
        json_caption = caption
    params["caption"] = json_caption

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/albums/{album}/photos".format(
            album=album,
        ),
        "params": params,
    }

    _body = body.to_multipart()

    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, Photo]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Photo.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = cast(Any, None)
        return response_409
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, HTTPValidationError, Photo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    album: str,
    *,
    client: AuthenticatedClient,
    body: BodyPhotoUploadAlbumsAlbumPhotosPost,
    ignore_duplicates: Union[Unset, bool] = False,
    compress: Union[Unset, bool] = True,
    caption: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, HTTPValidationError, Photo]]:
    """Photo Upload

     Upload a photo to album

    Args:
        album (str):
        ignore_duplicates (Union[Unset, bool]):  Default: False.
        compress (Union[Unset, bool]):  Default: True.
        caption (Union[None, Unset, str]):
        body (BodyPhotoUploadAlbumsAlbumPhotosPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, Photo]]
    """

    kwargs = _get_kwargs(
        album=album,
        body=body,
        ignore_duplicates=ignore_duplicates,
        compress=compress,
        caption=caption,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    album: str,
    *,
    client: AuthenticatedClient,
    body: BodyPhotoUploadAlbumsAlbumPhotosPost,
    ignore_duplicates: Union[Unset, bool] = False,
    compress: Union[Unset, bool] = True,
    caption: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, HTTPValidationError, Photo]]:
    """Photo Upload

     Upload a photo to album

    Args:
        album (str):
        ignore_duplicates (Union[Unset, bool]):  Default: False.
        compress (Union[Unset, bool]):  Default: True.
        caption (Union[None, Unset, str]):
        body (BodyPhotoUploadAlbumsAlbumPhotosPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, Photo]
    """

    return sync_detailed(
        album=album,
        client=client,
        body=body,
        ignore_duplicates=ignore_duplicates,
        compress=compress,
        caption=caption,
    ).parsed


async def asyncio_detailed(
    album: str,
    *,
    client: AuthenticatedClient,
    body: BodyPhotoUploadAlbumsAlbumPhotosPost,
    ignore_duplicates: Union[Unset, bool] = False,
    compress: Union[Unset, bool] = True,
    caption: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, HTTPValidationError, Photo]]:
    """Photo Upload

     Upload a photo to album

    Args:
        album (str):
        ignore_duplicates (Union[Unset, bool]):  Default: False.
        compress (Union[Unset, bool]):  Default: True.
        caption (Union[None, Unset, str]):
        body (BodyPhotoUploadAlbumsAlbumPhotosPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, Photo]]
    """

    kwargs = _get_kwargs(
        album=album,
        body=body,
        ignore_duplicates=ignore_duplicates,
        compress=compress,
        caption=caption,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    album: str,
    *,
    client: AuthenticatedClient,
    body: BodyPhotoUploadAlbumsAlbumPhotosPost,
    ignore_duplicates: Union[Unset, bool] = False,
    compress: Union[Unset, bool] = True,
    caption: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, HTTPValidationError, Photo]]:
    """Photo Upload

     Upload a photo to album

    Args:
        album (str):
        ignore_duplicates (Union[Unset, bool]):  Default: False.
        compress (Union[Unset, bool]):  Default: True.
        caption (Union[None, Unset, str]):
        body (BodyPhotoUploadAlbumsAlbumPhotosPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, Photo]
    """

    return (
        await asyncio_detailed(
            album=album,
            client=client,
            body=body,
            ignore_duplicates=ignore_duplicates,
            compress=compress,
            caption=caption,
        )
    ).parsed
