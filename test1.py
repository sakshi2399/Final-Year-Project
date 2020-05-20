import csv
a_file = open("names.csv", "w")
ref_male={'Fasting Sugar':120,
'Hemoglobin':{'min':14, 'max':18},
'RBC Count':{'min_RBC':4.5,'max_RBC':6.4},
'Packed Cell Volume (PCV)' : {'min':42,'max':52},
'MCV' :{'min':78,'max':94},
'MCH': {'min':27,'max':32},
'MCHC'	: {'min':32,'max':38},
'WBV (Leucocytes)': {'min':4000,'max':11000},	
'Neutrophils': {'min':60,'max':75},	
'Lymphocytes': {'min':20,'max':30},	
'Monocytes'	 : {'min':2,'max':8},
'Esoinophils': {'min':1,'max':6},
'Basophils' : {'min':0,'max':1},
'Platelets' : {'min':15000,'max':450000},
'Post Prandial (PP) Blood Sugar'	: 120,
'Blood-Glucose Level Maximum Value'	: 160,
'Glycosylated Haemoglobin':{'min' :	4.2, 'max': 7.6},
'Blood Urea' :{'min' :	0, 'max': 40} ,
'BUN-Blood Urea Nitrogen':{'min' :	0, 'max': 18},
'Serum Uric acid'	:{'min' :	3, 'max': 5.7},
'Serum Creatinine'	:{'min' :	0.5, 'max': 1.4},
'Routine urine for albumin':	'Nil',}
writer = csv.writer(a_file)
for key, value in ref_male.items():
    writer.writerow([key, value])

a_file.close()
