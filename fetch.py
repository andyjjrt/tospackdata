from bs4 import BeautifulSoup
import requests
import os
import json5 as json5
import json
from datetime import datetime
from seal import seal

if not os.path.isdir("data"):
	os.mkdir("data")

print("start from " + str(datetime.utcnow()))

uid = os.environ['TOS_UID']
auth = os.environ['TOS_AUTH']
with open('data/data.json', 'w') as f:
    f.write('{"uid":"' + str(uid) + '", "auth":"' + str(auth) + '", "update_time" : "' + str(datetime.utcnow().isoformat()) + '"}')

soup = BeautifulSoup(requests.get("https://checkup.tosgame.com/").text, 'html.parser')
script = soup.find_all('script')
for src in script:
    if "main" in str(src.get('src')):
        target_url = str(src.get('src'))

res = requests.get("https://checkup.tosgame.com" + target_url).text
monster_data = json.dumps(json5.loads(res.split("var n=new Map(")[1].split(".map((function(a){return[a.id,a]})))}")[0].replace("!", "")))
monster_active = json.dumps(json5.loads(res.split("var n=new Map(")[2].split(".map((function(a){return[a[0],{name:JSON.parse(a[1].name),description:JSON.parse(a[1].description)}]})))}")[0]))
monster_leader = json.dumps(json5.loads(res.split("var n=new Map(")[3].split(".map((function(a){return[a[0],{name:JSON.parse(a[1].name),description:JSON.parse(a[1].description)}]})))}")[0]))
monster_team = json.dumps(json5.loads(res.split("var n=new Map(")[4].split(".map((function(a){return[a[0],JSON.parse(a[1])]})))}")[0]))

with open('data/MONSTER_DATA.json', 'w') as f:
    f.write(monster_data)
with open('data/MONSTER_LEADER.json', 'w') as f:
    f.write(monster_leader)
with open('data/MONSTER_TEAM.json', 'w') as f:
    f.write(monster_team)
with open('data/MONSTER_ACTIVE.json', 'w') as f:
    f.write(monster_active)
with open('data/SEAL_DATA.json', 'w') as f:
    f.write(json.dumps(seal))

print("end at " + str(datetime.utcnow()))
print("job done")