# Agent Task Protocol (ATP) v0.1

ATP defines a minimal protocol for signed task exchange between autonomous agents.

Core elements:
- persistent cryptographic identity
- canonical JSON message signing
- TASK → RESULT | ERROR  message flow
- append-only local history

Transport is transport‑agnostic with HTTP POST used as the reference transport.
