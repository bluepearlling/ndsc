import csv
from operator import itemgetter
import pandas as pd
import numpy as np
from openpyxl import load_workbook
from openpyxl import workbook
import scipy.stats as stats


pData = pd.read_csv("/Users/ngshuling 1/Desktop/NDSC/fashion_data_info_train_competition.csv")
pDataSort = pData.sort_values("title", inplace= False)

#first will return true for all the unique value + the first instance of the dup found
#keep = false, it will keep everything where duplicate = true
bool_series = pData["title"].duplicated(keep= False)

#contains all the duplicated data ( # of times they are repeated )
pDataDuplicated = pData[bool_series]
pDataDuplicated.to_csv('/Users/ngshuling 1/Desktop/fashionsortedDp.csv')


#only taking the first instance of each dup
#returns an array of the titles that have a few duplicates
s_bool_series = pDataDuplicated["title"].duplicated(keep='first')
uniqueOfDuplicates = pDataDuplicated[~s_bool_series]
singleUniqueOfDuplicates = np.asarray(uniqueOfDuplicates['title'])
uniqueOfDuplicates.to_csv('/Users/ngshuling 1/Desktop/fashionuniqueDup.csv')



#create a new csv with the headers
#columns =['title','Operating System','Features','Network Connections','Memory RAM','Brand','Warranty Period','Storage Capacity','Color Family','Phone Model','Camera','Phone Screen Size','image_path','itemid']
#columns = ['title','Benefits','Brand','Colour_group','Product_texture','Skin_type','image_path','itemid']
columns = ['title','Pattern','Collar Type','Fashion Trend','Clothing Material','Sleeves','image_path','itemid']
df = pd.DataFrame(columns=columns)
df.to_csv('/Users/ngshuling 1/Desktop/fashionmodeDF.csv')

#for each of the title in the array , scan the duplicated excel and get those with the same title
#to improve shld append to df , not write to csv
with open('/Users/ngshuling 1/Desktop/fashionmodeDF.csv', 'a') as f:
    for line in singleUniqueOfDuplicates:
        indiBlockDup = pDataDuplicated.loc[pDataDuplicated['title'] == line]
        imagePath = indiBlockDup['image_path']
        itemId = indiBlockDup['itemid']
        indiBlockDup = indiBlockDup.drop(['itemid','image_path'], axis=1)
        modeDf = indiBlockDup.mode()
        gb = modeDf.apply(lambda x: tuple(x)).map(list)

        gb2 = pd.DataFrame(gb).T
        gb2['title']= line
        gb2['image_path'] = imagePath.iloc[0]
        gb2['itemid'] = itemId.iloc[0]
        gb2.to_csv(f, header=False)
        #modeDf['title'] = line
        # gb = indiBlockDup.groupby('title').apply(pd.DataFrame.mode).reset_index(drop=True)
        #gb = modeDf.groupby('title',as_index= False).apply(pd.DataFrame)
        #gb.apply(lambda x: tuple(x))).applymap(list).reset_index()
        #gbDf = pd.DataFrame(gb)
        #rowCount = len(gb)
        # #pd.DataFrame.mode).reset_index(drop=True)
        # gb=fullModeDf.groupby('title').apply(','.join).reset_index()


fullModeDf = pd.read_csv("/Users/ngshuling 1/Desktop/fashionmodeDF.csv")
m_bool_series = fullModeDf['title'].duplicated(keep='first')
fullModeDfFirst = fullModeDf[~m_bool_series]
print (list(fullModeDfFirst.columns.values))
pDataNonDups = pData[~bool_series]
concatDF = pd.concat([fullModeDfFirst, pDataNonDups],axis=0,ignore_index=True, sort=False)
concatDF.to_csv("/Users/ngshuling 1/Desktop/fashionfull.csv")

print ("ok le")

