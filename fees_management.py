from datetime import datetime as d
from dateutil.relativedelta import relativedelta
date = d.now().strftime("%Y-%m-%d")
year, month, day = map(int, date.split("-"))

#d.now().strftime("%d-%m-%y")
# year = d.now().strftime("%Y")
# month = d.now().strftime("%m")
# day = d.now().strftime("%d")


# year = int(date.split("-")[2])
# month = int(date.split("-")[1])
# day = int(date.split("-")[0])
fee_data = {
    "student_id_1": {"name": "john", "fees": 200, "total_due": 0, "deposition_date": '01-12-2024'},
    "student_id_2": {"name": "alice", "fees": 300, "total_due": 0, "deposition_date": '01-11-2024'},
}


def current():
    global year, month, day, date
    while True:
        new_date = input("\nEnter new current date (YYYY-MM-DD): ")
        try:
            new_year, new_month, new_day = map(int, new_date.split("-"))
            if 1 <= new_month <= 12 and 1 <= new_day <= 31:
                date = new_date
                year, month, day = new_year, new_month, new_day
                print(f"Current date changed to {date}")
                break
            else:
                print("\nInvalid date.")
        except ValueError:
            print("\nInvalid formate enter in YYYY-MM-DD format.")
    

def show():
    due_fees()
    for key, val in fee_data.items():
        print(key,end=" : ")
        print(val)

def add():
    num = 1 + len(fee_data)
    ids = "student_id_" + str(num)
    name = input('Enter student name: ')
    fees = int(input('Enter student monthly fees: '))
    deposition_date = d.now().strftime("%d-%m-%Y")
    fee_data[ids]={
        "name": name, 
        "fees": fees,
        "total_due": 0,
        "deposition_date": deposition_date,
        }
    show()
    print(f"student {name} is successfully added")
def delete():
    student_id = input("Enter student id number or name to remove: ")
    try:
        student_id = int(student_id)
        student_id = str(student_id)
        student_id = "student_id_" + student_id
        if student_id in fee_data:
            del fee_data[student_id]
        else:
            print(f"{student_id} doesn't exist")
    except ValueError:
        for key, val in fee_data.items():
            if val["name"]==student_id:
                del fee_data[key]
                return
        print(f"{student_id} doesn't exist")
def due_fees():
    current_year = int(year)
    current_month = int(month)
    current_day = int(day)
    for key, val in fee_data.items():
        name = val["name"]
        fees = val["fees"]
        deposition_date = val["deposition_date"]
        last_deposit_year = int(deposition_date.split("-")[2])
        last_deposit_month = int(deposition_date.split("-")[1])
        last_deposit_day = int(deposition_date.split("-")[0])
        months_due = (current_year - last_deposit_year) * 12 + (current_month - last_deposit_month)        
        if current_day < last_deposit_day:
            months_due -= 1
        # if val['total_due'] == 0:
        val["total_due"] = months_due*fees
def deposit():
    due_fees()
    name = input("Enter name to deposit fees for : ")
    amount = int(input("Enter amount of fees deposited : "))
    for key, val in fee_data.items():
        if val['name'] == name:
            if val["total_due"] > amount:
                val["total_due"] = val["total_due"] - amount
                print(f"Deposit of {amount} successfull to {val['name']}")
                if amount >= val['fees']:
                    month = amount//val['fees']
                    print(f"month = {month}")
                    if month>=1:
                        date=val['deposition_date']
                        date_obj = d.strptime(date, "%d-%m-%Y")  
                        new_date = date_obj + relativedelta(months=month)
                        new_date_str = new_date.strftime("%d-%m-%Y")
                        val['deposition_date'] = new_date_str
                        print(f"deposition_date is {val['deposition_date']}")
                elif amount < val['fees']:
                    print(f"Deposit of {amount} successfull to {val['name']}. Remaining fees
                          {val['fees']-amount}")
                    return
                break
            else:
                val["total_due"] = 0
                val["deposition_date"] = d.now().strftime("%d-%m-%Y")
                print(f"Deposit of {amount} successfull to {val['name']}")
        # else:
        #     print(f"No recode found for {name}")
def main():
    while True:
        print("\n1. Add Student")
        print("2. Delete Student")
        print("3. Show Student")
        print("4. Deposit Fees")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add()
        elif choice == "2":
            delete()
        elif choice == "3":
            show()
        elif choice == "4":
            deposit()
        elif choice == "6":
            current()
        elif choice == "5":
            break

main()