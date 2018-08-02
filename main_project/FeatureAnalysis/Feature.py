
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


# In[2]:


matches=pd.read_csv('Output.csv')
matches.info()


# In[3]:


to_drop=['MatchID','Margin','Date']
matches.drop(to_drop, inplace=True, axis=1)
matches.head(5)


# In[4]:


matches.replace(['Australia','India','Sri Lanka','South Africa','England',
                 'New Zealand','Pakistan','West Indies','Bangladesh','Zimbabwe']
                ,['AUS','IND','SL','SA','ENG','NZ','PAK','WI','BAN','ZIM'],inplace=True)

encode = {'TeamA': {'AUS':1,'IND':2,'SA':3,'ENG':4,'NZ':5,'PAK':6,'SL':7,'WI':8,'BAN':9,'ZIM':10},
          'TeamB':  {'AUS':1,'IND':2,'SA':3,'ENG':4,'NZ':5,'PAK':6,'SL':7,'WI':8,'BAN':9,'ZIM':10},
          'Toss':  {'AUS':1,'IND':2,'SA':3,'ENG':4,'NZ':5,'PAK':6,'SL':7,'WI':8,'BAN':9,'ZIM':10},
          'Winner':  {'AUS':1,'IND':2,'SA':3,'ENG':4,'NZ':5,'PAK':6,'SL':7,'WI':8,'BAN':9,'ZIM':10}}
matches.replace(encode, inplace=True)
matches.head(5)


# In[5]:


matches.head(10)


# In[6]:


#we maintain a dictionary for future reference mapping teams
dicVal = encode['Winner']
print(dicVal['AUS']) #key value
print(list(dicVal.keys())[list(dicVal.values()).index(1)]) #find key by value search 


# In[7]:


df = pd.DataFrame(matches)
df.describe()


# In[8]:


#Find some stats on the match winners and toss winners
temp1=df['Toss'].value_counts(sort=True)
temp2=df['Winner'].value_counts(sort=True)
#Mumbai won most toss and also most matches
print('No of toss winners by each team')
for idx, val in temp1.iteritems():
   print('{} -> {}'.format(list(dicVal.keys())[list(dicVal.values()).index(idx)],val))
print('No of match winners by each team')
for idx, val in temp2.iteritems():
   print('{} -> {}'.format(list(dicVal.keys())[list(dicVal.values()).index(idx)],val))


# In[39]:


from PIL import Image
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(16,8))
ax1 = fig.add_subplot(121)
ax1.set_xlabel('Country')
ax1.set_ylabel('Count of Toss Winners')
ax1.set_title("Toss winners")
temp1.plot(kind='bar')

ax2 = fig.add_subplot(122)
temp2.plot(kind = 'bar')
ax2.set_xlabel('Country')
ax2.set_ylabel('Count of Match Winners')
ax2.set_title("Match Winners")
plt.rcParams.update({'font.size': 25})

fig.savefig("match_winners.png")


# In[11]:


df.apply(lambda x: sum(x.isnull()),axis=0) 
   #find the null values in every column


# In[12]:


#building predictive model
from sklearn.preprocessing import LabelEncoder
var_mod = ['Venue','Toss_Decision']
le = LabelEncoder()
for i in var_mod:
    df[i] = le.fit_transform(df[i])
df.dtypes 


# In[13]:


#Import models from scikit learn module:
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import KFold   #For K-fold cross validation
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn import metrics

#Generic function for making a classification model and accessing performance:
def classification_model(model, data, predictors, outcome):
  model.fit(data[predictors],data[outcome])
  
  predictions = model.predict(data[predictors])
  
  accuracy = metrics.accuracy_score(predictions,data[outcome])
  print('Accuracy : %s' % '{0:.3%}'.format(accuracy))

  kf = KFold(data.shape[0], n_folds=5)
  error = []
  for train, test in kf:
    train_predictors = (data[predictors].iloc[train,:])
    
    train_target = data[outcome].iloc[train]
    
    model.fit(train_predictors, train_target)
    
    error.append(model.score(data[predictors].iloc[test,:], data[outcome].iloc[test]))
 
  print('Cross-Validation Score : %s' % '{0:.3%}'.format(np.mean(error)))

  model.fit(data[predictors],data[outcome]) 


# In[14]:


from sklearn.linear_model import LogisticRegression
outcome_var=['Winner']
predictor_var = ['TeamA','TeamB','Venue','Toss','Toss_Decision','HTH','WinningPerDes','Strength','Latest_Form']
model = LogisticRegression(n_jobs=1000)
classification_model(model, df,predictor_var,outcome_var)


# In[15]:


df.head(3)


# In[16]:


model = RandomForestClassifier(n_estimators=100)
outcome_var = ['Winner']
predictor_var = ['TeamA','TeamB','Venue','Toss','Toss_Decision','HTH','WinningPerDes','Strength','Latest_Form']
classification_model(model, df,predictor_var,outcome_var)


# In[102]:


#feature importances: If we ignore teams, Venue seems to be one of important factors in determining winners 
#followed by toss winning, city
from PIL import Image
import matplotlib.pyplot as plt
imp_input = pd.Series(model.feature_importances_, index=predictor_var).sort_values(ascending=True)
fig = plt.figure(figsize=(10,6))
imp_input.plot(kind='barh')
fig.savefig('fanalysis1.png',bbox_inches = 'tight')
plt.rcParams.update({'font.size': 10})

print(imp_input)


# In[99]:


#okay from the above prediction on features, we notice toss winner has least chances of winning matches
#but does the current stats shows the same result
#print(df.count) 
import matplotlib.pyplot as mlt
mlt.style.use('fivethirtyeight')
df_fil=df[df['Toss_Decision']==df['Winner']]
slices=[len(df_fil),(426-len(df_fil))]
mlt.pie(slices,labels=['Toss Decision & Win','Toss Decisiosn & Loss'],startangle=90,shadow=True,explode=(0,0),autopct='%1.1f%%',colors=['g','r'])
fig = mlt.gcf()
fig.set_size_inches(4,4)
mlt.show()
plt.rcParams.update({'font.size': 90})

fig.savefig("toss_decision.png",bbox_inches = 'tight')
# Toss winning does not gaurantee a match win from analysis of current stats and thus 
#prediction feature gives less weightage to that 

