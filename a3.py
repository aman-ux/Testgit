a = []
n = int(input('enter the number of elements:'))
i=0
while i<n:
 b=input('enter the elements and at last enter done:')
 a.append(b)
 i=i+1
a.sort()
if a[len(a)-1]=='done':
  try:
    i=0
    while i<(len(a)-2):
        max=int(a[0])
        if int(a[i])>max:
            max=int(a[i])
        i=i+1
    print('maximum is', max)
    while i<(len(a)-2):
        min=a[0]
        if int(a[i])<min:
            min=int(a[i])
        i=i+1
    print('minimum is',min)
  except:
    a=[i for i in a if i.isdigit()]
    a.sort()
    print(a)
    max = int(a[0])
    for i in range(len(a)):
        max=int(a[0])
        if int(a[i]) > max:
            max = int(a[i])
    print('invalid input')
    print('maximum is',max)
    min=int(a[0])
    for i in range(len(a)):
        if int(a[i])<min:
            min=int(a[i])
    print('minimum is', min)








