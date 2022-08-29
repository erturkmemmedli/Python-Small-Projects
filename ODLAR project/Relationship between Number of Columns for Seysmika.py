import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

a = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_seysmika/GGI_seysmika_LINK_SEISMIC_DOCUMENT.csv", encoding='latin1')
b = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_seysmika/GGI_seysmika_TB_ASCIIFILE.csv", encoding='latin1')
c = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_seysmika/GGI_seysmika_TB_DRAWINGSMAPS.csv", encoding='latin1')
d = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_seysmika/GGI_seysmika_TB_SEISMICDOCUMENTS.csv", encoding='latin1')
e = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_seysmika/GGI_seysmika_TB_SEISMICLINES.csv", encoding='latin1')
f = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_seysmika/GGI_seysmika_TB_SEISMICSECTIONS.csv", encoding='latin1')
g = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_seysmika/GGI_seysmika_TB_SEISMICSURVEYS.csv", encoding='latin1')
h = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_seysmika/GGI_seysmika_TBX_SCANNEDFILES.csv", encoding='latin1')
    
Tables = [[a,b,c,d,e,f,g,h]]

Count = []
Total_Columns = []
temp = []
for i in range (0,len(Tables)):
    for j in range(0,len(Tables[i])):
        Total_Columns += list(Tables[i][j].columns)
        temp += list(Tables[i][j].columns)
    for item in temp:
        Count.append(temp.count(item))
    temp = []

Overall_Counts = []
for item in Total_Columns:
    Overall_Counts.append(Total_Columns.count(item))

GGI_seysmika_Tables = ['LINK_SEISMIC_DOCUMENT']*len(a.columns)+['TB_ASCIIFILE']*len(b.columns)+\
                            ['TB_DRAWINGSMAPS']*len(c.columns)+['TB_SEISMICDOCUMENTS']*len(d.columns)+\
                            ['TB_SEISMICLINES']*len(e.columns)+['TB_SEISMICSECTIONS']*len(f.columns)+\
                            ['TB_SEISMICSURVEYS']*len(g.columns)+['TBX_SCANNEDFILES']*len(h.columns)

Table_List = GGI_seysmika_Tables

Excel_list = ['GGI_seysmika'] * len(GGI_seysmika_Tables)

Dictionary = {'Excels':Excel_list, 'Tables':Table_List, 'Columns':Total_Columns, 'Count':Count, 'Overall': Overall_Counts}

DataFrame = pd.DataFrame(Dictionary).drop(columns = 'Tables').drop_duplicates()


fig, ax = plt.subplots(figsize = (120, 80))
sns.set_style("whitegrid")
sns.catplot(ax = ax, x = 'Columns', y = 'Count', kind = 'bar', hue = 'Excels', palette = 'bright',
            data = DataFrame)
ax.set_xlabel("Columns", fontsize = 100)
ax.set_ylabel("Number of Columns", fontsize = 100)
ax.set_title("Relationship between Number of Columns for Seysmika", fontsize = 100, y = 1.05)
ax.set_yticks(np.arange(1, 7, step = 1))
ax.tick_params(axis = 'y', labelsize = 75)
ax.tick_params(axis = 'x', labelsize = 75)
ax.set_xticklabels(list(DataFrame['Columns'].unique()), rotation = 90)
ax.legend(loc = 'upper center', fontsize = 100)
fig.savefig('C:/Users/HP/Documents/Relationship between Number of Columns for Seysmika.png', format='png', dps = 4800)