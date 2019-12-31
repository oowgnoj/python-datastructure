
def isArithmeticSeq(num):
    strNum = str(num)
    if len(strNum) <= 2:
        return True
    else:
        commonDif = int(strNum[0]) - int(strNum[1])
    for i in range(len(strNum) - 1):
        if int(strNum[i]) - int(strNum[i+1]) == commonDif:
            continue
        else:
            return False
    return True


def hanNumber(num):
    number = 0
    if len(str(num)) <= 2:
        print(num)
    else:
        for i in range(1, num + 1):
            if isArithmeticSeq(i):
                number = number + 1
            else:
                continue
        print(number)


hanNumber(110)
hanNumber(1)
hanNumber(210)
hanNumber(1000)
