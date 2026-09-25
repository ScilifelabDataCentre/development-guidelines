# Observability

> [!NOTE]
> In distributed systems, [observability](<https://en.wikipedia.org/wiki/Observability_(software)>) is a term that encompasses both collection of metrics, logs and traces to make an application _"observable"_.

| Purpose       | Default Tool                                                             | Why?                                                                                                                  | Alternatives                                                                                                                         |
| ------------- | ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Alerts        | To be decided (probably Grafana)                                                           | To be decided.                                        |                                                                                                                                      |
| Logs          | Logs should be printed to `stdout` as JSON.                              | It's a well-defined format that most people are familiar with. It's very easy to produce and parse.                   | Any logging framework that can produce JSON may be used. Using [logfmt](https://brandur.org/logfmt) instead of JSON is also alright. |
| Metrics       | [OpenTelemetry](https://opentelemetry.io/docs/concepts/signals/metrics/) | OpenTelemetry is a vendor-neutral open standard for most aspects of observability in the cloud native world.          | [Prometheus](https://prometheus.io/)                                                                                                 |
| Traces        | [OpenTelemetry](https://opentelemetry.io/docs/concepts/signals/traces/)  | OpenTelemetry is a vendor-neutral open standard standard for most aspects of observability in the cloud native world. | [Jaeger](https://www.jaegertracing.io/)                                                                                              |
| Web analytics | [Matomo](https://github.com/matomo-org/matomo)                           | It's open source and used by several SciLifeLab applications already.                                                 | If you do not want to integrate with our self-hosted Matomo, consider exposing the analytics data using metrics and traces!          |

## Responsibilities

It's Team Agar's responsibility to implement the observability suite that collects all data and expose it to you in a friendly manner.
If you need to view metrics, traces or logs from your own applications, you will not have to implement a Prometheus backend or Grafana instance, for example.
The only reason for you to maintain separate instances would be if you need to provide your end users with Grafana or Prometheus.

What you will need to implement yourselves is anything that can enrich the data with information specific to your application.
For example:

- All output printed to `stdout` by the Kubernetes platform, but it's up to you to print structured logs with relevant data and different log levels.
- the Kubernetes platform will collect some metrics regarding the CPU and memory usage for all pods, but it has no knowledge about the internals of your application. So if you want to track "the number of logged-in users" or "the number of data objects" in your application over time, you need to expose those metrics so they can be scraped by the Kubernetes platform.
