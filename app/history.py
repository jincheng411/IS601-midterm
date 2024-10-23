from typing import List

from app.calculation import Calculation


class History:
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, cal: Calculation):
        cls.history.append(cal)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        return cls.history

    @classmethod
    def clear_history(cls):
        cls.history.clear()

    @classmethod
    def print_history(cls):
        output = ""
        for i in range(len(cls.history)):
            output += f"{i + 1}. {cls.history[i].print_calculation()}. "
        return output

    @classmethod
    def get_last_record(cls):
        return cls.history[-1]