from dagster import Definitions, load_assets_from_modules

from . import assets, resources

assets = load_assets_from_modules([assets])

defs = Definitions(assets=assets, resources={"duckdb": resources.duckdb_resource})
