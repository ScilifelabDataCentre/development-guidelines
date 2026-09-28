# How to Review a Pull Request

It's common to dive into the details immediately when starting a Pull Request (PR) review. For example, many reviewers start by commenting on spelling mistakes, empty lines, or minor bugs. While these _are_ a part of a review, they are not the primary purpose.

The main goal of a PR review is to ensure that changes work as intended, don't negatively affect the rest of the codebase, and are maintainable, while also strengthening shared understanding within the team.

Another important aspect of reviewing is phrasing. It is easy to focus only on the code and forget that there's a person reading and interpreting the comments. The way you phrase your feedback directly affects the team's collaboration and review efficiency.

This document provides guidance for PR reviewers on:

1. What to keep in mind during the review process, including what reviewers are responsible for (and what they are not)
2. How to perform a structured and efficient review

---

## TL;DR

- Review PRs in [three levels](#performing-a-pr-review---3-steps--levels): Understand the what and why → Assess structure and behaviour → Review code details and polish
- Apply the [Return On Investment (ROI) rule](#the-roi-rule-return-on-investment)
- [Phrase feedback constructively](#phrasing) - the goal is to improve the code as a team

---

## Keep this in mind

### Reviewer responsibility

As a reviewer, you are responsible for assessing:

- Correctness
- Risk
- Maintainability

You are **not** responsible for:

- Rewriting working code based on personal preference
- Requesting style changes that are not based on agreed standards

### During reviews and discussions

#### Phrasing

**Guidelines:**

- Use **"we"** - this is a team effort
- Use **"I think"** - you're expressing an opinion, not an absolute truth
- Avoid "you" - it can unintentionally feel personal and risks defensiveness from the PR author
- Make your comments clear and actionable. For example, when suggesting a change, outline a possible improvement or solution.

**Example:**

Instead of writing

> "This is very inefficient"

You could phrase it as

> "I think we can improve the performance here by..."

#### Amount of comments

During the review, if you realise that there will be many suggested changes:

- Suggest a meeting
- Follow up with a summary in the PR of what was discussed and decided

This often saves time and helps avoid misunderstandings.

## Performing a PR review - 3 steps / levels

There's no point in focusing on details before understanding the intent and approach of a PR. For this reason, reviews should be approached on three distinct levels / steps:

1. **High level** - Understand the what and why
2. **Medium level** - Assess the structure and behaviour
3. **Low level** - Review code details and polish

A useful mental model that aligns with these levels:

**Why → What could break → Does it break → Is it clean**

This model describes where to focus first - it does not require each level to be "perfect" before moving on. You do not need separate review rounds for each level.
However, if you identify fundamental issues at one level (e.g. unclear description or structural problems), address those first and wait for the author's response and possible adjustments before continuing. Detailed comments may become irrelevant if there are changes in the implementation.

> [!NOTE]
>
> - In some cases, you might want or need to make changes to someone else's PR. The preferred and recommended approach is to open a PR against the author's branch, not to push changes directly to it. However, if pushing directly is necessary, this should be explicitly communicated within the team and documented in a PR comment.
> - A person performing a high level review does not necessarily need to perform the medium- or low level reviews. For example, a team member who is not a developer might not be able to perform a high-quality code review, but might still have valuable input on the idea behind the PR. However, a medium level review should always be preceded by high level, and low level should always be preceded by both high- and medium level reviews. The PR should only be merged when all review levels have been reviewed and approved.

### 1. **High level** - Understand the what and why

**Goal of this level:** Understand the purpose of the PR and assess potential risks.

1. Read the PR title, description, and additional context provided by the author.

   Ask yourself:
   - Do you understand what the PR is trying to do and why?
   - Does the proposed solution make sense?
   - Does the PR's scope match the task's [acceptance criteria](./README.md#acceptance-criteria)?
   - Does the PR provide enough information?

   **If not:**
   - Ask for clarification before continuing with the review
   - If the scope of the PR seems too large or unclear, consider suggesting that the PR be split into multiple parts

2. Think about what this PR changes and what areas it affects (without diving into the code or starting the service locally)

   You are not validating implementation here.
   You are identifying where extra attention will be needed in the next step.

   Look at:
   - The PR title and description
   - The linked task and Acceptance Criteria
   - The PR template / checklist
   - The list of files changed
   - The overall changes in the diff (`Files Changed` tab)
   - Any screenshots, logs, or short explanations provided by the author

   Ask yourself:
   - What behaviour is changing or being introduced?
   - What parts of the codebase are affected?
   - Does the change touch or involve any sensitive areas such as security, authentication, permissions, data handling, etc?
   - Could the change affect performance?
   - Does it change user-facing behaviour?
   - Does it modify functionality that other parts of the codebase depend on?

### 2. **Medium level** - Assess the structure and behaviour

**Assumption:** The goal and background of the PR are clear.

**Goal of this level:** Validate behaviour and structure. Identify logical bugs, assumptions in the code that might not hold in all cases, and issues in how the solution is implemented or structured.

At this level, look at the implementation with focus on behaviour and structure rather than formatting or minor stylistic details. This may include starting the service locally and manually testing the functionality.

Ask yourself:

- Does the code behave as described in the PR?
- Are edge cases and unexpected situations handled appropriately?
- Are the risks identified in the high-level review addressed?
- Does the PR introduce tests to validate the functionality?
  - Would these tests catch a bug?

### 3. **Low level** - Review code details and polish

**Assumption:** The behaviour and structure of the solution are clear and unlikely to change significantly.

**Goal of this level:** Improve clarity, maintainability, and consistency. Understand code details and suggest possible improvements.

Look at details such as:

- Naming - are variables, classes, and functions clear, self-explanatory and consistent across the codebase?
- Function length - are functions doing one thing, or becoming too large?
- Duplications - is similar code repeated?
- Readability - is the code easy to follow?
- Comments - are comments added where they are useful?
- Docstrings - are functions, classes, and modules clearly explained?
- Consistency with style guidelines (e.g. naming conventions, formatting)
- Unused imports or unused code
- Spelling and typos
- General formatting

This is where the **ROI (return on investment) rule** becomes important.

#### The ROI Rule: Return on Investment

Before requesting changes, ask yourself:

- Is this worth fixing now?
- Is it a blocker?
- Is it a preference?
- Is the change important enough to justify the author's effort?
- Would the suggestion significantly improve readability, maintainability, or reliability?

If the change would significantly increase scope or complexity, consider discussing it with the PR author during a meeting or suggesting it as a separate task.

_When comments and suggestions from this step are resolved, an approval is appropriate and the author can merge the PR._

---

## References & Further Reading

- Google Engineering Practices – Code Review Guidelines  
  https://google.github.io/eng-practices/review/

- Google Engineering Practices – How to Write Code Review Comments  
  https://google.github.io/eng-practices/review/reviewer/comments.html

- Atlassian – Code Review Best Practices  
  https://www.atlassian.com/agile/software-development/code-reviews

- GitHub Docs – About Pull Requests  
  https://docs.github.com/en/pull-requests

- GitLab – Code Review Guidelines  
  https://docs.gitlab.com/development/code_review/

- SmartBear – Code Review Best Practices  
  https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/

- Dorin Baba – The Perfect PR Review Checklist  
  https://medium.com/@dorinbaba/the-perfect-pr-review-checklist-no-one-is-talking-about-50ca213a4ac1

<!-- cspell:ignore Pullpo -->

- Pullpo - Conventional Comments
  https://github.com/pullpo-io/conventional-comments
