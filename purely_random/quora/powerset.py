def powerset(nums):
    if not nums:
        return
    for i in range(1, 2**len(nums)):
        yield [nums[j] for j in gen_ones(i)]

def gen_ones(x):
    i = 0
    while x > 0:
        if x & 1:
            yield i
        x >>= 1
        i += 1

def reduce_mul(nums):
    product = 1
    for x in nums:
        product *= x
    return product

        
def subset_products(nums):
    for subset in powerset(nums):
        print reduce_mul(subset)
    

subset_products([2,7,3])
