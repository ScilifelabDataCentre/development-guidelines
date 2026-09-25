# Comparisons of deployment-related tools

This document concerns the deployment of server-side applications (mostly related to Kubernetes).

## Helm vs Kustomize

When building manifests to deploy your application in Kubernetes, you need a tool to manage them. Kustomize help you increase code reuse by having different variants for each target environment (e.g., changing the hostname between dev and prod).

If you intend to package an application that should be _installed_ by other teams, Helm is a better alternative than Kustomize.
Helm provides more powerful templating than Kustomize, since it's intended to be a package manager.
This increased complexity is needed if you want to publish your application online for others to install.
But if it's just a matter of changing from `dev` to `prod`, then Kustomize is way easier to use to manage that.

It is possible to install Helm charts using Kustomize. This is a convenient way to include third party dependencies (such as PostgreSQL or OpenSearch) via Helm while still using Kustomize to manage your application.
For details, see <https://kubectl.docs.kubernetes.io/references/kustomize/builtins/#_helmchartinflationgenerator_>

## Docker Desktop vs Rancher Desktop

Docker Desktop is the most popular software for running containers on your personal machine or running a virtual Kubernetes cluster.
It integrates well with other applications and has a lot to offer.
Yet we cannot recommend it since it is a closed source software with a proprietary license that requires a paid license to run if you work for a large organisation.

It's worth noting here that the `docker` command line interface (Docker Engine) _is_ open source and does not come with a restrictive commercial license.
Unfortunately, the `docker` CLI is not provided as a pre-built binary for Mac or Windows, only Linux.

Rancher Desktop offers much of the same functionality as Docker Desktop, but is open source and comes bundled with some useful tools (like `docker` and `nerdctl`).
