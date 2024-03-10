from abc import ABC, abstractmethod

class Plugin(ABC):
    @abstractmethod
    async def on_message(self, message: str) -> None:
        """处理接收到的消息"""
        pass