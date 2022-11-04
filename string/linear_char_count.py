s="aaabbcccaadffddee"

start=0
end=0

res=""

while end<len(s):
    i=0
    while end<len(s):
        if s[start]==s[end]:
            i+=1
            end+=1
        else:
            break
    res+=s[start]+str(i)
    start=end
print(res)