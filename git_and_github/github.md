# GitHub

## Authentication

- All users must use 2FA (2 Factor Authentication) - this is enforced by the Organisation settings.
  - [Follow GitHub's instructions](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication)
  - Make sure that you keep the backup codes and/or set up multiple ways to login in case you e.g. lose your phone
- Each user should configure commit signing - see [instructions](commit_signing.md).

## Repositories

- Any repo for a DC service or component belongs in our [organisation](https://github.com/ScilifelabDataCentre).
- Make repos public from the start, unless there’s a specific reason why they cannot be (e.g. deployment repos).
- Always add a brief _About_ to any repo, even if it's a PoC (Proof of Concept) or test that you're working on alone.

![Example 'About' section of a repo](images/example_github_about.png)

- Use the [data-centre-template](https://github.com/ScilifelabDataCentre/data-centre-template) for new repositories (WIP).
  This contains elements all our repositories should have, including:
  - 1 or 2 LICENSE files at the top-level
  - CODEOWNERS file
  - Code signing required for `main`

## Members, roles & teams

- Add collaborators (i.e. non-DC staff) who need additional privileges to repositories as External Collaborators, rather
  than organisation members.
- Add people to teams, rather than individually to repos or higher-level groups (e.g. developers). This helps keep
  permissions consistent and tidy.
- Teams in the organisation that contribute to development in GitHub have a corresponding GitHub Team.
  - The naming convention is 'TeamXxxx', e.g. TeamHermes, TeamFreya.
  - Create additional sub- or cross-cutting teams as necessary. Prefer CamelCase with no spaces and populate the team
    description.
