"""Какие ты видишь проблемы в следующем фрагменте кода?"""
"""В лямбду передавалось неправильное значение"""

from typing import Callable

def create_handlers(callback: Callable) -> list:
    handlers = []
    for step in range(5):
        handlers.append(lambda step = step: callback(step))
    return handlers


def execute_handlers(handlers: list):
    for handler in handlers:
        handler()