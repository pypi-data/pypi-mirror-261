from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_results_video import SearchResultsVideo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    album: str,
    *,
    q: Union[None, Unset, str] = UNSET,
    caption: Union[None, Unset, str] = UNSET,
    token: Union[None, Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 100,
) -> Dict[str, Any]:

    params: Dict[str, Any] = {}

    json_q: Union[None, Unset, str]
    if isinstance(q, Unset):
        json_q = UNSET
    else:
        json_q = q
    params["q"] = json_q

    json_caption: Union[None, Unset, str]
    if isinstance(caption, Unset):
        json_caption = UNSET
    else:
        json_caption = caption
    params["caption"] = json_caption

    json_token: Union[None, Unset, str]
    if isinstance(token, Unset):
        json_token = UNSET
    else:
        json_token = token
    params["token"] = json_token

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/albums/{album}/videos".format(
            album=album,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, SearchResultsVideo]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SearchResultsVideo.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = cast(Any, None)
        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, SearchResultsVideo]]:
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
    q: Union[None, Unset, str] = UNSET,
    caption: Union[None, Unset, str] = UNSET,
    token: Union[None, Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 100,
) -> Response[Union[Any, SearchResultsVideo]]:
    """Video Find

     Find a video by filename, caption or token

    Args:
        album (str):
        q (Union[None, Unset, str]):
        caption (Union[None, Unset, str]):
        token (Union[None, Unset, str]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SearchResultsVideo]]
    """

    kwargs = _get_kwargs(
        album=album,
        q=q,
        caption=caption,
        token=token,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    album: str,
    *,
    client: AuthenticatedClient,
    q: Union[None, Unset, str] = UNSET,
    caption: Union[None, Unset, str] = UNSET,
    token: Union[None, Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 100,
) -> Optional[Union[Any, SearchResultsVideo]]:
    """Video Find

     Find a video by filename, caption or token

    Args:
        album (str):
        q (Union[None, Unset, str]):
        caption (Union[None, Unset, str]):
        token (Union[None, Unset, str]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SearchResultsVideo]
    """

    return sync_detailed(
        album=album,
        client=client,
        q=q,
        caption=caption,
        token=token,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    album: str,
    *,
    client: AuthenticatedClient,
    q: Union[None, Unset, str] = UNSET,
    caption: Union[None, Unset, str] = UNSET,
    token: Union[None, Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 100,
) -> Response[Union[Any, SearchResultsVideo]]:
    """Video Find

     Find a video by filename, caption or token

    Args:
        album (str):
        q (Union[None, Unset, str]):
        caption (Union[None, Unset, str]):
        token (Union[None, Unset, str]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SearchResultsVideo]]
    """

    kwargs = _get_kwargs(
        album=album,
        q=q,
        caption=caption,
        token=token,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    album: str,
    *,
    client: AuthenticatedClient,
    q: Union[None, Unset, str] = UNSET,
    caption: Union[None, Unset, str] = UNSET,
    token: Union[None, Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 100,
) -> Optional[Union[Any, SearchResultsVideo]]:
    """Video Find

     Find a video by filename, caption or token

    Args:
        album (str):
        q (Union[None, Unset, str]):
        caption (Union[None, Unset, str]):
        token (Union[None, Unset, str]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SearchResultsVideo]
    """

    return (
        await asyncio_detailed(
            album=album,
            client=client,
            q=q,
            caption=caption,
            token=token,
            page=page,
            page_size=page_size,
        )
    ).parsed
