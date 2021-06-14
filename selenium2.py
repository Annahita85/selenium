#!/usr/bin/env python
# coding: utf-8

# In[77]:


from selenium import webdriver


# In[78]:


driver = webdriver.Chrome(executable_path=r"C:\selenium beispiel\chromedriver.exe")


# In[79]:


driver.get("https://realpython.com/")


# In[80]:


driver.current_url


# 

# In[81]:


#tag1 = driver.find_element_by_css_selecotr("body > div > div > div:nth-child(11)")


# 

# In[82]:


tag1 =driver.find_element_by_css_selector("body > div > div > div:nth-child(11)")


# In[83]:


tag1.get_attribute("class")


# # 

# In[84]:


tag1.get_attribute("outerHTML")


# In[85]:


tag1.get_attribute("innerHTML")


# In[86]:


print(tag1.get_attribute("innerHTML"))


# In[87]:


tag2 = driver.find_element_by_xpath("""/html/body/div/div/div[11]""")


# In[88]:


print(tag2.get_attribute("outerHTML"))


# In[89]:


print(tag2.text)


# In[90]:


tags1 = driver.find_elements_by_class_name("col-12")


# In[91]:


tags1


# In[92]:


tags1 = driver.find_elements_by_css_selector("body > div> div > div.col-12.col-md-6.col-lg-4.mb-5")


# In[93]:


tags1


# In[94]:


tags2 = driver.find_elements_by_css_selector("body > div> div > div.col-12.col-md-6.col-lg-4.mb-5")


# In[95]:


tags2


# In[96]:


len(tags2)


# In[98]:


for tag in list(set(tags1)-set(tags2)):
    print(tag.get_attribute("class"))

