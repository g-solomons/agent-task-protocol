import base64, hashlib, json
from pathlib import Path
from nacl.signing import SigningKey

def derive_agent_id(pub):
    return base64.urlsafe_b64encode(hashlib.sha256(pub).digest()).decode().rstrip("=")

def generate_identity():
    sk = SigningKey.generate()
    vk = sk.verify_key
    return {
        "agent_id": derive_agent_id(vk.encode()),
        "public_key": base64.b64encode(vk.encode()).decode(),
        "private_key": base64.b64encode(sk.encode()).decode(),
        "key_type": "Ed25519"
    }

def load_or_create_identity(path):
    p = Path(path)
    if p.exists():
        return json.loads(p.read_text())
    ident = generate_identity()
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(ident, indent=2))
    return ident
