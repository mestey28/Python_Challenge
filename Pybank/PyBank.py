#PyBank

#Bring in Dependencies
import os
import csv
Datalist=[]

# csvpath= os.path.join('..', 'users','smile','pythonstuff','resources','budget_data.csv')
csvpath= os.path.join('..', 'pythonstuff', 'resources','budget_data.csv')
# budget_data.csv is sitting at c:/users/smile/pythonstuff/resources/
# PythonHW is sitting at c:/users/smile/pythonstuff/

#Variables
total_profit_loss=0
months=0
dates=[0]
row=[0]
profits=[]   
count=0 
net_total=0
profit_list=[]
profit_diff_sum=0
profit_diff_list=[]
max_month=row[0]
min_month=row[0]


with open(csvpath) as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        count=count+1   #Calculate total number of months included in dataset
        net_total=net_total+int(row[1])#the net total amount of "P/L" over the entire period

        profit_list.append(int(row[1]))

# print(count)
# print(sum)

for datarow in range(0,len(profit_list)-1):  #The Avg of the changes in "P/L" over the entire period
# [0, 1, ... 84]
# for datarow in range(0, 85)
# for datarow in range(85)
    profit_diff=profit_list[datarow+1]-profit_list[datarow]
    profit_diff_list.append(profit_diff)
    # profit_diff = profit_list[86]-profit_list[85]
    profit_diff_sum=profit_diff+profit_diff_sum
    # avg_sum=avg_change[datarow+1]-avg_change[datarow]
       
# print(avg_sum)
#print(profit_diff_list) DOUBLE CHECKS
# print(len(profit_diff_list))
# print(profit_diff_sum/len(profit_diff_list))
# print(max(profit_diff_list))
# print(min(profit_diff_list))

for datarow in range(0, len(profit_diff_list)):
    # [0, 1, 2, 3, ... 85]
    if profit_diff_list[datarow]==max(profit_diff_list):
        max_row=datarow    


for datarow in range(0, len(profit_diff_list)):
    if profit_diff_list[datarow]==min(profit_diff_list):
        min_row=datarow

#     #Date tracking
# dates.append(row[0])  
# # #greatest profit increase
# profit_diff_list> max(profit_diff_list)
# max_month=row[0]
# max(profit_diff_list)=profit_diff_list   

# print(max_month)

# #greates profit decrease
# greatest_decrease=min(profit_diff_list)
# lowest_index=profits.index(greatest_decrease)
# lowest_date=dates[lowest_index]    


#print(min_row)

# #The greatest decrease in losses (date and amount) over the entire period
       
#        min_value=min(values)

# #print_Financial_Analysis():

print('Financial Analysis')
print("---------------------------------------------")
print(f"Total Months: {count}")
print(f"Total:${net_total}")
print(f"Average Change: $ {profit_diff_sum/len(profit_diff_list)}")
print(f"Greatest Increase in Profits: {max_month} (${max(profit_diff_list)})")
print(f"Decrease in Profits: (${min(profit_diff_list)})")

# # #Create a CSV "w" file
# output_path=os.path.join('..', 'pythonstuff', 'output','budget_data2.csv')
# with open(output_path,'w') as csvfile:
#     csvwriter=csv.writer(csvfile,delimiter=',')

# Print to text file
output_file = os.path.join("C:/Users/smile/PythonStuff/Output/Pybank2")
with open(output_file, 'w') as txtfile:
    txtfile.writelines('Financial Analysis \n')
    txtfile.writelines("------------------------------------ \n")
    txtfile.writelines(f"Total Months: {count}\n")
    txtfile.writelines(f"Total Revenue: {net_total}\n")
    txtfile.writelines(f"Average Revenue Change:$ {profit_diff_sum/len(profit_diff_list)} \n")
    txtfile.writelines(f"Greatest Increase in Revenue: {max_month} {max(profit_diff_list)}\n")
    txtfile.writelines(f"Greatest Decrease in Revenue: {min_month} {min(profit_diff_list)}\n")
