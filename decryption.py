import os
k=[]
def d(s):
    f=open(s,"rb")
    p=f.read()
    p=list(p)
    l=len(p)
    for i in range(n):
        t=k[i]
        for j in range(l):
            p[j]=(p[j]+256-(t%10))%256
            t=t//10
            if t==0:
                t=k[i]
    f.close()
    f=open(s,"wb")
    f.write(bytes(p))
    f.close
    return

def dec():
    z=0
    print("Enter no of keys")
    global n
    n=int(input())
    print("Enter each key and press enter")
    for i in range(n):
        k.append(int(input()))
    s=input("Enter file path or a path to decrypt multiple files:")
    if s.find('.')>-1:
        d(s)
        z=z+1
    for root, dirs, files in os.walk(s):
        for file in files:
            try:
                d(root+'/'+str(file))
                print (root+'/'+str(file))
                z=z+1
            except:
                print("error")
    print("Number of files accessed : ",end="")
    print(z)
dec()
