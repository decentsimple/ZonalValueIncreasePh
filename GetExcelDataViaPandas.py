import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import datetime

############ DATA FRAME ###################
revision7 = pd.read_excel("RDO No. 49 - North Makati City - Edited.xls", sheet_name="Sheet 7 (DO 35-2021)")
revision6 = pd.read_excel("RDO No. 49 - North Makati City - Edited.xls", sheet_name="Sheet 6 (DO 24-2017)")
df = pd.concat([revision7,revision6])

############# DATA MODIFIED  ####################

df["Effectivity Date"] = pd.to_datetime(df["Effectivity Date"],errors="coerce") 

df["Effectivity Year"] = df["Effectivity Date"].dt.year

############# SUMMARIZE  #####################
df_sum = df.groupby(["STREET/SUBDIVISION","CLASSIFICATION","Effectivity Year"])["Z.V./SQ.M."].mean().unstack()


df_sum["Percentage 2017-2022"] = (df_sum[2022] - df_sum[2017]) / df_sum[2017]
print(df_sum.sort_values(["Percentage 2017-2022"],ascending=False))

#df_count = df.groupby(["STREET/SUBDIVISION","CLASSIFICATION","Effectivity Year"])["Z.V./SQ.M."].count().unstack()
#print(df_count)
#df.info()
#print(df)



################ PLOT ################

x = df["Effectivity Year"]
y = df["Z.V./SQ.M."]


slope, intercept, r, p, std_err = stats.linregress(x, y)

#def myfunc(x):
# return slope * x + intercept

#mymodel = list(map(myfunc, x))
'''
plt.scatter(x, y)
plt.plot(x,y, '-o')
#plt.plot(x, mymodel)
#plt.ylim(ymin=0, ymax=2000)
#plt.xlim(xmin=0, xmax=200)
plt.xlabel("Effectivity Year")
plt.ylabel("Z.V./SQ.M.")
plt.show()
'''
##############

df_sum[[2017, 2022]].plot(kind = "line")
plt.show()
