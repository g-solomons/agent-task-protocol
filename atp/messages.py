import uuid, datetime

def ts():
    return datetime.datetime.utcnow().replace(microsecond=0).isoformat()+"Z"

def msg_id():
    return "msg-"+str(uuid.uuid4())

def build_task(sender, recipient, task_id, task_type, input_data, deadline=None):
    return {
        "protocol":"ATP/0.1",
        "message_type":"TASK",
        "message_id":msg_id(),
        "sender_id":sender,
        "recipient_id":recipient,
        "timestamp":ts(),
        "payload":{
            "task_id":task_id,
            "task_type":task_type,
            "input":input_data,
            "deadline":deadline
        }
    }
