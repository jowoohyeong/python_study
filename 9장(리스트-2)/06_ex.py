# 친군 관리 프로그램

# 출력문구
def menu_print():
    print("1. 친구 리스트 출력")
    print("2. 친구 추가")
    print("3. 친구 삭제")
    print("4. 이름 변경")
    print("9. 종료")

namelist = []
while True:
    menu_print()
    choice = int(input("메뉴를 선택하세요: "))

    if choice == 1:
        print(namelist)
    elif choice == 2:
        name = input("이름을 입력하세요: ")
        namelist.append(name)
    elif choice == 3:
        name = input("삭제할 친구를 입력하세요: ")
        if name in namelist:
            namelist.remove(name)
            print(name, "님이 삭제되었습니다.")
        else:
            print("존재하지 않는 친구이다.")
    elif choice == 4:
        chname = input("변경할 이름을 입력하세요: ")
        if chname in namelist:
            idx = namelist.index(chname)
            name = input("이름을 입력하세요: ")
            namelist[idx] = name
            print(chname, "님이", name, "으로 변경되었습니다.")
        else:
            print("검색한 이름이 없다.")
    elif choice == 9:
        print("프로그램 종료")
        break
    else:
        print("잘못된 입력")
