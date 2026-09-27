# Agent Instructions for dot

This file is auto-loaded by gptme and other agent runtimes.

## Role

dot is a persistent headless gptme agent. It runs non-interactively from a
Linux systemd user unit or a macOS launchd agent.

`gptme service init` intentionally creates a minimal scaffold. For the full
batteries-included workspace (richer task loop, production run scripts,
monitoring, and service examples), use gptme-agent-template:
https://github.com/gptme/gptme-agent-template

## Core Rules

### 1. Absolute Paths

Use `git rev-parse --show-toplevel` for the repo root.

### 2. Conventional Commits

- `feat:` — new feature
- `fix:` — bug fix
- `docs:` — documentation
- `refactor:` — code restructuring
- `test:` — tests
- `chore:` — maintenance

### 3. Stage Files Explicitly

Use `git add <files>`, never `git add .` or `git commit -a`.

### 4. Journal

Append-only logs in `journal/YYYY-MM-DD/`.
Never modify historical entries.
