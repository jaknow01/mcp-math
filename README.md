# mcp-math

Exact calculations over numbers, as an [MCP](https://modelcontextprotocol.io) server — so a
model computes averages, trends and correlations in code instead of in its head. No data
source of its own: the client passes the numbers.

| Tool | What it does |
|---|---|
| `calculate_statistics` | count, sum, mean, median, min, max, range, standard deviation, variance |
| `percentage_change` | absolute and % change between an old and a new value |
| `linear_trend` | least-squares slope/direction over an ordered sequence |
| `correlation` | Pearson correlation of two equal-length series |
| `whoami` | which client your key belongs to |

Part of the Jarvis tool servers; built on
[jarvis-mcp-kit](https://github.com/jaknow01/jarvis-mcp-kit) (API keys, rate limits, logs).

## Run

```bash
cp config/clients.example.yaml config/clients.yaml
uv run jarvis-mcp-keys new me --servers math     # paste the printed block into config/clients.yaml
uv run mcp-math serve                            # http://localhost:8010/mcp/math
```

Docker: `docker run -p 8010:8010 -v $PWD/config:/config ghcr.io/jaknow01/mcp-math:latest`.
Kubernetes: `deploy/kubernetes.yaml`.

## Connect

- **Claude Code:** `claude mcp add --transport http math https://<host>/mcp/math --header "Authorization: Bearer jvk_…"`
- **Claude app (custom connector):** URL `https://<host>/mcp/math/jvk_…` (key in the path, no OAuth)
- **Jarvis:** an entry in its `config/subagents.yaml` pointing at the in-cluster URL.

Configuration: see `.env.example` and the [kit README](https://github.com/jaknow01/jarvis-mcp-kit#environment).
