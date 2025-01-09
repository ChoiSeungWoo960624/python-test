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
            gr_it = {item: vending_machine.count(item) for item in set(vending_machine)}
            gr_di = [f"{item}({count})" for item, count in gr_it.items()]
            print(f"{new_it} 추가되었습니다. 현재 재고: {', '.join(gr_di)}")
        
        elif host == '삭제':
            del_it = input("삭제할 음료 이름을 입력하세요: ")
            if del_it in vending_machine:
                vending_machine.remove(del_it)
                print(f"{del_it} 삭제되었습니다. 현재 재고: {vending_machine}")
            else:
                print("삭제하려는 음료가 존재하지 않습니다.")
        else:
            print("잘못 선택하셨습니다.")
    else:
        print("잘못 입력하셨습니다. 다시 확인해주세요.")
except ValueError:
    print("잘못 입력하셨습니다. 숫자로 입력해주세요.")

