import csv

included_cols = [17, 0, 1, 3]  #column index numbers to be extracted
extracted = []
with open('Consumer_Complaints.csv', newline='') as csvfin:
   csvReader = csv.reader(csvfin, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
   with open('result.csv', 'a', newline='') as csvfout:
      csvWriter = csv.writer(csvfout, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      for row in csvReader:
         for col_num in included_cols:
            extracted.append(row[col_num])
         csvWriter.writerow(extracted)
         extracted = [] #flash the content once extracted data for a row are written out to a log flie.