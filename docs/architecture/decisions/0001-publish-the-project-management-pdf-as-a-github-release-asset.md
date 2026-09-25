<!--
ADR (Architecture Decision Record) template

This template is copied from the linked template in the development-guidelines repository.
Link to guidelines (latest version): https://github.com/ScilifelabDataCentre/development-guidelines/tree/main/adrs

Name the file NNNN-short-title.md, where NNNN is the next number in line.
    Example: '0001-some-decision.md' exists -> next ADR file becomes '0002-another-decision.md'.
Use the unpadded number in the title.
    Example: '0001-some-decision.md' -> "# 1. Some decision"
-->

# 1. Publish the Project Management PDF as a GitHub release asset

Date: 2026-07-06 <!-- YYYY-MM-DD -->

## Status

Accepted <!-- One of: Accepted, Deprecated, Superseded -->
<!-- If Superseded, add: Superseded by {{ SUPERSEDING_ADR_NUMBER }} -->

## Context

The development-guidelines repo has a project_management directory and when there's a change to that or some other related file, there's a new PDF generated in the PR. There's then an instruction to the author to upload said file to the Google Drive. This is manual work that should be avoided. The initial goal of this was to have versioning of the PDF. <!-- What is the issue that we're seeing that is motivating this decision or change? -->

## Decision

Use GitHub Actions to automatically release a new version of the Project Management PDF whenever there's a change in a file related to the project_management directory. <!-- What is the change that we're proposing and/or doing? -->

## Consequences

<!-- What becomes easier or more difficult to do because of this change? -->

- No manual upload to Google Drive
- Everything kept in the same place in GitHub
- This can be extended to more PDFs later

**BUT**

- The file's location and intent need communicating

<!-- Optional section.
Uncomment if relevant for decision and fill with sources.

## References

{{ REFERENCES }}
-->
