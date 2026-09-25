# Making Services and Code Citable

All services and code should include clear instructions for how they should be cited, both on the service itself and in accompanying user-facing documentation.

Descriptive metadata (authors, affiliations, keywords) should be added to records (paper, RRID metadata, Zenodo metadata) to ensure accurate citation and improve discoverability.

> [!IMPORTANT]
> **Your instructions should clearly provide the elements listed in [What a citation must include](./citing.md#what-a-citation-must-include).**

> [!TIP]
> An example of instructions on how to cite a service can be found on the data.scilifelab.se page ["How to cite the Platform"](https://data.scilifelab.se/about/citation/).

## What you need to put in place

### Services

#### RRID

All SciLifeLab services should acquire an RRID, even when another PID (e.g. the PID of an associated publication) is available.

Follow these steps to acquire an RRID for your service:

1. Go to the [Resource Identification Portal](https://rrid.site/about/resource) and select _‘Suggest a resource (resources include software, organisations, databases, etc). Organisms and antibodies should not be submitted to the resource registry.'_.
2. The curators assess the suggestion, and determine whether it is suitable. If it is, then you will be emailed an RRID for your service. This typically occurs within 24 hours.
3. The curators will then fill in all of the additional information about the service, and it will appear on their database within 2 days.
4. Note that anyone can create an RRID for a resource, to edit or update the record you must claim ownership by logging in and demonstrating a connection to the service (for example, by linking to the SciLifeLab DC staff list).

#### FAIRsharing

You should also register your service for [FAIRsharing](https://fairsharing.org/) to demonstrate FAIR compliance. Note that the FAIRsharing process takes a considerable amount of time (with records often being confirmed by moderators months later), so it's best to apply relatively quickly, and the DOI you get is only for the FAIRsharing record (not for citation).

### Code

#### DOI via GitHub and Zenodo

A DOI should be acquired for the code, ideally by an automated link between the GitHub repository and Zenodo entry so that DOIs are generated for versions of the code.

Follow these steps to acquire a DOI for your code:

1. For guidance on how to set this up, follow the [instructions provided by Zenodo](https://help.zenodo.org/docs/github/), and the [instructions provided by GitHub](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content).
2. Add the Zenodo badge to the README file of your development repository.
3. Add a [CITATION.cff file](#citationcff) to your repository, as Zenodo's autofill information is likely to be incorrect.

> [!NOTE]
> Zenodo entries are linked to individual accounts. This can be changed by Zenodo, even if the previous owner does not respond. However, in order to avoid problems, make sure to follow the correct off-boarding practices and move records to another owner in the event that you leave SciLifeLab.

#### CITATION.cff

1. Create a `CITATION.cff` in your repository.
2. In the file:
   - List all individual contributors and their ORCIDs
   - Include SciLifeLab Data Centre (or relevant group) as the final author to reflect institutional ownership, replacing the ORCID of the SciLifeLab entry with the [SciLifeLab RORID](https://ror.org/04ev03g22).
   - **Omit** the version and date fields in the CITATION.cff file - including them overrides Zenodo’s metadata.
