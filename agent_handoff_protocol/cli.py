"""Command line interface for agent-handoff-protocol."""
from .handoff import HandoffPacket, HandoffManager

def main():
    mgr = HandoffManager()
    pkt = HandoffPacket("planner", "coder", "write_auth_service", {"db": "postgres"})
    mgr.dispatch(pkt)
    print("Handoff packet dispatched. History count:", len(mgr.history))

if __name__ == "__main__":
    main()
