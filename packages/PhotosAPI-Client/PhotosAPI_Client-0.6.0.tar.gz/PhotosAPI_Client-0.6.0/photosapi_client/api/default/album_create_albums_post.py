from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.album import Album
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response


def _get_kwargs(
    *,
    name: str,
    title: str,
) -> Dict[str, Any]:

    params: Dict[str, Any] = {}

    params["name"] = name

    params["title"] = title

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/albums",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Album, Any, HTTPValidationError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Album.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_ACCEPTABLE:
        response_406 = cast(Any, None)
        return response_406
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
) -> Response[Union[Album, Any, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    name: str,
    title: str,
) -> Response[Union[Album, Any, HTTPValidationError]]:
    """Album Create

     Create album with name and title

    Args:
        name (str):
        title (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Album, Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        name=name,
        title=title,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    name: str,
    title: str,
) -> Optional[Union[Album, Any, HTTPValidationError]]:
    """Album Create

     Create album with name and title

    Args:
        name (str):
        title (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Album, Any, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        name=name,
        title=title,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    name: str,
    title: str,
) -> Response[Union[Album, Any, HTTPValidationError]]:
    """Album Create

     Create album with name and title

    Args:
        name (str):
        title (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Album, Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        name=name,
        title=title,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    name: str,
    title: str,
) -> Optional[Union[Album, Any, HTTPValidationError]]:
    """Album Create

     Create album with name and title

    Args:
        name (str):
        title (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Album, Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            title=title,
        )
    ).parsed
