# python3.11.4 New features test
# TypedDict, NotRequired

from typing import TypedDict, NotRequired



class TestClass(TypedDict):
    
    name: str
    gender: int
    nickname: NotRequired[str] # 이야아 Optional 이랑 같은걸까?
    
test_dict = TestClass(name = '동디디은', gender = 1)
print(type(test_dict)) # dict
