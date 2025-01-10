
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
    ot_city = input("도시 이름을 입력하세요 : ")
    if ot_city in ["서울", "부산"]:
        city_po = [entry[2] for entry in weather_data if entry[1] == ot_city]
        if city_po:
            max_temp = max(city_po)
            min_temp = min(city_po)
            print(f"{ot_city}의 최고 기온 : {max_temp:.2f}℃")
            print(f"{ot_city}의 최저 기온 : {min_temp:.2f}℃")
        else:
            print("현재 서울과 부산만 검색할 수 있습니다.")
    else:
        print("현재 서울과 부산만 검색할 수 있습니다.")

elif NS_type == 3:
    ot_city = input("도시 이름을 입력하세요 : ")
    if ot_city in ["서울", "부산"]:
        city_kha = [entry[3] for entry in weather_data if entry[1] == ot_city]
        if city_kha:
            total_rainfall = sum(city_kha)
            rainy_days = len([rain for rain in city_kha if rain > 0])
            print(f"{ot_city}의 총 강수량 : {total_rainfall:.2f}mm")
            print(f"{ot_city}에서 강수량이 있었던 날 : {rainy_days}일")
        else:
            print("현재 서울과 부산만 검색할 수 있습니다.")
    else:
        print("현재 서울과 부산만 검색할 수 있습니다.")


elif NS_type == 6:
    print ("종료 되었습니다.")

else:
    print ("잘 못 입력 하셨습니다. 옵션 1부터 6까지 있으며, 아라리아숫자 입력 바랍니다.")

    #ctrl + f 해당단어 찾기
    #블록 + ctrl + 마우스 왼쪽 블록 처리된 단어 이동