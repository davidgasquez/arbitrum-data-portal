import polars as pl
import requests
from dagster import AssetKey, asset

from .resources import CustomDuckDBResource


@asset
def raw_discourse_categories() -> pl.DataFrame:
    url = "https://forum.arbitrum.foundation/categories.json"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return pl.DataFrame(data["category_list"]["categories"]).drop("default_view")


@asset(deps=AssetKey("raw_discourse_categories"))
def materialized_discourse_categories(duckdb: CustomDuckDBResource) -> None:
    duckdb.materialize(
        "public.raw_discourse_categories", "materialized_discourse_categories"
    )
