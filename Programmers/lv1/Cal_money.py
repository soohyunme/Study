def solution(price, money, count):
    return max(0, sum(price * (i+1) for i in range(count)) - money)

# 등차수열의 합을 이용한 코드
def solution(price, money, count):
    return int(max(0,(price*count*(count+1))/2-money))


