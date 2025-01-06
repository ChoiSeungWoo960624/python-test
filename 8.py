#딕셔너리(dictionary)

#생성
dict1 = {} #{}
#dict1 = dict() #{}
print(dict1)

#딕셔너리 생성
dict1 = {
    "name" : "홍길동",
    "age"  : "20",
    "city" : "seoul",
    "hobby" : ["런닝", "등산", "헬스"]
}
print(dict1)

dict2 = dict(name="홍길동", age="21")
print(dict2)

# 값 접근하기
print(dict1["name"]) # 홍길동
print(dict1["hobby"]) #['런닝', '등산', '헬스']
print(dict1["hobby"][2]) #헬스

# 값 수정
dict1["age"] = 30 
print(dict1) #{'name': '홍길동', 'age': 30, 'city': 'seoul', 'hobby': ['런닝', '등산', '헬스']}

# 요소 추가 
dict1["birthday"] = "19960101"
print(dict1) # {'name': '홍길동', 'age': 30, 'city': 'seoul', 'hobby': ['런닝', '등산', '헬스'], 'birthday': '19960101'}

# 키 삭제
del dict1["birthday"]
print(dict1) #{'name': '홍길동', 'age': 30, 'city': 'seoul', 'hobby': ['런닝', '등산', '헬스']}

# 딕셔너리 매서드
fruits = {"apple": "사과", "banana": "바나나"}
print(fruits.get("apple")) #사과
print(fruits.get("peach")) # None #존재하지 않는 키로 get 하는 경우 'none' 반환
print(fruits.get("peach", "복숭아"))
# -> 존재하지 않는 키로 검색시 기본값 설정
print(fruits)
# -> 기본값을 설정할 뿐, 딕셔너리 요소 추가 x

# 여러 요소 추가
fruits.update({"grapes": "포도", "melon": "멜론"})
print(fruits) #dict_keys(['apple', 'banana', 'grapes', 'melon'])
print(fruits.keys()) #dict_keys(['apple', 'banana', 'grapes', 'melon'])
print(fruits.values())# dict_values(['사과', '바나나', '포도', '멜론'])
print(fruits.items()) # dict_items([('apple', '사과'), ('banana', '바 나나'), ('grapes', '포도'), ('melon', '멜론')])

# 요소 모두 지우기
fruits.clear()
print(fruits) #{}

#성적관리
fruits = {"Alice": "85", "Bob": "90", "Charlie": "95"}
fruits["David"] = "80"
fruits["Alice"] = 88
del fruits["Bob"]
print(fruits)

# 내장 함수
numbers = [10, 20, 30, 40]
print(sum(numbers))

scores = {"국어": 83, "영어": 90, "수학": 95}
print(scores.values())
total_score = sum(scores.values())
print(total_score)

print(max(numbers))
print(min(numbers))

print(max(scores.values()))
print(min(scores.values()))

names = ["Alice", "Bob", "Charlie", "Lily"]
scores = [85, 90, 95, 100, 105]
zipped = list(zip(names, scores))
zipped2 = dict(zip(names, scores))
print(zipped)
print(zipped2)