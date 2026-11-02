"""Unit tests for HandoffProtocol."""
import unittest
from agent_handoff_protocol.handoff import HandoffPacket, HandoffManager

class TestHandoff(unittest.TestCase):
    def test_packet_serialization(self):
        pkt = HandoffPacket("agent_a", "agent_b", "refactor", {"file": "app.py"}, ["no_breaking_changes"])
        raw = pkt.serialize()
        restored = HandoffPacket.deserialize(raw)
        self.assertEqual(restored.sender, "agent_a")
        self.assertEqual(restored.task, "refactor")
        self.assertEqual(restored.state["file"], "app.py")

if __name__ == "__main__":
    unittest.main()
