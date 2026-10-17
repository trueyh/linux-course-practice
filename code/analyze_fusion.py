import json

with open("data/fusion_result.json", encoding="utf-8") as f:
    data = json.load(f)

rules = data["session_and_graph_id_0_0"]["graph_fusion"]
count = 0

print("Rules with effect_times > 0:")
for name, counters in rules.items():
    effect = int(counters["effect_times"])
    if effect > 0:
        print(name, effect)
        count = count + 1

print("Total rules:", len(rules))
print("Rules with positive effect_times:", count)
