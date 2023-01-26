import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import seaborn as sns
print("succesfully imported")
succesfully imported
df=pd.read_csv("ex_im_2022.csv")
print("dataset imported")
dataset imported
df.head(10)
Country	Export	Import	Total Trade	Trade Balance	Year(start)	Year(end)
0	AFGHANISTAN	21.25	10.7	31.95	10.55	97	98
1	AFGHANISTAN	12.81	28.14	40.95	-15.33	98	99
2	AFGHANISTAN	33.2	21.06	54.26	12.15	99	2000
3	AFGHANISTAN	25.86	26.59	52.45	-0.73	2000	2001
4	AFGHANISTAN	24.37	17.52	41.89	6.85	2001	2002
5	AFGHANISTAN	60.77	18.46	79.23	42.31	2002	2003
6	AFGHANISTAN	145.47	40.51	185.98	104.96	2003	2004
7	AFGHANISTAN	165.44	47.01	212.44	118.43	2004	2005
8	AFGHANISTAN	142.67	58.42	201.09	84.24	2005	2006
9	AFGHANISTAN	182.11	34.37	216.48	147.73	2006	2007
df.shape
(5767, 7)
df.columns
Index(['Country', 'Export', 'Import', 'Total Trade', 'Trade Balance',
       'Year(start)', 'Year(end)'],
      dtype='object')
country=df.Country.value_counts()
country
AFGHANISTAN                              25
NICARAGUA                                25
MONTSERRAT                               25
MOROCCO                                  25
MOZAMBIQUE                               25
                                         ..
GUERNSEY                                  4
INSTALLATIONS IN INTERNATIONAL WATERS     3
CURACAO                                   2
JERSEY                                    2
SVALLBARD AND J                           1
Name: Country, Length: 250, dtype: int64
 
 
 
df['Total Trade'].apply(lambda x: str(x))
df['Export'].apply(lambda x: str(x))
df['Import'].apply(lambda x: str(x))
0        10.7
1       28.14
2       21.06
3       26.59
4       17.52
        ...  
5762     62.2
5763     7.79
5764    13.59
5765     5.71
5766     1.69
Name: Import, Length: 5767, dtype: object
df['Total Trade'] =df['Total Trade'].astype(str)
df['Export'] =df['Export'].astype(str)
df['Import'] =df['Import'].astype(str)
for i in range(0,len(df)):
    df['Total Trade'][i] = (df['Total Trade'][i]).replace(',','')
    df['Total Trade'][i] = (df['Total Trade'][i]).replace('nan','0')
    df['Export'][i] = (df['Export'][i]).replace(',','')
    df['Export'][i] = (df['Export'][i]).replace('nan','0')
    df['Import'][i] = (df['Import'][i]).replace(',','')
    df['Import'][i] = (df['Import'][i]).replace('nan','0')
C:\Users\MCG\AppData\Local\Temp/ipykernel_12732/3124171252.py:2: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  df['Total Trade'][i] = (df['Total Trade'][i]).replace(',','')
C:\Users\MCG\AppData\Local\Temp/ipykernel_12732/3124171252.py:3: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  df['Total Trade'][i] = (df['Total Trade'][i]).replace('nan','0')
C:\Users\MCG\AppData\Local\Temp/ipykernel_12732/3124171252.py:4: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  df['Export'][i] = (df['Export'][i]).replace(',','')
C:\Users\MCG\AppData\Local\Temp/ipykernel_12732/3124171252.py:5: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  df['Export'][i] = (df['Export'][i]).replace('nan','0')
C:\Users\MCG\AppData\Local\Temp/ipykernel_12732/3124171252.py:6: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  df['Import'][i] = (df['Import'][i]).replace(',','')
C:\Users\MCG\AppData\Local\Temp/ipykernel_12732/3124171252.py:7: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  df['Import'][i] = (df['Import'][i]).replace('nan','0')
df['Total Trade'].apply(lambda x : float(x))
df['Export'].apply(lambda x : float(x))
df['Import'].apply(lambda x : float(x))
0       10.70
1       28.14
2       21.06
3       26.59
4       17.52
        ...  
5762    62.20
5763     7.79
5764    13.59
5765     5.71
5766     1.69
Name: Import, Length: 5767, dtype: float64
df.fillna(0,inplace=True)
df['Total Trade'] = pd.to_numeric(df['Total Trade'])
df['Export'] = pd.to_numeric(df['Export'])
df['Import'] = pd.to_numeric(df['Import'])
df['Year(start)'].apply(lambda x : str(x))
df['Year(start)'] =df['Year(start)'].astype(str)
df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5767 entries, 0 to 5766
Data columns (total 7 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   Country        5767 non-null   object 
 1   Export         5767 non-null   float64
 2   Import         5767 non-null   float64
 3   Total Trade    5767 non-null   float64
 4   Trade Balance  5767 non-null   object 
 5   Year(start)    5767 non-null   object 
 6   Year(end)      5767 non-null   int64  
dtypes: float64(3), int64(1), object(3)
memory usage: 315.5+ KB
exp=px.line(x=df[df['Country']==country.index[0]]['Year(start)'], y=df[df['Country']==country.index[0]]['Export'], labels={'x': 'Year', 'y': 'Export'}, title='EXPORT')
for i in range(0,5):
    exp.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Export'], mode='lines', name=country.index[i])
exp.show()

imp=px.line(x=df[df['Country']==country.index[0]]['Year(start)'], y=df[df['Country']==country.index[0]]['Import'], labels={'x': 'Year', 'y': 'Import'}, title='IMPORT')
for i in range(0,5):
    imp.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Import'], mode='lines', name=country.index[i])
imp.show()


fig=px.line(x=df[df['Country']==country.index[0]]['Year(start)'], y=df[df['Country']==country.index[0]]['Total Trade'], labels={'x': 'Year', 'y': 'Total Trade'}, title='EXPORT AND IMPORT Between India and Other Countries')
for i in range(0,5):
    fig.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Total Trade'], mode='lines', name=country.index[i])
fig.show()
exp=px.line(x=df[df['Country']==country.index[5]]['Year(start)'], y=df[df['Country']==country.index[5]]['Export'], labels={'x': 'Year', 'y': 'Export'}, title='EXPORT')
for i in range(5,10):
    exp.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Export'], mode='lines', name=country.index[i])
exp.show()



imp=px.line(x=df[df['Country']==country.index[5]]['Year(start)'], y=df[df['Country']==country.index[5]]['Import'], labels={'x': 'Year', 'y': 'Import'}, title='IMPORT')
for i in range(5,10):
    imp.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Import'], mode='lines', name=country.index[i])
imp.show()



fig=px.line(x=df[df['Country']==country.index[5]]['Year(start)'], y=df[df['Country']==country.index[5]]['Total Trade'], labels={'x': 'Year', 'y': 'Total Trade'}, title='EXPORT AND IMPORT Between India and Other Countries')
for i in range(5,10):
    fig.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Total Trade'], mode='lines', name=country.index[i])
fig.show()
exp=px.line(x=df[df['Country']==country.index[11]]['Year(start)'], y=df[df['Country']==country.index[11]]['Export'], labels={'x': 'Year', 'y': 'Export'}, title='EXPORT')
for i in range(10,15):
    exp.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Export'], mode='lines', name=country.index[i])
exp.show()


imp=px.line(x=df[df['Country']==country.index[11]]['Year(start)'], y=df[df['Country']==country.index[11]]['Import'], labels={'x': 'Year', 'y': 'Import'}, title='IMPORT')
for i in range(10,15):
    imp.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Import'], mode='lines', name=country.index[i])
imp.show()


fig=px.line(x=df[df['Country']==country.index[11]]['Year(start)'], y=df[df['Country']==country.index[11]]['Total Trade'], labels={'x': 'Year', 'y': 'Total Trade'}, title='EXPORT AND IMPORT Between India and Other Countries')
for i in range(10,15):
    fig.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Total Trade'], mode='lines', name=country.index[i])
fig.show()
exp=px.line(x=df[df['Country']==country.index[15]]['Year(start)'], y=df[df['Country']==country.index[15]]['Total Trade'], labels={'x': 'Year', 'y': 'Export'}, title='EXPORT')
for i in range(15,20):
    exp.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Export'], mode='lines', name=country.index[i])
exp.show()



imp=px.line(x=df[df['Country']==country.index[15]]['Year(start)'], y=df[df['Country']==country.index[15]]['Import'], labels={'x': 'Year', 'y': 'Import'}, title='IMPORT')
for i in range(15,20):
    imp.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Import'], mode='lines', name=country.index[i])
imp.show()



fig=px.line(x=df[df['Country']==country.index[15]]['Year(start)'], y=df[df['Country']==country.index[15]]['Total Trade'], labels={'x': 'Year', 'y': 'Total Trade'}, title='EXPORT AND IMPORT Between India and Other Countries')
for i in range(15,20):
    fig.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Total Trade'], mode='lines', name=country.index[i])
fig.show()
exp=px.line(x=df[df['Country']==country.index[20]]['Year(start)'], y=df[df['Country']==country.index[20]]['Export'], labels={'x': 'Year', 'y': 'Export'}, title='EXPORT')
for i in range(20,30):
    exp.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Export'], mode='lines', name=country.index[i])
exp.show()


imp=px.line(x=df[df['Country']==country.index[20]]['Year(start)'], y=df[df['Country']==country.index[20]]['Import'], labels={'x': 'Year', 'y': 'Import'}, title='IMPORT')
for i in range(20,30):
    imp.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Import'], mode='lines', name=country.index[i])
imp.show()



fig=px.line(x=df[df['Country']==country.index[20]]['Year(start)'], y=df[df['Country']==country.index[20]]['Total Trade'], labels={'x': 'Year', 'y': 'Total Trade'}, title='EXPORT AND IMPORT Between India and Other Countries')
for i in range(20,30):
    fig.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Total Trade'], mode='lines', name=country.index[i])
fig.show()
exp=px.line(x=df[df['Country']==country.index[30]]['Year(start)'], y=df[df['Country']==country.index[30]]['Export'], labels={'x': 'Year', 'y': 'Export'}, title='EXPORT')
for i in range(30,40):
    exp.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Export'], mode='lines', name=country.index[i])
exp.show()



imp=px.line(x=df[df['Country']==country.index[30]]['Year(start)'], y=df[df['Country']==country.index[30]]['Import'], labels={'x': 'Year', 'y': 'Import'}, title='EXPORT AND IMPORT Between India and Other Countries')
for i in range(30,40):
    imp.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Import'], mode='lines', name=country.index[i])
imp.show()



fig=px.line(x=df[df['Country']==country.index[30]]['Year(start)'], y=df[df['Country']==country.index[30]]['Total Trade'], labels={'x': 'Year', 'y': 'Total Trade'}, title='EXPORT AND IMPORT Between India and Other Countries')
for i in range(30,40):
    fig.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Total Trade'], mode='lines', name=country.index[i])
fig.show()
exp=px.line(x=df[df['Country']==country.index[20]]['Year(start)'], y=df[df['Country']==country.index[20]]['Export'], labels={'x': 'Year', 'y': 'Export'}, title='EXPORT')
for i in range(40,50):
    exp.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Export'], mode='lines', name=country.index[i])
exp.show()

imp=px.line(x=df[df['Country']==country.index[20]]['Year(start)'], y=df[df['Country']==country.index[20]]['Import'], labels={'x': 'Year', 'y': 'Import'}, title='IMPORT')
for i in range(40,50):
    imp.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Import'], mode='lines', name=country.index[i])
imp.show()

fig=px.line(x=df[df['Country']==country.index[20]]['Year(start)'], y=df[df['Country']==country.index[20]]['Total Trade'], labels={'x': 'Year', 'y': 'Total Trade'}, title='EXPORT AND IMPORT Between India and Other Countries')
for i in range(40,50):
    fig.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Total Trade'], mode='lines', name=country.index[i])
fig.show()
exp=px.line(x=df[df['Country']==country.index[50]]['Year(start)'], y=df[df['Country']==country.index[50]]['Export'], labels={'x': 'Year', 'y': 'Export'}, title='EXPORT')
for i in range(50,60):
    exp.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Export'], mode='lines', name=country.index[i])
exp.show()



imp=px.line(x=df[df['Country']==country.index[50]]['Year(start)'], y=df[df['Country']==country.index[50]]['Import'], labels={'x': 'Year', 'y': 'Import'}, title='IMPORT')
for i in range(50,60):
    imp.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Import'], mode='lines', name=country.index[i])
imp.show()



fig=px.line(x=df[df['Country']==country.index[50]]['Year(start)'], y=df[df['Country']==country.index[50]]['Total Trade'], labels={'x': 'Year', 'y': 'Total Trade'}, title='EXPORT AND IMPORT Between India and Other Countries')
for i in range(50,60):
    fig.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Total Trade'], mode='lines', name=country.index[i])
fig.show()
exp=px.line(x=df[df['Country']==country.index[60]]['Year(start)'], y=df[df['Country']==country.index[60]]['Export'], labels={'x': 'Year', 'y': 'Export'}, title='EXPORT')
for i in range(60,70):
    exp.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Export'], mode='lines', name=country.index[i])
exp.show()


imp=px.line(x=df[df['Country']==country.index[60]]['Year(start)'], y=df[df['Country']==country.index[60]]['Import'], labels={'x': 'Year', 'y': 'Import'}, title='IMPORT')
for i in range(60,70):
    imp.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Import'], mode='lines', name=country.index[i])
imp.show()


fig=px.line(x=df[df['Country']==country.index[60]]['Year(start)'], y=df[df['Country']==country.index[60]]['Total Trade'], labels={'x': 'Year', 'y': 'Total Trade'}, title='EXPORT AND IMPORT Between India and Other Countries')
for i in range(60,70):
    fig.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Total Trade'], mode='lines', name=country.index[i])
fig.show()
exp=px.line(x=df[df['Country']==country.index[70]]['Year(start)'], y=df[df['Country']==country.index[70]]['Export'], labels={'x': 'Year', 'y': 'Export'}, title='EXPORT')
for i in range(70,80):
    exp.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Export'], mode='lines', name=country.index[i])
exp.show()


imp=px.line(x=df[df['Country']==country.index[70]]['Year(start)'], y=df[df['Country']==country.index[70]]['Import'], labels={'x': 'Year', 'y': 'Import'}, title='IMPORT')
for i in range(70,80):
    imp.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Import'], mode='lines', name=country.index[i])
imp.show()


fig=px.line(x=df[df['Country']==country.index[70]]['Year(start)'], y=df[df['Country']==country.index[70]]['Total Trade'], labels={'x': 'Year', 'y': 'Total Trade'}, title='EXPORT AND IMPORT Between India and Other Countries')
for i in range(70,80):
    fig.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Total Trade'], mode='lines', name=country.index[i])
fig.show()
exp=px.line(x=df[df['Country']==country.index[70]]['Year(start)'], y=df[df['Country']==country.index[70]]['Export'], labels={'x': 'Year', 'y': 'Export'}, title='EXPORT')
for i in range(70,80):
    exp.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Export'], mode='lines', name=country.index[i])
exp.show()


imp=px.line(x=df[df['Country']==country.index[70]]['Year(start)'], y=df[df['Country']==country.index[70]]['Import'], labels={'x': 'Year', 'y': 'Import'}, title='IMPORT')
for i in range(70,80):
    imp.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Import'], mode='lines', name=country.index[i])
imp.show()


fig=px.line(x=df[df['Country']==country.index[70]]['Year(start)'], y=df[df['Country']==country.index[70]]['Total Trade'], labels={'x': 'Year', 'y': 'Total Trade'}, title='EXPORT AND IMPORT Between India and Other Countries')
for i in range(70,80):
    fig.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Total Trade'], mode='lines', name=country.index[i])
fig.show()
exp=px.line(x=df[df['Country']==country.index[100]]['Year(start)'], y=df[df['Country']==country.index[100]]['Export'], labels={'x': 'Year', 'y': 'Export'}, title='EXPORT')
for i in range(100,120):
    exp.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Export'], mode='lines', name=country.index[i])
exp.show()

imp=px.line(x=df[df['Country']==country.index[100]]['Year(start)'], y=df[df['Country']==country.index[100]]['Import'], labels={'x': 'Year', 'y': 'Import'}, title='IMPORT')
for i in range(100,120):
    imp.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Import'], mode='lines', name=country.index[i])
imp.show()

fig=px.line(x=df[df['Country']==country.index[100]]['Year(start)'], y=df[df['Country']==country.index[100]]['Total Trade'], labels={'x': 'Year', 'y': 'Total Trade'}, title='EXPORT AND IMPORT Between India and Other Countries')
for i in range(100,120):
    fig.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Total Trade'], mode='lines', name=country.index[i])
fig.show()
exp=px.line(x=df[df['Country']==country.index[120]]['Year(start)'], y=df[df['Country']==country.index[120]]['Export'], labels={'x': 'Year', 'y': 'Export'}, title='EXPORT')
for i in range(120,150):
    exp.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Export'], mode='lines', name=country.index[i])
exp.show()

imp=px.line(x=df[df['Country']==country.index[120]]['Year(start)'], y=df[df['Country']==country.index[120]]['Import'], labels={'x': 'Year', 'y': 'Import'}, title='IMPORT')
for i in range(120,150):
    imp.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Import'], mode='lines', name=country.index[i])
imp.show()

fig=px.line(x=df[df['Country']==country.index[120]]['Year(start)'], y=df[df['Country']==country.index[120]]['Total Trade'], labels={'x': 'Year', 'y': 'Total Trade'}, title='EXPORT AND IMPORT Between India and Other Countries')
for i in range(120,150):
    fig.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Total Trade'], mode='lines', name=country.index[i])
fig.show()
exp=px.line(x=df[df['Country']==country.index[150]]['Year(start)'], y=df[df['Country']==country.index[150]]['Export'], labels={'x': 'Year', 'y': 'Export'}, title='EXPORT')
for i in range(150,200):
    exp.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Export'], mode='lines', name=country.index[i])
exp.show()

imp=px.line(x=df[df['Country']==country.index[150]]['Year(start)'], y=df[df['Country']==country.index[150]]['Import'], labels={'x': 'Year', 'y': 'Import'}, title='IMPORT')
for i in range(150,200):
    imp.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Import'], mode='lines', name=country.index[i])
imp.show()

fig=px.line(x=df[df['Country']==country.index[150]]['Year(start)'], y=df[df['Country']==country.index[150]]['Total Trade'], labels={'x': 'Year', 'y': 'Total Trade'}, title='EXPORT AND IMPORT Between India and Other Countries')
for i in range(150,200):
    fig.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Total Trade'], mode='lines', name=country.index[i])
fig.show()
exp=px.line(x=df[df['Country']==country.index[200]]['Year(start)'], y=df[df['Country']==country.index[200]]['Export'], labels={'x': 'Year', 'y': 'Export'}, title='EXPORT')
for i in range(200,250):
    exp.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Export'], mode='lines', name=country.index[i])
exp.show()

imp=px.line(x=df[df['Country']==country.index[200]]['Year(start)'], y=df[df['Country']==country.index[200]]['Import'], labels={'x': 'Year', 'y': 'Import'}, title='IMPORT')
for i in range(200,250):
    imp.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Import'], mode='lines', name=country.index[i])
imp.show()

fig=px.line(x=df[df['Country']==country.index[200]]['Year(start)'], y=df[df['Country']==country.index[200]]['Total Trade'], labels={'x': 'Year', 'y': 'Total Trade'}, title='EXPORT AND IMPORT Between India and Other Countries')
for i in range(200,250):
    fig.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Total Trade'], mode='lines', name=country.index[i])
fig.show()
exp=px.line(x=df[df['Country']==country.index[0]]['Year(start)'], y=df[df['Country']==country.index[0]]['Export'], labels={'x': 'Year', 'y': 'Export'}, title='EXPORT By India to Other Countries')
for i in range(0,250):
    exp.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Export'], mode='lines', name=country.index[i])
exp.show()



imp=px.line(x=df[df['Country']==country.index[0]]['Year(start)'], y=df[df['Country']==country.index[0]]['Import'], labels={'x': 'Year', 'y': 'Import'}, title='IMPORT to India from Other Countries')
for i in range(0,250):
    imp.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Import'], mode='lines', name=country.index[i])
imp.show()



fig=px.line(x=df[df['Country']==country.index[0]]['Year(start)'], y=df[df['Country']==country.index[0]]['Total Trade'], labels={'x': 'Year', 'y': 'Total Trade'}, title='EXPORT AND IMPORT Between India and Other Countries')
for i in range(0,250):
    fig.add_scatter(x=df[df['Country']==country.index[i]]['Year(start)'], y=df[df['Country']==country.index[i]]['Total Trade'], mode='lines', name=country.index[i])
fig.show()