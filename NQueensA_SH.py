#NQueensA_SH.py
# ask the user for an N value
# generate a candidate NQ solution [random.randint(0,n-1) for x in range(n)]
# define a function to count number of conflicts()
# while number of conflicts in NQ > 0
    # randomize (or improve) NQ
# print NQ
# print number of iterations

import random
n = int(input("Please enter N "))

nq = list(range(n))

def conflicts(list):
    conflicts = 0
    for x in range(len(list)):
        for y in range(x+1, len(list)):
            #Horizontal Conflicts
            if list[x] == list[y]:
                conflicts +=1
            #Diagonal conflicts
            if abs(list[x] - list[y]) == abs(x - y):
                conflicts +=1
    return conflicts
    
x = random.randint(0, n-1)
iters = o
while conflicts(nq) > 0:
    iteration += 1
    randon.shuffle(nq)

print("After",iteration,"iterations, NQ",nq,"has",conflicts(nq),"conflicts.")

# for x in range(n):
    
    
    
