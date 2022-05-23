from tkinter import *
root = Tk()
root.title("idk")
root.geometry("600x600")
root.configure(background = "black")



Months = ["January","Febuary","March","April","May","June","July","August","September","October","November","December"]
Profits = ["20000","45000","78000","97000","12000","46000","65000","54000","10000","30000","70000","9000"]

max_profit = max(Profits)
max_profit_index = Profits.index(max_profit)
print(max_profit_index)

max_profit_month = Months[max_profit_index]
print(" max profit of " + str(max_profit) + " at the month of " + str(max_profit_month))

min_profit = min(Profits)
min_profit_index = Profits.index(min_profit)
print(min_profit_index)

min_profit_month = Months[min_profit_index]
print(" min profit of " + str(min_profit) + " at the month of " + str(min_profit_month))

MonthsLabel = Label(root, text = "Months = [January, Febuary, March, April, May, June, July, August, sepember, Octobe, November, December]")
MonthsLabel.place(relx = 0.5, rely = 0.1, anchor = CENTER)


MonthsLabel = Label(root, text = "Profits = [20000, 45000, 78000, 97000, 12000, 46000, 65000, 54000, 10000, 30000, 70000, 90000]")
MonthsLabel.place(relx = 0.5, rely = 0.2, anchor = CENTER)

def MaxLabel():
    MaxLabel["text"] = " max profit of " + str(max_profit) + " at the month of " + str(max_profit_month)

    
def MinLabel():                                      
    MinLabel["text"] = " min profit of " + str(min_profit) + " at the month of " + str(min_profit_month)
    
    
MaxBtn = Button(root, text = "Max profits and the month", command = MaxLabel)
MaxBtn.place(relx = 0.5, rely = 0.3, anchor = CENTER)

MaxLabel = Label(root)
MaxLabel.place(relx = 0.5, rely = 0.4, anchor = CENTER)

MinBtn = Button(root, text = "Min profits and the month", command = MinLabel)
MinBtn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

MinLabel = Label(root)
MinLabel.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()