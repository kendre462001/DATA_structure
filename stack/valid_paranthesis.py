s=input()
list1=[]

for ele in s:
    if ele=="(" or ele=="{" or ele=="[":
        list1.append(ele)
    else:
        if not list1:
            print("No")
            break
        else:
            if  list1[-1]=="(" and ele==")":
                list1.pop()
                continue
            if  list1[-1]=="[" and ele=="]":
                list1.pop()
                continue
            if  list1[-1]=="{" and ele=="}":
                list1.pop()
                continue
            else:
                print("NO")
                break
else:
    if not list1:
        print("YES")
    else:
        print("NO")


