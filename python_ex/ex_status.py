'''- 있던 없던 주민번호를 다 읽을 수 있도록 remove -'''
'''주민번호 체계가 맞지 않으면 다시 입력'''
'''00년생부터는 뒷자리 3,4'''
'''뒤 자리를 x로 표시'''


'''당신의 나이는 56세입니다'''
'''생일은 3월 11일입니다'''
'''당신의 성별은 남자입니다'''



''' -기호 삭제 '''
def delHP(arg):
    if '-' in arg:
        arg.remove('-')
        return arg
    else :
        return arg
    
'''나이구하기'''
def agePrint(cList):
    
    ageYear = (int)(cList[0])*10+(int)(cList[1])
    if 0<=ageYear<=20:
        age = 2020 - (2000+ageYear)
    else:
        age = 2020 - (1900+ageYear)
        
    print("당신의 나이는 %d세 입니다. "%age)

'''생일구하기'''
def birthPrint(cList):
    birthMonth = (int)(cList[2])*10+(int)(cList[3])
    birthDay = (int)(cList[4])*10 + (int)(cList[5])
    
    print("당신의 생일은 %d월 %d일 입니다" %(birthMonth, birthDay))
    
'''성별구하기'''
def mfPrint(cList):
    if cList[6]=="1" or cList[6]=="3":
        print("당신의 성별은 남자입니다.")
    elif cList[6]=="2"or cList[6]=="4":
        print("당신의 성별은 여자입니다.")
    
'''*가리기'''
def maskingPrint(cList):
    strTemp = ""
    for i in range(7,13):  
        cList[i] = "*"
    for i in cList:
        index = cList.index(i)
        if index==6 :
            strTemp += "-"
        strTemp += i
        
    print(strTemp)

    
def main():
    
    '''주민등록번호 담기'''
    
    cNum = input("주민등록번호를 입력하세요 : ")
    cListTemp = list(cNum)
    cList = delHP(cListTemp)
    
    maskingPrint(cList)
    
    '''13자리가 아닐 시'''
    if len(cList)!=13:
        print("주민번호 체계가 맞지 않습니다.")
    else :
        agePrint(cList)
        birthPrint(cList)
        mfPrint(cList)
        print()
    

'''실행'''
isRun = True
while(isRun):
    print("1.실행 0.종료")
    menu = (int)(input("메뉴를 선택하세요 : "))
    if menu==1:
        main()
    elif menu==0:
        break
