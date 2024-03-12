from lightningrobot.adapter import Adapter
from lightningrobot import log

class ConsoleAdapter(Adapter):
    async def connect(self) -> None:
        log.info("已加载-ConsoleAdapter")
        pass

    async def send_message(self, message: str) -> None:
        if event_type == "message":
            log.info("[群聊]Bot机器人：", message)
        elif event_type == "event":
            log.info("[私聊]Bot机器人：", message)

    async def listen(self) -> str:
        user_input = input("User用户：")
        global event_type
        event_type_temp = input("请选择场景：1.群聊 2.私聊")
        if event_type_temp == "1":
            event_type = "group"
        elif event_type_temp == "2":
            event_type = "private"
        else:
            log.error("输入错误")
        return user_input