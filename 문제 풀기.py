'''
NU = int(input("몇단을 출력할까요? : "))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = [n*NU for n in numbers]
print(f"squares)
'''
'''
NU = int(input("어디까지 계산할까요?? : "))
numbers = NU + 
total = 0
for numbers in NU:
    total += numbers
    if total % 1 == 0:
print(f"합계는 {total}입니다.")
'''

st_dict = {
    "st_di1": {"국어": 83, "영어": 92, "수학": 88},
    "st_di2": {"국어": 90, "영어": 79, "수학": 86},
    "st_di3": {"국어": 88, "영어": 86, "수학": 94}
}

kr_nu = [st["국어"] for st in st_dict.values()]
en_nu = [st["영어"] for st in st_dict.values()]
ma_nu = [st["수학"] for st in st_dict.values()]

kr_avg = sum(kr_nu) / len(kr_nu)
en_avg = sum(en_nu) / len(en_nu)
ma_avg = sum(ma_nu) / len(ma_nu)

print(f"국어 평균: {kr_avg:.3f}")
print(f"영어 평균: {en_avg:.3f}")
print(f"수학 평균: {ma_avg:.3f}")

'''
NU = int(input("몇 단을 출력할까요? : "))
MU = [1, 2, 3, 4, 5, 6, 7, 8, 9]
eqm = [n * NU for n in MU]
for i, result in enumerate(eqm, start=1):
    print (f"{NU} x {i} = {result}")
    '''