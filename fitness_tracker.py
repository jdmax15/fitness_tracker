from datetime import datetime
import re

HEIGHT = 178



def get_weight():
    while True:
        try:
            weight = float(input("What is your weight? "))
            return weight
        except ValueError:
            print("Please enter a number only.")

def get_date():
    date = datetime.today()
    date = date.strftime("%d/%m/%Y")
    return date

def get_weight_str(weight, date):
    return f"Your weight was {weight}kg on {date}.\n"

def read_weights_from_file(file_name):
    weights = []
    dates = []
    with open(file_name, 'r') as file:
        for line in file:
            weight_match = re.search(r'(\d+\.\d+|\d+)kg', line)
            date_match = re.search(r'on (.+)\.', line)
            if weight_match and date_match:
                weight = float(weight_match.group(1))
                date = date_match.group(1)
                weights.append(weight)
                dates.append(date)
    print(f"Weights {weights}")
    print(f"Dates: {dates}")
    return dates, weights

def main():

    date = get_date()
    weight = get_weight()
    weight_str = get_weight_str(weight, date)

    with open('weights.txt', 'a') as file:
        file.write(weight_str)

    read_weights_from_file('weights.txt')
    
    print(weight_str)

if __name__ == "__main__":
    main()