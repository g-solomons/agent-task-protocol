import json, uuid, datetime
from pathlib import Path

def append_history(path, direction, status, message):
    event={
        "event_id":"evt-"+str(uuid.uuid4()),
        "recorded_at":datetime.datetime.utcnow().isoformat()+"Z",
        "direction":direction,
        "verification_status":status,
        "message":message
    }
    p=Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p,"a") as f:
        f.write(json.dumps(event)+"\n")
