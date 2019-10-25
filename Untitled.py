
# coding: utf-8

# In[3]:

names=["a","b","c"]
ages=[10,20,30]
for i in range(len(names)):
    print(names[i],ages[i])


# In[4]:

names=["a","b","c"]
ages=[10,20,30]
for name,age in zip(names,ages):
    print(name,age)


# In[6]:

a=list(zip(names,ages))
a


# In[7]:

names=["a","b","c"]
for i in range(len(names)):
    print(i+1,names[i])


# In[9]:

names=["a","b","c"]
i=1
for name in names:
    print(i,name)
    i+=1


# In[11]:

names=["a","b","c"]
for i,name in enumerate(names):
    print(i,name)


# In[13]:

a=list(enumerate(names))
a


# In[14]:

a=list(range(0,10))
b=list()
for item in a:
    b.append(item*item)
print(a)
print(b)


# In[15]:

b=[item*item for item in range(0,10)]
b


# In[17]:

a=[item for item in range(0,100) if item%3==0]
print(a)


# In[19]:

coordinates=[]
for x in range(0,10):
    for y in range(0,10):
        coordinates.append((x,y))
print(coordinates)


# In[20]:

coordinated=[(x,y) for x in range(0,10) for i in range(0,10)]
print(coordinates)


# In[23]:

girls=["alice","bernice","clarice"]
boys=["chris","arnold","bob"]
result=[boy+"+"+girl for boy in boys for girl in girls if boy[0]==girl[0]]
print(result)


# In[25]:

a=[1,2,3]
b=a
del a
b


# In[27]:

exec('print("sdfdf")')


# In[1]:

get_ipython().magic('whos')


# In[12]:

scope={}
exec=('y=1',scope)
print(scope)


# In[13]:

scope["y"]


# In[14]:

get_ipython().magic('whos')


# In[15]:

eval("1+2+3")


# In[17]:

expr=input("please input a expression:")
print(eval(expr))


# In[22]:

def hello(name):
    print("hello"+name)


# In[25]:

hello("dsf")


# In[26]:

callable(hello)


# In[27]:

get_ipython().magic('pinfo hello')


# In[29]:

def print_banner(text):
    print("*"*40)
    print(text.center(38).center(40,"*"))
    print("*"*40)
print_banner("hello")


# In[32]:

fibs=[1,1]
for i in range(0,9):
    fibs.append(fibs[-2]+fibs[-1])
print(fibs)


# In[33]:

def fibs(num):
    result=[1,1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result

num=int(input("how"))
print(fibs(num))


# In[34]:

def fibs(num):
    result=[1,1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result[-1]

num=int(input("how"))
print(fibs(num))


# In[41]:

def fibs(num):
    item_before_last,last_item=1,1
    for i in range(num-2):
        item_before_last,last_item=last_item,item_before_last+last_item
    return last_item

num=int(input("how"))
print(fibs(num+1))


# In[46]:

def change_it(a):
    a=a*2
    
x=2
change_it(x)
print(x)


# In[48]:

def change_it(a):
    a[0]="Hello"
    
x=["hello","hi"]
change_it(x)
print(x)


# In[56]:

def sum(*params):
    result=0
    for item in params:
        result+=item
    return result
assert(sum(1,2,3,4)==10)
print("ok ")


# In[57]:

def foo():x=42
x=1
foo()
print(x)


# In[ ]:



