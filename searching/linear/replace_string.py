s="i.like.this.page.vey.m"
# temp=s.split(".")

result=""
start=0
end=0
flag=0
while end<len(s):
    try:
        while s[end]!="." and end<len(s):
            end+=1
    except:
        pass
    if not flag:
        flag=1
        result+=s[start:end+1]
        start=end
        end+=1
    else:
        result+="abc"
        start=end
        end+=1
        flag=0
print(result)

    
    
