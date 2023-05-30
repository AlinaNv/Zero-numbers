#coding=windows-1251
print("Введите число N")
N=int(input())
k=0
for i in range(1,N+1):
    print("Введите числа")
    a=int(input())
    if a==0:
        k+=1
print(k)

