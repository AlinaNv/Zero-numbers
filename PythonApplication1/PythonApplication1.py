#coding=windows-1251
print("������� ����� N")
N=int(input())
k=0
for i in range(1,N+1):
    print("������� �����")
    a=int(input())
    if a==0:
        k+=1
print(k)

