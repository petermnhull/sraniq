class Task:
    def __init__(self, name: str):
        self.name = name

    def run(self, number: int) -> str:
        return str(number * 213)
