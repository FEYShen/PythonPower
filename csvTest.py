path="c:\PythonScripts\google_stock.csv"
file=open(path)
##for line in file:
##	print(line)
##
##
##line=[line for line in open(path)]
dataset=[line.strip().split(',') for line in open(path)]


         
import csv
from datetime import datetime
file=open(path, newline='')

reader=csv.reader(file)

header=next(reader)

data=[]

for row in reader:
    #row=[Data,Open,High,Low,Close,Volume,Adj.close]
    date=datetime.strptime(row[0],'%m/%d/%Y']
    open_price=float(row[1])
    high=float(row[2])
    low=float(row[3])
    close=float(row[4])
    volume=int(row[5])
    adj_close=float(row[6])
    data.append([date,open_price,high,low,close,volume,adj_close])
    print(data[0])
