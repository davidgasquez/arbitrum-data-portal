import polars as pl
import requests
from dagster import asset


@asset
def raw_discourse_categories() -> pl.DataFrame:
    url = "https://forum.arbitrum.foundation/categories.json"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return pl.DataFrame(data["category_list"]["categories"])
