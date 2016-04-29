from typing import List, Dict, Union, cast, TypeVar


T = TypeVar('T')


def first(elements: List[T]) -> T:
    return elements[0]


def sorted_keys(d: Dict[str, int]) -> List[str]:
    return sorted(d.keys())


def parse(value: Union[int, str]) -> float:
    if isinstance(value, int):
        return value
    return value


class Person:
    def __init__(self, name: str, year: int) -> None:
        self.name = name
        self.year = year

    def age(self) -> str:
        age = 2016 - self.year  # Update this next year...
        return "I'm " + age + " years old."


people = []
people.append(Person("Alice", 1982))
people.append(Person("Bob", 1986))

for p in people:
    print(p.name, p.age())


print(1 + cast(int, "uh oh"))
