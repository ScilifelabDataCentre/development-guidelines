# Paved Paths

This directory documents the "paved path" - the recommended, supported default technology choices and practices for new DC-managed software projects and major rewrites.
The defaults are intended to make projects easier to start, review and maintain. Deviations are allowed but must be justified in an Architectural Decision Record (ADR).

## How are the defaults chosen?

We pick and update each default based on a pragmatic balance between the qualities of the tool such as being open source and well documented, and DC-specific considerations, such as existing use in multiple locations and expertise within the DC team.

## How should you use these paved paths?

If you are introducing a new tool to DC software or starting a software from scratch, check whether there is an applicable paved path choice (see [Paved Path Areas](#paved-path-areas)).
This also applies if we are forking an existing open source project or working as part of a collaboration.

We do not necessarily aim to migrate all existing tools to use these defaults, though that may be appropriate in some cases.

## Paved Path Areas

The table below contains all areas currently covered by our paved path. Each area is covered by a separate subdirectory; Go to the directory's README to see which defaults and alternatives there are, as well as the rationale behind the decisions. Some of the areas also have more elaborate explanations and motivations, usually covered by separate files.

| Area                                   | Directory                                       | Covers                                              |
| -------------------------------------- | ----------------------------------------------- | --------------------------------------------------- |
| Languages                              | [languages](./languages/)                       | Programming languages                               |
| Web development                        | [web_development](./web_development/)           | Frameworks and tools for web applications (**WIP**) |
| Desktop application development        | [desktop_applications](./desktop_applications/) | Tools for creating desktop applications             |
| Linting & static analysis              | [linting](./linting/)                           | Formatting, linting, and code quality tools         |
| Testing                                | [testing](./testing/)                           | Automated testing and quality assurance             |
| Databases                              | [databases](./databases/)                       | Different database options depending on purpose     |
| Data storage                           | [data_storage](./data_storage/)                 | Data storage options (**WIP**)                      |
| Deployment of server-side applications | [deployments](./deployments/)                   | Tool options for working with kubernetes            |
| Observability                          | [observability](./observability/)               | Logging, metrics, traces, and analytics             |
| Productivity tools                     | [productivity_tools](./productivity_tools/)     | Project tracking and team collaboration             |

## How to propose updates

There are lots of reasons you might want to suggest an update. Common reasons are:

- A tool is no longer the best default because it is becoming obsolete.
- There's a type of tool that lots of the team will use.
- A type of tool is becoming irrelevant.

### Step by step

1. To propose a change in a paved path, [open an issue](https://github.com/ScilifelabDataCentre/development-guidelines/issues) and pick the template "Paved Path proposal". Fill in the fields and submit.
2. The [code owner](../.github/CODEOWNERS) reviews the proposal and verifies that it contains enough information.
3. The code owner tags the developers and / or another relevant group in the proposal. A review deadline is decided on, e.g. 2 weeks, by which anyone can voice their opinions if they have any. Anyone can at any time suggest that the proposal is discussed during e.g. a developer meeting.
4. The proposal is approved if there are no unresolved objections by the deadline. The code owner makes the call.
5. If approved, the proposer or the code owner opens a PR updating the paved path. If an ADR is needed, it goes in the same PR, written from what's in the issue.
6. The code owner checks that the PR matches what was approved in the issue. No discussion is reopened. The code owner approves and merges the PR, and the proposal is the new default.

_If the proposal was rejected_: The code owner closes the issue with a short reason so that there's a record if and when it comes up again.
