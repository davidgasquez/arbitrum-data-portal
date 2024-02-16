.DEFAULT_GOAL := run

run:
	dagster job execute -j datasets

dev:
	dagster dev

clean:
	rm -rf data/*.duckdb

# Check if uv is installed else install install it
setup:
	@command -v uv >/dev/null 2>&1 || pip install -U uv
	uv venv
	uv pip install -U -e .[dev]
