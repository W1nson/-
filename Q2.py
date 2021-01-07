


def create_ary(n): 
    ary=[]
    ary = [i for i in range(1, n+1)]

    return ary

def function(ary): 
    count = 0
    
    for i in range(len(ary)): 
        # if not ary[i]%3 != 0: # keep
        #     ary[i] = 0
        if(ary[i] %3 == 0 and ary[i] % 5 == 0):
            count = count+1
            continue
        elif (ary[i]%3 == 0 or ary[i]%5 == 0):
            ary[i] = 0
        else: 
            count = count+1

    return count





num = int(input("input: "))
user_ary = create_ary(num)

print(user_ary)
print(function(user_ary))
# print(user_ary)

