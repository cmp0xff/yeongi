# yeongi / 연기 / 緣起 - Project Plan

`yeongi` (緣起 - Dependent Origination) is a Python-based monorepo template for building extensible echo bots that can run locally or on Google Cloud. It focuses on Test-Driven Development (TDD) and modular storage.

## 1. Architecture (Monorepo)

- **`libs/core`**: Abstract bot interfaces, standard message models, and snapshot logic.
- **`libs/storage`**: Providers for persisting messages and media (Filesystem, GCS).
- **`libs/adapters`**: Platform implementations (Telegram, Feishu).
- **`apps/telegram-echo`**: The Telegram bot entry point.
- **`infrastructure/tofu`**: Infrastructure-as-Code (IaC) using OpenTofu for GCP deployment.

## 2. Core Features

- [ ] **Echo Engine**: Reliable echoing of text, photos, and files.
- [ ] **Persistence Sink**: Automatically save every incoming/outgoing message and file to storage.
- [ ] **Snapshotting**: Capture and serialize the bot's state (e.g., conversation context) for recovery or inspection.
- [ ] **Cloud-Native**: Containerized (Docker) and deployed via Cloud Run.

## 3. Technology Stack

- **Language**: Python 3.12+
- **Dependency Management**: `uv` (workspace mode).
- **Bot Framework**: `aiogram` (v3).
- **IaC**: OpenTofu (GCP Cloud Run, GCS, Secret Manager).
- **Testing**: `pytest` (Strict TDD).

## 4. Roadmap

1.  **Phase 1: Foundation**: Set up `uv` workspace, basic `core` models, and `storage` interface.
2.  **Phase 2: Telegram & Echo**: Implement `aiogram` adapter with TDD.
3.  **Phase 3: Persistence**: Implement File/Message saving and snapshotting logic.
4.  **Phase 4: Cloud Infrastructure**: Provision GCP resources using OpenTofu.
5.  **Phase 5: Extensibility**: Add Feishu adapter support.
