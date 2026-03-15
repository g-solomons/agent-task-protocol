# Agent Coordination Stack Architecture

Agent Coordination Stack

┌─────────────────────────────────────────┐
│        Economic / Incentive Layer       │
│     (payments, pricing, incentives)     │
└─────────────────────────────────────────┘
                    ▲
                    │
┌─────────────────────────────────────────┐
│              Shared State               │
│   (event streams, databases, blackboard)│
└─────────────────────────────────────────┘
                    ▲
                    │
╔═════════════════════════════════════════╗
║          Task Exchange Layer            ║
║          Agent Task Protocol            ║
║                  (ATP)                  ║
║        TASK → RESULT / ERROR            ║
╚═════════════════════════════════════════╝
                    ▲
                    │
┌─────────────────────────────────────────┐
│           Communication Layer           │
│   (HTTP, messaging, pub/sub, streams)   │
└─────────────────────────────────────────┘
                    ▲
                    │
┌─────────────────────────────────────────┐
│             Identity Layer              │
│   (cryptographic identity, signatures)  │
└─────────────────────────────────────────┘

ATP occupies the task exchange layer within the broader Agent Coordination Stack.
