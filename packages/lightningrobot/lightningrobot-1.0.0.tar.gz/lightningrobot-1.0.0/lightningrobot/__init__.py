from lightningrobot.plugin import Plugin
from lightningrobot.adapter import Adapter
from lightningrobot import log

class ChatBot:
    def __init__(self, adapter: Adapter, plugins: list[Plugin]):
        self.adapter = adapter
        self.plugins = plugins

    async def start(self):
        await self.adapter.connect()
        log.info("成功连接到聊天平台！")
        
        while True:
            message = await self.adapter.listen()
            for plugin in self.plugins:
                await plugin.on_message(message)