"""Blackboard Pattern Multi-Agent Coordination Engine
100% Python Standard Library.
"""

class BlackboardArchitecture:
    """Shared state space with conditional Knowledge Source execution."""
    def __init__(self):
        self.state = {}
        self.knowledge_sources = []
        self.event_log = []

    def register_ks(self, name, condition_fn, action_fn, priority=1):
        self.knowledge_sources.append({
            "name": name,
            "condition": condition_fn,
            "action": action_fn,
            "priority": priority
        })

    def post(self, key, value):
        self.state[key] = value
        self.event_log.append(f"POST {key}={value}")

    def step(self):
        eligible = []
        for ks in self.knowledge_sources:
            if ks["condition"](self.state):
                eligible.append(ks)
        if not eligible:
            return None
        eligible.sort(key=lambda k: k["priority"], reverse=True)
        chosen = eligible[0]
        chosen["action"](self)
        return chosen["name"]
