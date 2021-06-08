from bs4 import BeautifulSoup
import requests
import os
import json5 as json5
import json
from datetime import datetime

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

seal = {
    "black": {
        "sec1":[
            [1189, 1371, 1372], #黑水妍
            [1190, 1373, 1374], #黑火妍
            [2176], #光妍
            [2177], #暗妍
        ],
        "sec2":[
            [1626, 2545], #亞特蘭提斯
            [1719, 2634], #龐貝,
            [1818], #美索不達米亞
            [1439, 2379], #瑪雅
            [1440, 2244], #阿努比斯
        ],
        "sec3":[
            [2081], #艾莉亞
            [2149], #賈比爾,
            [2207], #青圭
            [2480], #拉普拉斯
            [2380], #潘朵拉
        ],
        "sec4":[
            [1983], #秦始皇
            [2305], #項羽,
            [2595], #蚩尤
            #[1404, 1981], #鐵扇
            #[1405, 1982], #唐三藏
        ],
        "sec5":[
            [1868], #貝西摩斯
            [1869], #莎娜,
            [1870], #巴哈姆特,
            [1562], #弗麗嘉
            [2099], #虹伶
        ],
    }
}

print("end at " + str(datetime.utcnow()))
print("job done")