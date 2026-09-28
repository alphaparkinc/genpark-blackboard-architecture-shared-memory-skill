import sys
import json
from client import BlackboardArchitecture

bb = BlackboardArchitecture()
bb.post("system_status", "operational")
bb.register_ks("HealthCheckKS", lambda s: s.get("system_status") == "operational", lambda b: b.post("last_verified", True), priority=5)

def handle_rpc(line):
    global bb
    try:
        req = json.loads(line)
    except Exception:
        return
    req_id = req.get("id")
    method = req.get("method")
    params = req.get("params", {})

    if method == "initialize":
        res = {
            "protocolVersion": "2024-11-05",
            "serverInfo": {"name": "genpark-blackboard-architecture-shared-memory-skill", "version": "1.0.0"},
            "capabilities": {"tools": {}}
        }
    elif method == "tools/list":
        res = {
            "tools": [
                {
                    "name": "post_fact",
                    "description": "Post new fact or observation to shared blackboard memory",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "key": {"type": "string"},
                            "value": {"type": "string"}
                        },
                        "required": ["key", "value"]
                    }
                },
                {
                    "name": "run_agenda_step",
                    "description": "Trigger agenda controller evaluation cycle for active knowledge sources",
                    "inputSchema": {"type": "object", "properties": {}}
                }
            ]
        }
    elif method == "tools/call":
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "post_fact":
            bb.post(args.get("key"), args.get("value"))
            res = {"content": [{"type": "text", "text": json.dumps({"status": "posted", "state": bb.state})}]}
        elif tool_name == "run_agenda_step":
            fired = bb.step()
            res = {"content": [{"type": "text", "text": json.dumps({"executed_ks": fired, "current_state": bb.state})}]}
        else:
            res = {"isError": True, "content": [{"type": "text", "text": f"Unknown tool {tool_name}"}]}
    else:
        res = {"error": {"code": -32601, "message": "Method not found"}}

    resp = {"jsonrpc": "2.0", "id": req_id, "result": res.get("result", res)}
    sys.stdout.write(json.dumps(resp) + "\n")
    sys.stdout.flush()

def main():
    for line in sys.stdin:
        if line.strip():
            handle_rpc(line.strip())

if __name__ == "__main__":
    main()
