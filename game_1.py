from random import randint

while True:
    random_num = randint(1, 100)
    cnt_try = 0
    best_try = None
    while True:
        n = input("숫자를 입력하세요: ")
        if int(n) <= 0:
            print("유효한 범위 내의 숫자를 입력하세요")
        elif int(n) > 100:
            print("유효한 범위 내의 숫자를 입력하세요")
        elif int(n) > random_num:
            cnt_try += 1
            print("down",random_num)
        elif int(n) < random_num:
            cnt_try += 1
            print("up",random_num)
        else:
            cnt_try += 1
            print("정답입니다.")
            print(f'시도한 횟수: {cnt_try}')

            answer = input("다시 하시겠습니까? (y/n) ")
            if answer == "n":
                print("게임을 종료합니다.")
                exit()
            elif answer == "y":
                if best_try is None or cnt_try < best_try:
                    best_try = cnt_try
                print(f'이전 게임 플레이어 최고 시도 횟수: {best_try}')
                break
            else:
                print("y/n 중 선택하세요")
