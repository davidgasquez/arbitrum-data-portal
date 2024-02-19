import os
from typing import Any, Dict
from contextlib import contextmanager

import duckdb
from dagster import ConfigurableResource
from pydantic import Field
from dagster_duckdb_polars import DuckDBPolarsIOManager
from dagster._utils.backoff import backoff


class CustomDuckDBResource(ConfigurableResource):
    database: str = Field(
        description=(
            "Path to the DuckDB database. Setting database=':memory:' will use an in-memory"
            " database "
        )
    )
    connection_config: Dict[str, Any] = Field(
        description=(
            "DuckDB connection configuration options. See"
            " https://duckdb.org/docs/sql/configuration.html"
        ),
        default={},
    )

    environment: str = Field(
        description="The environment in which the resource is being used",
        default="local",
    )

    @classmethod
    def _is_dagster_maintained(cls) -> bool:
        return True

    @contextmanager
    def get_connection(self):
        conn = backoff(
            fn=duckdb.connect,
            retry_on=(RuntimeError, duckdb.IOException),
            kwargs={
                "database": self.database,
                "read_only": False,
                "config": self.connection_config,
            },
            max_retries=10,
        )

        yield conn

        conn.close()

    def materialize(self, table: str, filename: str):
        with self.get_connection() as c:
            if self.environment == "s3":
                KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
                SECRET = os.environ["AWS_SECRET_ACCESS_KEY"]
                ENDPOINT = os.environ["AWS_ENDPOINT_URL"]
                BUCKET = os.environ["AWS_BUCKET"]
                query = f"""
                CREATE SECRET aws (
                    TYPE S3,
                    KEY_ID '{KEY_ID}',
                    SECRET '{SECRET}',
                    REGION 'us-east-1',
                    USE_SSL true,
                    ENDPOINT '{ENDPOINT}'
                );

                COPY {table} TO 's3://{BUCKET}/{filename}.parquet';
                """
                c.execute(query)
            else:
                c.execute(f"COPY {table} TO 'data/{filename}.parquet'")


duckdb_resource = CustomDuckDBResource(database="data/db.duckdb", environment="local")
duckdb_polars_io_manager = DuckDBPolarsIOManager(database="data/db.duckdb")
