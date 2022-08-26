def Tri(x,y):
    for i in range(x,y,3):
        s = i*'*'
        print(s)

def Moon1():
    j=4
    k=0
    L=8
    M=2
    ss=3*'*'
    
    
    for i in range(4):
        j= j-1
        k = k + 1
        L = L-2
        M = M+3
 

        sp = k*' '
        st = j*'*'

        ts = L*'*'
        
        s = ss + k*'*' + sp + st + ss + st + sp + st + sp + st + st+  sp + sp + st +st +sp +st + sp + ts + ss + sp +  k*'*' + M*'*'
        print(s)
    
def Moon2():
    j= 20
    k = 8
    L = 8
    M = 8

    for i in range(3):
        j= j-3
        k = k + 2
        L = L + 2
        M = M + 5
        
        sp = i*'*'
        st = j*' '

        s = k*'*' + st + st+  L*'*' + M*'*'
        print(s)


def Sun1():
    j=4
    k=0
    L=8
    M=7
    ss=11*'*'
    
    
    for i in range(4):
        j= j-1
        k = k + 1
        L = L-2
        M = M+3
 

        sp = k*' '
        st = j*'*'

        ts = L*'*'
        
        s =  ss + k*'*' + sp + st + st + sp + st + sp + st +st +sp +st + sp + ts + sp +  k*'*' + M*'*'
        print(s)


def Sun2():
    j=4
    k=20
    L=2
    M=28
    ss=11*'*'
    P = 20
    Q = 30
    
    
    for i in range(3):
        k = k + 4
        P=P+3
 
        sp = k*' '
        st = j*'*'

        
        s = ss + st + sp  +st + P*'*'
        j= j-2
        print(s)

    for i in range(2):
        sp = M*' '
        st = L*'*'
        Q= Q+3

        
        s = ss + st +sp +st+ Q*'*'
        M= M-4
        L = L+2
        print(s)



def Sun3():
    j=4
    k=0
    M=36
    N=0
    ss=11*'*'

    
    
    for i in range(4):
        N = N + 2
        j= j-1
        k = k + 1
        M = M+3

 

        sp = k*'*'
        st = j*'*'
        ts = j*' '
        tt = N*'*'
        
        s =  ss+ st + ts + sp + sp + ts + sp + ts + sp + sp + ts + sp + ts + tt + ts + st+ M*'*'
        print(s)




Tri(0,52)
Moon1()
Moon2()
Tri(77,85)
Tri(5,52)
Sun1()
Sun2()
Sun3()
Tri(94,100)






