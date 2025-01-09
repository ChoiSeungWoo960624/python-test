weather_data = [
    ["2024-11-20", "서울", 15.2, 0.0],
    ["2024-11-20", "부산", 18.4, 0.0],
    ["2024-11-21", "서울", 10.5, 2.3],
    ["2024-11-21", "부산", 14.6, 1.2],
    ["2024-11-22", "서울", 8.3, 0.0],
    ["2024-11-22", "부산", 12.0, 0.0],
]

NS_type = int(input("[날씨 데이터 분석 프로그램] \n1. 평균 기온 계산\n2. 최고|최저 기온 찾기\n3. 강수량 분석\n4. 날씨 데이터 추가\n5. 전체 데이터 출력\n6.종료\n원하는 기능의 번호를 입력하세요 : "))

if NS_type == 1:
    ot_city = input("도시 이름을 입력하세요 : ")
    if ot_city in ["서울", "부산"]:
        city_temps = [entry[2] for entry in weather_data if entry[1] == ot_city]
        if city_temps:
            avg_temp = sum(city_temps) / len(city_temps)
            print(f"{ot_city}의 평균 기온 : {avg_temp:.2f}℃")
        else:
            print ("현재 서울과 부산만 검색 할 수 있습니다.")
    else:
        print("현재 서울과 부산만 검색 할 수 있습니다.")

elif NS_type == 2:
    pass
elif NS_type == 3:
    pass
elif NS_type == 4:
    pass
elif NS_type == 5:
    def weather_data (day, ct, zr) :
        ["2024-11-20", "서울", 15.2, 0.0],
        ["2024-11-20", "부산", 18.4, 0.0],
        ["2024-11-21", "서울", 10.5, 2.3],
        ["2024-11-21", "부산", 14.6, 1.2],
        ["2024-11-22", "서울", 8.3, 0.0],
        ["2024-11-22", "부산", 12.0, 0.0],
    print ("날짜 : {} 도시 : {} , 평균 기온 : {} , 강수량 : {}")
elif NS_type == 6:
    pass
1=