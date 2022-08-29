import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
    
Tables = [a,b,c,d,e,
          a1,b1,c1,d1,e1,f1,
          a2,b2,c2,d2,e2,f2,g2,h2,i2,j2,k2,l2,m2,n2,o2,p2,q2,r2,s2,t2,
          a3,b3,c3,d3,e3,f3,
          a4,b4,c4,d4,e4,f4,g4,h4,i4,j4,k4,l4,m4,n4,o4,p4]

Total_Columns = []
for i in range (0,len(Tables)):
    Total_Columns += (list(Tables[i].columns))

Columns = []
for elem in Total_Columns:
    if elem not in Columns:
        Columns.append(elem)
        
Count = []
for item in Columns:
    Count.append(Total_Columns.count(item))

Dictionary = {'Columns':Columns ,'Count':Count}
        
#First, dictionary is created, then, it can be turned into list and dictionary again.
#Dictionary = {}
#for item in Columns:
#    Dictionary.update({item : Total_Columns.count(item)})

#If you want to eliminate columns which occurred only once.
#for key,value in list(Dictionary.items()):
#    if value == 1:
#        del Dictionary[key]


DataFrame = pd.DataFrame(Dictionary).sort_values(by = ['Count'], ascending = False).set_index("Columns")
DataFrame.to_csv("C:/Users/HP/Documents/All Columns over 5 Tables (by excluding GGI_Seysmika).csv")

DataFrame = DataFrame.reset_index()
fig, ax = plt.subplots(figsize = (100, 50))
ax.bar(DataFrame.Columns, DataFrame.Count, color = 'firebrick')
ax.set_xlabel("Count of Columns", fontsize = 75)
ax.set_ylabel("Columns", fontsize = 75)
ax.set_title("All Columns over 5 Tables (by excluding GGI_Seysmika)", fontsize = 100)
ax.set_yticks(np.arange(1, 46, step=1))
ax.set_xticklabels(DataFrame.Columns, rotation = 90)
plt.style.use('ggplot')
plt.grid(True)
fig.savefig('C:/Users/HP/Documents/All Columns over 5 Tables (by excluding GGI_Seysmika).png',
            format='png', dps = 4800)








import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

a = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_seysmika/GGI_seysmika_LINK_SEISMIC_DOCUMENT.csv", encoding='latin1')
b = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_seysmika/GGI_seysmika_TB_ASCIIFILE.csv", encoding='latin1')
c = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_seysmika/GGI_seysmika_TB_DRAWINGSMAPS.csv", encoding='latin1')
d = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_seysmika/GGI_seysmika_TB_SEISMICDOCUMENTS.csv", encoding='latin1')
e = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_seysmika/GGI_seysmika_TB_SEISMICLINES.csv", encoding='latin1')
f = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_seysmika/GGI_seysmika_TB_SEISMICSECTIONS.csv", encoding='latin1')
g = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_seysmika/GGI_seysmika_TB_SEISMICSURVEYS.csv", encoding='latin1')
h = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_seysmika/GGI_seysmika_TBX_SCANNEDFILES.csv", encoding='latin1')
    
Tables = [a,b,c,d,e,f,g,h]

Total_Columns = []
for i in range (0,len(Tables)):
    Total_Columns += (list(Tables[i].columns))

Columns = []
for elem in Total_Columns:
    if elem not in Columns:
        Columns.append(elem)     

Count = []
for item in Columns:
    Count.append(Total_Columns.count(item))

Dictionary = {'Columns':Columns ,'Count':Count}

DataFrame = pd.DataFrame(Dictionary).sort_values(by = ['Count'], ascending = False).set_index("Columns")
DataFrame.to_csv("C:/Users/HP/Documents/All Columns over GGI_Seysmika Table.csv")

DataFrame = DataFrame.reset_index()
fig, ax = plt.subplots(figsize = (50, 25))
ax.bar(DataFrame.Columns, DataFrame.Count, color = 'firebrick')
ax.set_xlabel("Count of Columns", fontsize = 30)
ax.set_ylabel("Columns", fontsize = 30)
ax.set_title("All Columns over GGI_Seysmika Table)", fontsize = 40)
ax.set_yticks(np.arange(1, 7, step=1))
ax.set_xticklabels(DataFrame.Columns, rotation = 90)
plt.style.use('ggplot')
plt.grid(True)
fig.savefig('C:/Users/HP/Documents/All Columns over GGI_Seysmika Table.png',
            format='png', dps = 1200)
