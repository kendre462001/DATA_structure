s=input()
x="+/-*^"
list1=[]
# ans=0
for ele in s.split(" "):
    if ele!=" ":
        if ele=="+":
            t=list1.pop()
            t1=list1.pop()
            ans=t+t1
            list1.append(ans)
            continue
        elif ele=="-":
            t=list1.pop()
            t2=list1.pop()
            ans=t2-t
            print(t,t2)
            list1.append(ans)
            continue
        elif ele=="*":
            t=list1.pop()
            t2=list1.pop()
            ans=t*t2
            list1.append(ans)
            continue
        elif ele=="/":
            t=list1.pop()
            t2=list1.pop()
            ans=t/t2
            list1.append(ans)
            continue
        elif ele=="^":
            t=list1.pop()
            t1=list1.pop()
            ans=t1**t
            list1.append(ans)
            continue
        else:
            list1.append(int(ele))
print(*list1)