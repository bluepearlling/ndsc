import csv
from operator import itemgetter
import pandas as pd
import numpy as np
from openpyxl import load_workbook
from openpyxl import workbook


pData = pd.read_csv("/Users/ngshuling 1/Desktop/beauty_data_info_train_competition_edited.csv")
pDataSort = pData.sort_values("title", inplace= False)

maiData = pd.read_csv('/Users/ngshuling 1/Desktop/fullBeau.csv')

for column in pData:

    #pData.set_index('title').combine_first(maiData.set_index('title')).reset_index()'
    print(pData[column])
    i = np.where(np.isnan(pData[column].values))[0]
    j = maiData.title.values.searchsorted(pData.title.values[i])
    pData[column].values[i] = maiData[column].values[j]
    #pData.column = pData[column].fillna(pData[column].map(maiData.set_index('title').score))

pData.to_csv("/Users/ngshuling 1/Desktop/replacedCsv.csv")

#tryList =  list(pDataDuplicated.columns.values)
#print(tryList )
print ("ok le")

