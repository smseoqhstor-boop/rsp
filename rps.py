#가위 = 1, 바위 = 2 보 = 3
import random as r
user_rsp = 0

def choice_rsp(num):
        if num == 1:
            return "가위"
        elif num ==2:
            return "바위"
        elif num ==3:
            return "보"

def rspGame(com_rsp,user_rsp):
    result = ""

    if com_rsp == user_rsp: #무승부
        result = "무승부"
    elif (com_rsp == 1 and user_rsp == 2) or (com_rsp ==2 and user_rsp == 3) or (com_rsp == 3 and user_rsp == 1):
        result = "승리"
    else:
        result = "패배"
    
    com_rsp = choice_rsp(com_rsp)
    user_rsp = choice_rsp(user_rsp)  
    print("컴퓨터: {}".format(com_rsp))
    print("나: {}".format(user_rsp))
    print(result)
    print("-"*50)
  
while True:
    com_rsp = r.randrange(1,4)

    try:
        user_rsp = int(input("가위 : 1, 바위: 2 보:3 중 하나를 입력하세요(4 입력시 종료): " ))
    except ValueError:
        print("숫자만 입력해주세요")
        continue
    
    if user_rsp == 4:
        break
    elif user_rsp not in[1,2,3]:
        print("1,2,3중에 입력해주세요")
        continue

    rspGame(com_rsp,user_rsp)