# genpark-blackboard-architecture-shared-memory-skill

> Blackboard pattern architecture for multi-agent coordination with Knowledge Sources and prioritized agenda controller.

Part of the **GenPark AI Agent Skills Matrix**. Production-ready, zero external dependencies, native Python 3.9+ standard library.

## Architecture

```mermaid
flowchart TD
    A[Environment Perception / Goal] --> B[Blackboard / BDI Deliberator]
    B --> C[Contract Net / Task DAG Pipeline]
    C --> D[Subsumption Action Execution]
    D --> E[MCP Protocol Endpoint]
```

## Features
- **Zero Third-Party Dependencies**: Pure Python standard library (`collections`, `heapq`).
- **Autonomous Swarm Intelligence**: Blackboard pattern, Critical Path DAG scheduler, Contract Net Protocol auctions, Subsumption architecture, and BDI reasoning.
- **Native MCP Protocol Support**: Integrated JSON-RPC 2.0 stdio server ready for Claude Desktop, Cursor, and Windsurf.

## Installation

```bash
pip install genpark-blackboard-architecture-shared-memory-skill
```

Or clone directly:

```bash
git clone https://github.com/alphaparkinc/genpark-blackboard-architecture-shared-memory-skill.git
cd genpark-blackboard-architecture-shared-memory-skill
python example_usage.py
```

## Quick Start

```python
from client import *
# Refer to example_usage.py for end-to-end execution
```

## Model Context Protocol (MCP) Setup

Add to your `claude_desktop_config.json` or `cursor.json`:

```json
{
  "mcpServers": {
    "genpark-blackboard-architecture-shared-memory-skill": {
      "command": "python",
      "args": ["-m", "genpark-blackboard-architecture-shared-memory-skill.mcp_server"]
    }
  }
}
```

## License
MIT License. Copyright (c) 2026 AlphaPark Inc. & Alpha-Park.
