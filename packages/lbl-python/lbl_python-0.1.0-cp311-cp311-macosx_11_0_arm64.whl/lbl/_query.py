from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from typing import Any, Literal, Mapping

    # class Label(typing.TypedDict):
    #     address: str | bytes
    #     name: str | None
    #     collection: str | None
    #     project: str | None
    #     function: str | None
    #     network: str | None
    #     extra_data: Mapping[str, Any]
    #     added_by: str | None
    #     date_added: int | None


def query(
    *,
    address: str | bytes | None = None,
    name: str | None = None,
    collection: str | None = None,
    network: str | int | None = None,
    function: str | None = None,
    # extra_data_contains: Mapping[str, Any] | None = None,
    # extra_data_equals: Mapping[str, Any] | None = None,
    added_by: str | None = None,
    added_before: int | None = None,
    added_after: int | None = None,
    added_at: int | None = None,
    hex: bool = False,
) -> pl.DataFrame:
    """query address data"""

    from . import _lbl_rust

    df = _lbl_rust._query(
        collection=collection,
        address=address,
        network=network,
        # extra_data_equals=extra_data_equals,
        # extra_data_contains=extra_data_contains,
        function=function,
        added_by=added_by,
        added_before=added_before,
        added_after=added_after,
        added_at=added_at,
        hex=hex,
    )

    return df

    # if output_format == 'polars':
    #     return df
    # elif output_format == 'native':
    #     raise NotImplementedError('native output format')
    # else:
    #     raise Exception('unknown output format: ' + str(output_format))
