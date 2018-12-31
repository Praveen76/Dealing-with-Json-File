
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 17:21:58 2018

@author: praveenanwla
"""

import json
import pandas as pd
from pandas.io.json import json_normalize

import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

with open('C:/Users/praveenanwla/Desktop/MachinLearning/Chatlog/Data.json',encoding='utf-8-sig') as data_file:
    data=json.load(data_file)
    
    
print(type(data))    
data.keys()
data['matching_results']
#################################
data['results'][0].keys()
len(data['results'])
data['results'][0].keys()
#data['results'][0:3]['Quarter']
#data['results'][0:]['Quarter'][0:4]

# Extracting Quarter data
type(data['results'][i])
l1_Qartr=[]
for i in range(0,len(data['results'])):
    l1_Qartr.append(data['results'][i]['Quarter'])
    

# Extracting Read Ratio data
type(data['results'][i])
l1_ratio=[]
for i in range(0,len(data['results'])):
    l1_ratio.append(data['results'][i]['Read_ratio'])
    

# Extracting Entiched Text data
type(data['results'][i])
l1_entext=[]
for i in range(0,len(data['results'])):
    l1_entext.append(data['results'][i]['enriched_text'])
    
l1_entext[0:5]
    
# Exrtacting the columns from enriched text

# Extracting entities
l1_entities=[]
for i in range(0,len(data['results'])):
    # data['results'][8]['enriched_text']['entities']  
    l1_entities.append(data['results'][i]['enriched_text']['entities'])
    
l1_entities[0:5] 


# Extracting Concepts
l1_concepts_text=[]
l1_concepts_relev=[]
l1_concepts_dbpedia_resource=[]

for i in range(0,len(data['results'])):
    # data['results'][8]['enriched_text']['entities']  
    if len(data['results'][i]['enriched_text']['concepts'])==0:
        l1_concepts_text.append(0)
    else:
        l1_concepts_text.append(data['results'][i]['enriched_text']['concepts'][0]['text'])
        l1_concepts_relev.append(data['results'][i]['enriched_text']['concepts'][0]['relevance'])
        l1_concepts_dbpedia_resource.append(data['results'][i]['enriched_text']['concepts'][0]['dbpedia_resource'])
    
l1_concepts_text[0:5] 
l1_concepts_relev[0:5] 
l1_concepts_dbpedia_resource[0:5] 


# Extracting categories for score 1 and label 1
l1_categories_score1=[]
l1_categories_lebel1=[]

#l1_categories_score1=[]

for i in range(0,len(data['results'])):
    # data['results'][8]['enriched_text']['entities']  
    if len(data['results'][i]['enriched_text']['categories'][0])==0:
        l1_categories_score1.append(0)
        l1_categories_lebel1.append(0)
    else:
        l1_categories_score1.append(data['results'][i]['enriched_text']['categories'][0]['score'])
        l1_categories_lebel1.append(data['results'][i]['enriched_text']['categories'][0]['label'])
        
    
l1_categories_score1[0:5] 
l1_categories_lebel1[0:5] 


#==============================================================================
# # Extracting categories for score 2 and label 2
# l1_categories_score2=[]
# l1_categories_lebel2=[]
# 
# #l1_categories_score1=[]
# 
# for i in range(0,len(data['results'])):
#     # data['results'][8]['enriched_text']['entities']  
#     if len(data['results'][3]['enriched_text']['categories'][1])==1:
#         l1_categories_score2.append(0)
#         l1_categories_lebel2.append(0)
#     else:
#         l1_categories_score2.append(data['results'][i]['enriched_text']['categories'][1]['score'])
#         l1_categories_lebel2.append(data['results'][i]['enriched_text']['categories'][1]['label'])
#         
#     
# l1_categories_score2[0:5] 
# l1_categories_lebel2[0:5] 
#==============================================================================


# Extracting keyword 
l1_keyword_text=[]
l1_keyword_relevance=[]
l1_keyword_count=[]

for i in range(0,len(data['results'])):
    # data['results'][8]['enriched_text']['entities']  
    if len(data['results'][3]['enriched_text']['keywords'][0])==0:
        l1_keyword_text.append(0)
        l1_keyword_relevance.append(0)
        l1_keyword_count.append(0)
    else:
        l1_keyword_text.append(data['results'][i]['enriched_text']['keywords'][0]['text'])
        l1_keyword_relevance.append(data['results'][i]['enriched_text']['keywords'][0]['relevance'])
        l1_keyword_count.append(data['results'][i]['enriched_text']['keywords'][0]['count'])
        
    
l1_keyword_text[0:5] 
l1_keyword_relevance[0:5] 
l1_keyword_count 

df1=pd.concat([pd.Series(l1_Qartr),pd.Series(l1_concepts_text),pd.Series(l1_concepts_relev),pd.Series(l1_concepts_dbpedia_resource),
           pd.Series(l1_categories_score1),pd.Series(l1_categories_lebel1),pd.Series(l1_concepts_text),pd.Series(l1_concepts_relev),
           pd.Series(l1_concepts_dbpedia_resource),],axis=1)




df1.head()

df1.columns=['Quarter','Concepts_Text','Concepts_Rel','Concepts_dbpedia_resource',
             'categories_score1','categories_label1','concepts_text',
             'concepts_relev','concepts_dbpedia_resource',
             ]    

del df1['concepts_relev']
del df1['concepts_text']

df1=df1[['Quarter','Concepts_Text','Concepts_Rel']]


df1.to_csv("C:/Users/praveenanwla/Desktop/MachineLearning/Chatlog/df1.csv",index=False)


