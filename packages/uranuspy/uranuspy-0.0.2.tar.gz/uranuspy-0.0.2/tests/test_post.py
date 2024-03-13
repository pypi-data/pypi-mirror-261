import requests
import pickle
import json
from datetime import datetime, timezone


token = pickle.load(open("config/token.pkl", "rb"))
db_todo_url = "https://db.manaai.cn/api/v2/daybreak_add_tasks"
t = datetime.now(timezone.utc)
data = {}
data["super_token"] = token
data["user_addr"] = "usrfNzS5ZYIzo"
tasks = {
    "tasks_comment": "由机器人自动同步创建的todo",
    "tasks_title": "hahhahaha",
    "tasks_create_time": datetime.now(timezone.utc).isoformat(),
    "tasks_due_date": t.isoformat(),
    "tasks_project_id": 0,
    "tasks_priority": 0,
    "tasks_type_id": 0,
}
data["data"] = json.dumps([tasks])
# data["data"] = [tasks]
print(data)
headers = {"Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Custom"}
# headers = {"Content-Type": "application/json", "User-Agent": "Custom"}
rep = requests.post(url=db_todo_url, headers=headers, data=data)
print(rep.text)
rep = json.loads(rep.text)
