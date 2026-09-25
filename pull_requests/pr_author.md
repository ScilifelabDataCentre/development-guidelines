# How to Prepare a Pull Request for Review

Preparing a Pull Request (PR) properly before requesting a review saves time and effort for everyone involved. A well-prepared PR reduces back-and-forth discussions, shortens review time, and increases overall code quality.

This document provides guidance for PR authors on:

1. What to keep in mind during the review process
2. How to prepare a PR before marking it as ready

A PR should only be marked as **Ready for Review** when you believe it could be merged in its current state.

This document complements the [**Pull Request Guidelines**](./README.md).

---

## TL;DR

Before marking a PR as **Ready for Review**, ask yourself:

- Does the PR clearly explain what the change does and why?
- Is the scope reasonable?
- Does it meet the Acceptance Criteria as defined in the task?
- Does it meet the Definition of Done (DoD)?
- Have I [reviewed it myself](#5-self-review-before-requesting-review)?
- Would I merge this if I were the reviewer?

If not, it's probably not ready for a review yet.

The items above are described in more detail in the sections below.

---

## Keep this in mind

### Preparation mindset

- Think: "Have I made this easy to review?"
- The goal is clarity and quality aligned with the Definition of Done (DoD), **not** perfection
- Draft PRs are encouraged
- Ask questions as early as possible. Align with the team **before** putting a huge amount of work in
- If you need feedback in the middle of a task (e.g. you're stuck or have worked on something for a long time), consider:
  - Splitting the task into smaller subtasks (you can speak to your project leader about this)
  - Discussing in person instead of pushing half-ready review work onto others
- Mark the PR as **Ready for Review** only when you believe it could be merged as-is

### During reviews and discussions

- Your code is not your child
  - Try not to take comments or suggested changes personally. The feedback is directed at the code, not you as a person.
- Comments and discussions improve code quality
- Leaving and receiving comments is in the team's best interest
- When responding to feedback:
  - Use "we should" / "I think", etc
  - Focus on improving the solution, not defending the implementation

## Preparing a PR – Before Marking It Ready for Review

### 1. Write an Informative Title

A good title helps reviewers quickly understand the purpose of the change.

- Use imperative mood, for example:
  - `Add` instead of `Adding`
  - `Fix` instead of `Fixing`
- Think of it as a command: "This PR will..."

### 2. Explain the Change

Not everyone knows or understands the problem. Without context, reviews slow down significantly.

Your PR description should:

- Explain **why** the change is needed
- Describe **what** was done
- Clarify anything that might be unclear to a reviewer
- Mention related issues or tasks
- Highlight breaking changes if there are any

### 3. Keep the PR Focused

Each PR should address a specific task as defined in Jira.

- Split the PR into smaller, focused pieces if it contains multiple independent changes
- Refactoring and feature work in the same PR should be avoided
- Unrelated changes should be moved to a new task / PR

The reasoning behind this is that oversized PRs:

- Overwhelm reviewers
- Slow down review cycles
- Lead to less thorough reviews

### 4. Align with the DoD

Every PR must satisfy the shared Definition of Done. Use a PR template checklist to keep track of this, e.g. [this template](https://github.com/ScilifelabDataCentre/data-centre-template/blob/main/.github/pull_request_template.md) in the `data-centre-template` repository.

This ensures:

- All PRs meet the same standard
- Reviewers focus on important aspects instead of basic fixes
- Reduced back-and-forth

The DoD is explained in the [README](./README.md).

### 5. Self-Review Before Requesting Review

Before requesting a review, open your PR and review it as if you were not the author. This reduces trivial reviewer comments and improves review quality.

Ask yourself:

- Have I explained the what and why?
- Does the logic make sense?
- Is naming clear?
- Are there obvious bugs?
- Did I leave debug code?
- Did I include unrelated changes?
- Is the implementation consistent with the task and existing design?
- If this wasn't my code, would I approve it?

#### The ROI Rule: Return on Investment

Reviews should not replace basic self-quality checks and not every suggestion must block a merge.

Before requesting a review, ask yourself:

- Is this ready, or am I pushing work onto the reviewer?
- Did I fix obvious small issues?
- Is this the right time to request feedback?
- Would a short meeting be more efficient than a PR discussion?

---

## References & Further Reading

The guidelines above are based on widely accepted engineering practices for code review and collaboration. The following resources provide additional perspectives and practical guidance:

- **Google Engineering Practices – Code Review Guidelines**  
  https://google.github.io/eng-practices/review/

- **Atlassian – What is Code Review?**  
  https://www.atlassian.com/agile/software-development/code-reviews

- **Atlassian – Definition of Done**  
  https://www.atlassian.com/agile/project-management/definition-of-done

- **GitLab – What is Code Review?**  
  https://about.gitlab.com/topics/version-control/what-is-code-review/

- **GitHub Docs – About Pull Requests**  
  https://docs.github.com/en/pull-requests

- **Dorin Baba – The Perfect PR Review Checklist No One is Talking About**  
  https://medium.com/@dorinbaba/the-perfect-pr-review-checklist-no-one-is-talking-about-50ca213a4ac1
