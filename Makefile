.DEFAULT_GOAL := run

run:
	dagster job execute -j datasets

dev:
	dagster dev

clean:
	rm -rf data/*.duckdb
