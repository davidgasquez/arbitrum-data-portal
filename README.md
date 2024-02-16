# ⛓️ Arbitrum Data Portal

Open Data Platform for Arbitrum. This goal with this portal is to improve data access and empower data scientists to conduct research that drives the community forward.

## 🛠️ Contributing

This project is in active development. You can help by giving ideas, answering questions, reporting bugs, proposing enhancements, improving the documentation, and fixing bugs. Feel free to open issues and pull requests!

Some ways you can contribute to this project:
- Adding new data sources.
- Improving the data quality of existing datasets.
- Adding tests to the data pipelines.

## ⚙️ Development

You can run the entire Arbitrum Data Portal locally using Python Virtual Environment or VSCode Development Containers.

### 🐍 Python Virtual Environment

Clone the repository and run the following commands (or `make setup`) from the root folder:

```bash
# Create a virtual environment
pip install uv && uv venv

# Install the package and dependencies
uv pip install -U -e .[dev]
```

Now, you should be able to spin up Dagster UI (`make dev`) and [access it locally](http://127.0.0.1:3000).

### 🐳 Dev Container

You can jump into the repository [Development Container](https://code.visualstudio.com/docs/remote/containers). Once inside the develpment environment, you'll only need to run `make dev` to spin up the [Dagster UI locally](http://127.0.0.1:3000). The development environment can also run in your browser thanks to GitHub Codespaces!

[![](https://github.com/codespaces/badge.svg)](https://codespaces.new/davidgasquez/arbitrum-data-portal)

## 📝 License

MIT
