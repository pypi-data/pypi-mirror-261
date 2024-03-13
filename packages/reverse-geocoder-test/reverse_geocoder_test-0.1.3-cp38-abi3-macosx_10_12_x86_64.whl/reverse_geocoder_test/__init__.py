from __future__ import annotations

from typing import TYPE_CHECKING

import polars as pl
from polars.utils.udfs import _get_shared_lib_location

from reverse_geocoder_test.utils import parse_into_expr

if TYPE_CHECKING:
    from polars.type_aliases import IntoExpr

lib = _get_shared_lib_location(__file__)


def reverse_geocode(lat: IntoExpr, long: IntoExpr) -> pl.Expr:
    lat = parse_into_expr(lat)
    return lat.register_plugin(
        lib=lib, symbol="reverse_geocode", is_elementwise=True, args=[long]
    )
