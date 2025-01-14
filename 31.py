# JSON(JavaScript Object Notaion) : "텍스트 형식"으로 JavaScript(언어) Object 자료형과 유사하게 생긴 텍스 형식
# -> 가독성이 뛰어남 (컴퓨터도 사람도 해석하기 편함)
# -> "경량하다는 특성으로 인해" 네트워크를 통해 다른 시스템간 소통할 때 자주 사용
#-> JavaScript 언어에서 부터 파생되었는데, 현재는 다른 프로그래밍 언어(Python 등) 에서도 지원
# A 시스템(python) <-> JSON 텍스트 데이터 <-> B 시스템(타 프로그래밍 언어

import json

python_dict = {
    "name": "Lily", "age": 20, "city": "Busan","isLogin": True
} # dumps (): 딕셔너리를 JSON 문자열로 변환
json_str = json.dumps(python_dict)
print(json_str)
#python_dict : 파이썬의 딕셔너리 객체
#json_str : json 형식의 텍스트 데이터



# loads(): JSON 문자열을 python 객체로 변환
json_obj = json.loads(json_str)
print(json_obj)
print(json_obj["name"])