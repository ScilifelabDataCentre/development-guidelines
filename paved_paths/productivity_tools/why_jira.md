# Why is Jira the paved path tool for project management/issue tracking?

## What is a project management/issue tracking tool?

- A tool for tracking work for software development.
- Allows documenting of ideas/issues, assignment of work to team members, planning and discussion.
- May (or may not) allow end-users to view the status of issues in the backlog.

## Why Jira?

- SciLifeLab has a Jira instance, which DC manages.
- Most of DC's teams already use Jira. Aside from familiarity with the tool, this also means that people who
  work across team/products can easily view their assigned work [in one place](https://scilifelab.atlassian.net/jira/your-work).
- Teams in DC often have a mix of people who do and don't do development work, so there are often people who are already
  working in Jira but not in GitHub.
- Jira is flexible and has many features. It can be configured to accommodate a wide range of team workflows.

## What are the downsides?

- Separating the issue tracking from the open source code in GitHub is a barrier to external contributors. Technically,
  a Jira project can be configured to be open so that external contributors can find, create etc. tickets.
- Jira configuration can be complicated and unintuitive.

### GitHub Issues

- The choice of Jira over GitHub Issues is fundamentally due to weighting the ease of working _within_ DC, especially
  when many teams work on multiple services and not all team members are developers, over the ease of onboarding external
  collaborators.
- DC repositories currently have almost no outside collaborators and, for many (but not all) repos, it is unlikely that
  we will ever have external collaborators.
- If you have a repository where creating an open source community with external collaborators is key, consider GitHub
  Issues.
