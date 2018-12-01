import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df.head()

# In[ ]:

GOLD_S = 'Gold'
GOLD_W = 'Gold.1'
GOLD_G = 'Gold.2'
SILVER_G = 'Silver.2'
BRONZE_G = 'Bronze.2'
POINTS = 'Points'
SUMLEV = "SUMLEV"
STNAME = 'STNAME'
CTYNAME = 'CTYNAME'
MIN = 'Min'
MAX = 'Max'
REGION = "REGION"
POPESTIMATE_ARRAY = ["POPESTIMATE2010", "POPESTIMATE2011", "POPESTIMATE2012", "POPESTIMATE2013", "POPESTIMATE2014", "POPESTIMATE2015"]

# In[ ]:
def answer_one():
    return df.loc[df[GOLD_S].idxmax()].name

# In[ ]:


def answer_two():    
   return (df[GOLD_S]-df[GOLD_W]).idxmax()

# In[ ]:

def answer_three():
    copy_df = df.copy()
    copy_df = copy_df[(copy_df[GOLD_S]>0) & (copy_df[GOLD_W]>0)]
    return ((copy_df[GOLD_S]-copy_df[GOLD_W])/copy_df[GOLD_G]).idxmax()

# In[ ]:


def answer_four():
    df[POINTS] = df[GOLD_G]*3 + df[SILVER_G]*2 + df[BRONZE_G]
    return df[POINTS]

# In[ ]:


census_df = pd.read_csv('census.csv')
census_df.head()

# In[ ]:


def answer_five():
    return census_df[census_df[SUMLEV] == 50].groupby(STNAME)[CTYNAME].count().idxmax()

# In[ ]:


def answer_six():
    return census_df[census_df[SUMLEV] == 50].groupby(STNAME)['CENSUS2010POP'].apply(lambda x: x.nlargest(3).sum()).nlargest(3).index.format()

# In[ ]:


def answer_seven():
    census_df[MIN] = census_df.loc[census_df[SUMLEV] == 50, POPESTIMATE_ARRAY].min(axis=1)
    census_df[MAX] = census_df.loc[census_df[SUMLEV] == 50, POPESTIMATE_ARRAY].max(axis=1)
    census_df["PopGrowth"] = census_df[MAX] - census_df[MIN]
    return census_df.loc[census_df["PopGrowth"] == census_df["PopGrowth"].max(), CTYNAME].max()

# In[ ]:

def answer_eight():
    return census_df.loc[((census_df[REGION] == 1) | (census_df[REGION] == 2)) & (census_df[CTYNAME].str.startswith('Washington')) & (census_df[POPESTIMATE_ARRAY[5]] > census_df[POPESTIMATE_ARRAY[4]]), [STNAME, CTYNAME]]