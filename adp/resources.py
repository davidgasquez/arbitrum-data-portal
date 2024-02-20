from dagster_duckdb import DuckDBResource
from dagster_duckdb_polars import DuckDBPolarsIOManager


class CustomDuckDBResource(DuckDBResource):
    def materialize(self, table: str, filename: str) -> None:
        with self.get_connection() as c:
            c.execute(f"COPY {table} TO 'data/{filename}.parquet'")


duckdb_resource = CustomDuckDBResource(database="data/db.duckdb")
duckdb_polars_io_manager = DuckDBPolarsIOManager(database="data/db.duckdb")
