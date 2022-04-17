def self_num(n):
    ret_ = n
    while True:
        if n < 10:
            ret_ += n
            break
        ret_ += n % 10
        n = n // 10
    return ret_


self_nums = set()
for i in range(10000):
    self_nums.update([self_num(i)])
for i in range(10000):
    if i not in self_nums:
        print(i)
