def santu():
    print("def dfs(cap_x,cap_y,target):
    stack=[(0,0,[])]
    visited=set()
    while stack:
        x,y,path=stack.pop()
        if (x,y) in visited:
            continue
        visited.add((x,y))
        if x==target or y==target:
            return path+[(x,y)]
        ops=[("x_full",cap_x,y),
            ("y_full",x,cap_y),
            ("x_emp",0,y),
            ("y_emp",x,0),
            ("pour_from_x_to_y",max(0,x-(cap_y-y)),min(cap_y,y+x)),
            ("pout_y_to_x",min(cap_x,x+y),max(0,y-(cap_x-x)))]
        print(ops)
        for o,new_x,new_y in ops:
            if 0<=new_x<=cap_x and 0<=new_y<=cap_y:
                stack.append((new_x,new_y,path+[(x,y,o)]))
    return None







cap_x=4
cap_y=3
target=2
res=dfs(cap_x,cap_y,target)
for i in res:
    print(f"({i[0]},{i[1]})")




tree={1:[2,9,10],
     2:[3,4],
     3:[],
     4:[5,6,7],
     5:[8],
     6:[],
     7:[],
     8:[],
     9:[],
     10:[]}





def bfs(tree,start):
    q=[start]
    v=[]
    while q:
        print("be",q)
        n=q.pop(0)
        v.append(n)
        for child in (tree[n]):
            if child not in v and child not in q:
                q.append(child)
                print("after",q)
    return v

r=bfs(tree,1)
for i in r:
    print(i)







n=int(input())
board=[[0]*n for _ in range(n)]
def attack(i,j):
    for k in range(0,n):
        if board[i][k]==1 or board[k][j]==1:
            return True
    for k in range(0,n):
        for l in range(0,n):
            if(k+l==i+j) or (k-l==i-j):
                if(board[k][l]==1):
                    return True
    return False
                




def nq(n):
    if n==1:
        return True
    for i in range(0,n):
        for j in range(0,n):
            if(not(attack(i,j))) and (board[i][j]!=1):
                board[i][j]=1
                if nq(n-1)==True:
                    return True
                board[i][j]=0
    return False

nq(n)
for i in board:
    print(i)






from itertools import permutations

def mp(tour,distances):
    t=0
    for i in range(len(tour)-1):
        t+=distances[tour[i]][tour[i+1]]   
    t+=distances[tour[-1]][tour[0]]
    return t

def tsp(distances):
    c=list(range(len(distances)))
    m=float('inf')
    o=None
    for tour in permutations(c):
        dis=mp(tour,distances)
        if dis<m:
            m=dis
            o=tour
    return m,o

distances=[[0,10,15,20],
         [10,0,35,25],
         [15,35,0,30],
         [20,25,30,0]]
m,o=tsp(distances)
print(m)
print(o)








global facts
global rules
rules=True
facts=[["plant","mango"],["eat","mango"],["seed","sprout"]]
def asse(fact):
    global facts
    global rules
    if not fact in facts:
        facts+=[fact]
        rules=True

while rules:
    rules=False
    for a in facts:
        if a[0]=="seed":
            asse(["plant",a[1]])
        if a[0]=="plant":
            asse(["fruit",a[1]])
        if a[0]=="plant" and ["eat",a[1]] in facts:
            asse(["human",a[1]])

print(facts)








from sympy import symbols,Not,Or,simplify

def d(cl1,cl2):
    t=[]
    for l1 in cl1:
        for l2 in cl2:
            if l1==Not(l2) or l2==Not(l1):
                t.extend([l for l in (cl1+cl2) if l!=l1 and l!=l2])
                print(t)
    return list(set(t))






def t(c):
    new_c=list(c)
    while True:
        n=len(new_c)
        pairs=[(new_c[i],new_c[j]) for i in range(n) for j in range(i+1,n)]
        for (cl1,cl2) in pairs:
            r=d(cl1,cl2)
            print(r)
            if not r:
                return True
            if r not in new_c:
                new_c.append(r)
        if n==len(new_c):
            return False







if __name__=="__main__":
    c1=[symbols('p'),Not(symbols('q'))]
    c2=[Not(symbols('p')),symbols('q')]
    c3=[Not(symbols('p')),Not(symbols('q'))]
    c=[c1,c2,c3]
    r=t(c)
    if r:
        print("not")
    else:
        print("ok")






board=[" " for _ in range(9)]
def pb():
    r1="|{}|{}|{}|".format(board[0],board[1],board[2])
    r2="|{}|{}|{}|".format(board[3],board[4],board[5])
    r3="|{}|{}|{}|".format(board[6],board[7],board[8])
    print()
    print(r1)
    print(r2)
    print(r3)
    print()

def ac(icon):
    if icon=='x':
        n=1
    elif icon=='o':
        n=2
    print("your turn palyer {}".format(n))
    c=int(input().strip())
    if board[c-1]==" ":
        board[c-1]=icon
    else:
        print("not")

def win(icon):
    if((board[0]==icon and board[1]==icon and board[2]==icon) or (board[0]==icon and board[4]== icon and board[8]==icon)):
        return True
    else:
        return False
def dra():
    if " " not in board:
        return True
    else:
        return False

while True:
    pb()
    ac('x')
    if win('x'):
        print("won")
        break
    elif dra():
        print("darw")
        break
    ac('o')
    if win('o'):
        print("won")
        break
    elif dra():
        print("darw")
        break

")
