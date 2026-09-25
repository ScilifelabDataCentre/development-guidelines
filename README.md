# Development guidelines for SciLifeLab Data Centre

[![Project Management PDF Build](https://github.com/ScilifelabDataCentre/development-guidelines/actions/workflows/pandoc.yml/badge.svg)](https://github.com/ScilifelabDataCentre/development-guidelines/actions/workflows/pandoc.yml)
[![Markdown link check](https://github.com/ScilifelabDataCentre/development-guidelines/actions/workflows/markdown-link-check.yml/badge.svg)](https://github.com/ScilifelabDataCentre/development-guidelines/actions/workflows/markdown-link-check.yml)
[![Prettier](https://github.com/ScilifelabDataCentre/development-guidelines/actions/workflows/prettier.yml/badge.svg)](https://github.com/ScilifelabDataCentre/development-guidelines/actions/workflows/prettier.yml)

These are our guidelines and policies for software development practices at SciLifeLab Data Centre. They serve as a starting point for any developer working with our infrastructure and codebases, helping to maintain a common understanding and level of quality across all our projects.

They are intended to evolve and anyone involved in development can propose changes (see [How to suggest changes](#how-to-suggest-changes)).

## Repository structure

### Area/Topic-specific directories

The majority of all files in this repository should be placed in area/topic-specific directories. The repository root should contain as few files as possible; Only place files in the root if they absolutely need to be there.

Each area- or topic-specific directory should contain a `README` which should act as a landing page. The `README` should explain what the purpose of that area / topic is, while additional or more detailed information should be placed in separate files in the same directory.

### File formats

The files in this repository should be mainly markdown. Images should be SVG files.

### Naming of files and directories

Files and folders should use lowercase snake_case format, e.g. `paved_paths` as opposed to `Paved_Paths` or `PavedPaths` etc.

## Repository contents

- **Guidelines**
  - [`accessibility/`](./accessibility/) — Information and instructions regarding accessibility
  - [`adrs/`](./adrs/) — Guidance regarding Architectural Decision Records
  - [`citing_and_citability/`](./citing_and_citability/) — Guidance on how to cite code and make code citable
  - [`git_and_github/`](./git_and_github/) — Policies and instructions regarding GitHub and repository hygiene
  - [`project_management/`](./project_management/) — Project management specific topics and processes
  - [`pull_requests/`](./pull_requests/) — Guidelines on how to prepare and review PRs
  - [`regulations/`](./regulations/) — Information on important regulations we need to adhere to
- **Paved paths**
  - [`paved_paths/`](./paved_paths/) — Guidance on which tools to choose. Recommended defaults and supported tools.
- **Repository docs**
  - [`docs/`](./docs/) — Instructions specific to this repository
- **Repository configurations**
  - [`.config/`](.config/) — Configurations for tools used in this repository, often connected to specific workflows in `.github/workflows/`. One subdirectory per tool.
  - [`.github/`](.github/) — Templates and repository specific configurations that are required by the tool or GitHub to be placed here
  - [`.github/workflows/`](.github/workflows/) — Workflow definitions for GitHub Actions
  - [Repository root](.) — Repository configurations that don't fit anywhere else

## How to suggest changes

Suggestions for improvement of this repository are always appreciated.

If you want to improve these guidelines, open a PR or [issue](https://github.com/ScilifelabDataCentre/development-guidelines/issues).

If you have a suggestion regarding the [Paved Paths](./paved_paths/), follow the ["How to propose updates"](./paved_paths/README.md#how-to-propose-updates) section in the README.

In some cases, the suggestions will be simple and uncomplicated enough for the [code owner](.github/CODEOWNERS) to approve immediately. Bigger changes will be discussion/decision topics at a DC dev meeting.

## Other guidelines

- [Documentation for the K1H platform ("the KTH Kubernetes clusters")](.)
- [Licensing Guidelines: how to license your work](.)

## Licensing

Neither licence below applies to the repository as a whole.

**Content** — all Markdown files and images.

[![License: CC BY 4.0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by.svg)](https://creativecommons.org/licenses/by/4.0/)

This work is licensed under a Creative Commons Attribution 4.0 International
License: https://creativecommons.org/licenses/by/4.0/ (full text:
[`LICENSE-CONTENT`](./LICENSE-CONTENT))

**Code** — all other files (configuration, workflows, build).

This project is licensed under the terms of the MIT license (full text:
[`LICENSE-CODE`](./LICENSE-CODE)).
