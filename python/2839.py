N = int(input())
result = 0

while N >= 0 :
    if N%5 == 0 :
        result += N//5
        break
    N -= 3
    result += 1
else :
    result = -1

print(result)


# N은 설탕의 무게를 초기값으로 한 데이터이다.
# N을 5로 나눈 나머지가 0이라면 봉지개수 result에 N을 5로 나눈 몫이 들어가고 
# while 문이 끝난다.
# 만약 나머지가 0이 아니라면 N에서 3을 빼고 result 에 1을 더한 뒤
# 다시 while 문을 돌려 3이 빠진 만큼의 N을 5로 나누길 반복한다.
# 이는 5로 전부 나누어지지 않았을 시 설탕에서 3만큼을 3짜리 봉지 하나에 넣고
# 다시 5짜리 봉지에 나누어넣어보길 반복하는 행동을 의미한다.

# while 문을 반복하다가 N값이 음수가 된다면 문제에서 요청한대로 -1을 result에 넣어준다.
