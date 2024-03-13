import json
from utils.send_message import send_group_message
from utils.logger import *
from lightningrobot import log

def on_adaptermessage(ws, message):
    message = json.loads(message)
    user_id = message['user_id']
    group_id = message['group_id']
    nickname = message.get('sender', {}).get('nickname', '')
    type = message['message_type']
    card = message.get('sender', {}).get('card', '')
    role = message.get('sender', {}).get('role', '')
    reply_id = message['message'][0]['data']['id'] if 'id' in message['message'][0]['data'] else ""
    reply_type = message['message'][0]['type'] if 'type' in message['message'][0] else ""
    image_data = message['message'][0]['data'] if 'data' in message['message'][0] else ""
    file_id = image_data['file_id'] if 'file_id' in image_data else ""
    file_path = ""
    if message['message'][0]['type'] == 'image':
        file_path = message['message'][0]['data']['path']
    if role == "owner":
        role = "群主"
    elif role == "admin":
        role = "群管"
    elif role == "member":
        role = "群员"
    else:
        role = role
    text = message['message'][0]['data']['text']
    if type == "group":
        message = f'''群消息 | {group_id} | {nickname} | {user_id} | {role} >>> {text} {file_path} {reply_id}'''
    elif type == "private":
        message = '1'
    else:
        message = f'''用户消息 | 用户ID：{user_id} | 用户名：{nickname} | 消息类型：{type} >>> {text}'''
    log.info(message)
    return (user_id,group_id,nickname,type,card,role,text)