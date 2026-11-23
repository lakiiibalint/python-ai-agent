# Python AI Agent

A small educational AI coding agent. Given a prompt, it uses an LLM (via [OpenRouter](https://openrouter.ai)) with tool calling to explore, read, write and run Python files inside a sandboxed working directory (`calculator/`).

## Tools available to the agent

- `get_files_info` – list files and directories
- `get_file_content` – read a file
- `write_file` – create or overwrite a file
- `run_python_file` – run a Python file and return its output

All paths are restricted to the working directory.

## Setup

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync
echo 'OPENROUTER_API_KEY=your_key_here' > .env
```

## Usage

```bash
uv run main.py "fix the bug in the calculator" --verbose
```

`--verbose` prints token usage and tool results. The agent loops for up to 20 iterations before giving up.

## Note

This is a learning project. The agent can write and execute code, so only run it on code you trust.
