"""
WebSocket Router — Real-time chat & notifications
"""
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import Dict, List
import json
from datetime import datetime
from loguru import logger

ws_router = APIRouter()

# Connection manager
class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}  # user_id → socket
        self.rooms: Dict[str, List[str]] = {}  # room_id → [user_ids]

    async def connect(self, websocket: WebSocket, user_id: str):
        await websocket.accept()
        self.active_connections[user_id] = websocket
        logger.info(f"WS connected: {user_id}")

    def disconnect(self, user_id: str):
        self.active_connections.pop(user_id, None)
        logger.info(f"WS disconnected: {user_id}")

    async def send_personal(self, message: dict, user_id: str):
        ws = self.active_connections.get(user_id)
        if ws:
            await ws.send_json(message)

    async def broadcast_to_room(self, message: dict, room_id: str):
        user_ids = self.rooms.get(room_id, [])
        for uid in user_ids:
            await self.send_personal(message, uid)

    async def broadcast_all(self, message: dict):
        for ws in self.active_connections.values():
            try:
                await ws.send_json(message)
            except Exception:
                pass

    def join_room(self, user_id: str, room_id: str):
        self.rooms.setdefault(room_id, [])
        if user_id not in self.rooms[room_id]:
            self.rooms[room_id].append(user_id)

    def leave_room(self, user_id: str, room_id: str):
        if room_id in self.rooms and user_id in self.rooms[room_id]:
            self.rooms[room_id].remove(user_id)


manager = ConnectionManager()


@ws_router.websocket("/chat/{user_id}")
async def chat_endpoint(websocket: WebSocket, user_id: str):
    """Real-time chat WebSocket endpoint"""
    await manager.connect(websocket, user_id)
    try:
        while True:
            data = await websocket.receive_text()
            msg = json.loads(data)

            envelope = {
                "type": msg.get("type", "message"),
                "sender_id": user_id,
                "content": msg.get("content", ""),
                "timestamp": datetime.utcnow().isoformat(),
                "room_id": msg.get("room_id"),
            }

            if msg.get("type") == "join_room":
                manager.join_room(user_id, msg["room_id"])
                await manager.send_personal({"type": "system", "message": f"Joined room {msg['room_id']}"}, user_id)

            elif msg.get("type") == "leave_room":
                manager.leave_room(user_id, msg["room_id"])

            elif msg.get("room_id"):
                await manager.broadcast_to_room(envelope, msg["room_id"])

            elif msg.get("receiver_id"):
                await manager.send_personal(envelope, msg["receiver_id"])
                await manager.send_personal(envelope, user_id)  # echo

            else:
                await manager.broadcast_all(envelope)

    except WebSocketDisconnect:
        manager.disconnect(user_id)


@ws_router.websocket("/notifications/{user_id}")
async def notifications_endpoint(websocket: WebSocket, user_id: str):
    """Real-time notifications WebSocket"""
    await websocket.accept()
    try:
        while True:
            await websocket.receive_text()  # keep-alive pings
    except WebSocketDisconnect:
        pass
