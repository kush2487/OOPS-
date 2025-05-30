from typing import List, Dict, Optional

def add (a: int, b: int) -> int:
    return (a+b)

def concate_names(first: str, last: str) -> str:
    return f"{first} {last}"


ASum = add(5, 4)
print(ASum)


first_name = 'kushgra'
last_name = "memani"
print(concate_names(first_name, last_name))
