arr=['john','johnny','jackie','johnny','john' 
'jackie','jamie','jamie','john','johnny','jamie',
'johnny','john']
d={}
for ele in arr:
    if ele in d:
        d[ele]+=1
    else:
        d[ele]=1
t=max(d.values())
ele1=[]
for ele,value in d.items():
    if value==t:
        ele1.append(ele)
ele1.sort()
print( *[ele1[0],t])