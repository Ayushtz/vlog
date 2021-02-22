a= [9,1,2,1,3,6]

total=0
for m in range(0,len(a)):

    total=total+a[m]

c=total*2
print("sum of list a:",c)
a.sort(reverse=True)
mul = a[0]*a[1]
if mul < c :

    print("True")
else:
    print("false")
'''
for i in range(0,5):
    for j in range(0,5):
        multi=a[i]*a[j+1]

    if multi > c:


        print('True')
        break
    else:
        print('False')

        break
'''

