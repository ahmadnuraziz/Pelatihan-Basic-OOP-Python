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

# In[97]:


class Hero:
    
    def __init__(self,name,position,atk,defn,spd):
        self.position = position
        self.name = name
        self.atk = atk
        self.defn = defn
        self.spd = spd
    
    def description(self):
        print("Hero ini bernama {}".format(self.name))
        print("Hero ini bernama {}".format(self.name))
    
    def move(self,step):
        self.position[0],self.position[1] = self.position[0] + step[0],self.position[1] + step[1]
        return self.position
    
    def setattrb(self,atk,defn,spd):
        self.atk = atk
        self.defn = defn
        self.spd = spd
        
    def pwr_desc(self):
        print("Attack: "+str(self.atk))
        print("Defense: "+str(self.defn))
        print("Speed: "+str(self.spd)+"\n")    
    
class Warrior(Hero):
    skill = ["tenaga kentir","pukulan kentir"]
    tipe = "warrior"
    
    def job_desc(self):
        print("Hero ini memiliki daya serangan dan pertahanan fisik yang kuat \n")
        
    def skill_desc(self):
        print("Skill 1: {}".format(Warrior.skill[0]))
        print("Skill 2: {}".format(Warrior.skill[1]))

class Mage(Hero):
    skill = ["ramalan maut","ilmu hitam"]
    tipe = "mage"
    
    def job_desc(self):
        print("Hero ini memiliki daya serangan paling kuat tapi hatinya rapuh \n")
    
    def skill_desc(self):
        print("Skill 1: {}".format(Mage.skill[0]))
        print("Skill 2: {}".format(Mage.skill[1]))


# In[98]:


a = Warrior("aziz",[0,0],100,200,30)
b = Mage("kentir",[1,1],200,30,40)


# In[99]:


b.move([1,3])


# In[100]:


a.setattrb(300,100,20)
b.setattrb(500,30,30)


# In[101]:


a.description()
b.description()


# In[102]:


a.pwr_desc()
b.pwr_desc()


# In[103]:


a.skill_desc()
b.skill_desc()


# In[36]:


a.defn


# In[37]:


a.name


# In[107]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

def plot_obj(*hero):
    plt.scatter(a.position[0],a.position[1])
    plt.scatter(b.position[0],b.position[1])


# In[114]:


a.move([-3,-3])
b.move([-1,0])
plot_obj(a,b)


# In[ ]:




