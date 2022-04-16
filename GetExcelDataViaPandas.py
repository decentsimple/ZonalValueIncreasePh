import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


revision7 = pd.read_excel("RDO No. 49 - North Makati City - Edited.xls", sheet_name="Sheet 7 (DO 35-2021)")
revision6 = pd.read_excel("RDO No. 49 - North Makati City - Edited.xls", sheet_name="Sheet 6 (DO 24-2017)")
pd = pd.concat([revision7,revision6])
print(pd)
