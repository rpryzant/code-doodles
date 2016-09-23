

def subsets(nums):
    if not nums:
        return
    for i in range((2 ** len(nums))):
        yield [nums[j] for j in gen_ones(i)]

def gen_ones(x):
    print x
    i = 0
    while x > 0:
        if x & 1:
            yield i
        x >>= 1
        i += 1


print [subset for subset in subsets([1,2,3])]
