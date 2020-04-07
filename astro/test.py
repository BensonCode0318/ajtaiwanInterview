import json
with open('output.json', 'r+') as f:
    a = json.loads(f.read())
    print(a)
    