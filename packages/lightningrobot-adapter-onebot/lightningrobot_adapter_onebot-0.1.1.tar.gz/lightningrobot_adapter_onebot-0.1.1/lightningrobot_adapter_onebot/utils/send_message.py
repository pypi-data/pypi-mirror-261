import websocket
import json

def send_group_message(ws_url,group_id,message):
    ws = websocket.create_connection(ws_url)
    event_data = {
        "action": "send_msg",
        "params": {
            "message_type": "group",
            "group_id": group_id,  # 替换为目标群号
            "message": message
        }
    }
    ws.send(json.dumps(event_data))
    message = f'''发送群 | {group_id} >>> {message}'''


def send_private_message(ws_url,user_id,message):
    ws = websocket.create_connection(ws_url)
    event_data = {
        "action": "send_private_msg",
        "params": {
            "user_id": user_id,  # 替换为目标群号
            "message": message
        }
    }
    ws.send(json.dumps(event_data))
    message = f'''发送好友 | {user_id} >>> {message}'''