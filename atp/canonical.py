import json
def canonical_json(obj):
    return json.dumps(obj, sort_keys=True, separators=(",",":"), ensure_ascii=False)
def canonical_bytes(obj):
    return canonical_json(obj).encode("utf-8")
