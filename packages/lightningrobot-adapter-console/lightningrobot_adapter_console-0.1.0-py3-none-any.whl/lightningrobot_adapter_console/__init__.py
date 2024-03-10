from lightningrobot.adapter import Adapter

class ConsoleAdapter(Adapter):
    async def connect(self) -> None:
        pass

    async def send_message(self, message: str) -> None:
        print("机器人：", message)

    async def listen(self) -> str:
        user_input = input("你：")
        return user_input