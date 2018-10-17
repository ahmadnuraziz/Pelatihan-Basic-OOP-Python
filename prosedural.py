#!/usr/bin/env python
# coding: utf-8

# # Hero
# 
# ## attribut 
# nama,posisi,attack,defense,speed
# ## method
# #### move: mengubah posisi
# #### description: deskripsi nama hero
# #### setattrb: mengubah atribut hero
# #### pwr_desc: deskripsi kekuatan hero
# 
# ## job hero
# skill_desc
# job_desc

# In[39]:


hero = {"name":{}}


# In[107]:


def add_hero(name,position,attack,defense,speed,job=""):
    hero[name] = {"name":name,"position":position,"attack":attack,
                  "defense":defense,"speed":speed,"job":""}
    return print("Berhasil ditambahkan!")

def set_attrb(name,**kwargs):
    for key,value in kwargs.items():
        hero[name][key] = value
        
def pwr_desc(name):
    print("Nama : {}".format(name))
    print("Attack  : {}".format(hero[name]['attack']))
    print("Defense  : {}".format(hero[name]['defense']))
    print("Speed  : {}".format(hero[name]['speed']))
    print("Job : {}".format(hero[name]['job']))

def job_desc(name):
    if hero[name]['job'] == "Warrior":
        print("Warrior adalah hero yang memiliki serangan dan pertahanan fisik yang kuat")
    elif hero[name]['job'] == "Mage":
        print("Mage adalah hero yang memiliki serangan sangat kuat namun hatinya lemah")
    else:
        print("Hero belum memiliki job alias nganggur")
        
def skill_desc(name):
    if hero[name]['job'] == "Warrior":
        print("Skill 1: tenaga kentir")
        print("Skill 2: pukulan kentir")
    elif hero[name]['job'] == "Mage":
        print("Skill 1: ramalan maut")
        print("Skill 2: ilmu hitam")
    else:
        print("Hero belum memiliki job alias nganggur")
        
def move(name,step):
    hero[name]['position'][0] = hero[name]['position'][0] + step[0]
    hero[name]['position'][1] = hero[name]['position'][1] + step[1]


# In[68]:


add_hero("kentir",[0,0],100,200,30)
add_hero("aziz",[1,3],200,100,50)


# In[69]:


pwr_desc('aziz')


# In[70]:


job_desc("aziz")


# In[101]:


kwargs = {"job":"Mage","attack":150}
set_attrb(name="aziz",**kwargs)


# In[102]:


pwr_desc("aziz")


# In[97]:


hero['aziz']['job'] = 'Warrior'


# In[109]:


hero['aziz']


# In[108]:


move('aziz',[2,-3])


# In[104]:


[0] + [1]


# In[ ]:




