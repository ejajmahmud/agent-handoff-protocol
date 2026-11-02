"""Structured context handoff schema and manager."""
import json
import time
from typing import Dict, Any, List

class HandoffPacket:
    def __init__(self, sender: str, recipient: str, task: str, state: Dict[str, Any], constraints: List[str] = None):
        self.sender = sender
        self.recipient = recipient
        self.task = task
        self.state = state
        self.constraints = constraints or []
        self.timestamp = time.time()

    def serialize(self) -> str:
        return json.dumps({
            "sender": self.sender,
            "recipient": self.recipient,
            "task": self.task,
            "state": self.state,
            "constraints": self.constraints,
            "timestamp": self.timestamp
        }, sort_keys=True)

    @classmethod
    def deserialize(cls, json_str: str) -> "HandoffPacket":
        d = json.loads(json_str)
        pkt = cls(d["sender"], d["recipient"], d["task"], d["state"], d.get("constraints", []))
        pkt.timestamp = d["timestamp"]
        return pkt

class HandoffManager:
    def __init__(self):
        self.history: List[HandoffPacket] = []

    def dispatch(self, packet: HandoffPacket) -> bool:
        if not packet.recipient or not packet.task:
            return False
        self.history.append(packet)
        return True
