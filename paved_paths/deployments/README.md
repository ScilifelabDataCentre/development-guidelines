# Deployment of server-side applications

In SciLifeLab Data Centre, we use Kubernetes as the target platform for server-side applications.
In this section, we define the paved path tools for working with Kubernetes and managing your applications effectively.

| Purpose                              | Default Tool                                       | Why?                                                                                                                                                                                                                     | Alternatives                                                                                                                                     |
| ------------------------------------ | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Run Kubernetes locally               | [Rancher Desktop][rancher-desktop]                 | Details in [kubernetes_tools.md](./kubernetes_tools.md#docker-desktop-vs-rancher-desktop)                                                                                                                                | [minikube][minikube]                                                                                                                             |
| Build container images               | [`docker`][docker] (installed via Rancher Desktop) | `docker` is the de facto industry standard for building containers.                                                                                                                                                      | [nerdctl][nerdctl]                                                                                                                               |
| Run containers locally               | [`docker`][docker] (installed via Rancher Desktop) | `docker` is the de facto industry standard for running containers.                                                                                                                                                       | [nerdctl][nerdctl]                                                                                                                               |
| Container registry                   | [GitHub Container Registry][ghcr]                  | GHCR (GitHub Packages) is provided as part of our GitHub organisation.                                                                                                                                                   | Nothing else should be used.                                                                                                                     |
| Package _your_ application           | [Kustomize][kustomize]                             | Kustomize is a great tool to increase code reuse and have different variants for each environment (e.g. changing the hostname between dev and prod).<br>[More details here](./kubernetes_tools.md#helm-vs-kustomize)     | [Helm][helm]. See discussion in [kubernetes_tools](./kubernetes_tools.md).                                                                       |
| Install an off-the-shelf application | [Helm][helm]                                       | Helm is a great tool to install someone else's application in your Kubernetes environment. Pro tip: [include the chart using Kustomize][kustomize-helm]!<br>[More details here](./kubernetes_tools.md#helm-vs-kustomize) | [Kustomize](https://kustomize.io/). See discussion in [kubernetes_tools](./kubernetes_tools.md).                                                 |
| Off-the-shelf applications           | TODO                                               | TODO: Previously Bitnami; under discussion due to licensing changes                                                                                                                                                      | Whatever Helm chart is the "official" for a given application, e.g. [opensearch-project-helm-charts/opensearch][opensearch-helm] for OpenSearch. |
| Secrets management                   | [SealedSecrets][sealedsecrets]                     | SealedSecrets lets you store encrypted files in Git which will be decrypted as regular Kubernetes Secrets once deployed to Kubernetes.                                                                                   | [ExternalSecrets][externalsecrets] is also supported in K1H, but we have no secret store for you to pull secrets from.                           |

[bitnami]: https://artifacthub.io/packages/search?org=bitnami
[docker]: https://docs.docker.com/engine/install/
[externalsecrets]: https://external-secrets.io/
[ghcr]: https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry
[helm]: https://helm.sh
[kustomize]: https://kustomize.io/
[kustomize-helm]: https://kubectl.docs.kubernetes.io/references/kustomize/builtins/#_helmchartinflationgenerator_
[minikube]: https://minikube.sigs.k8s.io/
[nerdctl]: https://github.com/containerd/nerdctl
[opensearch-helm]: https://artifacthub.io/packages/helm/opensearch-project-helm-charts/opensearch
[podman]: https://podman.io/
[rancher-desktop]: https://rancherdesktop.io/
[sealedsecrets]: https://github.com/bitnami-labs/sealed-secrets
