import json

with open("settings.json") as file:
    json.load(file)


def get(memb):
    lvl=[0]
    for r in memb.roles:
        if r.name in lvl3:
            lvl.append(3)
        elif r.name in lvl2:
            lvl.append(2)
        elif r.name in lvl1:
            lvl.append(1)
    print(lvl,max(lvl))
    return max(lvl)


def check(memb, lvl):
    return get(memb) >= lvl
