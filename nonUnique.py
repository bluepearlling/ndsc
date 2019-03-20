import csv
from operator import itemgetter
import pandas as pd
import numpy as np
from openpyxl import load_workbook
from openpyxl import workbook


pData = pd.read_csv("/Users/ngshuling 1/Desktop/NDSC/beauty_data_info_train_competition.csv")
pDataSort = pData.sort_values("title", inplace= False)

#first will return true for all the unique value + the first instance of the dup found
#keep = false, it will keep everything where duplicate = true
bool_series = pData["title"].duplicated(keep= False)

#contains all the duplicated data ( # of times they are repeated )
pDataDuplicated = pData[bool_series]
pDataDuplicated.to_csv('/Users/ngshuling 1/Desktop/sortedGBDp.csv')

#only taking the first instance of each dup
#returns an array of the titles that have a few duplicates
s_bool_series = pDataDuplicated["title"].duplicated(keep='first')
uniqueOfDuplicates = pDataDuplicated[~s_bool_series]
singleUniqueOfDuplicates = np.asarray(uniqueOfDuplicates['title'])
uniqueOfDuplicates.to_csv('/Users/ngshuling 1/Desktop/uniqueDupGB.csv')



#create a new csv with the headers
#columns =['itemid','title','image_path','Operating System','Features','Network Connections','Memory','RAM','Brand','Warranty','Period','Storage','Capacity','Color','Family','Phone Model','Camera','Phone Screen Size']
columns = ['itemid','title','image_path','Benefits','Brand','Colour_group','Product_texture','Skin_type']
#columns = ['itemid','title','image_path','Pattern',	'Collar Type','Fashion Trend','Clothing Material','Sleeves']
df = pd.DataFrame(columns=columns)
df.to_csv('/Users/ngshuling 1/Desktop/GBmodeDF.csv')

#for each of the title in the array , scan the duplicated excel and get those with the same title
#to improve shld append to df , not write to csv
with open('/Users/ngshuling 1/Desktop/GBmodeDF.csv', 'a') as f:
    for line in singleUniqueOfDuplicates:
        indiBlockDup = pDataDuplicated.loc[pDataDuplicated['title'] == line]
        modeDF = indiBlockDup.mode()
        modeDF.to_csv(f, header=False)




fullModeDf = pd.read_csv("/Users/ngshuling 1/Desktop/GBmodeDF.csv")
m_bool_series = fullModeDf['title'].duplicated(keep='first')
fullModeDfFirst = fullModeDf[~m_bool_series]
print (list(fullModeDfFirst.columns.values))


gb= fullModeDf.groupby('title')

print(gb)

fullModeDf.to_csv("/Users/ngshuling 1/Desktop/GB.csv")
#gb.to_csv("/Users/ngshuling 1/Desktop/gbTry")

'''
pDataNonDups = pData[~bool_series]
concatDF = pd.concat([fullModeDfFirst, pDataNonDups],axis=0,ignore_index=True, sort=False)
concatDF.to_csv("/Users/ngshuling 1/Desktop/fullMobile.csv")
'''
#tryList =  list(pDataDuplicated.columns.values)
#print(tryList )
print ("ok le")

