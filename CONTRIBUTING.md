# Contributing to yeongi / 연기 / 緣起

Welcome! We appreciate your interest in contributing to `yeongi`. This project follows strict engineering standards to ensure reliability and maintainability.

## Development Principles

### 1. TDD First (Test-Driven Development)
We believe that tests are the best documentation and the only way to ensure long-term stability.
- **Red**: Write a failing test for the new behavior or bug fix first.
- **Green**: Write the minimum code necessary to make the test pass.
- **Refactor**: Improve the code while keeping the tests green.
- **Verification**: No feature is complete without comprehensive test coverage in the `tests/` directory.

### 2. Monorepo Architecture
Maintain a clean separation between:
- `libs/core`: Core logic, abstract bot interfaces, and snapshot serialisation.
- `libs/adapters`: Platform-specific implementations (e.g., Telegram, Feishu).
- `libs/storage`: Persistence providers for saving messages and media.
- `apps/`: Deployable bot entry points (e.g., `apps/telegram-echo`).
- `infrastructure/tofu`: Infrastructure-as-Code (IaC) using OpenTofu for GCP deployment.

### 3. Conventional Commits
We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification for all commit messages. This helps in generating clear changelogs and automating versioning.
- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation only changes
- **style**: Changes that do not affect the meaning of the code (white-space, formatting, etc)
- **refactor**: A code change that neither fixes a bug nor adds a feature
- **perf**: A code change that improves performance
- **test**: Adding missing tests or correcting existing tests
- **build**: Changes that affect the build system or external dependencies
- **ci**: Changes to our CI configuration files and scripts
- **chore**: Other changes that don't modify src or test files
- **revert**: Reverts a previous commit

### 4. Infrastructure (OpenTofu)
We use OpenTofu (a Terraform fork) for Infrastructure-as-Code.
- Keep `.tf` files in `infrastructure/tofu/`.
- Ensure all resources (GCS buckets, Cloud Run services) are managed via IaC.

### 5. Tooling & Environment
- **Language**: Python 3.12+
- **Dependency Management**: `uv` (workspace mode).
- **Bot Framework**: `aiogram` (v3).
- **Test Runner**: `pytest`.
- **Infrastructure**: OpenTofu.

---

## Getting Started

1.  **Environment Setup**: Install `uv`.
    ```bash
    uv sync
    uv run pre-commit install
    uv run pre-commit install --hook-type commit-msg
    ```
2.  **Infrastructure Initialization**:
    ```bash
    uv run poe tofu-init
    ```
3.  **Run Tests**:
    ```bash
    uv run poe test
    ```
4.  **Linting**:
    ```bash
    uv run poe lint
    ```

---

## AI Agent Guidelines

If you are an AI agent (like Gemini, Claude, or ChatGPT) assisting with this project, please adhere to these specific workflows:

### Phase 1: Research & Reproduction
- **Never guess**: Use `grep_search` and `read_file` to understand existing patterns before proposing changes.
- **Reproduce First**: For bug fixes, always write a reproduction script or test case that fails before applying a fix.

### Phase 2: Strategy & Implementation
- **TDD Workflow**: Propose the test case *before* the implementation.
- **Surgical Updates**: Use the `replace` tool for targeted edits. Avoid rewriting entire files unless necessary.
- **Idiomatic Python**: Use modern Python features (3.12+) and leverage `uv` for managing dependencies.

### Phase 3: Validation
- **Run Tests**: Always execute `pytest` after any change to verify that existing functionality is preserved and new tests pass.
- **No Regressions**: Ensure that your changes do not break other parts of the monorepo.
- **Linting**: If available, run linting and type-checking tools to maintain code quality.
