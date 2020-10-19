import csv

CBSA_T = []
CBSA09 = []
POP00 = []
POP10 = []
PPCHG = []

index_id = []

file_to_open = "C:/Users/Ruofan_2020_Desktop/Downloads/InsightDataScience/censustract-00-10.csv"
with open(file_to_open, "r") as this_csv_file:
    pop_data = csv.reader(this_csv_file, delimiter=',')
    
    for line in pop_data:
        if line[7] != '' and line[8] != '' and line[12] != '' and line[12] != '0' and line[14] != '' and line[17] != '':
            CBSA09.append(line[7])
            CBSA_T.append(line[8])
            POP00.append(line[12])
            POP10.append(line[14])
            PPCHG.append(line[17])
    del CBSA09[0]
    del CBSA_T[0]
    del POP00[0]
    del POP10[0]
    del PPCHG[0]
    
    for i in range(len(PPCHG)):
        PPCHG[i] = PPCHG[i].replace(',', '')

    for i in range(1, len(CBSA09)):
        if CBSA_T[i-1] != CBSA_T[i]:
            index_id.append(i)
    
    CBSA_T_ = []
    CBSA09_ = []
    POP00_ = []
    POP10_ = []
    PPCHG_ = []
    COUNT_ = []
    
    for j in range(len(index_id)):
        
        CBSA09_.append(CBSA09[index_id[j]-1])
        CBSA_T_.append(CBSA_T[index_id[j]-1])
        
        temp00 = 0
        temp10 = 0
        tempchg = 0
        
        if j == 0:
            for k in range(0, index_id[j]):
                temp00 = temp00 + int(POP00[k])
                temp10 = temp10 + int(POP10[k])
                tempchg = tempchg + float(PPCHG[k])
            POP00_.append(temp00)
            POP10_.append(temp10)
            PPCHG_.append(tempchg/index_id[j])
        else:
            for k in range(index_id[j-1], index_id[j]):
                temp00 = temp00 + int(POP00[k])
                temp10 = temp10 + int(POP10[k])
                tempchg = tempchg + float(PPCHG[k])
            POP00_.append(temp00)
            POP10_.append(temp10)
            PPCHG_.append(tempchg/(index_id[j]-index_id[j-1]))
        
    n = index_id[len(index_id)-1]
        
    CBSA09_.append(CBSA09[n])
    CBSA_T_.append(CBSA_T[n])
    
    temp00 = 0
    temp10 = 0
    tempchg = 0
    for k in range(n, len(CBSA_T)):
        temp00 = temp00 + int(POP00[k])
        temp10 = temp10 + int(POP10[k])
        tempchg = tempchg + float(PPCHG[k])
    POP00_.append(temp00)
    POP10_.append(temp10)
    PPCHG_.append(tempchg/(len(CBSA_T)-n))
        
    for m in range(len(index_id)):
        if m == 0:
            COUNT_.append(index_id[m])
        else:
            COUNT_.append(index_id[m]-index_id[m-1])
    COUNT_.append(len(CBSA_T)-n)
   
    for f in range(len(PPCHG_)):
        PPCHG_[f] = round(PPCHG_[f], 2)
    
    report = []
    for g in range(len(CBSA09_)):
        report.append([int(CBSA09_[g]), CBSA_T_[g], COUNT_[g], POP00_[g], POP10_[g], PPCHG_[g]])

with open("C:/Users/Ruofan_2020_Desktop/Downloads/InsightDataScience/report.csv", "wt", newline="") as file:
    writer = csv.writer(file, delimiter=",")
    writer.writerows(report)