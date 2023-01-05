#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from faker import Faker
import random
from random import randrange
from datetime import datetime


# In[2]:


# creating fake data
fake = Faker()


# In[3]:


# function to create a dataframe with fake values for our workers
def fact_underwritting_deals(number):
    
    # lists to randomly assign values to columns
#     Amount= [Faker.seed() for x in range(100)]
#     team_list = [fake.color_name() for x in range(4)]
    

    fake_columns = [{'Numeric ID':(x+1),
                  'Applicant ID':fake.first_name(), 
                  'Last Name':fake.last_name(),'Isunderwritting':fake.boolean(),
                     'Industry Type ID':fake.random_int(1,10),'gender' :np.random.choice(["M", "F"]),'Occupation':fake.job(),'Address 1':fake.address(),'Address 2':fake.address(),
                     'city':fake.city(),'state':fake.state(),'Country':fake.country(),'postalcode':fake.postalcode(),'PhoneNumber': fake.phone_number(),
                     'EmailAddress': fake.email(),'Experience':fake.random_int(5,15)
                     } for x in range(number)]
        
    return fake_columns


# In[4]:


micro_df = pd.DataFrame(fact_underwritting_deals(number=300))
micro_df.head(5)


# In[8]:


micro_df.to_csv(r'C:\Users\kaveri.shende_jai-ki\OneDrive\Desktop\NEW POLICY\Faker.csv')


# In[9]:


micro_df


# In[ ]:




