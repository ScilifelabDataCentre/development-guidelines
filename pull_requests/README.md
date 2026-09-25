# Pull Request Guidelines

The goal of this guide is to establish a shared Pull Request (PR) process for the Data Centre.

The aim is to:

- Improve collaboration
- Increase efficiency
- Strengthen software reliability

This is an evolving document intended to help us continuously improve how we work — not a rigid framework.

The guide begins with information that is relevant to both PR authors and reviewers. Later, [`pr_author.md`](./pr_author.md) and [`pr_reviewer.md`](./pr_reviewer.md) will cover guides for these two roles, so that it is clear what to do when writing or reviewing a PR.

## Definition of Done (DoD)

The Definition of Done (DoD) defines what "done" means. For PRs, it provides a shared baseline for when the PR can be considered complete and ready to merge.

Both authors and reviewers should refer to the DoD and the [Acceptance Criteria](#acceptance-criteria) when evaluating a PR.

### Why use a DoD?

The DoD helps prevent common issues such as:

- **Multiple approvals**

  When everyone adheres to the same definition, there’s usually no need for excessive reviews and approvals.

- **Merges blocked due to minor issues or personal preferences**

  If it’s a “nice-to-have” and not a must, it’s not in the scope of the task, and should therefore not block a merge.

- **Premature merges**

  Merging before a PR reaches an agreed standard often leads to additional work later, slowing the team.

- **Moving goalpost**

  During development and review, it’s easy to think of additional improvements and enhancements. The DoD helps keep discussions focused on the original scope of the task. The goal of a PR is to complete the task as defined, **not** to create the most perfect or optimised code possible.

### A PR is ready to merge when

- **The branch is up to date with `main`** (or `master` for some repositories)

- **The change works as expected**
  - The expected behaviour matches what is defined in the task and / or during sprint planning
  - If you have attempted to fix a bug in the PR, the bug should actually be fixed before you merge
  - If you have introduced a new feature, the feature should work as you (and the team) intended

- **Quality standards are met.** This means:
  - All configured checks (tests, linters, formatters, CI workflows, etc) pass
  - Unused code has been removed
  - Debug leftovers have been removed
  - Naming and structure follow the agreed upon conventions. For SciLifeLab Data Centre, it’s the [Google Style Guide](https://google.github.io/styleguide/) and the [development guidelines](https://github.com/ScilifelabDataCentre/development-guidelines).
  - If you have changed the behaviour of a feature, tests should confirm that it works as expected

- **Risks have been considered.** This does not mean that the PR has to have dealt with all potential risks to the fullest possible degree. Rather, it means that:
  - Edge cases have been handled according to what was defined in the task and / or during sprint planning
  - There are no obvious breaking changes
  - There are no known security or data integrity risks introduced

- **The changes made in the PR are documented appropriately.** For example:
  - The PR includes a clear description
  - Documentation has been updated if needed
  - Any changes in configuration have been documented
  - If there are any breaking changes, they are clearly stated
  - The PR has been reviewed and approved
  - There are no known unresolved blocking issues / PRs

- **The code is ready for a review** according to rules defined in the section for PR authors

  The PR author section partly overlaps with the items above.

**The PR author is by default responsible for merging after approval.** If the author chooses to delegate that responsibility, they should communicate it clearly through a PR comment.

The guides on how to prepare a PR and how to review one are directly connected to the DoD. Together, they help ensure that changes are prepared thoroughly and evaluated consistently.

## Acceptance Criteria

While the DoD sets general conditions that apply to **all tasks**, Acceptance Criteria clarify what "done" means for **a specific task**. Task-specific **acceptance criteria** should be outlined where the original task is defined, e.g. in Jira.

> **Example:**
>
> _Task:_ Add a new button to the page
>
> _Acceptance Criteria:_
>
> - The button is visible
> - The button has the correct label
> - Clicking the button results in the intended action

## Suggestion: Rotate review responsibility

As the title indicates, this is a suggestion. Its usefulness depends on the team's composition (size, skills, and workload), so it is recommended that each team discuss whether this would be useful.

### The suggestion

- Rotate review responsibility periodically to improve the flow and distribute responsibility across the entire team.
- Assign a backup in case the review responsible team member is away (and as a first line for delegations).

In addition:

- Agree on a reasonable timeframe for how long a PR should remain open before it is revisited, updated, or closed (e.g. 2 sprints).

### Why?

PRs can quickly pile up and remain open if responsibility is unclear. Teams often fall into one of two patterns: one person handles most reviews or all reviews on a given topic (creating knowledge silos and key-person dependency), or everyone reviews everything (leading to inefficiency).

Rotating review responsibility helps:

- Prevent PR backlogs
- Distribute review workload more evenly across the team
- Reduce key-person dependency over time
- Increase shared understanding of the codebase

Defining a reasonable timeframe for open PRs helps to prevent outdated or irrelevant changes from lingering and becoming difficult to review, and minimises risk of merge conflicts.

### Responsibility of the assigned reviewer

The assigned reviewer is responsible for ensuring that PRs are reviewed and move forward - not necessarily for performing every technical review themselves.
When specific domain knowledge is required for a review, they can delegate the technical review to another appropriate team member.
However, the responsibility for ensuring that the PR moves forward remains with the assigned reviewer during that period.

If the assigned reviewer is also the author of a PR, they are responsible for delegating the review to another team member. Merging your own PR without a team review should not happen unless absolutely necessary, for example, if there’s a critical bug requiring an immediate fix and no team member is available to perform a review.

<!-- cspell:ignore Standup -->

When delegating a review to another team member, first communicate with them via Slack and / or during a meeting (e.g. Daily Standup) and then assign them as a reviewer in the PR. If they do not agree, discuss within the team to decide on the reviewer.

---

## References & Further Reading

- Atlassian – What is Code Review?

  https://www.atlassian.com/agile/software-development/code-reviews

- Atlassian – Definition of Done  
  https://www.atlassian.com/agile/project-management/definition-of-done

- Google Engineering Practices – Code Review Guidelines  
  https://google.github.io/eng-practices/review/

- GitLab – What is Code Review?  
  https://about.gitlab.com/topics/version-control/what-is-code-review/

