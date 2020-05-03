
menuList = [["커피",3000], ["햄버거",5400], ["돈까스",4500], ["오므라이스",5000]]
isExist = False

while True:
    print("1.메뉴선택 2.설정 0.종료")
    manage = (int)(input("원하시는 기능을 선택하세요 : "))
    
    if manage == 1:
        print()
        print(menuList)
        print()
        menu = input("메뉴를 입력하세요 : ")
        count=0
        
        for i in menuList:
            if i[0]==menu:
                isExist=True
                break
            count+=1
        
        
        if isExist==True:
            print("%s는 %d원 입니다." % (menuList[count][0],menuList[count][1]))
            money = (int)(input("금액을 투입하세요 : "))
            if money - menuList[count][1] >= 0:
                print("주문되었습니다. 거스름돈은 %d입니다\n" %(money-menuList[count][1]))
            else:
                print("금액이 부족합니다\n")
        elif isExist==False:
            print("판매하지 않습니다\n")

            
    elif manage == 2:
        print("1. 메뉴 추가 2. 메뉴 삭제")
        menuMan = (int)(input("번호를 선택하세요 : "))
        if menuMan == 1:
            nameTemp = input("메뉴이름을 입력하세요 : ")
            moneyTemp = (int)(input("가격을 입력하세요 : "))
            menuList.append([nameTemp,moneyTemp])
        elif menuMan ==2:
            count = 0
            delTemp = input("삭제할 음식의 이름을 입력하세요 : ")
            for i in menuList:
                if i[0]==delTemp:
                    break
                count+=1
            menuList.pop(count)
            
    elif manage == 0:
        break
    else:
        print("다시 입력하세요\n")
