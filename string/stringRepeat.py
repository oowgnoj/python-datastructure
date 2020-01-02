# 문제
# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
#  즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.

# QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다.

# 출력
# 각 테스트 케이스에 대해 P를 출력한다.
# 예제 입력 1
# 2
# 3 ABC AAABBBCCC
# 5 /HTP  /////HHHHHTTTTTPPPPP


for _ in range(3):
    print()
# s = '2\n3 ABC\n5 /HTP'
# cnt = input()
# arr = s.split('\n')[1:]
# print(arr)
# for element in range(int(cnt)):
# case = input()
# case = case.split()
# text = ''
# print(cnt, case)
# for c in case[0]:
#     text += c*int(case[0])
#     print(case[0])
#     print(text)
#     for c in case[1]:
#         text = c*int(case[0])
#     if(len(element.split(' ')) >= 2 and int(element.split(' ')[0]) >= 1 and len(element.split(' ')[1]) >= 1):
#         num = element.split(' ')[0]
#         string = element.split(' ')[1]
#         answer = ''
#         for el in string:
#             answer = answer + (el*int(num))
#         print(answer)

# # s = '5 /HTP'
# # s = input()
# # if(len(s.split(' ')) >= 2 and int(s.split(' ')[0]) >= 1 and len(s.split(' ')[1]) >= 1):
# #     num = s.split(' ')[0]
# #     string = s.split(' ')[1]
# #     answer = ''
# #     for el in string:
# #         answer = answer + (el*int(num))
# #     print(answer)
