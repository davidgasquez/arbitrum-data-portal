from dagster_duckdb import DuckDBResource
from dagster_duckdb_polars import DuckDBPolarsIOManager

duckdb_resource = DuckDBResource(database="data/db.duckdb")
duckdb_polars_io_manager = DuckDBPolarsIOManager(database="data/db.duckdb")
