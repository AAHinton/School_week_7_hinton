#!/usr/bin/env python
# coding: utf-8

# In[2]:


fin=open('C:/Users/hinto/Desktop/School/GIS6345_Program/week_5_pandas/words_moby/crosswd.txt')


# In[3]:


fin.readline()


# In[4]:


fout=open('C:/Users/hinto/Desktop/School/GIS6345_Program/week_7_fiona_shapely/output.txt', 'w')


# In[6]:


line1="This here's the wattle,\n"
fout.write(line1)


# In[7]:


line2="the emblem of our land.\n"
fout.write(line2)


# In[8]:


fout.close()


# In[9]:


x=52
fout.write(str(x))


# In[10]:


fout=open('C:/Users/hinto/Desktop/School/GIS6345_Program/week_7_fiona_shapely/output2.txt', 'w')


# In[11]:


x=55
fout.write(str(x))


# In[12]:


camels=42
'%d'% camels


# In[13]:


'I have spotted %d camels.' % camels


# In[14]:


'In %d years I have spotted %g%s.' % (3, 0.2,'camels')


# In[15]:


import os
cwd=os.getcwd()
cwd


# In[16]:


os.path.abspath('memo.txt')


# In[17]:


os.path.exists('memo.txt')


# In[18]:


os.listdir(cwd)


# In[20]:


def walk(dirname):
    for name in os.listdir(dirname):
        path=os.path.join(dirname, name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)


# In[21]:


try:
    fin=open('bad_file')
except:
    print('Something went wrong.')


# In[22]:


import dbm


# In[23]:


db=dbm.open('captions', 'c')


# In[24]:


db['cleese.png']="Photo of John Cleese."


# In[25]:


db['cleese.png']


# In[26]:


db['cleese.png']='Photo of John Cleese doign a silly walk.'
db['cleese.png']


# In[27]:


for key in db:
    print(key, db[key])


# In[28]:


db.close()


# In[29]:


import pickle
t=[1,2,3]
pickle.dumps(t)


# In[30]:


t1=[1,2,3]
s=pickle.dumps(t1)
t2=pickle.loads(s)
t2


# In[31]:


t1==t2


# In[32]:


t1 is t2


# In[33]:


cmd='ls -l'


# In[34]:


fp=os.popen(cmd)


# In[35]:


res=fp.read()


# In[36]:


stat=fp.close()
print(stat)


# In[37]:


filename='book.txt'
cmd='md5sum'+filename
fp=os.popen(cmd)
res=fp.read()
stat=fp.close()
print(res)


# In[38]:


print(stat)


# In[39]:


def linecount(filename):
    count=0
    for line in open(filename):
        count+=1
    return count
print(linecount('wc.py'))


# In[40]:


import wc


# In[48]:


def sed(s, replace_string, input, output):
    fin=open(input, 'r')
    fout=open(ouput, 'w')
    trantab=maketrans(s, replace_string)
    for word in fin:
        re_word = word.translate(trantab)
        fout.write(re_word)
    fin.close()
    fout.close()


# In[58]:


sed('wd', 'y', 'C:/Users/hinto/Desktop/School/GIS6345_Program/week_5_pandas/words_moby/crosswd.txt', 'C:/Users/hinto/Desktop/School/GIS6345_Program/out.txt')


# In[ ]:




