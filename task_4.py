"""
Напишите функцию Python, которая возражает текущий
публичный IP-адрес компьютера (например, с использованием сервиса ifconfig.me)
"""

import requests


def get_ip():
    return requests.get('https://ifconfig.me').text


if __name__ == '__main__':
    print(get_ip())