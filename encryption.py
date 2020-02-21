
import os
k=[]
def e(s):
    f=open(s,"rb")
    p=list(f.read())
    f.close()
    l=len(p)
    for i in range(n):
        t=k[i]
        for j in range(l):
            p[j]=(p[j]+(t%10))%256
            t=t//10
            if t==0:
                t=k[i]
    p=bytes(p)
    f=open(s,"wb")
    f.write(p)
    f.close()
    return
z=0
print("Enter no of keys")
global n
n=int(input())
print("Enter each key and press enter")
for i in range(n):
    k.append(int(input()))
s=input("Enter file path or a path to encrypt multiple files:")
if s.find('.')>-1:
    e(s)
    z=z+1
for root, dirs, files in os.walk(s):
    for file in files:
        try:
            e(root+'/'+str(file))
            print (root+'/'+str(file))
            z=z+1
        except:
            print("error")
print("Number of files accessed : ",end="")
print(z)
