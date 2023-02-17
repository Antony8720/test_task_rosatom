"""
Напишите функцию на Python, выполняющую сравнение версий. Условие:
- Return -1 if version A is older than version B
- Return 0 if version A and B are equivalent
- Return 1 if version A is newer than version B
- Each subsection is supposed to be interpreted as a number, therefore 1.10 > 1.1
"""

from packaging import version

def compare_version(x, y):
    if version.parse(x) < version.parse(y):
        return -1
    elif version.parse(x) == version.parse(y):
        return 0
    else:
        return 1

if __name__ == "__main__":
    print(compare_version('1.1', '1.10'))