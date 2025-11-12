#가위 = 1, 바위 = 2 보 = 3
import random as r
import os
import time
user_coin = 1000

def choice_rsp(num): #숫자(0,1,2)를 가위/바위/보 문자열로 변환
        if num == 0:
            return "가위"
        elif num ==1:
            return "바위"
        elif num ==2:
            return "보"

def rspGame(com_rsp,user_rsp): #게임 승패 여부 판단 후 결과 출력
    result = ""

    if com_rsp == user_rsp: #무승부
        return "Draw"
    elif (com_rsp == 0 and user_rsp == 1) or (com_rsp ==1 and user_rsp == 2) or (com_rsp == 2 and user_rsp == 0):
        return "Win"
    else:
        return "Lose"
  

def menu(): #메뉴 함수
    while True:
        print("[+] Menu\n0: Play\n1:Exit\n")
        menu_num = int(input("Choice > "))
        if menu_num == 0:
            if user_coin <= 0:
                print("[$] 코인이 없습니다. 게임을 종료합니다.")
                return 1
            bet_coin = int(input("이번 게임에 베팅할 코인을 입력해주세요. (현재 {} 코인)\n> ".format(user_coin)))
            if user_coin < bet_coin:
                print("돈이 부족합니다. 다시 걸어주세요")
                continue
            user_rsp = int(input("[-] 아래 선택지 중 선택해주세요.\n0 : 가위\n1 : 바위\n2 : 보\n\n> "))
            print("[$] 가위!!",end="\r")
            time.sleep(1)
            print("[$] 바위!!!!!",end="\r")
            time.sleep(1)
            print("[$] 보!!!!!!!",end="\r")
            time.sleep(1)
            os.system('cls')
            return bet_coin, user_rsp, menu_num
        elif menu_num == 1:
            print("[$] 종료됩니다")
            exit()

def result_rsp(): #게임 결과 함수
    result = choice_rsp()
    bet_coin = menu()
    if result == "Draw":
        print("무승부")
        print("[$] 베팅한 코인은 그대로 유지됩니다.")
        return result
    elif result == "Win":
        print("[$] 게임에서 승리하셨습니다.")
        print("[$] 베팅한 코인만큼 가산됩니다.")
        user_coin += bet_coin
        print("[$] 가산된 코인: {}".format(user_coin))
        return result
    else:
        print("[$] 게임에 지셨습니다.")
        user_coin -= bet_coin
        print("베팅한 코인 : {}".format(user_coin))
        

    print("[$] 현재 남은 코인: {}".format(user_coin))
    # print("[$] 계속하려면 Enter를 누르세요.")

def bye(): #파산시 게임 종료
    if user_coin <= 0:
        print("[$] 당신은 파산했습니다.")
        print("[$] 퇴장처리됩니다.")
        print("[^_^] 또 찾아와주세요! :)")
        exit()

print("[$] 가위/바위/보 게임 Machine [$]")
print("$"+"-+"*12+"$")

user_name = input("이름: > ")
print("[$] {} 님! 대박나세요!".format(user_name))
print("[$] 입장을 도와드리겠습니다. 잠시만 기다려주세요...")
time.sleep(3)
os.system('cls')

while True:    
    print("[User Info]")
    print("-- User Name: {}".format(user_name))
    print("-- User Coin: {}".format(user_coin))

    menu_result = menu()
    bet_coin, user_rsp, menu_num = menu_result #언패킹 > 튜플로

    #게임 시작
    com_rsp = r.randrange(0,3)
    result = rspGame(com_rsp,user_rsp) #승패 여부
    com_rsp = choice_rsp(com_rsp) #가위바위보 값 지정
    user_rsp = choice_rsp(user_rsp) #가위바위보 값 지정 
    print("[$] User : {}".format(user_rsp))
    print("[$] Computer : {}".format(com_rsp))
    print("[$] Game 결과: " + result +"\n")
    
    if result == "Draw":
        print("무승부")
        print("[$] 베팅한 코인은 그대로 유지됩니다.")
    elif result == "Win":
        print("[$] 게임에서 승리하셨습니다.")
        print("[$] 베팅한 코인만큼 가산됩니다.")
        user_coin += bet_coin
        print("[$] 가산된 코인: {}".format(user_coin))
    else:
        print("[$] 게임에 지셨습니다.")
        user_coin -= bet_coin
        print("감소한 코인 : {}".format(user_coin))
        

    print("[$] 현재 남은 코인: {}".format(user_coin))
    # print("[$] 계속하려면 Enter를 누르세요.")

    bye()
