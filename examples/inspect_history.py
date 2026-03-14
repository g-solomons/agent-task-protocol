import sys, json
for line in open(sys.argv[1]):
    e=json.loads(line)
    print(e["direction"], e["message"]["message_type"])
