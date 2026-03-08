# yeongi / 연기 / 緣起

A Python-based monorepo template for building extensible echo bots (Telegram, Feishu, etc.) with state snapshotting and cloud-ready deployment.

## Key Features
- **TDD First**: Built from the ground up with `pytest`.
- **Monorepo Architecture**: Clean separation between core logic, storage, and platform adapters.
- **Persistence**: Save every message and file to local storage or Google Cloud Storage.
- **Snapshots**: Capture and restore bot state for robust conversation management.
- **Cloud Ready**: Deploys to Google Cloud Run using OpenTofu (Terraform).

## Quick Start
1.  **See the [Project Plan](PLAN.md)** for detailed architecture and roadmap.
2.  **Environment Setup**: Install `uv`.
    ```bash
    uv sync
    ```
3.  **Run Tests**:
    ```bash
    pytest
    ```

## License
MIT
