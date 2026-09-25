# Project management overview

## Updating these docs

The raw, editable files are stored in [GitHub](https://github.com/ScilifelabDataCentre/development-guidelines/tree/main/project_management).

When a PR is merged in the `development-guidelines` repository, a new GitHub release is automatically created and the compiled PDF of the project management files are uploaded to the release as an asset.

## Introduction

Many project management processes are decided at the team-level but some DC-level processes exist. Currently, this
consists of:

- A proposal process
- A roadmap process

Ultimately, the goal of both is to:

- Have a written down plan at the kick-off of a project and for each year
- Have a shared format across DC applications
- Ensure key stakeholders have a shared picture of the plan

## Local build

Changes in the project_management directory trigger a GitHub Action to build a PDF using [pandoc](https://pandoc.org/MANUAL.html).
To build it locally, you need Docker, and then run:

`docker build -f .config/pandoc/Dockerfile -t pandoc-latex-lato .`

Create `output` directory.

```commandline
docker run --rm \
  -v "$(pwd)":/output \
  -w /output \
  pandoc-latex-lato \
  "pandoc \
    --output=output/project_management.pdf \
    --defaults=project_management/pandoc_config.yaml \
    --metadata subtitle="Local"
  "
```

> [!WARNING]
> You may need --platform=linux/amd64 in both commands to run on Apple Silicon.
