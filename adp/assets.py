import polars as pl
import requests
from dagster import MaterializeResult, MetadataValue, asset

from .resources import DuckDBResource


@asset
def raw_discourse_categories(duckdb: DuckDBResource) -> MaterializeResult:
    url = "https://forum.arbitrum.foundation/categories.json"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    df = pl.DataFrame(data["category_list"]["categories"])
    with duckdb.get_connection() as conn:
        conn.cursor().execute(
            """
            create or replace table raw_discourse_categories
            as
            select * from df
            """
        )
    return MaterializeResult(
        metadata={
            "rows": MetadataValue.int(df.shape[0]),
        }
    )
