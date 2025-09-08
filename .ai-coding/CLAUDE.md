# AI Coding Directory - Instructions for Claude

## Directory Purpose
This directory contains specifications and tracking for AI-assisted coding workflows, specifically focusing on the integration of mise (a development environment setup tool) with various AI coding tools.

## Key Files
- `spec.md` - Product Requirements Document for installing, configuring, and trying mise
- `todo.md` - Implementation checklist with current task statuses

## Current Project Status
The project involves configuring Harper Reed's AI coding workflow tasks with mise. Current status:
- ✅ mise installation completed
- 🟡 Configuration of global mise tasks for AI coding workflow in progress
- ⬜ Testing of basic AI workflow functionality pending

## AI Tools Being Configured
- Repomix - For bundle generation
- llm-cli - Command-line interface for LLMs
- aider - AI-assisted coding tool

## Task Status Definitions
In the todo.md file:
- `DONE` - Task completed
- `DOING` - Task currently in progress
- `TODO` - Task not yet started

## Working with This Directory
When assisting with tasks related to this directory:

1. **Stay consistent with task tracking**:
   - Maintain the format of spec.md and todo.md
   - Keep task status indicators (`DONE`, `DOING`, `TODO`) updated

2. **mise configuration tasks**:
   - Configuration should follow Harper Reed's dotfiles pattern
   - Focus on AI-related tasks in ~/.config/mise/config.toml

3. **Testing workflow**:
   - Tests should validate the end-to-end functionality
   - Each mise task should be tested individually

4. **Documentation approach**:
   - Document configuration steps in the Logseq knowledge graph
   - Create appropriate namespaced pages under `[[AI/Coding/]]` namespace

## Reference Links
- [Harper Reed's LLM Codegen Workflow](https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/)
- [Harper's mise config files](https://github.com/harperreed/dotfiles/tree/560ebda30d1b8cea81acee8d44ebe1cf8be3aa2e/.config/mise)
- [Original GitHub issue #1](https://github.com/codekiln/logseq-encode-garden/issues/1)