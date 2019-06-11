# Pandas
#-----------------------------------------

import pandas as pd
import numpy as np

lst = [1,2,3,4,5,6,78]
#print(lst)

# create a data frame
df=pd.DataFrame(lst) # 'D' & 'F' are caps

# cheking for array
lst=np.array(lst)
df=pd.DataFrame(lst) # 'D' & 'F' are caps

#print(df)

#--------------------------------------

#data = [[10,'Rohit'],[11,'Kumar'],[12,'Chethan'],[13, 'Pradeep']]

#df=pd.DataFrame(data)

#df=pd.DataFrame(data,columns=['Id', 'Name'],index=None)

#print(df)

#-------JSON----------------------------------
data = {
       'Id':[10,11,12,13],
       'Name':['Rohit', 'Kumar', 'Chethan', 'Pradeep']
       }

#print(pd.DataFrame(data))
#------------------------------------------------------------

#-----Read CSV-----------------------------------------------

sample=pd.read_csv("C:\\Users\\training_b4b.01.20\\.PyCharmCE2019.1\\config\\scratches\\sample.csv")

df1=sample.describe() # you get the statistical results like Mean, median, sd from describe

#print(sample)
#print(df1)

#-----------------------------------------Index parsing----------------

data = {
       'Id':[10,11,12,13],
       'Name':['Rohit', 'Kumar', 'Chethan', 'Pradeep']
       }

#parsing index

df2= pd.DataFrame(data,index=['Id1', 'Id2', 'Id3', 'Id4'])
#print(df2)

#----Read EXCEL---------------------------
# pip install xlrd to read excel files

excl=pd.read_excel("C:\\Users\\training_b4b.01.20\\.PyCharmCE2019.1\\config\\scratches\\ReadExcel.xlsx")

#print(excl)


#--------------------------------------------------------------------------------------
#reading json from web https://jsonplaceholder.typicode.com/todos
#--------------------------------------------------------------------------------------

jdf=pd.read_json('https://jsonplaceholder.typicode.com/todos') # reading json from web

#print(jdf)

#---------------------------------------------------------------------------------------

#---------------slicing---------------
#-------------------------------------------


data = {
       'Id':[10,11,12,13],
       'Name':['Rohit', 'Kumar', 'Chethan', 'Pradeep']
       }

df3=pd.DataFrame(data)

#print(df3)

#head & tail funcn for slicing
#print(df3.head(2))
#print(df3.tail(2))

#---------------------------------------------------------------------------------------------------------
#                       analysis from csv file
#---------------------------------------------------------------------------------------------------------

ana=pd.read_csv("C:\\Users\\training_b4b.01.20\\.PyCharmCE2019.1\\config\\scratches\\CSVDEMO.csv")

#print(ana)

# print col names
#print(ana.columns)

# print only any 1 or 2 cols


#print(ana.date, ana.duration)

#--- print only rows

#print(ana.head(1))

#-----slicing

#print(ana[2:5]) # prints rows from 2nd index till 4th(5-1) index




#---------------------------------------------------------------------------------------------------------------
# Handling Null fields
#----------------------------------------------------------------------------------------------------------

nul=pd.read_csv("C:\\Users\\training_b4b.01.20\\.PyCharmCE2019.1\\config\\scratches\\CSVDemoNull.csv")

#nul.set_index('date',inplace=True) # setting index

#values = {'name of training': 'N/A', 'duration': 0, 'Location': 'N/A'} # creating dict to be used for null values in df

#nulf=nul.fillna(value=values)# using null dict in fillna function

#print(nul)
#print(nul.isna().sum())  # count of NaN values in a row

#nul1=nul[nul.isna().any(axis=1)]  # to display only rows with NaN values

#print(nul1)
      
# drop na

#newdf=nul.dropna()  # drops the rows with Nan values
    
# transpose-- row to col / col to row

#newd= newdf.T

#print(newd)


#------------------------------------------------------------------------------------------------------------------------
#pandas sorting
#-----------------------------------------------------------------------------------------------------------------------

srt=pd.read_csv("C:\\Users\\training_b4b.01.20\\.PyCharmCE2019.1\\config\\scratches\\CSVDemoNull.csv")

#print(srt)
srt.set_index('date',inplace=True) # setting index

#print(srt)

# sorting

#srt.sort_values("name of training", axis=0, ascending=True, inplace=True, na_position='last')
#srt.sort_values("name of training", axis=0, ascending=True, inplace=True, na_position='first')

#print(srt)

#parsing condition

analysis=srt[srt["name of training"]== 'Splunk']# single value condition

analysis1=srt[srt["name of training"].isin(['Splunk','Spark'])] # multiple value condition

#print(analysis)
#print(analysis1)

#===============================================================================================
# adding columns

data={
    'one':pd.Series([100,200,300],
                index=['a1','a2','a3']),
    'two':pd.Series([150,250,350,400],
                index=['a1','a2','a3','a4']),
    }

daf=pd.DataFrame(data)

#add column doubt
daf['three'] = pd.Series([100,200,300,400],index=['a1','a2','a3','a4'])

#add row doubt
#dcf= pd.DataFrame([100,200,300],index=['one','two','three'])

#dcf= pd.DataFrame([100,200,300],columns=['one','two','three'],index=['a5 '])

#print(dcf)


#-------------------------------------------------------------------------------------

#update

#daf.three.loc[(daf['three']>=250)]=1000  #loc- locate the values

#print(daf)

#drop cols

#daf=daf.drop('three', axis=1)

#daf=daf.drop(['three','two'], axis=1)
#print(daf)

# drop rows

#daf=daf.drop(['a1','a2'],axis=0)
#print(daf)



#----------------------------------------------------------------------------------------    
# write data to excel file
#----------------------------------------------------------------------------------------

import openpyxl as pxl


data1 = {
       'Id':[10,11,12,13],
       'Name':['Rohit', 'Kumar', 'Chethan', 'Pradeep']
       }

dx=pd.DataFrame(data1)

writer=pd.ExcelWriter("C:\\Users\\training_b4b.01.20\\.PyCharmCE2019.1\\config\\scratches\\mydef.xlsx")
dx.to_excel(writer,'DataFrame')
writer.save()
#print("data saved")


#===================================================================================

grp = pd.read_csv("C:\\Users\\training_b4b.01.20\\.PyCharmCE2019.1\\config\\scratches\\foundation.csv",index_col='Id')

#print(grp)

# group by

#print(grp.groupby('Id').groups)

#multicol=grp.groupby(['Course','Location']).groups
#print(multicol)

#cl=grp.groupby('Course')
#print(cl)

# print first entry

#print(cl.first())

# get no of course in each location

#datacount = grp.groupby('Course')['Location'].count()

#print(datacount)

#---------
#for loop

#grped = grp.groupby('Course')

#for name, group in grped:
    #print(name)
#    print(group)

    #----------------------

# to print single group
#grped = grp.groupby('Course')

#print(grped.get_group('DIGITAL'))


#----------------------------------------------------------
# Aggregate Functions
#----------------------------------------------------


Agr = pd.read_csv("C:\\Users\\training_b4b.01.20\\.PyCharmCE2019.1\\config\\scratches\\phonedetails.csv",index_col='index')

new=Agr.groupby('network_type')

#print(new)

# aggregate functions

aggfun = new['duration'].agg([np.size,np.sum, np.mean, np.std])

#print(aggfun)


# stat data

statdata= Agr.describe()
#print(statdata)


# descibe

dt =pd.Series(['B','C','D','G','F','H','Z'])
#print(dt.describe())

 

#+======================================================================================================
# date in pandas
#===========================================================================

import pandas as pd
from datetime import datetime

x=datetime.now()

#print(x)
#print(x.month)
#print(x.year)
#print(x.day)

currdate=pd.Timestamp.now()

#print(currdate)
#print(currdate.year)
#print(currdate.month)
#print(currdate.day)
#print(currdate.hour)
#print(currdate.second)

date_rng=pd.date_range(start='1/1/2019',
                       end='1/10/2019')

#print(date_rng)

#dt= pd.DataFrame(date_rng, columns=['date'])

dt=pd.date_range('2019-01-04',periods=4,freq='H')

dt= dt.tz_localize('UTC') # local time india

#dt['data'] = np.random.randint(0,100,size=(len(date_rng)))

# converting to defferent time zone

cdt=dt.tz_convert('US/Pacific')

#print(cdt)

#---------------------------------------------------------------------------
#              Merging
#------------------------------------------

#first= pd.DataFrame({
#       'Id':[1,2,3,4,5],
#       'Name':['Rohit', 'Kumar', 'Chethan', 'Pradeep','Boom'],
#       'subject_id':['eng','math','science','social','kann']
#       })

#second= pd.DataFrame({
#       'Id':[1,2,3,4,5],
#       'Name':['Radhika', 'Kavya', 'Chaitra', 'Rachita','Doom'],
#       'subject_id':['eng','math','science','social','kann']
#       })

#print(pd.merge(first,second, on=['Id']))

#print(pd.merge(first,second, on=['Id','subject_id']))


#------------------------------------------------------------------------------------
#                      JOIN
#---------------------------------------------------------------------------------------

#first= pd.DataFrame({
#       'Id':[1,2,3,4,5],
#       'Name':['Rohit', 'Kumar', 'Chethan', 'Pradeep','Boom'],
#       'subject_id':['eng','hin','science','social','kann']
#       })
#second= pd.DataFrame({
#       'Id':[1,2,3,4,5],
#       'Name':['Radhika', 'Kavya', 'Chaitra', 'Rachita','Doom'],
#       'subject_id':['can','math','science','social','kann']
#       })

# Left Join

#print(pd.merge(first,second, on='subject_id',how='left'))

#right
#print(pd.merge(first,second, on='subject_id',how='right'))

#outer
#print(pd.merge(first,second, on='subject_id',how='outer'))

#inner
#print(pd.merge(first,second, on='subject_id',how='inner'))



#---------------------------------------------------------------------------------------
#               Queries
#-------------------------------------------------------------------------------------------------------

dfc=pd.read_csv("C:\\Users\\training_b4b.01.20\\.PyCharmCE2019.1\\config\\scratches\\foundation.csv",index_col='Id')

# conditions using query

#dfq =dfc.query('index>15')
#dfq =dfc.query('Id>15') 
#print(dfc)
#print('\n')
#print(dfq)

# equal to

dfq=dfc.query("Location=='BDC'")

#dfq=dfc.query("Location=='BDC'" and "Id>15")
print(dfq)
