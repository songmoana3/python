from typing import TypedDict



class TestClass(TypedDict):
    
    name: str
    gender: int
    nickname: NotRequired[str]
    
test_dict = TestClass(name = '동디디은', gender = 1)
print(type(test_dict)) # dict
