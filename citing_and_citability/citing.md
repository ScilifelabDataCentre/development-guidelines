# Citing Services and Code

SciLifeLab Data Centre staff should follow the citation instructions provided by the creator of the service or code. If the creator does not supply citation instructions covering the elements listed below, they should instead follow the guidance in this file.

## What a citation must include

| Element                                                         | Service                                                                                                     | Code                                                                                                                                |
| --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Name                                                            | The service name                                                                                            | The software name                                                                                                                   |
| Contributors and organisation                                   | All contributors, plus the affiliated organisation, if applicable                                           | All contributors, plus the affiliated organisation, if applicable                                                                   |
| Version                                                         | Where the version is specified depends on the service. If no version is available, specify the date of use. | The version used. If no version is available, specify the git commit hash. If no git commit hash is available, specify date of use. |
| Globally unique, machine-actionable persistent identifier (PID) | See [Citing a Service](#citing-a-service)                                                                   | See [Citing Code](#citing-code)                                                                                                     |

Format these elements according to the style required by your target journal or publisher. For APA, see the [Uppsala University Library guide to citing software](https://libguides-en.ub.uu.se/apa7/software).

## Citing a Service

When using a service (for example, applying a tool to perform a function, which could include the Data Delivery System to transfer data), cite the first identifier available from this list:

1. The **PID of the publication** describing the service, if one exists.
2. The service's **RRID**.
3. Another suitable PID, e.g. **the service's DOI**.
4. The **URL** of the service (e.g. the website for Serve).
5. The development **repository URL**.

**Referencing a service using an RRID (SciCrunch format):**

```text
<service name> (<access date>), <organisation name>, version <version number> from <URL>, RRID:<RRID>.
```

For further guidance on citing RRIDs see the [SciCrunch page on RRID citations](https://rrid.site/about/guidelines).

## Citing Code

When using the code itself (for example, rewriting or reusing it), cite the first identifier available from this list:

1. The **PID** of the code (e.g. a DOI from Zenodo, or an area-specific repository).
2. The **URL** of the development repository.

**Referencing code using a Zenodo DOI (APA):**

```text
<organisation name>. (<year>). <software name> (Version <version number>) [Software]. Zenodo. https://doi.org/<DOI>
```
