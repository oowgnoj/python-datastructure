def sumDigit(num):
    strNum = str(num)
    sum = 0
    for digit in strNum:
        sum = sum + int(digit)
    return sum


def selfNum():
    answer = list(range(1, 10000))
    for i in range(1, 10000):
        notASelfNum = sumDigit(i) + i
        if notASelfNum in answer:
            answer.remove(notASelfNum)

    print(answer)


selfNum()
