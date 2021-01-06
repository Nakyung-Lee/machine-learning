#!/usr/bin/env python
# coding: utf-8

# # Matplotlib를 이용한 시각화

# ## 선으로 시각화 하기

# ### Python package 가져오기 및 matplotlib 출력 옵션 설정

# In[2]:


import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

get_ipython().run_line_magic('matplotlib', 'inline')


# ### 임의의 값 40개로 이루어진 배열

# In[2]:


value = np.random.standard_normal(40)
value


# In[3]:


type(value)


# ### 선 plot 그리기

# In[4]:


index = range(len(value))
plt.plot(index, value)
# x/y 축 범위 설정
plt.xlim(0, 20)
plt.ylim(np.min(value) -1, np.max(value) + 1)


# In[5]:


plt.figure(figsize=(7,4)) #plot의 새로운 모양을 생성하는 함수
plt.plot(value.cumsum(), 'b', lw= 1.5) #누적합계 구하는 함수
plt.plot(value.cumsum(), 'ro')
plt.xlabel('index') #x축 이름 설정
plt.ylabel('value') #y축 이름 설정
plt.title('Line Plot 1') #plot의 제목 설정


# ### 랜덤 값으로 이루어진 2차원 배열

# In[6]:


value = np.random.standard_normal((30, 2))
value


# ### 2차원 데이터 생성 및 시각화

# In[7]:


plt.figure(figsize=(10,4))
plt.plot(value[:,0], lw= 1.5)
plt.plot(value[:,1], lw= 1.5)
plt.plot(value, 'ro')
plt.grid(True)
# plt.legend(loc=0)
plt.xlabel('index')
plt.ylabel('value')
plt.title('Line Plot 2')


# ### 데이터 별로 각각 그리기

# In[8]:


# 1번째
plt.figure(figsize=(10,5))
plt.subplot(211)
plt.plot(value[:,0], lw = 1.5, label = '1st')
plt.plot(value[:,0], 'ro')
plt.grid(True)
plt.legend(loc = 0)
plt.ylabel("value")
plt.title('Line Plot 3')
# 2번째
plt.subplot(212)
plt.plot(value[:,1], 'g', lw = 1.5, label = '2nd')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.ylabel('value')


# ## 산점도로 시각화 하기

# ### 표준정규분포를 따르는 랜덤 값들로 이루어진 numpy.ndarray형 변수

# In[3]:


value = np.random.standard_normal((500,2))
plt.plot(value[:,0], value[:,1], 'ro')
plt.grid(False)
plt.xlabel('value 1')
plt.ylabel('value 2')
plt.title('Scatter Plot 1')


# ### x변수 대 y변수의 산점도를 만드는 pyplot.scatter 함수

# In[4]:


plt.figure(figsize=(7,5))
plt.scatter(value[:,0], value[:,1], marker='o')
plt.grid(True)
plt.xlabel('value 1')
plt.ylabel('value 2')
plt.title('Scatter Plot 2')


# ### 산점도에 색깔 입히기

# In[5]:


color = np.random.randint(0,10,len(value)) 
#0에서 10사이의 정수 중 value변수데이터 길이 만큼의 값들로 이루어진 numpy.ndarray형 변수
#np.random.randint() : 정수로 이루어진 랜덤값들을 생성하는 함수
plt.figure(figsize=(10,5))
plt.scatter(value[:,0], value[:,1], c=color, marker = 'o')
plt.colorbar()
#pyplot.colorbar() : 플롯에 색깔막대기를 추가하는 함수
plt.xlabel('value 1')
plt.ylabel('value 2')
plt.title('Scatter Plot 3')


# ## 히스토그램으로 시각화하기

# In[6]:


plt.figure(figsize=(12,7))
plt.hist(value, label = ['1st', '2nd'], bins = 30)
plt.grid(True)
plt.legend(bbox_to_anchor = (1.2, 1), loc="upper right")
plt.xlabel('value')
plt.ylabel('frequency')
plt.title('Histogram 1')


# ### 히스토그램 색 입히기

# In[7]:


plt.cm.get_cmap('Spectral')


# In[8]:


value = np.random.standard_normal(500)
cm = plt.cm.get_cmap('Spectral')
plt.figure(figsize=(12,6))

# Plot histogram.
n, bins, patches = plt.hist(value,bins = 30, color='green')
print("1. bins : " + str(bins))
print("2. the length of bins : " + str(len(bins)))
bin_centers = 0.5 * (bins[:-1] + bins[1:])
print("3. bin_centers :" + str(bin_centers))

# scale values to interval [0,1]
col = bin_centers - min(bin_centers)
col = col / max(col)
print("4. col : " + str(col))

for c, p in zip(col, patches):
    plt.setp(p, 'facecolor', cm(c))

plt.xlabel('value')
plt.ylabel('frequency')
plt.title('Histogram 3')
plt.show()


# In[ ]:




