###1
'''sotien = int(input('nhap so tien: '))

to500 = sotien//500
sotienconlai=sotien%500
if to500>0:
    print('so to 500: ',to500)
to200 = sotienconlai//200
sotienconlai=sotienconlai%200
if to200>0:
    print('so to 200: ',to200)
to100 = sotienconlai//100
sotienconlai=sotienconlai%100
if to100>0:
    print('so to 100: ',to100)
to50 = sotienconlai//50
sotienconlai=sotienconlai%50
if to50>0:
    print('so to 50: ',to50)
to20 = sotienconlai//20
sotienconlai=sotienconlai%20
if to20>0:
    print('so to 20: ',to20)
to10 = sotienconlai//10
sotienconlai=sotienconlai%10
if to10>0:
    print('so to 10: ',to10)
to5 = sotienconlai//5
sotienconlai=sotienconlai%5
if to5>0:
    print('so to 5: ',to5)
to2 = sotienconlai//2
sotienconlai=sotienconlai%2
if to2>0:
    print('so to 2: ',to2)
to1 = sotienconlai
if to1>0:
    print('so to 1: ',to1)
tongsoto = to500 + to200 + to100 + to50 + to20 + to10 + to5 + to2 + to1
print('tong so to: ',tongsoto)'''

###2
'''sodiem = int(input("nhap diem:"))

if sodiem<0 or  sodiem>100:
    print('chi nhan cac gia tri tu 0 den 100')
elif sodiem >= 90:
    print('xep loai A')
elif sodiem >= 80:
    print('xep loai B')
elif sodiem >= 70:
    print('xep loai C')
elif sodiem >= 65:
    print('xep loai D')
elif sodiem <65:
    print('xep loai E')'''
###3
'''a,b,c = map(int,input('nhap 3 so abc: ').split(' '))
bien1 = c - b
bien2 = b - a
bien3 = c/b
bien4 = b/a
if bien1 == bien2:
    print('a,b,c tao thanh cap so cong')
if bien3 == bien4:
    print('a,b,c tao thanh cap so nhan')'''
###4
'''a,b,c = map(int,input('nhap 3 so abc: ').split(' '))
if c//b == b//a:
    print('la cap so nhan')
elif c - b == b - a:
    print('la cap so cong')
else:
    print(' k la cap so cong, khong la cap so nhan')'''
###5
'''n = int(input('nhap so nguyen n:'))
so=1
tong = 0
tongchan = 0
tonguoc = 0
while so <= n:
    print(so, end=' ')
    if n%so == 0:
        tonguoc = tonguoc + so
    if so%2 == 0:
        tongchan = tongchan + so
    tong = tong + so
    so = so + 1
print('\t')
print('tong bang: ',tong)
print('tong chan bang: ',tongchan)
print('tong uoc bang: ',tonguoc)
so=1
while so <= n:

    if so%5==0:
        print('boi cua 5 la: ', so)
    so = so + 1
so = n
while so <= n:
    if so%2==1 and n%so==0:
        print('uoc lon nhat le: ', so)
    so = so - 1'''
'''n = int(input('nhap n :'))
s = int(input('nhap S :'))
so = 1
tong=0
while so<=n:
    tong=tong+so
    so=so+1
print('tong = ',tong)
if tong-s==0:
    print('bo ve du')
else:
    print(f'so thu tu cua con bo bi mat la {tong-s}')'''
###6
'''a = int(input('nhập số a:'))
for i in range(1,11):
    print(f"{a} x {i:2} = {i*a:2}")'''
###7
'''tonguoc = 0
a = int(input('nhập số a:'))
for i in range(1,a):
    if a%i==0:
        tonguoc = tonguoc + i
if tonguoc>a:
    print('tong uoc so:',tonguoc)
    print('a la so phong phu')
else:
    print('tong uoc so:', tonguoc)
    print('a khong la so phong phu')'''
###8
'''tong = 0
a = int(input('nhap so a:'))
for i in range(1, a+1):
    tong+=i
print('tong =',tong)'''
###9
'''tong = 0
a = int(input('nhap so a:'))
for i in range(1, a+1):
    tong+=1/i
print('tong =',tong)'''

###10
'''n = int(input("nhập cạnh n: "))
for dong in range(1,n+1):
    for cot in range(1,n+1):
        if dong+cot <= n+1:
            print('X',end=' ')
        else:
            print(' ',end=' ')
    print()'''
###11
'''n = int(input("nhập cạnh n: "))
for dong in range(1,n+1):
    for cot in range(1,n+1):
        if dong+cot >= n+1:
            print('X',end=' ')
        else:
            print(' ',end=' ')
    print()'''
###12
'''n = int(input("nhập cạnh n: "))
for dong in range(1,n+1):
    for cot in range(1,n+1):
        if dong >= cot:
            print('X',end=' ')
        else:
            print(' ',end=' ')
    print()'''

###13
'''n = int(input("nhập cạnh n: "))
for cot in range(1,n+1):
    for dong in range(1,n+1):
        if dong <= cot:
            print('X',end=' ')
        else:
            print(' ',end=' ')
    print()'''
###14
'''n = int(input("nhập cạnh n: "))
for cot in range(1,n+1):
    for dong in range(1,n+1):
        if dong == 1 or cot == 1 or dong + cot == n+1:
            print('X',end=' ')
        else:
            print(' ',end=' ')
    print()'''

###15
'''n = int(input("nhập cạnh n: "))
for dong in range(1,n+1):
    for cot in range(1,n+1):
        if dong == n or cot == n or dong + cot == n+1:
            print('X',end=' ')
        else:
            print(' ',end=' ')
    print()'''
###16
'''n = int(input("nhập cạnh n: "))
for dong in range(1,n+1):
    for cot in range(1,n+1):
        if dong == n or cot == 1 or dong == cot:
            print('X',end=' ')
        else:
            print(' ',end=' ')
    print()'''
##17
'''n = int(input("nhập cạnh n: "))
for dong in range(1,n+1):
    for cot in range(1,n+1):
        if dong == 1 or cot == n or dong == cot:
            print('X',end=' ')
        else:
            print(' ',end=' ')
    print()'''
###18
'''S = input('nhap chuoi:')
kytu = input('nhap ky tu:')
print('cau b')
dem=S.count(kytu)
print(f'trong chuoi {S} co {dem} ky tu {kytu} ')
print('cau c')
slkytu = slkyso = 0
for i in S:
    if i.isalpha()==True:
        slkytu+=1
    elif i.isnumeric()==True:
        slkyso+=1
print(f'trong chuoi {S} co {slkytu} ky tu va {slkyso} ky so')'''
###19
'''S = input('nhap chuoi:')
A = 'aeiou'
nguyenam = 0
phuam = 0
for i in S:
    if i in A:
        nguyenam+=1
    else:
        phuam+=1
print(f'chuoi {S} co {nguyenam} nguyen am va co {phuam} phu am')'''