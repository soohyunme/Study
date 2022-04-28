def solution(absolutes, signs):
    return sum([num if sig else -num for num, sig in zip(absolutes, signs)])
