import vk_api
import json

with open('schedule-1a9ab-default-rtdb-export.json', 'r', encoding='utf-8') as db:
    data = json.load(db)

from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token='5279abc478d8ea4d7447c244f110bbfd52e2f24c33eb1ffa77be01f6997b0d3c750115343cfa6018d4f27')
session_api = vk_session.get_api()
longpool = VkLongPoll(vk_session)

def send_some_msg(id, some_text):
    vk_session.method("messages.send", {"user_id":id, "message":some_text, "random_id":0})

for event in longpool.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text.lower()
            id = event.user_id

            if msg == "среда":
                for item in data['ИМИТ']['МОСб-202']['Знаменатель']['Среда']:
                    send_some_msg(id, "Предмет: "+item['subject']+"\nПреподаватель: "+item['teacher']+"\nВремя пары: "+item['time'])




