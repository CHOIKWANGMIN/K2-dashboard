#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import pandas as pd


# In[2]:


data = pd.read_excel('//Users/choikwangmin/Desktop/캡스톤디자인_케이투코리아(주) 성능평가 결과.ver2.xlsx',sheet_name='성능평가 데이터 관리') #파일 경로 변경
data.head()


# In[3]:


data1=data.iloc[ : , :-15].drop(columns=['몰드명','라스트명','사이즈','수행일','의뢰부서'])


# In[4]:


data1


# In[5]:


data_1 = data1[data1.키 == '완제마모'].set_index(['키'])
data_2 = data1[data1.키 == '완제품미끄럼저항성'].set_index(['키'])
data_3 = data1[data1.키 == '정하중_충격흡수에너지'].set_index(['키'])


# In[6]:


data_1


# In[7]:


data_2


# In[8]:


data_3


# In[9]:


import collections
d = collections.defaultdict(list)
d2 = collections.defaultdict(list)
d3 = collections.defaultdict(list)
d4 = collections.defaultdict(list)
print(data_1)

for i,data in enumerate(pd.DataFrame.itertuples(data_1)):
    if i == 0: continue
    if str(data[10]) != "nan":
        d[data[7]].append(data[10])
    if str(data[11]) != "nan":
        d2[data[7]].append(data[11])
    if str(data[12]) != "nan":
        d3[data[7]].append(data[12])
    if str(data[13]) != "nan":
        d4[data[7]].append(data[13])
for dd in d:
    l = len(d[dd])
    s = sum(d[dd])
    a = s / l
    print(f"시즌 :{dd} 전체높이[mm] 평균 : {a}")
    
for dd in d2:
    l = len(d2[dd])
    s = sum(d2[dd])
    a = s / l
    print(f"시즌 :{dd} 러그높이[mm] 평균 : {a}")

for dd in d3:
    l = len(d3[dd])
    s = sum(d3[dd])
    a = s / l
    print(f"시즌 :{dd} 결과[회] 평균 : {a}")
    
for dd in d4:
    count = [0,0,0]
    for ddd in d4[dd]:
        if ddd == "부틸 30":
            count[0] += 1
        elif ddd == "부틸 70":
            count[1] += 1
        else:
            count[2] += 1
    print(f"시즌 : {dd} 아웃솔물성 부틸 30 : {int(count[0]/sum(count) * 100)}%")
    print(f"시즌 : {dd} 아웃솔물성 부틸 70 : {int(count[1]/sum(count) * 100)}%")
    print(f"시즌 : {dd} 아웃솔물성 일반 : {int(count[2]/sum(count) * 100)}%")


# In[10]:


import collections
d = collections.defaultdict(list)
d2 = collections.defaultdict(list)
d3 = collections.defaultdict(list)
d4 = collections.defaultdict(list)
print(data_1)

for i,data in enumerate(pd.DataFrame.itertuples(data_1)):
    if i == 0: continue
    if str(data[10]) != "nan":
        d[data[5]].append(data[10])
    if str(data[11]) != "nan":
        d2[data[5]].append(data[11])
    if str(data[12]) != "nan":
        d3[data[5]].append(data[12])
    if str(data[13]) != "nan":
        d4[data[5]].append(data[13])
for dd in d:
    l = len(d[dd])
    s = sum(d[dd])
    a = s / l
    print(f"카테고리 :{dd} 전체높이[mm] 평균 : {a}")
    
for dd in d2:
    l = len(d2[dd])
    s = sum(d2[dd])
    a = s / l
    print(f"카테고리 :{dd} 러그높이[mm] 평균 : {a}")

for dd in d3:
    l = len(d3[dd])
    s = sum(d3[dd])
    a = s / l
    print(f"카테고리 :{dd} 결과[회] 평균 : {a}")
    
for dd in d4:
    count = [0,0,0]
    for ddd in d4[dd]:
        if ddd == "부틸 30":
            count[0] += 1
        elif ddd == "부틸 70":
            count[1] += 1
        else:
            count[2] += 1
    print(f"카테고리 : {dd} 아웃솔물성 부틸 30 : {int(count[0]/sum(count) * 100)}%")
    print(f"카테고리 : {dd} 아웃솔물성 부틸 70 : {int(count[1]/sum(count) * 100)}%")
    print(f"카테고리 : {dd} 아웃솔물성 일반 : {int(count[2]/sum(count) * 100)}%")


# In[11]:


import collections
d = collections.defaultdict(list)
d2 = collections.defaultdict(list)
d3 = collections.defaultdict(list)
d4 = collections.defaultdict(list)
print(data_1)

for i,data in enumerate(pd.DataFrame.itertuples(data_1)):
    if i == 0: continue
    if str(data[10]) != "nan":
        d[data[3]].append(data[10])
    if str(data[11]) != "nan":
        d2[data[3]].append(data[11])
    if str(data[12]) != "nan":
        d3[data[3]].append(data[12])
    if str(data[13]) != "nan":
        d4[data[3]].append(data[13])
for dd in d:
    l = len(d[dd])
    s = sum(d[dd])
    a = s / l
    print(f"브랜드 :{dd} 전체높이[mm] 평균 : {a}")
    
for dd in d2:
    l = len(d2[dd])
    s = sum(d2[dd])
    a = s / l
    print(f"브랜드 :{dd} 러그높이[mm] 평균 : {a}")

for dd in d3:
    l = len(d3[dd])
    s = sum(d3[dd])
    a = s / l
    print(f"브랜드 :{dd} 결과[회] 평균 : {a}")
    
for dd in d4:
    count = [0,0,0]
    for ddd in d4[dd]:
        if ddd == "부틸 30":
            count[0] += 1
        elif ddd == "부틸 70":
            count[1] += 1
        else:
            count[2] += 1
    print(f"브랜드 : {dd} 아웃솔물성 부틸 30 : {int(count[0]/sum(count) * 100)}%")
    print(f"브랜드 : {dd} 아웃솔물성 부틸 70 : {int(count[1]/sum(count) * 100)}%")
    print(f"브랜드 : {dd} 아웃솔물성 일반 : {int(count[2]/sum(count) * 100)}%")


# In[12]:


import collections
d = collections.defaultdict(list)
d2 = collections.defaultdict(list)
d3 = collections.defaultdict(list)
d4 = collections.defaultdict(list)
d5 = collections.defaultdict(list)
print(data_2)

for i,data in enumerate(pd.DataFrame.itertuples(data_2)):
    if i == 0: continue
    if str(data[10]) != "nan":
        d[data[7]].append(data[10])
    if str(data[11]) != "nan":
        d2[data[7]].append(data[11])
    if str(data[12]) != "nan":
        d3[data[7]].append(data[12])
    if str(data[13]) != "nan":
        d4[data[7]].append(data[13])
    if str(data[14]) != "nan":
        d5[data[7]].append(data[14])
for dd in d:
    l = len(d[dd])
    s = sum(d[dd])
    a = s / l
    print(f"시즌 :{dd} 건식[도] 평균 : {a}")
    
for dd in d2:
    l = len(d2[dd])
    s = sum(d2[dd])
    a = s / l
    print(f"시즌 :{dd} 습식[도] 평균 : {a}")

for dd in d3:
    l = len(d3[dd])
    s = sum(d3[dd])
    a = s / l
    print(f"시즌 :{dd} 건습차[도] 평균 : {a}")
    
for dd in d4:
    l = len(d4[dd])
    s = sum(d4[dd])
    a = s / l
    print(f"시즌 :{dd} 건식[μ] 평균 : {a}")

for dd in d5:
    l = len(d5[dd])
    s = sum(d5[dd])
    a = s / l
    print(f"시즌 :{dd} 습식[μ] 평균 : {a}")


# In[13]:


import collections
d = collections.defaultdict(list)
d2 = collections.defaultdict(list)
d3 = collections.defaultdict(list)
d4 = collections.defaultdict(list)
d5 = collections.defaultdict(list)
print(data_2)

for i,data in enumerate(pd.DataFrame.itertuples(data_2)):
    if i == 0: continue
    if str(data[10]) != "nan":
        d[data[5]].append(data[10])
    if str(data[11]) != "nan":
        d2[data[5]].append(data[11])
    if str(data[12]) != "nan":
        d3[data[5]].append(data[12])
    if str(data[13]) != "nan":
        d4[data[5]].append(data[13])
    if str(data[14]) != "nan":
        d5[data[5]].append(data[14])
for dd in d:
    l = len(d[dd])
    s = sum(d[dd])
    a = s / l
    print(f"카테고리 :{dd} 건식[도] 평균 : {a}")
    
for dd in d2:
    l = len(d2[dd])
    s = sum(d2[dd])
    a = s / l
    print(f"카테고리 :{dd} 습식[도] 평균 : {a}")

for dd in d3:
    l = len(d3[dd])
    s = sum(d3[dd])
    a = s / l
    print(f"카테고리 :{dd} 건습차[도] 평균 : {a}")
    
for dd in d4:
    l = len(d4[dd])
    s = sum(d4[dd])
    a = s / l
    print(f"카테고리 :{dd} 건식[μ] 평균 : {a}")

for dd in d5:
    l = len(d5[dd])
    s = sum(d5[dd])
    a = s / l
    print(f"카테고리 :{dd} 습식[μ] 평균 : {a}")


# In[14]:


import collections
d = collections.defaultdict(list)
d2 = collections.defaultdict(list)
d3 = collections.defaultdict(list)
d4 = collections.defaultdict(list)
d5 = collections.defaultdict(list)
print(data_2)

for i,data in enumerate(pd.DataFrame.itertuples(data_2)):
    if i == 0: continue
    if str(data[10]) != "nan":
        d[data[3]].append(data[10])
    if str(data[11]) != "nan":
        d2[data[3]].append(data[11])
    if str(data[12]) != "nan":
        d3[data[3]].append(data[12])
    if str(data[13]) != "nan":
        d4[data[3]].append(data[13])
    if str(data[14]) != "nan":
        d5[data[3]].append(data[14])
for dd in d:
    l = len(d[dd])
    s = sum(d[dd])
    a = s / l
    print(f"브랜드 :{dd} 건식[도] 평균 : {a}")
    
for dd in d2:
    l = len(d2[dd])
    s = sum(d2[dd])
    a = s / l
    print(f"브랜드 :{dd} 습식[도] 평균 : {a}")

for dd in d3:
    l = len(d3[dd])
    s = sum(d3[dd])
    a = s / l
    print(f"브랜드 :{dd} 건습차[도] 평균 : {a}")
    
for dd in d4:
    l = len(d4[dd])
    s = sum(d4[dd])
    a = s / l
    print(f"브랜드 :{dd} 건식[μ] 평균 : {a}")

for dd in d5:
    l = len(d5[dd])
    s = sum(d5[dd])
    a = s / l
    print(f"브랜드 :{dd} 습식[μ] 평균 : {a}")


# In[15]:


import collections
d = collections.defaultdict(list)
d2 = collections.defaultdict(list)
d3 = collections.defaultdict(list)
d4 = collections.defaultdict(list)
d5 = collections.defaultdict(list)
print(data_3)

for i,data in enumerate(pd.DataFrame.itertuples(data_3)):
    if i == 0: continue
    if str(data[10]) != "nan":
        d[data[7]].append(data[10])
    if str(data[11]) != "nan":
        d2[data[7]].append(data[11])
    if str(data[12]) != "nan":
        d3[data[7]].append(data[12])
for dd in d:
    l = len(d[dd])
    s = sum(d[dd])
    a = s / l
    print(f"시즌 :{dd} 압축에너지[J] 평균 : {a}")
    
for dd in d2:
    l = len(d2[dd])
    s = sum(d2[dd])
    a = s / l
    print(f"시즌 :{dd} 탄성에너지[J] 평균 : {a}")

for dd in d3:
    l = len(d3[dd])
    s = sum(d3[dd])
    a = s / l
    print(f"시즌 :{dd} 에너지 효율[%] 평균 : {a}")


# In[16]:


import collections
d = collections.defaultdict(list)
d2 = collections.defaultdict(list)
d3 = collections.defaultdict(list)
d4 = collections.defaultdict(list)
d5 = collections.defaultdict(list)
print(data_3)

for i,data in enumerate(pd.DataFrame.itertuples(data_3)):
    if i == 0: continue
    if str(data[10]) != "nan":
        d[data[5]].append(data[10])
    if str(data[11]) != "nan":
        d2[data[5]].append(data[11])
    if str(data[12]) != "nan":
        d3[data[5]].append(data[12])
for dd in d:
    l = len(d[dd])
    s = sum(d[dd])
    a = s / l
    print(f"카테고리 :{dd} 압축에너지[J] 평균 : {a}")
    
for dd in d2:
    l = len(d2[dd])
    s = sum(d2[dd])
    a = s / l
    print(f"카테고리 :{dd} 탄성에너지[J] 평균 : {a}")

for dd in d3:
    l = len(d3[dd])
    s = sum(d3[dd])
    a = s / l
    print(f"카테고리 :{dd} 에너지 효율[%] 평균 : {a}")


# In[17]:


import collections
d = collections.defaultdict(list)
d2 = collections.defaultdict(list)
d3 = collections.defaultdict(list)
d4 = collections.defaultdict(list)
d5 = collections.defaultdict(list)
print(data_3)

for i,data in enumerate(pd.DataFrame.itertuples(data_3)):
    if i == 0: continue
    if str(data[10]) != "nan":
        d[data[3]].append(data[10])
    if str(data[11]) != "nan":
        d2[data[3]].append(data[11])
    if str(data[12]) != "nan":
        d3[data[3]].append(data[12])
for dd in d:
    l = len(d[dd])
    s = sum(d[dd])
    a = s / l
    print(f"브랜드 :{dd} 압축에너지[J] 평균 : {a}")
    
for dd in d2:
    l = len(d2[dd])
    s = sum(d2[dd])
    a = s / l
    print(f"브랜드 :{dd} 탄성에너지[J] 평균 : {a}")

for dd in d3:
    l = len(d3[dd])
    s = sum(d3[dd])
    a = s / l
    print(f"브랜드 :{dd} 에너지 효율[%] 평균 : {a}")


# In[18]:


import collections
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

d = collections.defaultdict(list)
d2 = collections.defaultdict(list)
d3 = collections.defaultdict(list)
d4 = collections.defaultdict(list)
print(data_1)

for i,data in enumerate(pd.DataFrame.itertuples(data_1)):
    if i == 0: continue
    if str(data[10]) != "nan":
        d[data[7]].append(data[10])
    if str(data[11]) != "nan":
        d2[data[7]].append(data[11])
    if str(data[12]) != "nan":
        d3[data[7]].append(data[12])
    if str(data[13]) != "nan":
        d4[data[7]].append(data[13])
list_graph_x = [] # x축에 들어갈 시즌
list_graph_y = [] # y축에 들어갈 평균
for dd in d:
    l = len(d[dd])
    s = sum(d[dd])
    a = s / l
    print(f"시즌 :{str(dd)} 전체높이[mm] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x.append("기타")
    else:
        list_graph_x.append(str(dd))
    if str(a) == "nan":
        list_graph_y.append(0)
    else:
        list_graph_y.append(a)
fig = px.line(x=list_graph_x, y=list_graph_y, title="전체높이[mm] 평균", markers=True)
fig.show()

        
list_graph_x = []
list_graph_y = []        
for dd in d2:
    l = len(d2[dd])
    s = sum(d2[dd])
    a = s / l
    print(f"시즌 :{dd} 러그높이[mm] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x.append("기타")
    else:
        list_graph_x.append(str(dd))
    if str(a) == "nan":
        list_graph_y.append(0)
    else:
        list_graph_y.append(a)

fig = px.line(x=list_graph_x, y=list_graph_y, title="러그높이[mm] 평균", markers=True)
fig.show()

list_graph_x = []
list_graph_y = []
for dd in d3:
    l = len(d3[dd])
    s = sum(d3[dd])
    a = s / l
    print(f"시즌 :{dd} 결과[회] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x.append("기타")
    else:
        list_graph_x.append(str(dd))
    if str(a) == "nan":
        list_graph_y.append(0)
    else:
        list_graph_y.append(a)
fig = px.line(x=list_graph_x, y=list_graph_y, title="결과[회] 평균", markers=True)
fig.show()
    
for dd in d4:
    count = [0,0,0]
    for ddd in d4[dd]:
        if ddd == "부틸 30":
            count[0] += 1
        elif ddd == "부틸 70":
            count[1] += 1
        else:
            count[2] += 1
    a = count[0]/sum(count) * 100
    b = count[1]/sum(count) * 100
    c = count[2]/sum(count) * 100
    print(f"시즌 : {dd} 아웃솔물성 부틸 30 : {a}%")
    print(f"시즌 : {dd} 아웃솔물성 부틸 70 : {b}%")
    print(f"시즌 : {dd} 아웃솔물성 일반 : {c}%")
    labels = ["부틸 30", "부틸 70", "일반"]
    fig = make_subplots(rows=1, cols=1, specs=[[{'type':'domain'}]])
    fig.add_trace(go.Pie(labels=labels, values=[a, b, c], name=dd),1, 1)
    fig.update_traces(hole=.4, hoverinfo="label+percent+name")
    if str(dd) == "nan":
        dd = "기타"
    fig.update_layout(
        title_text=f"{dd} 아웃솔물성",
        # Add annotations in the center of the donut pies.
        annotations=[dict(text=dd, x=0.18, y=0.5, font_size=20, showarrow=False)])
    fig.show()


# In[19]:


import collections
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

d = collections.defaultdict(list)
d2 = collections.defaultdict(list)
d3 = collections.defaultdict(list)
d4 = collections.defaultdict(list)
print(data_1)

for i,data in enumerate(pd.DataFrame.itertuples(data_1)):
    if i == 0: continue
    if str(data[10]) != "nan":
        d[data[5]].append(data[10])
    if str(data[11]) != "nan":
        d2[data[5]].append(data[11])
    if str(data[12]) != "nan":
        d3[data[5]].append(data[12])
    if str(data[13]) != "nan":
        d4[data[5]].append(data[13])
list_graph_x = [] # x축에 들어갈 시즌
list_graph_y = [] # y축에 들어갈 평균
for dd in d:
    l = len(d[dd])
    s = sum(d[dd])
    a = s / l
    print(f"카테고리 :{str(dd)} 전체높이[mm] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x.append("기타")
    else:
        list_graph_x.append(str(dd))
    if str(a) == "nan":
        list_graph_y.append(0)
    else:
        list_graph_y.append(a)
fig = px.line(x=list_graph_x, y=list_graph_y, title="전체높이[mm] 평균", markers=True)
fig.show()

        
list_graph_x = []
list_graph_y = []        
for dd in d2:
    l = len(d2[dd])
    s = sum(d2[dd])
    a = s / l
    print(f"카테고리 :{dd} 러그높이[mm] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x.append("기타")
    else:
        list_graph_x.append(str(dd))
    if str(a) == "nan":
        list_graph_y.append(0)
    else:
        list_graph_y.append(a)

fig = px.line(x=list_graph_x, y=list_graph_y, title="러그높이[mm] 평균", markers=True)
fig.show()

list_graph_x = []
list_graph_y = []
for dd in d3:
    l = len(d3[dd])
    s = sum(d3[dd])
    a = s / l
    print(f"카테고리 :{dd} 결과[회] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x.append("기타")
    else:
        list_graph_x.append(str(dd))
    if str(a) == "nan":
        list_graph_y.append(0)
    else:
        list_graph_y.append(a)
fig = px.line(x=list_graph_x, y=list_graph_y, title="결과[회] 평균", markers=True)
fig.show()
    
for dd in d4:
    count = [0,0,0]
    for ddd in d4[dd]:
        if ddd == "부틸 30":
            count[0] += 1
        elif ddd == "부틸 70":
            count[1] += 1
        else:
            count[2] += 1
    a = count[0]/sum(count) * 100
    b = count[1]/sum(count) * 100
    c = count[2]/sum(count) * 100
    print(f"카테고리 : {dd} 아웃솔물성 부틸 30 : {a}%")
    print(f"카테고리 : {dd} 아웃솔물성 부틸 70 : {b}%")
    print(f"카테고리 : {dd} 아웃솔물성 일반 : {c}%")
    labels = ["부틸 30", "부틸 70", "일반"]
    fig = make_subplots(rows=1, cols=1, specs=[[{'type':'domain'}]])
    fig.add_trace(go.Pie(labels=labels, values=[a, b, c], name=dd),1, 1)
    fig.update_traces(hole=.4, hoverinfo="label+percent+name")
    if str(dd) == "nan":
        dd = "기타"
    fig.update_layout(
        title_text=f"{dd} 아웃솔물성",
        # Add annotations in the center of the donut pies.
        annotations=[dict(text=dd, x=0.18, y=0.5, font_size=20, showarrow=False)])
    fig.show()


# In[20]:


import collections
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

d = collections.defaultdict(list)
d2 = collections.defaultdict(list)
d3 = collections.defaultdict(list)
d4 = collections.defaultdict(list)
print(data_1)

for i,data in enumerate(pd.DataFrame.itertuples(data_1)):
    if i == 0: continue
    if str(data[10]) != "nan":
        d[data[3]].append(data[10])
    if str(data[11]) != "nan":
        d2[data[3]].append(data[11])
    if str(data[12]) != "nan":
        d3[data[3]].append(data[12])
    if str(data[13]) != "nan":
        d4[data[3]].append(data[13])

list_graph_x = [] # x축에 들어갈 시즌
list_graph_y = [] # y축에 들어갈 평균
for dd in d:
    l = len(d[dd])
    s = sum(d[dd])
    a = s / l
    print(f"브랜드 :{str(dd)} 전체높이[mm] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x.append("기타")
    else:
        list_graph_x.append(str(dd))
    if str(a) == "nan":
        list_graph_y.append(0)
    else:
        list_graph_y.append(a)
fig = px.line(x=list_graph_x, y=list_graph_y, title="전체높이[mm] 평균", markers=True)
fig.show()

        
list_graph_x = []
list_graph_y = []        
for dd in d2:
    l = len(d2[dd])
    s = sum(d2[dd])
    a = s / l
    print(f"브랜드 :{dd} 러그높이[mm] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x.append("기타")
    else:
        list_graph_x.append(str(dd))
    if str(a) == "nan":
        list_graph_y.append(0)
    else:
        list_graph_y.append(a)

fig = px.line(x=list_graph_x, y=list_graph_y, title="러그높이[mm] 평균", markers=True)
fig.show()

list_graph_x = []
list_graph_y = []
for dd in d3:
    l = len(d3[dd])
    s = sum(d3[dd])
    a = s / l
    print(f"브랜드 :{dd} 결과[회] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x.append("기타")
    else:
        list_graph_x.append(str(dd))
    if str(a) == "nan":
        list_graph_y.append(0)
    else:
        list_graph_y.append(a)
fig = px.line(x=list_graph_x, y=list_graph_y, title="결과[회] 평균", markers=True)
fig.show()
    
for dd in d4:
    count = [0,0,0]
    for ddd in d4[dd]:
        if ddd == "부틸 30":
            count[0] += 1
        elif ddd == "부틸 70":
            count[1] += 1
        else:
            count[2] += 1
    a = count[0]/sum(count) * 100
    b = count[1]/sum(count) * 100
    c = count[2]/sum(count) * 100
    print(f"브랜드 : {dd} 아웃솔물성 부틸 30 : {a}%")
    print(f"브랜드 : {dd} 아웃솔물성 부틸 70 : {b}%")
    print(f"브랜드 : {dd} 아웃솔물성 일반 : {c}%")
    labels = ["부틸 30", "부틸 70", "일반"]
    fig = make_subplots(rows=1, cols=1, specs=[[{'type':'domain'}]])
    fig.add_trace(go.Pie(labels=labels, values=[a, b, c], name=dd),1, 1)
    fig.update_traces(hole=.4, hoverinfo="label+percent+name")
    if str(dd) == "nan":
        dd = "기타"
    fig.update_layout(
        title_text=f"{dd} 아웃솔물성",
        # Add annotations in the center of the donut pies.
        annotations=[dict(text=dd, x=0.18, y=0.5, font_size=20, showarrow=False)])
    fig.show()


# In[21]:


import collections
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

d = collections.defaultdict(list)
d2 = collections.defaultdict(list)
d3 = collections.defaultdict(list)
d4 = collections.defaultdict(list)
print(data_2)

for i,data in enumerate(pd.DataFrame.itertuples(data_2)):
    if i == 0: continue
    if str(data[10]) != "nan":
        d[data[7]].append(data[10])
    if str(data[11]) != "nan":
        d2[data[7]].append(data[11])
    if str(data[12]) != "nan":
        d3[data[7]].append(data[12])
    if str(data[13]) != "nan":
        d4[data[7]].append(data[13])
    if str(data[14]) != "nan":
        d5[data[7]].append(data[14])

list_graph_x = [] # x축에 들어갈 시즌
list_graph_y = [] # y축에 들어갈 평균
for dd in d:
    l = len(d[dd])
    s = sum(d[dd])
    a = s / l
    print(f"시즌 :{str(dd)} 건식[도] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x.append("기타")
    else:
        list_graph_x.append(str(dd))
    if str(a) == "nan":
        list_graph_y.append(0)
    else:
        list_graph_y.append(a)
fig = px.line(x=list_graph_x, y=list_graph_y, title="건식[도] 평균", markers=True)
fig.show()

        
list_graph_x = []
list_graph_y = []        
for dd in d2:
    l = len(d2[dd])
    s = sum(d2[dd])
    a = s / l
    print(f"시즌 :{dd} 습식[도] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x.append("기타")
    else:
        list_graph_x.append(str(dd))
    if str(a) == "nan":
        list_graph_y.append(0)
    else:
        list_graph_y.append(a)

fig = px.line(x=list_graph_x, y=list_graph_y, title="습식[도] 평균", markers=True)
fig.show()

list_graph_x = []
list_graph_y = []
for dd in d3:
    l = len(d3[dd])
    s = sum(d3[dd])
    a = s / l
    print(f"시즌 :{dd} 건습차[도] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x.append("기타")
    else:
        list_graph_x.append(str(dd))
    if str(a) == "nan":
        list_graph_y.append(0)
    else:
        list_graph_y.append(a)
fig = px.line(x=list_graph_x, y=list_graph_y, title="건습차[도] 평균", markers=True)
fig.show()

list_graph_x = []
list_graph_y = []        
for dd in d4:
    l = len(d4[dd])
    s = sum(d4[dd])
    a = s / l
    print(f"시즌 :{dd} 건식[μ] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x.append("기타")
    else:
        list_graph_x.append(str(dd))
    if str(a) == "nan":
        list_graph_y.append(0)
    else:
        list_graph_y.append(a)

fig = px.line(x=list_graph_x, y=list_graph_y, title="건식[μ] 평균", markers=True)
fig.show()

list_graph_x = []
list_graph_y = []
for dd in d5:
    l = len(d5[dd])
    s = sum(d5[dd])
    a = s / l
    print(f"시즌 :{dd} 습식[μ] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x.append("기타")
    else:
        list_graph_x.append(str(dd))
    if str(a) == "nan":
        list_graph_y.append(0)
    else:
        list_graph_y.append(a)
fig = px.line(x=list_graph_x, y=list_graph_y, title="습식[μ] 평균", markers=True)
fig.show()


# In[22]:


import collections
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

d = collections.defaultdict(list)
d2 = collections.defaultdict(list)
d3 = collections.defaultdict(list)
d4 = collections.defaultdict(list)
print(data_2)

for i,data in enumerate(pd.DataFrame.itertuples(data_2)):
    if i == 0: continue
    if str(data[10]) != "nan":
        d[data[5]].append(data[10])
    if str(data[11]) != "nan":
        d2[data[5]].append(data[11])
    if str(data[12]) != "nan":
        d3[data[5]].append(data[12])
    if str(data[13]) != "nan":
        d4[data[5]].append(data[13])
    if str(data[14]) != "nan":
        d5[data[5]].append(data[14])

list_graph_x = [] # x축에 들어갈 시즌
list_graph_y = [] # y축에 들어갈 평균
for dd in d:
    l = len(d[dd])
    s = sum(d[dd])
    a = s / l
    print(f"카테고리 :{str(dd)} 건식[도] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x.append("기타")
    else:
        list_graph_x.append(str(dd))
    if str(a) == "nan":
        list_graph_y.append(0)
    else:
        list_graph_y.append(a)
fig = px.line(x=list_graph_x, y=list_graph_y, title="건식[도] 평균", markers=True)
fig.show()

        
list_graph_x = []
list_graph_y = []        
for dd in d2:
    l = len(d2[dd])
    s = sum(d2[dd])
    a = s / l
    print(f"카테고리 :{dd} 습식[도] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x.append("기타")
    else:
        list_graph_x.append(str(dd))
    if str(a) == "nan":
        list_graph_y.append(0)
    else:
        list_graph_y.append(a)

fig = px.line(x=list_graph_x, y=list_graph_y, title="습식[도] 평균", markers=True)
fig.show()

list_graph_x = []
list_graph_y = []
for dd in d3:
    l = len(d3[dd])
    s = sum(d3[dd])
    a = s / l
    print(f"카테고리 :{dd} 건습차[도] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x.append("기타")
    else:
        list_graph_x.append(str(dd))
    if str(a) == "nan":
        list_graph_y.append(0)
    else:
        list_graph_y.append(a)
fig = px.line(x=list_graph_x, y=list_graph_y, title="건습차[도] 평균", markers=True)
fig.show()

list_graph_x = []
list_graph_y = []        
for dd in d4:
    l = len(d4[dd])
    s = sum(d4[dd])
    a = s / l
    print(f"카테고리 :{dd} 건식[μ] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x.append("기타")
    else:
        list_graph_x.append(str(dd))
    if str(a) == "nan":
        list_graph_y.append(0)
    else:
        list_graph_y.append(a)

fig = px.line(x=list_graph_x, y=list_graph_y, title="건식[μ] 평균", markers=True)
fig.show()

list_graph_x = []
list_graph_y = []
for dd in d5:
    l = len(d5[dd])
    s = sum(d5[dd])
    a = s / l
    print(f"카테고리 :{dd} 습식[μ] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x.append("기타")
    else:
        list_graph_x.append(str(dd))
    if str(a) == "nan":
        list_graph_y.append(0)
    else:
        list_graph_y.append(a)
fig = px.line(x=list_graph_x, y=list_graph_y, title="습식[μ] 평균", markers=True)
fig.show()


# In[23]:


import collections
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

d = collections.defaultdict(list)
d2 = collections.defaultdict(list)
d3 = collections.defaultdict(list)
d4 = collections.defaultdict(list)
print(data_2)

for i,data in enumerate(pd.DataFrame.itertuples(data_2)):
    if i == 0: continue
    if str(data[10]) != "nan":
        d[data[3]].append(data[10])
    if str(data[11]) != "nan":
        d2[data[3]].append(data[11])
    if str(data[12]) != "nan":
        d3[data[3]].append(data[12])
    if str(data[13]) != "nan":
        d4[data[3]].append(data[13])
    if str(data[14]) != "nan":
        d5[data[3]].append(data[14])

list_graph_x = [] # x축에 들어갈 시즌
list_graph_y = [] # y축에 들어갈 평균
for dd in d:
    l = len(d[dd])
    s = sum(d[dd])
    a = s / l
    print(f"브랜드 :{str(dd)} 건식[도] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x.append("기타")
    else:
        list_graph_x.append(str(dd))
    if str(a) == "nan":
        list_graph_y.append(0)
    else:
        list_graph_y.append(a)
fig = px.line(x=list_graph_x, y=list_graph_y, title="건식[도] 평균", markers=True)
fig.show()

        
list_graph_x = []
list_graph_y = []        
for dd in d2:
    l = len(d2[dd])
    s = sum(d2[dd])
    a = s / l
    print(f"브랜드 :{dd} 습식[도] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x.append("기타")
    else:
        list_graph_x.append(str(dd))
    if str(a) == "nan":
        list_graph_y.append(0)
    else:
        list_graph_y.append(a)

fig = px.line(x=list_graph_x, y=list_graph_y, title="습식[도] 평균", markers=True)
fig.show()

list_graph_x = []
list_graph_y = []
for dd in d3:
    l = len(d3[dd])
    s = sum(d3[dd])
    a = s / l
    print(f"브랜드 :{dd} 건습차[도] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x.append("기타")
    else:
        list_graph_x.append(str(dd))
    if str(a) == "nan":
        list_graph_y.append(0)
    else:
        list_graph_y.append(a)
fig = px.line(x=list_graph_x, y=list_graph_y, title="건습차[도] 평균", markers=True)
fig.show()

list_graph_x = []
list_graph_y = []        
for dd in d4:
    l = len(d4[dd])
    s = sum(d4[dd])
    a = s / l
    print(f"브랜드 :{dd} 건식[μ] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x.append("기타")
    else:
        list_graph_x.append(str(dd))
    if str(a) == "nan":
        list_graph_y.append(0)
    else:
        list_graph_y.append(a)

fig = px.line(x=list_graph_x, y=list_graph_y, title="건식[μ] 평균", markers=True)
fig.show()

list_graph_x = []
list_graph_y = []
for dd in d5:
    l = len(d5[dd])
    s = sum(d5[dd])
    a = s / l
    print(f"브랜드 :{dd} 습식[μ] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x.append("기타")
    else:
        list_graph_x.append(str(dd))
    if str(a) == "nan":
        list_graph_y.append(0)
    else:
        list_graph_y.append(a)
fig = px.line(x=list_graph_x, y=list_graph_y, title="습식[μ] 평균", markers=True)
fig.show()


# In[24]:


import collections
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

d = collections.defaultdict(list)
d2 = collections.defaultdict(list)
d3 = collections.defaultdict(list)
d4 = collections.defaultdict(list)
print(data_3)

for i,data in enumerate(pd.DataFrame.itertuples(data_3)):
    if i == 0: continue
    if str(data[10]) != "nan":
        d[data[7]].append(data[10])
    if str(data[11]) != "nan":
        d2[data[7]].append(data[11])
    if str(data[12]) != "nan":
        d3[data[7]].append(data[12])

list_graph_x = [] # x축에 들어갈 시즌
list_graph_y = [] # y축에 들어갈 평균
for dd in d:
    l = len(d[dd])
    s = sum(d[dd])
    a = s / l
    print(f"시즌 :{str(dd)} 압축에너지[J] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x.append("기타")
    else:
        list_graph_x.append(str(dd))
    if str(a) == "nan":
        list_graph_y.append(0)
    else:
        list_graph_y.append(a)
fig = px.line(x=list_graph_x, y=list_graph_y, title="압축에너지[J] 평균", markers=True)
fig.show()

        
list_graph_x = []
list_graph_y = []        
for dd in d2:
    l = len(d2[dd])
    s = sum(d2[dd])
    a = s / l
    print(f"시즌 :{dd} 탄성에너지[J] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x.append("기타")
    else:
        list_graph_x.append(str(dd))
    if str(a) == "nan":
        list_graph_y.append(0)
    else:
        list_graph_y.append(a)

fig = px.line(x=list_graph_x, y=list_graph_y, title="탄성에너지[J] 평균", markers=True)
fig.show()

list_graph_x = []
list_graph_y = []
for dd in d3:
    l = len(d3[dd])
    s = sum(d3[dd])
    a = s / l
    print(f"시즌 :{dd} 에너지효율[%] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x.append("기타")
    else:
        list_graph_x.append(str(dd))
    if str(a) == "nan":
        list_graph_y.append(0)
    else:
        list_graph_y.append(a)
fig = px.line(x=list_graph_x, y=list_graph_y, title="에너지효율[%] 평균", markers=True)
fig.show()


# In[25]:


import collections
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

d = collections.defaultdict(list)
d2 = collections.defaultdict(list)
d3 = collections.defaultdict(list)
d4 = collections.defaultdict(list)
print(data_3)

for i,data in enumerate(pd.DataFrame.itertuples(data_3)):
    if i == 0: continue
    if str(data[10]) != "nan":
        d[data[5]].append(data[10])
    if str(data[11]) != "nan":
        d2[data[5]].append(data[11])
    if str(data[12]) != "nan":
        d3[data[5]].append(data[12])

list_graph_x = [] # x축에 들어갈 시즌
list_graph_y = [] # y축에 들어갈 평균
for dd in d:
    l = len(d[dd])
    s = sum(d[dd])
    a = s / l
    print(f"카테고리 :{str(dd)} 압축에너지[J] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x.append("기타")
    else:
        list_graph_x.append(str(dd))
    if str(a) == "nan":
        list_graph_y.append(0)
    else:
        list_graph_y.append(a)
fig = px.line(x=list_graph_x, y=list_graph_y, title="압축에너지[J] 평균", markers=True)
fig.show()

        
list_graph_x = []
list_graph_y = []        
for dd in d2:
    l = len(d2[dd])
    s = sum(d2[dd])
    a = s / l
    print(f"카테고리 :{dd} 탄성에너지[J] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x.append("기타")
    else:
        list_graph_x.append(str(dd))
    if str(a) == "nan":
        list_graph_y.append(0)
    else:
        list_graph_y.append(a)

fig = px.line(x=list_graph_x, y=list_graph_y, title="탄성에너지[J] 평균", markers=True)
fig.show()

list_graph_x = []
list_graph_y = []
for dd in d3:
    l = len(d3[dd])
    s = sum(d3[dd])
    a = s / l
    print(f"카테고리 :{dd} 에너지효율[%] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x.append("기타")
    else:
        list_graph_x.append(str(dd))
    if str(a) == "nan":
        list_graph_y.append(0)
    else:
        list_graph_y.append(a)
fig = px.line(x=list_graph_x, y=list_graph_y, title="에너지효율[%] 평균", markers=True)
fig.show()


# In[26]:


import collections
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

d = collections.defaultdict(list)
d2 = collections.defaultdict(list)
d3 = collections.defaultdict(list)
d4 = collections.defaultdict(list)
print(data_3)

for i,data in enumerate(pd.DataFrame.itertuples(data_3)):
    if i == 0: continue
    if str(data[10]) != "nan":
        d[data[3]].append(data[10])
    if str(data[11]) != "nan":
        d2[data[3]].append(data[11])
    if str(data[12]) != "nan":
        d3[data[3]].append(data[12])

list_graph_x = [] # x축에 들어갈 시즌
list_graph_y = [] # y축에 들어갈 평균
for dd in d:
    l = len(d[dd])
    s = sum(d[dd])
    a = s / l
    print(f"브랜드 :{str(dd)} 압축에너지[J] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x.append("기타")
    else:
        list_graph_x.append(str(dd))
    if str(a) == "nan":
        list_graph_y.append(0)
    else:
        list_graph_y.append(a)
fig = px.line(x=list_graph_x, y=list_graph_y, title="압축에너지[J] 평균", markers=True)
fig.show()

        
list_graph_x = []
list_graph_y = []        
for dd in d2:
    l = len(d2[dd])
    s = sum(d2[dd])
    a = s / l
    print(f"브랜드 :{dd} 탄성에너지[J] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x.append("기타")
    else:
        list_graph_x.append(str(dd))
    if str(a) == "nan":
        list_graph_y.append(0)
    else:
        list_graph_y.append(a)

fig = px.line(x=list_graph_x, y=list_graph_y, title="탄성에너지[J] 평균", markers=True)
fig.show()

list_graph_x = []
list_graph_y = []
for dd in d3:
    l = len(d3[dd])
    s = sum(d3[dd])
    a = s / l
    print(f"브랜드 :{dd} 에너지효율[%] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x.append("기타")
    else:
        list_graph_x.append(str(dd))
    if str(a) == "nan":
        list_graph_y.append(0)
    else:
        list_graph_y.append(a)
fig = px.line(x=list_graph_x, y=list_graph_y, title="에너지효율[%] 평균", markers=True)
fig.show()


# In[27]:


fig = go.Figure(go.Box(x=data_2[data_2['시즌']=="15FW"].시즌,y=data_2['value1'], name='15FW',boxmean = 'sd'))
fig.add_trace(go.Box(x=data_2[data_2['시즌']=='16FW'].시즌,y=data_2['value1'], name='16FW',boxmean = 'sd'))
fig.add_trace(go.Box(x=data_2[data_2['시즌']=='17SS'].시즌,y=data_2['value1'], name='17SS',boxmean = 'sd'))
fig.add_trace(go.Box(x=data_2[data_2['시즌']=='17FW'].시즌,y=data_2['value1'], name='17FW',boxmean = 'sd'))
fig.add_trace(go.Box(x=data_2[data_2['시즌']=='18SS'].시즌,y=data_2['value1'], name='18SS',boxmean = 'sd'))
fig.add_trace(go.Box(x=data_2[data_2['시즌']=='18FW'].시즌,y=data_2['value1'], name='18FW',boxmean = 'sd'))
fig.add_trace(go.Box(x=data_2[data_2['시즌']=='19SS'].시즌,y=data_2['value1'], name='19SS',boxmean = 'sd'))
fig.add_trace(go.Box(x=data_2[data_2['시즌']=='19FW'].시즌,y=data_2['value1'], name='19FW',boxmean = 'sd'))
fig.add_trace(go.Box(x=data_2[data_2['시즌']=='20SS'].시즌,y=data_2['value1'], name='20SS',boxmean = 'sd'))
fig.add_trace(go.Box(x=data_2[data_2['시즌']=='20FW'].시즌,y=data_2['value1'], name='20FW',boxmean = 'sd'))
fig.add_trace(go.Box(x=data_2[data_2['시즌']=='21SS'].시즌,y=data_2['value1'], name='21SS',boxmean = 'sd'))
fig.add_trace(go.Box(x=data_2[data_2['시즌']=='21FW'].시즌,y=data_2['value1'], name='21FW',boxmean = 'sd'))
fig.add_trace(go.Box(x=data_2[data_2['시즌']=='22SS'].시즌,y=data_2['value1'], name='22SS',boxmean = 'sd'))
fig.update_layout(boxmode='group',title="미끄럼저항성 테스트 결과",xaxis={'categoryorder':'array','categoryarray':['15FW','16FW','17SS','17FW','18SS','18FW','19SS','19FW','20SS','20FW','21SS','21FW','22SS']})
fig.update_xaxes(title_text='시즌')
fig.update_yaxes(title_text='건식[도]')
fig.show()


# In[77]:


fig_mamo = go.Figure(go.Box(x=data_1[data_1['브랜드']=="케이투"].value4,y=data_1[data_1['브랜드']=="케이투"].value3, name='케이투',boxmean = 'sd'))
fig_mamo.add_trace(go.Box(x=data_1[data_1['브랜드']=='아이더'].value4,y=data_1[data_1['브랜드']=="아이더"].value3, name='아이더',boxmean = 'sd'))
fig_mamo.add_trace(go.Box(x=data_1[data_1['브랜드']=='다이나핏'].value4,y=data_1[data_1['브랜드']=="다이나핏"].value3, name='다이나핏',boxmean = 'sd'))
fig_mamo.add_trace(go.Box(x=data_1[data_1['브랜드']=='SAFETY'].value4,y=data_1[data_1['브랜드']=="SAFETY"].value3, name='SAFETY',boxmean = 'sd'))
fig_mamo.update_layout(boxmode='group',title="완제마모 테스트 결과",xaxis={'categoryorder':'array','categoryarray':['일반','부틸 30','부틸 70']})
fig_mamo.update_xaxes(title_text='아웃솔 물성')
fig_mamo.update_yaxes(title_text="완제마모(회)") 
fig_mamo.show()


# In[78]:


fig_dry = go.Figure(go.Box(x=data_2[data_2['카테고리']=="러닝화"].브랜드,y=data_2[data_2['카테고리']=="러닝화"].value1, name='러닝화',boxmean = 'sd'))
fig_dry.add_trace(go.Box(x=data_2[data_2['카테고리']=='릿지화'].브랜드,y=data_2[data_2['카테고리']=="릿지화"].value1, name='릿지화',boxmean = 'sd'))
fig_dry.add_trace(go.Box(x=data_2[data_2['카테고리']=='워킹화'].브랜드,y=data_2[data_2['카테고리']=="워킹화"].value1, name='워킹화',boxmean = 'sd'))
fig_dry.add_trace(go.Box(x=data_2[data_2['카테고리']=='캐쥬얼화'].브랜드,y=data_2[data_2['카테고리']=="캐쥬얼화"].value1, name='캐쥬얼화',boxmean = 'sd'))
fig_dry.add_trace(go.Box(x=data_2[data_2['카테고리']=='트레킹화'].브랜드,y=data_2[data_2['카테고리']=="트레킹화"].value1, name='트레킹화',boxmean = 'sd'))
fig_dry.add_trace(go.Box(x=data_2[data_2['카테고리']=='하이킹화'].브랜드,y=data_2[data_2['카테고리']=="하이킹화"].value1, name='하이킹화',boxmean = 'sd'))
fig_dry.add_trace(go.Box(x=data_2[data_2['카테고리']=='중작업안전화'].브랜드,y=data_2[data_2['카테고리']=="중작업안전화"].value1, name='중작업안전화',boxmean = 'sd'))
fig_dry.update_layout(boxmode='group',title="사용자미끄럼저항성 테스트 결과",xaxis={'categoryorder':'array','categoryarray':['다이나핏','살레와','아이더','케이투','케이투세이프티','타사']})
fig_dry.update_xaxes(title_text='브랜드')
fig_dry.update_yaxes(title_text="건식[도]") 
fig_dry.show()


# In[79]:


fig_wet = go.Figure(go.Box(x=data_2[data_2['카테고리']=="러닝화"].브랜드,y=data_2[data_2['카테고리']=="러닝화"].value2, name='러닝화',boxmean = 'sd'))
fig_wet.add_trace(go.Box(x=data_2[data_2['카테고리']=='릿지화'].브랜드,y=data_2[data_2['카테고리']=="릿지화"].value2, name='릿지화',boxmean = 'sd'))
fig_wet.add_trace(go.Box(x=data_2[data_2['카테고리']=='워킹화'].브랜드,y=data_2[data_2['카테고리']=="워킹화"].value2, name='워킹화',boxmean = 'sd'))
fig_wet.add_trace(go.Box(x=data_2[data_2['카테고리']=='캐쥬얼화'].브랜드,y=data_2[data_2['카테고리']=="캐쥬얼화"].value2, name='캐쥬얼화',boxmean = 'sd'))
fig_wet.add_trace(go.Box(x=data_2[data_2['카테고리']=='트레킹화'].브랜드,y=data_2[data_2['카테고리']=="트레킹화"].value2, name='트레킹화',boxmean = 'sd'))
fig_wet.add_trace(go.Box(x=data_2[data_2['카테고리']=='하이킹화'].브랜드,y=data_2[data_2['카테고리']=="하이킹화"].value2, name='하이킹화',boxmean = 'sd'))
fig_wet.add_trace(go.Box(x=data_2[data_2['카테고리']=='중작업안전화'].브랜드,y=data_2[data_2['카테고리']=="중작업안전화"].value2, name='중작업안전화',boxmean = 'sd'))
fig_wet.update_layout(boxmode='group',title="사용자미끄럼저항성 테스트 결과",xaxis={'categoryorder':'array','categoryarray':['다이나핏','살레와','아이더','케이투','케이투세이프티','타사']})
fig_wet.update_xaxes(title_text='브랜드')
fig_wet.update_yaxes(title_text="습식[도]") 
fig_wet.show()


# In[80]:


fig_energy = go.Figure(go.Box(x=data_3[data_3['카테고리']=="러닝화"].브랜드,y=data_3[data_3['카테고리']=="러닝화"].value3, name='러닝화',boxmean = 'sd'))
fig_energy.add_trace(go.Box(x=data_3[data_3['카테고리']=='트레킹화'].브랜드,y=data_3[data_3['카테고리']=="트레킹화"].value3, name='트레킹화',boxmean = 'sd'))
fig_energy.add_trace(go.Box(x=data_3[data_3['카테고리']=='하이킹화'].브랜드,y=data_3[data_3['카테고리']=="하이킹화"].value3, name='하이킹화',boxmean = 'sd'))
fig_energy.add_trace(go.Box(x=data_3[data_3['카테고리']=='중작업안전화'].브랜드,y=data_3[data_3['카테고리']=="중작업안전화"].value3, name='중작업안전화',boxmean = 'sd'))
fig_energy.update_layout(boxmode='group',title="정하중_충격흡수에너지 테스트 결과",xaxis={'categoryorder':'array','categoryarray':['다이나핏','살레와','아이더','케이투','케이투세이프티','타사']})
fig_energy.update_xaxes(title_text='브랜드')
fig_energy.update_yaxes(title_text="에너지 효율(%)") 
fig_energy.show()


# In[81]:


import plotly.graph_objects as go

d = collections.defaultdict(list)
d2 = collections.defaultdict(list)
d3 = collections.defaultdict(list)
d4 = collections.defaultdict(list)

for i,data in enumerate(pd.DataFrame.itertuples(data_1)):
    if i == 0: continue
    if str(data[10]) != "nan":
        d[data[3]].append(data[10])
    if str(data[11]) != "nan":
        d2[data[3]].append(data[11])
    if str(data[12]) != "nan":
        d3[data[3]].append(data[12])
    if str(data[13]) != "nan":
        d4[data[3]].append(data[13])

        
list_graph_x = []
list_graph_y = []
for dd in d3:
    l = len(d3[dd])
    s = sum(d3[dd])
    a = s / l
    print(f"브랜드 :{dd} 결과[회] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x.append("기타")
    else:
        list_graph_x.append(str(dd))
    if str(a) == "nan":
        list_graph_y.append(0)
    else:
        list_graph_y.append(a)
        
# 막대그래프
fig_mamo_bar = go.Figure(data=[go.Bar(
            x=list_graph_x, y=list_graph_y,
            textposition='auto',
        )])
fig_mamo_bar.update_layout(title="완제마모 실험 결과 평균")
# fig = px.line(x=list_graph_x, y=list_graph_y, title="결과[회] 평균", markers=True)
fig_mamo_bar.show()


# In[90]:


for i,data in enumerate(pd.DataFrame.itertuples(data_2)):
    if i == 0: continue
    if str(data[10]) != "nan":
        d[data[3]].append(data[10])
    if str(data[11]) != "nan":
        d2[data[3]].append(data[11])
    if str(data[12]) != "nan":
        d3[data[3]].append(data[12])
    if str(data[13]) != "nan":
        d4[data[3]].append(data[13])
    if str(data[14]) != "nan":
        d5[data[3]].append(data[14])

list_graph_x1 = [] # x축에 들어갈 시즌
list_graph_y1 = [] # y축에 들어갈 평균
for dd in d:
    l = len(d[dd])
    s = sum(d[dd])
    a = s / l
    print(f"브랜드 :{str(dd)} 건식[도] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x1.append("기타")
    else:
        list_graph_x1.append(str(dd))
    if str(a) == "nan":
        list_graph_y1.append(0)
    else:
        list_graph_y1.append(a)

list_graph_x2 = []
list_graph_y2 = []        
for dd in d2:
    l = len(d2[dd])
    s = sum(d2[dd])
    a = s / l
    print(f"브랜드 :{dd} 습식[도] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x2.append("기타")
    else:
        list_graph_x2.append(str(dd))
    if str(a) == "nan":
        list_graph_y2.append(0)
    else:
        list_graph_y2.append(a)

brands = list_graph_x1

fig_drywet_bar = go.Figure(data=[
    go.Bar(name='건식[도] 평균', x=brands, y=list_graph_y1),
    go.Bar(name='습식[도] 평균', x=brands, y=list_graph_y2)
])
# Change the bar mod
fig_drywet_bar.update_layout(barmode='group', title="미끄럼저항성 실험 결과 평균")
fig_drywet_bar.show()


# In[83]:


d = collections.defaultdict(list)
d2 = collections.defaultdict(list)
d3 = collections.defaultdict(list)
d4 = collections.defaultdict(list)
print(data_3)

for i,data in enumerate(pd.DataFrame.itertuples(data_3)):
    if i == 0: continue
    if str(data[10]) != "nan":
        d[data[3]].append(data[10])
    if str(data[11]) != "nan":
        d2[data[3]].append(data[11])
    if str(data[12]) != "nan":
        d3[data[3]].append(data[12])
        
list_graph_x = []
list_graph_y = []
for dd in d3:
    l = len(d3[dd])
    s = sum(d3[dd])
    a = s / l
    print(f"브랜드 :{dd} 에너지효율[%] 평균 : {a}")
    if str(dd) == "nan":
        list_graph_x.append("기타")
    else:
        list_graph_x.append(str(dd))
    if str(a) == "nan":
        list_graph_y.append(0)
    else:
        list_graph_y.append(a)

# 막대그래프
fig_energy_bar = go.Figure(data=[go.Bar(
            x=list_graph_x, y=list_graph_y,
            textposition='auto',
        )])

fig_energy_bar.update_layout(title="에너지효율[%] 평균")
fig_energy_bar.show()


# In[84]:


for i,data in enumerate(pd.DataFrame.itertuples(data_1)):
    if i == 0: continue
    if str(data[10]) != "nan":
        d[data[3]].append(data[10])
    if str(data[11]) != "nan":
        d2[data[3]].append(data[11])
    if str(data[12]) != "nan":
        d3[data[3]].append(data[12])
    if str(data[13]) != "nan":
        d4[data[3]].append(data[13])

for dd in d4:
    count = [0,0,0]
    for ddd in d4[dd]:
        if ddd == "부틸 30":
            count[0] += 1
        elif ddd == "부틸 70":
            count[1] += 1
        else:
            count[2] += 1
    a = count[0]/sum(count) * 100
    b = count[1]/sum(count) * 100
    c = count[2]/sum(count) * 100
    print(f"브랜드 : {dd} 아웃솔물성 부틸 30 : {a}%")
    print(f"브랜드 : {dd} 아웃솔물성 부틸 70 : {b}%")
    print(f"브랜드 : {dd} 아웃솔물성 일반 : {c}%")
    labels = ["부틸 30", "부틸 70", "일반"]
    fig = make_subplots(rows=1, cols=1, specs=[[{'type':'domain'}]])
    fig.add_trace(go.Pie(labels=labels, values=[a, b, c], name=dd),1, 1)
    fig.update_traces(hole=.4, hoverinfo="label+percent+name")
    if str(dd) == "nan":
        dd = "기타"
    fig.update_layout(
        title_text=f"{dd} 아웃솔물성",
        # Add annotations in the center of the donut pies.
        annotations=[dict(text=dd, x=0.18, y=0.5, font_size=20, showarrow=False)])
    if dd == '케이투':
        print("aa")
        fig_k2 = fig
        fig_k2.show()
    elif dd == '아이더':
        fig_eider = fig
        fig_eider.show()
    elif dd == '다이나핏':
        fig_dynafit = fig
        fig_dynafit.show()
    elif dd == 'SAFETY':
        fig_safety = fig
        fig_safety.show()
    


# In[85]:


import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output


# In[91]:


app = dash.Dash(__name__)
app.title = ('Dashboard | Sales Data')
server = app.server
app.layout = html.Div([
    html.H2('케이투코리아 성능평가 결과',
           style={'textAlign' : 'center',
                 'marginBottom' : 10, 'marginTop' : 10}),
    html.Div(className='Boxplot',
            children=[
                html.Div(dcc.Graph(id='mamo',figure = fig_mamo), style={'float':'left', 'display':'inline-block','width':'50%'}, ),
                html.Div(dcc.Graph(id='energy',figure = fig_energy), style={'float':'left', 'display':'inline-block','width':'50%'}),
            
            ]),
    html.Div(className='Boxplot2',
            children=[
                html.Div(dcc.Graph(id='dry',figure = fig_dry), style={'float':'left', 'display':'inline-block','width':'50%'}),
                html.Div(dcc.Graph(id='wet',figure = fig_wet), style={'float':'left', 'display':'inline-block','width':'50%'})
            ]),
    html.Div(className='bar',
            children=[
                html.Div(dcc.Graph(id='mamo_bar',figure = fig_mamo_bar), style={'float':'left', 'display':'inline-block','width':'33%'}),
                html.Div(dcc.Graph(id='drywet_bar',figure = fig_drywet_bar), style={'float':'left', 'display':'inline-block','width':'33%'}),
                html.Div(dcc.Graph(id='energy_bar',figure = fig_energy_bar), style={'float':'left', 'display':'inline-block','width':'33%'})
            ]),
    html.Div(className='pie_chart',
            children=[
                html.Div(dcc.Graph(id='k2_pie',figure = fig_k2), style={'float':'left', 'display':'inline-block','width':'25%'}),
                html.Div(dcc.Graph(id='eider_pie',figure = fig_eider), style={'float':'left', 'display':'inline-block','width':'25%'}),
                html.Div(dcc.Graph(id='dynafit_pie',figure = fig_dynafit), style={'float':'left', 'display':'inline-block','width':'25%'}),
                html.Div(dcc.Graph(id='safety_pie',figure = fig_safety), style={'float':'left', 'display':'inline-block','width':'25%'}),
            ])
])


# In[ ]:


app.run_server(debug = False)


# In[ ]:




