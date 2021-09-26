#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[5]:


data=pd.read_csv("d:50_Startups.csv")


# In[6]:


x=data.iloc[:,0:-2]
y=data.iloc[:,-1]


# In[7]:


from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.20)


# In[8]:


from sklearn.linear_model import LinearRegression
model=LinearRegression()


# In[9]:


model.fit(xtrain,ytrain)


# In[10]:


ypred=model.predict(xtest)


# In[ ]:


from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def kjgfkjgjkg('/'):
    return render_template('pro.html')
@app.route('/info',methods=['GET','POST'])
def kjgkjgkjg():
    if(request.method=='POST'):
        res=int(request.form['r'])
        admin=int(request.form['a'])
        mar=int(request.form['m'])
        ans=model.predict([[res,admin,mar]])
        return render_template('pro.html',monday=ans)
if __name__=='__main__':
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




