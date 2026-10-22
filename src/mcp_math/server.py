"""The `math` MCP server instance and its tool guide."""

from jarvis_mcp_kit import ToolServer

INSTRUCTIONS = (
    "Exact calculator. Use these tools for any arithmetic or statistics over numbers instead "
    "of computing in your head: summary statistics (average, median, min, max, sum, standard "
    "deviation), the percentage change between two values, a linear trend over an ordered "
    "sequence, and the correlation between two series. Pick the tool that matches the request, "
    "pass the numbers through verbatim (oldest first for sequences) and report the results as "
    "returned. The server has no data of its own — gather the figures first (e.g. a price "
    "history from another tool), then pass them here."
)

server = ToolServer("math", title="Jarvis Math", instructions=INSTRUCTIONS)
