from datetime import datetime
import re
import matplotlib.pyplot as plt
import os


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
            date_match = re.search(r'on (\d{2}/\d{2}/\d{4})\.', line)
            
            if weight_match and date_match:
                weight = float(weight_match.group(1))
                date_str = date_match.group(1)
                try:
                    date = datetime.strptime(date_str, "%d/%m/%Y")
                except ValueError as e:
                    print(f"Error parsing date: {date_str} - {e}")
                    continue
                
                weights.append(weight)
                dates.append(date)
    return dates, weights

def plot_weights(dates, weights):
    plt.figure(figsize=(10, 6))
    plt.plot(dates, weights, marker='o', linestyle='-', color='b')
    plt.title('Weight Over Time')
    plt.xlabel('Date')
    plt.ylabel('Weight (kg)')
    
    plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter("%d/%m/%Y"))
    plt.gca().xaxis.set_major_locator(plt.matplotlib.dates.DayLocator(interval=2))  # Adjust interval as needed

    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('weight_graph.png')
    print("Plot saved as 'weight_graph.png")

def print_menu():
    print("===============")
    print("1. Input Weight")
    print("2. View weight history")
    print("3. View Graph")
    print("===============")

def main():
    while True:
        print_menu()
        try:
            choice = int(input("Input: "))

            if choice == 1:
                os.system('clear')
                date = get_date()
                weight = get_weight()
                weight_str = get_weight_str(weight, date)
                with open('weights.txt', 'a') as file:
                    file.write(weight_str)

            elif choice == 2:
                os.system('clear')
                with open('weights.txt', 'r') as file:
                    contents = file.read()
                    print(contents)

            elif choice == 3:
                dates, weights = read_weights_from_file('weights.txt')
                plot_weights(dates, weights)              
                print(weight_str)

        except ValueError:
            print("Please enter a number only")

if __name__ == "__main__":
    main()