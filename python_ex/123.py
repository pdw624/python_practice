num1 = (int)(input())
num2 = (int)(input())
num3 = (int)(input())
num4 = (int)(input())
num5 = (int)(input())
num6 = (int)(input())
num7 = (int)(input())
num8 = (int)(input())
num9 = (int)(input())
num10 = (int)(input())

arrList = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]
arrSet = set(arrList)
arrTemp = list(arrSet)

import random

answer1 = random.choice(arrTemp)
arrSet.remove(answer1)

answer2 = random.choice(arrTemp)
arrSet.remove(answer2)

answer3 = random.choice(arrTemp)
arrSet.remove(answer3)

arrAnswer = answer1, answer2, answer3

