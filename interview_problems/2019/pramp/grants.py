
"""

Award Budget Cuts
The awards committee of your alma mater (i.e. your college/university) asked for your assistance with a budget allocation problem they’re facing. Originally, the committee planned to give N research grants this year. However, due to spending cutbacks, the budget was reduced to newBudget dollars and now they need to reallocate the grants. The committee made a decision that they’d like to impact as few grant recipients as possible by applying a maximum cap on all grants. Every grant initially planned to be higher than cap will now be exactly cap dollars. Grants less or equal to cap, obviously, won’t be impacted.

Given an array grantsArray of the original grants and the reduced budget newBudget, write a function findGrantsCap that finds in the most efficient manner a cap such that the least number of recipients is impacted and that the new budget constraint is met (i.e. sum of the N reallocated grants equals to newBudget).

Analyze the time and space complexities of your solution.

Example:

input:  grantsArray = [2, 100, 50, 120, 1000], newBudget = 190

output: 47 # and given this cap the new grants array would be
           # [2, 47, 47, 47, 47]. Notice that the sum of the
           # new grants is indeed 190
Constraints:

[time limit] 5000ms

[input] array.double grantsArray

0 ≤ grantsArray.length ≤ 20
0 ≤ grantsArray[i]
[input] double newBudget

[output] double






N
cap 

grants array [g1 ... gn]
new budget B


cap C : sum(gi's) < B AND fewest # grants is affected
      = biggest C?


BF: 
  1) set C to max(grants)
      decrement and check
      
========================================
  2) sort grants
  
grants  [g1   gn]
grantsArray = [2, 100, 50, 120, 1000]
newBudget = 190

output: 47

[2 50 100 120 1000]    190
   ^       
       
i             1
partial sum   52
cap'          50
newBudget'    (3 * 50) + 52 = 202 > newBudget . !!!! ===> current i - 1


case 1: 
  surplus = sum(grants array) - new budget 
      ==> return max of grant array
      
case 2:
  surplus > 0
  190
  lower bound (2 => 10?) 4       
  upper bound (50 => 202) 3
  
  (190 - 2) can spread this across 4 places
  (190 - 2) / 4 = 47
  
  
weird cases:
  new budget is too big
  new budget is super small (nothing fits)

"""



def find_grants_cap(grants, B):
  grants = sorted(grants)   
  partial_sum = 0
  i = 0
  while i < len(grants):
    money_spent = partial_sum + (len(grants[i:]) * grants[i])
    if money_spent > B:
      break
    partial_sum += grants[i]
    i += 1

  return partial_sum + (len(grants[i:]) // B)








