.DEFAULT_GOAL := run

run:
	dagster asset list -m adp

dev:
	dagster dev

clean:
	rm -rf data/*.duckdb

setup:
	@command -v uv >/dev/null 2>&1 || pip install -U uv
	uv venv
	uv pip install -U -e .[dev]
	. .venv/bin/activate
