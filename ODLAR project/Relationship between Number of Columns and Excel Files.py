import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

a = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_inklinometriya/GGI_inklinometriya_LINK_WELL_DOCUMENT.csv", encoding='latin1')
b = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_inklinometriya/GGI_inklinometriya_TB_HORIZONDEPTHS.csv", encoding='latin1')
c = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_inklinometriya/GGI_inklinometriya_TB_WELLDEVIATION.csv", encoding='latin1')
d = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_inklinometriya/GGI_inklinometriya_TB_WELLDOCUMENTS.csv", encoding='latin1')
e = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_inklinometriya/GGI_inklinometriya_TBX_SCANNEDFILES.csv", encoding='latin1')

a1 = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_well_logs/GGI_well_logs_LINK_WELL_DOCUMENT.csv", encoding='latin1')
b1 = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_well_logs/GGI_well_logs_TB_HORIZONDEPTHS.csv", encoding='latin1')
c1 = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_well_logs/GGI_well_logs_TB_WELLDEVIATION.csv", encoding='latin1')
d1 = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_well_logs/GGI_well_logs_TB_WELLDOCUMENTS.csv", encoding='latin1')
e1 = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_well_logs/GGI_well_logs_TB_WELLLOGS.csv", encoding='latin1')
f1 = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_well_logs/GGI_well_logs_TBX_SCANNEDFILES.csv", encoding='latin1')

a2 = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_LINK_WELL_DOCUMENT.csv", encoding='latin1')
b2 = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_COREINFORMATION.csv", encoding='latin1')
c2 = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_DRAWINGSMAPS.csv", encoding='latin1')
d2 = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_DRILLINGPARAMETERS.csv", encoding='latin1')
e2 = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_FORMATIONPRESSURES.csv", encoding='latin1')
f2 = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_FORMATIONTEMPERATURES.csv", encoding='latin1')
g2 = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_GASANALYSIS.csv", encoding='latin1')
h2 = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_GASFACTORS.csv", encoding='latin1')
i2 = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_HORIZONDEPTHS.csv", encoding='latin1')
j2 = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_INJECTIONANDPRODUCTION.csv", encoding='latin1')
k2 = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_OILANALYSIS.csv", encoding='latin1')
l2 = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_WATERANALYSIS.csv", encoding='latin1')
m2 = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_WELLCONSTRUCTIONINFO.csv", encoding='latin1')
n2 = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_WELLDOCUMENTS.csv", encoding='latin1')
o2 = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_WELLLOGS.csv", encoding='latin1')
p2 = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_WELLPERFORATION.csv", encoding='latin1')
q2 = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_WELLS.csv", encoding='latin1')
r2 = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_WELLSTOP.csv", encoding='latin1')
s2 = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_WELLTESTINFO.csv", encoding='latin1')
t2 = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TBX_SCANNEDFILES.csv", encoding='latin1')
u2 = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_COREANALYSIS.csv", encoding='latin1')

a3 = pd.read_csv("C:/Users/HP/Documents/ODLAR/NQETLI_GD/NQETLI_GD_LINK_SEISMIC_DOCUMENT.csv", encoding='latin1')
b3 = pd.read_csv("C:/Users/HP/Documents/ODLAR/NQETLI_GD/NQETLI_GD_TB_DRAWINGSMAPS.csv", encoding='latin1')
c3 = pd.read_csv("C:/Users/HP/Documents/ODLAR/NQETLI_GD/NQETLI_GD_TB_SEISMICDOCUMENTS.csv", encoding='latin1')
d3 = pd.read_csv("C:/Users/HP/Documents/ODLAR/NQETLI_GD/NQETLI_GD_TB_SEISMICSURVEYS.csv", encoding='latin1')
e3 = pd.read_csv("C:/Users/HP/Documents/ODLAR/NQETLI_GD/NQETLI_GD_TB_WELLDOCUMENTS.csv", encoding='latin1')
f3 = pd.read_csv("C:/Users/HP/Documents/ODLAR/NQETLI_GD/NQETLI_GD_TBX_SCANNEDFILES.csv", encoding='latin1')

a4 = pd.read_csv("C:/Users/HP/Documents/ODLAR/KQIT_cedveli/KQIT_cedveli_LINK_WELL_DOCUMENT.csv", encoding='latin1')
b4 = pd.read_csv("C:/Users/HP/Documents/ODLAR/KQIT_cedveli/KQIT_cedveli_TB_COREANALYSIS.csv", encoding='latin1')
c4 = pd.read_csv("C:/Users/HP/Documents/ODLAR/KQIT_cedveli/KQIT_cedveli_TB_COREINFORMATION.csv", encoding='latin1')
d4 = pd.read_csv("C:/Users/HP/Documents/ODLAR/KQIT_cedveli/KQIT_cedveli_TB_DRAWINGSMAPS.csv", encoding='latin1')
e4 = pd.read_csv("C:/Users/HP/Documents/ODLAR/KQIT_cedveli/KQIT_cedveli_TB_DRILLINGPARAMETERS.csv", encoding='latin1')
f4 = pd.read_csv("C:/Users/HP/Documents/ODLAR/KQIT_cedveli/KQIT_cedveli_TB_GASANALYSIS.csv", encoding='latin1')
g4 = pd.read_csv("C:/Users/HP/Documents/ODLAR/KQIT_cedveli/KQIT_cedveli_TB_HORIZONDEPTHS.csv", encoding='latin1')
h4 = pd.read_csv("C:/Users/HP/Documents/ODLAR/KQIT_cedveli/KQIT_cedveli_TB_OILANALYSIS.csv", encoding='latin1')
i4 = pd.read_csv("C:/Users/HP/Documents/ODLAR/KQIT_cedveli/KQIT_cedveli_TB_WATERANALYSIS.csv", encoding='latin1')
j4 = pd.read_csv("C:/Users/HP/Documents/ODLAR/KQIT_cedveli/KQIT_cedveli_TB_WELLCONSTRUCTIONINFO.csv", encoding='latin1')
k4 = pd.read_csv("C:/Users/HP/Documents/ODLAR/KQIT_cedveli/KQIT_cedveli_TB_WELLDOCUMENTS.csv", encoding='latin1')
l4 = pd.read_csv("C:/Users/HP/Documents/ODLAR/KQIT_cedveli/KQIT_cedveli_TB_WELLPERFORATION.csv", encoding='latin1')
m4 = pd.read_csv("C:/Users/HP/Documents/ODLAR/KQIT_cedveli/KQIT_cedveli_TB_WELLS.csv", encoding='latin1')
n4 = pd.read_csv("C:/Users/HP/Documents/ODLAR/KQIT_cedveli/KQIT_cedveli_TB_WELLSTOP.csv", encoding='latin1')
o4 = pd.read_csv("C:/Users/HP/Documents/ODLAR/KQIT_cedveli/KQIT_cedveli_TB_WELLTESTINFO.csv", encoding='latin1')
p4 = pd.read_csv("C:/Users/HP/Documents/ODLAR/KQIT_cedveli/KQIT_cedveli_TBX_SCANNEDFILES.csv", encoding='latin1')
    
Tables = [[a,b,c,d,e],
          [a1,b1,c1,d1,e1,f1],
          [a2,b2,c2,d2,e2,f2,g2,h2,i2,j2,k2,l2,m2,n2,o2,p2,q2,r2,s2,t2,u2],
          [a3,b3,c3,d3,e3,f3],
          [a4,b4,c4,d4,e4,f4,g4,h4,i4,j4,k4,l4,m4,n4,o4,p4]]

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

GGI_inklinometriya_Tables = ['LINK_WELL_DOCUMENT']*len(a.columns)+['TB_HORIZONDEPTHS']*len(b.columns)+\
                            ['TB_WELLDEVIATION']*len(c.columns)+['TB_WELLDOCUMENTS']*len(d.columns)+\
                            ['TBX_SCANNEDFILES']*len(e.columns)

GGI_well_logs_Tables = ['LINK_WELL_DOCUMENT']*len(a1.columns)+['TB_HORIZONDEPTHS']*len(b1.columns)+\
                        ['TB_WELLDEVIATION']*len(c1.columns)+['TB_WELLDOCUMENTS']*len(d1.columns)+\
                        ['TB_WELLLOGS']*len(e1.columns)+['TBX_SCANNEDFILES']*len(f1.columns)

Azneft_NQCI_Tables = ['LINK_WELL_DOCUMENT']*len(a2.columns)+['TB_COREINFORMATION']*len(b2.columns)+\
                        ['TB_DRAWINGSMAPS']*len(c2.columns)+['TB_DRILLINGPARAMETERS']*len(d2.columns)+\
                        ['TB_FORMATIONPRESSURES']*len(e2.columns)+['TB_FORMATIONTEMPERATURES']*len(f2.columns)+\
                        ['TB_GASANALYSIS']*len(g2.columns)+['TB_GASFACTORS']*len(h2.columns)+\
                        ['TB_HORIZONDEPTHS']*len(i2.columns)+['TB_INJECTIONANDPRODUCTION']*len(j2.columns)+\
                        ['TB_OILANALYSIS']*len(k2.columns)+['TB_WATERANALYSIS']*len(l2.columns)+\
                        ['TB_WELLCONSTRUCTIONINFO']*len(m2.columns)+['TB_WELLDOCUMENTS']*len(n2.columns)+\
                        ['TB_WELLLOGS']*len(o2.columns)+['TB_WELLPERFORATION']*len(p2.columns)+\
                        ['TB_WELLS']*len(q2.columns)+['TB_WELLSTOP']*len(r2.columns)+\
                        ['TB_WELLTESTINFO']*len(s2.columns)+['TBX_SCANNEDFILES']*len(t2.columns)+\
                        ['TB_COREANALYSIS']*len(u2.columns)

NQETLI_GD_Tables = ['LINK_SEISMIC_DOCUMENT']*len(a3.columns)+['TB_DRAWINGSMAPS']*len(b3.columns)+\
                    ['TB_SEISMICDOCUMENTS']*len(c3.columns)+['TB_SEISMICSURVEYS']*len(d3.columns)+\
                    ['TB_WELLDOCUMENTS']*len(e3.columns)+['TBX_SCANNEDFILES']*len(f3.columns)

KQIT_Tables = ['LINK_WELL_DOCUMENT']*len(a4.columns)+['TB_COREANALYSIS']*len(b4.columns)+\
                ['TB_COREINFORMATION']*len(c4.columns)+['TB_DRAWINGSMAPS']*len(d4.columns)+\
                ['TB_DRILLINGPARAMETERS']*len(e4.columns)+['TB_GASANALYSIS']*len(f4.columns)+\
                ['TB_HORIZONDEPTHS']*len(g4.columns)+['TB_OILANALYSIS']*len(h4.columns)+\
                ['TB_WATERANALYSIS']*len(i4.columns)+['TB_WELLCONSTRUCTIONINFO']*len(j4.columns)+\
                ['TB_WELLDOCUMENTS']*len(k4.columns)+['TB_WELLPERFORATION']*len(l4.columns)+\
                ['TB_WELLS']*len(m4.columns)+['TB_WELLSTOP']*len(n4.columns)+\
                ['TB_WELLTESTINFO']*len(o4.columns)+['TBX_SCANNEDFILES']*len(p4.columns)

Table_List = GGI_inklinometriya_Tables + GGI_well_logs_Tables + Azneft_NQCI_Tables + NQETLI_GD_Tables + KQIT_Tables

Excel_list = ['GGI_inklinometriya'] * len(GGI_inklinometriya_Tables) +\
              ['GGI_well_logs'] * len(GGI_well_logs_Tables) +\
              ['Azneft_NQCI'] * len(Azneft_NQCI_Tables) +\
              ['NQETLI_GD'] * len(NQETLI_GD_Tables) +\
              ['KQIT'] * len(KQIT_Tables)

Dictionary = {'Excels':Excel_list, 'Tables':Table_List, 'Columns':Total_Columns, 'Count':Count, 'Overall': Overall_Counts}

DataFrame = pd.DataFrame(Dictionary).drop(columns = 'Tables').drop_duplicates()

def Seaborn_Plot(count, path, size):
    fig, ax = plt.subplots(figsize = (120, 80))
    sns.set_style("whitegrid")
    sns.catplot(ax = ax, x = 'Columns', y = 'Count', kind = 'bar', hue = 'Excels', palette = 'bright',
                data = DataFrame[DataFrame['Overall'] == count])
    ax.set_xlabel("Columns", fontsize = 100)
    ax.set_ylabel("Number of Columns", fontsize = 100)
    ax.set_title(f"Relationship between Number of Columns ({count} times appeared) and Excel Files", fontsize = 100, y = 1.05)
    ax.set_yticks(np.arange(1, count + 1, step = 1))
    ax.tick_params(axis = 'y', labelsize = 75)
    ax.tick_params(axis = 'x', labelsize = size)
    ax.set_xticklabels(list(DataFrame[DataFrame["Overall"]==count]['Columns'].unique()), rotation = 90)
    ax.legend(loc = 'upper center', fontsize = 50)
    fig.savefig(path, format='png', dps = 4800)
#Seaborn_Plot(2, 'C:/Users/HP/Documents/2 times appeared columns.png', 10)

fig, ax = plt.subplots(figsize = (120, 80))
sns.set_style("whitegrid")
sns.catplot(ax = ax, x = 'Columns', y = 'Count', kind = 'bar', hue = 'Excels', palette = 'bright',
            data = DataFrame[DataFrame['Overall'] >= 8])
ax.set_xlabel("Columns", fontsize = 100)
ax.set_ylabel("Number of Columns", fontsize = 100)
ax.set_title("Relationship between Number of Columns (8+ times appeared) and Excel Files", fontsize = 100, y = 1.05)
ax.set_yticks(np.arange(1, 25, step = 1))
ax.tick_params(axis = 'y', labelsize = 75)
ax.tick_params(axis = 'x', labelsize = 45)
ax.set_xticklabels(list(DataFrame[DataFrame["Overall"]>=8]['Columns'].unique()), rotation = 90)
ax.legend(loc = 'upper center', fontsize = 50)
#fig.savefig('C:/Users/HP/Documents/8+ times appeared columns.png', format='png', dps = 4800)