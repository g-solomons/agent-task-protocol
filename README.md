# Agent Task Protocol (ATP)

ATP is a minimal open protocol for **signed task exchange between autonomous agents**.

ATP v0.1 establishes only three foundations:

- persistent cryptographic identity
- signed task messages
- signed result and error messages

This repository contains the seed specification and a minimal Python reference implementation.

## Quick Demo

Terminal 1:
python examples/beta_agent.py

Terminal 2:
python examples/run_sum_demo.py

Inspect history:
python examples/inspect_history.py data/alpha_history.jsonl
