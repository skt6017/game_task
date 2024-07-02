import random
win = 0
lose = 0
draw = 0
while True:
    a_list = ['가위', '바위', '보']
    user = input("가위, 바위, 보 중 하나를 선택하세요. ")
    com = random.choice(a_list)

    if user in a_list:
        if user == com:
            draw += 1
            print(f'사용자: {user} 컴퓨터: {com}')
            print("무승부입니다.")
        elif (user == "가위" and com == "보") or (user == "바위" and com == "가위") or (user == "보" and com == "바위"):
            win+=1
            print(f'사용자: {user} 컴퓨터: {com}')
            print("사용자 승리!")
        elif (user == "가위" and com == "바위") or (user == "바위" and com == "보") or (user == "보" and com == "가위"):
            lose += 1
            print(f'사용자: {user} 컴퓨터: {com}')
            print("컴퓨터 승리!")
        while True:
            answer = input("다시 하시겠습니까? (y/n) ")
            if answer.lower() == "n":
                print("게임을 종료합니다.")
                print(f'승: {win} 패: {lose} 무: {draw}')
                exit()
            elif answer.lower() == "y":
                break
    else:
        print("유효한 입력이 아닙니다.")
