# Architectural Decision Records (ADRs)

We use ADRs as the primary mechanism for documenting important architectural decisions. They should capture the rationale
for decisions which are key choices for the software and which would be a significant amount of work to change later.

## Why?

- Ensures the rationale is explained properly for initial review.
- Records the details before they are forgotten/lost, which is useful when onboarding new team members and to prevent
  decisions being unnecessarily reinvestigated.
- Can inform other teams that encounter the same situation.

## How to use ADRs

_ALWAYS_

- Use the [ADR template](https://github.com/ScilifelabDataCentre/data-centre-template/blob/main/docs/architecture/decisions/adr-template.md?plain=1) in the `data-centre-template` repository.
  - The template is based on a [template/format by Michael Nygard](https://github.com/architecture-decision-record/architecture-decision-record/blob/464354b7d94901916542f64eb8b62dc9048a6486/locales/en/templates/decision-record-template-by-michael-nygard/index.md).
- Use the standard file naming convention, i.e. 0001-something-architectural.md, 0002-some-other-thing.md.
- Consider before the ADR is public whether there is some reason why this specific decision should be internal only.

_IDEALLY_

- Keep the ADRs in the repository with the code. We recommend a `./docs/architecture/decisions` directory.
- Use diagrams for complex ideas. [Mermaid](https://mermaid.js.org/) is good for diagramming, as per the Paved Path
  Tools.

_DO NOT_

- Update merged ADRs retrospectively, except for the _Status_ field. They serve as a record for past decisions.
- Use ADRs to store policies.

## Examples: Good and bad uses of ADRs

### :green_circle: Good

- Should we use a static web framework?
- How will we handle authentication in this system?
- How is this system going to integrate with another existing system?

### :red_circle: Bad:

- What colour should we set this button on this page? (_Not significant enough_)
- Should we sanitise user input? (_This is industry standard and should not be a question_)
- Which Python variable naming convention should we use? (_Enforce this with linting_)

## References

[Command line tool to standardise ADR creation/management](https://github.com/npryce/adr-tools)

[Microsoft](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record),
[AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/introduction.html),
[GCP](https://cloud.google.com/architecture/architecture-decision-records),
[RedHat](https://www.redhat.com/en/blog/architecture-decision-records) and
[the British Government Digital Service](https://gds-way.digital.cabinet-office.gov.uk/standards/architecture-decisions.html)
all recommend using ADRs.

[Definitions, templates and examples](https://github.com/joelparkerhenderson/architecture-decision-record)

[Further collected resources](https://adr.github.io/)
