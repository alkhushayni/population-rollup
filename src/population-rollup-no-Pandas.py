import csv

file_to_open = "C:/Users/Ruofan_2020_Desktop/Downloads/InsightDataScience/censustract-00-10.csv"
with open(file_to_open, "r") as this_csv_file:
    pop_data = csv.reader(this_csv_file, delimiter=",")
    
    # define variables
    CBSA09 = []
    CBSA_T = []
    POP00 = []
    POP10 = []
    PPCHG = []
    
    for line in pop_data:
        # only read the columns we need and drop the NA values
        if line[7] != '' and line[8] != '' and line[12] != '' and line[12] != '0' and line[14] != '' and line[17] != '':
            CBSA09.append(line[7])
            CBSA_T.append(line[8])
            POP00.append(line[12])
            POP10.append(line[14])
            PPCHG.append(line[17])
    # delete the headers
    del CBSA09[0]
    del CBSA_T[0]
    del POP00[0]
    del POP10[0]
    del PPCHG[0]
    # if the PPCHG's value is out of the range of 3 digits' number, it contains the comma symbol, which needs to be deleted when doing the calculation
    for i in range(len(PPCHG)):
        PPCHG[i] = PPCHG[i].replace(',', '')
        
    # find the unique CBSA Code/Title
    unique_list = [] 
    for x in CBSA09:
        if x not in unique_list:
            unique_list.append(x)
            
    # sort the list
    unique_list.sort()
            
    # number of unique CBSA Code
    n_code = len(unique_list)
    
    # find out the index for each unique value
    unique_code = []      
    for i in range(n_code):
        index = []
        for j in range(len(CBSA09)):
            if CBSA09[j] == unique_list[i]:
                index.append(j)
        unique_code.append(index)
    
    # define variables        
    CBSA09_new = []
    CBSA_T_new = []
    COUNT_new = []
    POP00_new = []
    POP10_new = []
    PPCHG_new = []
    
    for i in range(n_code):
        index = unique_code[i]
        CBSA09_new.append(CBSA09[index[0]])
        CBSA_T_new.append(CBSA_T[index[0]])
        COUNT_new.append(len(index))
        
        tmp_00 = 0
        tmp_10 = 0
        tmp_pp = 0
        for j in range(len(index)):
            tmp_00 = tmp_00 + int(POP00[index[j]])
            tmp_10 = tmp_10 + int(POP10[index[j]])
            tmp_pp = tmp_pp + float(PPCHG[index[j]])
        POP00_new.append(tmp_00)
        POP10_new.append(tmp_10)
        PPCHG_new.append(round(tmp_pp/len(index), 2))
    
    report = []
    for i in range(n_code):
        report.append([int(CBSA09_new[i]), CBSA_T_new[i], COUNT_new[i], POP00_new[i], POP10_new[i], PPCHG_new[i]])

file_to_save = "C:/Users/Ruofan_2020_Desktop/Downloads/InsightDataScience/report.csv"
with open(file_to_save, "wt", newline="") as file:
    writer = csv.writer(file, delimiter=",")
    writer.writerows(report)