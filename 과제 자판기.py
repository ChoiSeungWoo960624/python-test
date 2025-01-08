vending_machine = ['게토레이', '게토레이', '레스비', '레스비', '생수', '생수', '생수', '이프로']

try:
    use_type = int(input("사용 종류를 입력해주세요 (1. 소비자, 2. 주인): "))

    if use_type == 1:
        gast_pick = input("마시고 싶은 음료를 입력하세요: ")
        if gast_pick in vending_machine:
            vending_machine.remove(gast_pick)
            print(f"{gast_pick} 드릴게요.")
        else:
            print("현재 해당 물품은 재고가 다 떨어졌거나 없는 제품입니다.")
        print(f"남은 음료는 {vending_machine}")

    elif use_type == 2: 
        host = (input("할 일 선택 : 1. 추가 2. 삭제 "))
        if host == '추가':
            new_it = input("추가할 음료 이름을 입력하세요: ")
            vending_machine.append(new_it)
            grouped_it = {item: vending_machine.count(item) for item in set(vending_machine)}
            grouped_display = [f"{item}({count})" for item, count in grouped_it.items()]
            print(f"{new_it} 추가되었습니다. 현재 재고: {', '.join(grouped_display)}")
        
        elif host == '삭제':
            delete_item = input("삭제할 음료 이름을 입력하세요: ")
            if delete_item in vending_machine:
                vending_machine.remove(delete_item)
                print(f"{delete_item} 삭제되었습니다. 현재 재고: {vending_machine}")
            else:
                print("삭제하려는 음료가 존재하지 않습니다.")
        else:
            print("잘못된 선택입니다.")
    else:
        print("잘못된 값입니다. 다시 입력해주세요.")
except ValueError:
    print("숫자를 입력해주세요.")

