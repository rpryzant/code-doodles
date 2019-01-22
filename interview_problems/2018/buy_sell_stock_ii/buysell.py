

"""
     1 5 3 2 10 49 1 4 8
         s 
           b

       s        s      s
     b     b       b



algo:
  1) first pass: zip through array and save peaks
  2) snd pass: zip through and find valleys between peaks
  TODO  - roll 1, 2 in to one loop
  3) return peak/valley pairs

"""



def gen_buy_sell(arr):
    b = s = 0
    i = 1
    while i <= len(arr):
        if i == len(arr) or arr[i] < arr[i - 1]:
            if b < s:
                yield b, s
            b = s = i
        elif arr[i] < arr[b]:
            b = i
        elif arr[i] > arr[i-1]:
            s = i
        i += 1

def buy_sell(arr):
    return [transaction for transaction in gen_buy_sell(arr)]
            


print buy_sell([1,5,3,2,10,49,1,4,8]), [1,5,3,2,10,49,1,4,8]
print buy_sell([6,5,4,3,2,1])
print buy_sell([1,1,1,1,2])
