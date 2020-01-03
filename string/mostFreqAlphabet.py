# 단어 공부
# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 2 초	128 MB	47020	17642	14231	38.243%
# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
# 단, 대문자와 소문자를 구분하지 않는다.

# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.


x = input()

x = x.upper()


vocabDict = {}
for el in x:
    if el in vocabDict:
        vocabDict[el] += 1
    else:
        vocabDict[el] = 1

sortedVocabDict = sorted(vocabDict.values(), reverse=True)
# print(sortedVocabDict)
if len(sortedVocabDict) == 1:
    print(list(vocabDict.keys())[0])

elif sortedVocabDict[0] == sortedVocabDict[1]:
    print('?')
else:
    for key in vocabDict:
        if vocabDict[key] == sortedVocabDict[0]:
            print(key)
