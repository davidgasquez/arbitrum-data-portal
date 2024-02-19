from dagster import Definitions, load_assets_from_modules

from . import assets, resources

module_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=module_assets,
    resources={
        "duckdb": resources.duckdb_resource,
        "io_manager": resources.duckdb_polars_io_manager,
    },
)
