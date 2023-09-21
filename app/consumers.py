# channels  version 3.0.4

from channels.consumer import AsyncConsumer


class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("Connected", event)
        await self.send({"type": "websocket.accept"})

    async def websocket_receive(self, event):
        print("Received", event)
        print(event["text"])

    async def websocket_disconnect(self, event):
        print("Disconnected", event)
