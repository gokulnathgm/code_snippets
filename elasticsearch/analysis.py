import json
file = open("world_bank.json")
for line in file:
	parse = json.loads(line)
print parse.keys()
