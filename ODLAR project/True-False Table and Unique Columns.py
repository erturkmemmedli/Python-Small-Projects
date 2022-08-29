import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

List_True_False = []
Temporary = []
for item in range (0,len(Tables)):
    for col in range(0,len(Columns)):
        if Columns[col] in Tables[item].columns:
            Temporary.append(True)
        else:
            Temporary.append(False)
    List_True_False.append(Temporary)
    Temporary = []
    
Keys = ["LINK_SEISMIC_DOCUMENT","TB_ASCIIFILE","TB_DRAWINGSMAPS","TB_SEISMICDOCUMENTS",
         "TB_SEISMICLINES","TB_SEISMICSECTIONS","TB_SEISMICSURVEYS","TBX_SCANNEDFILES"]

Dictionary = {}
for key in range(0,len(Keys)):
    Dictionary.update({Keys[key] : List_True_False[key]})
    
DataFrame = pd.DataFrame(Dictionary)
DataFrame.index = Columns

#display(DataFrame)

#Example: DataFrame[DataFrame["TBX_SCANNEDFILES"] == True]

#DataFrame.to_csv("C:/Users/HP/Documents/DataFrame for True-False.csv")

Unique_Columns = []
count = 0
for i in range(0, len(DataFrame.index)):
    for j in range(0, len(DataFrame.columns)):
        if DataFrame.iloc[i][j] == True:
            count += 1
    if count == 1:
        Unique_Columns.append(DataFrame.index[i])
    count = 0






a = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_inklinometriya/GGI_inklinometriya_LINK_WELL_DOCUMENT.csv", encoding='latin1')
b = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_inklinometriya/GGI_inklinometriya_TB_HORIZONDEPTHS.csv", encoding='latin1')
c = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_inklinometriya/GGI_inklinometriya_TB_WELLDEVIATION.csv", encoding='latin1')
d = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_inklinometriya/GGI_inklinometriya_TB_WELLDOCUMENTS.csv", encoding='latin1')
e = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_inklinometriya/GGI_inklinometriya_TBX_SCANNEDFILES.csv", encoding='latin1')
    
Tables = [a,b,c,d,e]

Total_Columns = []
for i in range (0,len(Tables)):
    Total_Columns += (list(Tables[i].columns))

Columns = []
for elem in Total_Columns:
    if elem not in Columns:
        Columns.append(elem)     

List_True_False = []
Temporary = []
for item in range (0,len(Tables)):
    for col in range(0,len(Columns)):
        if Columns[col] in Tables[item].columns:
            Temporary.append(True)
        else:
            Temporary.append(False)
    List_True_False.append(Temporary)
    Temporary = []
    
Keys = ["LINK_WELL_DOCUMENT","TB_HORIZONDEPTHS","TB_WELLDEVIATION","TB_WELLDOCUMENTS","TBX_SCANNEDFILES"]

Dictionary = {}
for key in range(0,len(Keys)):
    Dictionary.update({Keys[key] : List_True_False[key]})
    
DataFrame = pd.DataFrame(Dictionary)
DataFrame.index = Columns

display(DataFrame)

#Example: DataFrame[DataFrame["TBX_SCANNEDFILES"] == True]

#DataFrame.to_csv("C:/Users/HP/Documents/GGI_inklinometriya_True_False.csv")

Unique_Columns = []
count = 0
for i in range(0, len(DataFrame.index)):
    for j in range(0, len(DataFrame.columns)):
        if DataFrame.iloc[i][j] == True:
            count += 1
    if count == 1:
        Unique_Columns.append(DataFrame.index[i])
    count = 0







a = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_well_logs/GGI_well_logs_LINK_WELL_DOCUMENT.csv", encoding='latin1')
b = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_well_logs/GGI_well_logs_TB_HORIZONDEPTHS.csv", encoding='latin1')
c = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_well_logs/GGI_well_logs_TB_WELLDEVIATION.csv", encoding='latin1')
d = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_well_logs/GGI_well_logs_TB_WELLDOCUMENTS.csv", encoding='latin1')
e = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_well_logs/GGI_well_logs_TB_WELLLOGS.csv", encoding='latin1')
f = pd.read_csv("C:/Users/HP/Documents/ODLAR/GGI_well_logs/GGI_well_logs_TBX_SCANNEDFILES.csv", encoding='latin1')
    
Tables = [a,b,c,d,e,f]

Total_Columns = []
for i in range (0,len(Tables)):
    Total_Columns += (list(Tables[i].columns))

Columns = []
for elem in Total_Columns:
    if elem not in Columns:
        Columns.append(elem)     

List_True_False = []
Temporary = []
for item in range (0,len(Tables)):
    for col in range(0,len(Columns)):
        if Columns[col] in Tables[item].columns:
            Temporary.append(True)
        else:
            Temporary.append(False)
    List_True_False.append(Temporary)
    Temporary = []
    
Keys = ["LINK_WELL_DOCUMENT","TB_HORIZONDEPTHS","TB_WELLDEVIATION","TB_WELLDOCUMENTS","TB_WELLLOGS","TBX_SCANNEDFILES"]

Dictionary = {}
for key in range(0,len(Keys)):
    Dictionary.update({Keys[key] : List_True_False[key]})
    
DataFrame = pd.DataFrame(Dictionary)
DataFrame.index = Columns

display(DataFrame)

#Example: DataFrame[DataFrame["TBX_SCANNEDFILES"] == True]

#DataFrame.to_csv("C:/Users/HP/Documents/GGI_well_logs_True_False.csv")

Unique_Columns = []
count = 0
for i in range(0, len(DataFrame.index)):
    for j in range(0, len(DataFrame.columns)):
        if DataFrame.iloc[i][j] == True:
            count += 1
    if count == 1:
        Unique_Columns.append(DataFrame.index[i])
    count = 0







a = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_LINK_WELL_DOCUMENT.csv", encoding='latin1')
b = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_COREINFORMATION.csv", encoding='latin1')
c = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_DRAWINGSMAPS.csv", encoding='latin1')
d = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_DRILLINGPARAMETERS.csv", encoding='latin1')
e = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_FORMATIONPRESSURES.csv", encoding='latin1')
f = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_FORMATIONTEMPERATURES.csv", encoding='latin1')
g = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_GASANALYSIS.csv", encoding='latin1')
h = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_GASFACTORS.csv", encoding='latin1')
i = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_HORIZONDEPTHS.csv", encoding='latin1')
j = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_INJECTIONANDPRODUCTION.csv", encoding='latin1')
k = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_OILANALYSIS.csv", encoding='latin1')
l = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_WATERANALYSIS.csv", encoding='latin1')
m = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_WELLCONSTRUCTIONINFO.csv", encoding='latin1')
n = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_WELLDOCUMENTS.csv", encoding='latin1')
o = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_WELLLOGS.csv", encoding='latin1')
p = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_WELLPERFORATION.csv", encoding='latin1')
q = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_WELLS.csv", encoding='latin1')
r = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_WELLSTOP.csv", encoding='latin1')
s = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TB_WELLTESTINFO.csv", encoding='latin1')
t = pd.read_csv("C:/Users/HP/Documents/ODLAR/Azneft_NQCI_cedvel/Azneft_NQCI_cedvel_TBX_SCANNEDFILES.csv", encoding='latin1')

Tables = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t]

Total_Columns = []
for i in range (0,len(Tables)):
    Total_Columns += (list(Tables[i].columns))

Columns = []
for elem in Total_Columns:
    if elem not in Columns:
        Columns.append(elem)     

List_True_False = []
Temporary = []
for item in range (0,len(Tables)):
    for col in range(0,len(Columns)):
        if Columns[col] in Tables[item].columns:
            Temporary.append(True)
        else:
            Temporary.append(False)
    List_True_False.append(Temporary)
    Temporary = []
    
Keys = ["LINK_WELL_DOCUMENT","TB_COREINFORMATION","TB_DRAWINGSMAPS","TB_DRILLINGPARAMETERS",
        "TB_FORMATIONPRESSURES","TB_FORMATIONTEMPERATURES","TB_GASANALYSIS","TB_GASFACTORS",
       "TB_HORIZONDEPTHS","TB_INJECTIONANDPRODUCTION","TB_OILANALYSIS","TB_WATERANALYSIS",
       "TB_WELLCONSTRUCTIONINFO","TB_WELLDOCUMENTS","TB_WELLLOGS","TB_WELLPERFORATION",
       "TB_WELLS","TB_WELLSTOP","TB_WELLTESTINFO","TBX_SCANNEDFILES"]

Dictionary = {}
for key in range(0,len(Keys)):
    Dictionary.update({Keys[key] : List_True_False[key]})
    
DataFrame = pd.DataFrame(Dictionary)
DataFrame.index = Columns

display(DataFrame)

#Example: DataFrame[DataFrame["TBX_SCANNEDFILES"] == True]

#DataFrame.to_csv("C:/Users/HP/Documents/Azneft_NQCI_cedvel_True_False.csv")

Unique_Columns = []
count = 0
for i in range(0, len(DataFrame.index)):
    for j in range(0, len(DataFrame.columns)):
        if DataFrame.iloc[i][j] == True:
            count += 1
    if count == 1:
        Unique_Columns.append(DataFrame.index[i])
    count = 0







a = pd.read_csv("C:/Users/HP/Documents/ODLAR/NQETLI_GD/NQETLI_GD_LINK_SEISMIC_DOCUMENT.csv", encoding='latin1')
b = pd.read_csv("C:/Users/HP/Documents/ODLAR/NQETLI_GD/NQETLI_GD_TB_DRAWINGSMAPS.csv", encoding='latin1')
c = pd.read_csv("C:/Users/HP/Documents/ODLAR/NQETLI_GD/NQETLI_GD_TB_SEISMICDOCUMENTS.csv", encoding='latin1')
d = pd.read_csv("C:/Users/HP/Documents/ODLAR/NQETLI_GD/NQETLI_GD_TB_SEISMICSURVEYS.csv", encoding='latin1')
e = pd.read_csv("C:/Users/HP/Documents/ODLAR/NQETLI_GD/NQETLI_GD_TB_WELLDOCUMENTS.csv", encoding='latin1')
f = pd.read_csv("C:/Users/HP/Documents/ODLAR/NQETLI_GD/NQETLI_GD_TBX_SCANNEDFILES.csv", encoding='latin1')


Tables = [a,b,c,d,e,f]

Total_Columns = []
for i in range (0,len(Tables)):
    Total_Columns += (list(Tables[i].columns))

Columns = []
for elem in Total_Columns:
    if elem not in Columns:
        Columns.append(elem)     

List_True_False = []
Temporary = []
for item in range (0,len(Tables)):
    for col in range(0,len(Columns)):
        if Columns[col] in Tables[item].columns:
            Temporary.append(True)
        else:
            Temporary.append(False)
    List_True_False.append(Temporary)
    Temporary = []
    
Keys = ["LINK_WELL_DOCUMENT","TB_DRAWINGSMAPS","TB_SEISMICDOCUMENTS",
        "TB_SEISMICSURVEYS","TB_WELLDOCUMENTS","TBX_SCANNEDFILES"]

Dictionary = {}
for key in range(0,len(Keys)):
    Dictionary.update({Keys[key] : List_True_False[key]})
    
DataFrame = pd.DataFrame(Dictionary)
DataFrame.index = Columns

display(DataFrame)

#Example: DataFrame[DataFrame["TBX_SCANNEDFILES"] == True]

#DataFrame.to_csv("C:/Users/HP/Documents/NQETLI_GD_True_False.csv")

Unique_Columns = []
count = 0
for i in range(0, len(DataFrame.index)):
    for j in range(0, len(DataFrame.columns)):
        if DataFrame.iloc[i][j] == True:
            count += 1
    if count == 1:
        Unique_Columns.append(DataFrame.index[i])
    count = 0







a = pd.read_csv("C:/Users/HP/Documents/ODLAR/KQIT_cedveli/KQIT_cedveli_LINK_WELL_DOCUMENT.csv", encoding='latin1')
b = pd.read_csv("C:/Users/HP/Documents/ODLAR/KQIT_cedveli/KQIT_cedveli_TB_COREANALYSIS.csv", encoding='latin1')
c = pd.read_csv("C:/Users/HP/Documents/ODLAR/KQIT_cedveli/KQIT_cedveli_TB_COREINFORMATION.csv", encoding='latin1')
d = pd.read_csv("C:/Users/HP/Documents/ODLAR/KQIT_cedveli/KQIT_cedveli_TB_DRAWINGSMAPS.csv", encoding='latin1')
e = pd.read_csv("C:/Users/HP/Documents/ODLAR/KQIT_cedveli/KQIT_cedveli_TB_DRILLINGPARAMETERS.csv", encoding='latin1')
f = pd.read_csv("C:/Users/HP/Documents/ODLAR/KQIT_cedveli/KQIT_cedveli_TB_GASANALYSIS.csv", encoding='latin1')
g = pd.read_csv("C:/Users/HP/Documents/ODLAR/KQIT_cedveli/KQIT_cedveli_TB_HORIZONDEPTHS.csv", encoding='latin1')
h = pd.read_csv("C:/Users/HP/Documents/ODLAR/KQIT_cedveli/KQIT_cedveli_TB_OILANALYSIS.csv", encoding='latin1')
i = pd.read_csv("C:/Users/HP/Documents/ODLAR/KQIT_cedveli/KQIT_cedveli_TB_WATERANALYSIS.csv", encoding='latin1')
j = pd.read_csv("C:/Users/HP/Documents/ODLAR/KQIT_cedveli/KQIT_cedveli_TB_WELLCONSTRUCTIONINFO.csv", encoding='latin1')
k = pd.read_csv("C:/Users/HP/Documents/ODLAR/KQIT_cedveli/KQIT_cedveli_TB_WELLDOCUMENTS.csv", encoding='latin1')
l = pd.read_csv("C:/Users/HP/Documents/ODLAR/KQIT_cedveli/KQIT_cedveli_TB_WELLPERFORATION.csv", encoding='latin1')
m = pd.read_csv("C:/Users/HP/Documents/ODLAR/KQIT_cedveli/KQIT_cedveli_TB_WELLS.csv", encoding='latin1')
n = pd.read_csv("C:/Users/HP/Documents/ODLAR/KQIT_cedveli/KQIT_cedveli_TB_WELLSTOP.csv", encoding='latin1')
o = pd.read_csv("C:/Users/HP/Documents/ODLAR/KQIT_cedveli/KQIT_cedveli_TB_WELLTESTINFO.csv", encoding='latin1')
p = pd.read_csv("C:/Users/HP/Documents/ODLAR/KQIT_cedveli/KQIT_cedveli_TBX_SCANNEDFILES.csv", encoding='latin1')


Tables = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p]

Total_Columns = []
for i in range (0,len(Tables)):
    Total_Columns += (list(Tables[i].columns))

Columns = []
for elem in Total_Columns:
    if elem not in Columns:
        Columns.append(elem)     

List_True_False = []
Temporary = []
for item in range (0,len(Tables)):
    for col in range(0,len(Columns)):
        if Columns[col] in Tables[item].columns:
            Temporary.append(True)
        else:
            Temporary.append(False)
    List_True_False.append(Temporary)
    Temporary = []
    
Keys = ["LINK_WELL_DOCUMENT","TB_COREANALYSIS","TB_COREINFORMATION","TB_DRAWINGSMAPS",
        "TB_DRILLINGPARAMETERS","TB_GASANALYSIS","TB_HORIZONDEPTHS","TB_OILANALYSIS",
       "TB_WATERANALYSIS","TB_WELLCONSTRUCTIONINF","TB_WELLDOCUMENTS","TB_WELLPERFORATION",
       "TB_WELLS","TB_WELLSTOP","TB_WELLTESTINFO","TBX_SCANNEDFILES"]

Dictionary = {}
for key in range(0,len(Keys)):
    Dictionary.update({Keys[key] : List_True_False[key]})
    
DataFrame = pd.DataFrame(Dictionary)
DataFrame.index = Columns

display(DataFrame)

#Example: DataFrame[DataFrame["TBX_SCANNEDFILES"] == True]

#DataFrame.to_csv("C:/Users/HP/Documents/KQIT_cedveli_True_False.csv")

Unique_Columns = []
count = 0
for i in range(0, len(DataFrame.index)):
    for j in range(0, len(DataFrame.columns)):
        if DataFrame.iloc[i][j] == True:
            count += 1
    if count == 1:
        Unique_Columns.append(DataFrame.index[i])
    count = 0