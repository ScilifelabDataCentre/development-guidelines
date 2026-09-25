# RACI matrix

The RACI matrix is a project management tool to clarify stakeholders' roles and responsibilities.
Each stakeholder or stakeholder group is assigned to one of the following:

| Role        | Description                                                                  |
| ----------- | ---------------------------------------------------------------------------- |
| Responsible | Do the work, can be >1 person                                                |
| Accountable | _1 person_, owner at a high-level, ensures all responsibilities are assigned |
| Consulted   | Give input, e.g. specialist skills                                           |
| Informed    | Require updates                                                              |

As you move down the table (Responsible -> Informed), stakeholders become less involved. That is, the
Responsible team will likely be working on the project or service every day or week, whilst an Informed stakeholder
might receive a monthly summary of progress.

## Why?

- Right people have the right involvement
- Clarify & document who is responsible for what
- The identified stakeholders and their roles should be used to set up the execution/organisation of the work -
  communication channels and ways of working with all stakeholders need to be decided

## Tips

> [!TIP]
> Accountable should be 1 person. ['The buck stops'](https://en.wikipedia.org/wiki/Buck_passing#the-buck-stops-here) with them,
> they should have both the mandate but also are accountable when things do not go to plan. With multiple Accountable
> people, there is a higher risk of no one actually being Accountable.

> [!TIP]
> Keep the stakeholder list short. Only include someone as Consulted or Informed if you plan to actively communicate
> with them. If there’s no clear channel or need for regular updates, they probably don’t need to be included.

## Where do we use the RACI matrix?

### Documentation

- [Project/service proposal](proposal.md)
- [Service roadmap](roadmap.md)

Responsible and Accountable stakeholders should be involved in creating those documents.
Consulted stakeholders should be consulted about relevant sections, e.g. if a software roadmap has a theme that heavily
involves changes to the Kubernetes cluster, the sys admin team would be Consulted and should get to review that section.

### Beyond documentation

The RACI matrix in those documents should have consequences for how the work is organised.

- How are you going to keep the Accountable person informed enough that they are able to give input when required?
- How are the different Consulted stakeholders consulted? Is it on a rolling basis? Are there recurring meetings?
- How are the Informed stakeholders informed? Meetings? Emails? Slides?

## (Fictional) example

_Building a magic carpet_

| Role        | Description                                                                                              |
| ----------- | -------------------------------------------------------------------------------------------------------- |
| Responsible | Team Tyr - actually design and build the carpet                                                          |
| Accountable | Firstname Lastname (Manager) - 'the buck stops with them to ensure that the work gets delivered'                 |
| Consulted   | SciLifeLab Solna operations - need to collaborate them on storage and facilities                         |
| Informed    | SciLifeLab Solna WEG - end-user representative group - want info on when something new will be available |

## Further reading

- https://project-management.com/understanding-responsibility-assignment-matrix-raci-matrix/
- https://www.atlassian.com/work-management/project-management/raci-chart
- https://en.wikipedia.org/wiki/Responsibility_assignment_matrix
- The RACI matrix: Your blueprint for project success. (2022). CIO (0894-9301), N.PAG.
