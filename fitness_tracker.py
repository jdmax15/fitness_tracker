from datetime import datetime
import re
import matplotlib.pyplot as plt
import os
import sys


def get_weight():
    while True:
        try:
            weight = float(input("What is your weight in Kilograms? "))
            return weight
        except ValueError:
            print("Please enter a number only.")

def get_date():
    date = datetime.today()
    date = date.strftime("%d/%m/%Y")
    return date

def get_weight_str(weight, date, HEIGHT):
    BMI = weight / (HEIGHT**2) 
    return f"Your weight was {weight}kg on {date}. Your BMI was {BMI:.2f}.\n"

def read_weights_from_file(file_name):
    weights = []
    dates = []
    BMIs = []

    with open(file_name, 'r') as file:
        for line in file:
            weight_match = re.search(r'(\d+\.\d+|\d+)kg', line)
            date_match = re.search(r'on (\d{2}/\d{2}/\d{4})\.', line)
            BMI_match = re.search(r'Your BMI was (\d+\.\d+)', line)
            
            if weight_match and date_match and BMI_match:
                weight = float(weight_match.group(1))
                date_str = date_match.group(1)
                BMI = float(BMI_match.group(1))
                try:
                    date = datetime.strptime(date_str, "%d/%m/%Y")
                except ValueError as e:
                    print(f"Error parsing date: {date_str} - {e}")
                    continue
                
                weights.append(weight)
                dates.append(date)
                BMIs.append(BMI)

    return dates, weights, BMIs

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

def plot_BMI(dates, BMIs):
    plt.figure(figsize=(10, 6))
    plt.plot(dates, BMIs, marker='o', linestyle='-', color='b')
    plt.title('BMI Over Time')
    plt.xlabel('Date')
    plt.ylabel('BMI')

    plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter("%d/%m/%Y"))
    plt.gca().xaxis.set_major_locator(plt.matplotlib.dates.DayLocator(interval=2))  # Adjust interval as needed

    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('BMI_graph.png')
    print("Plot saved as 'BMI_graph.png")

def print_menu():
    print("===============")
    print("1. Input Weight")
    print("2. View weight history")
    print("3. Generate Weight and BMI Graphs")
    print("4. Exit")
    print("===============")

def main():
    # My height.
    HEIGHT = 1.78
    
    while True:
        print_menu()
        try:
            choice = int(input("Input: "))

            if choice == 1:
                os.system('clear')
                date = get_date()
                weight = get_weight()
                weight_str = get_weight_str(weight, date, HEIGHT)
                with open('weights.txt', 'a') as file:
                    file.write(weight_str)

            elif choice == 2:
                os.system('clear')
                print("========================================================")
                print("                    WEIGHT HISTORY")
                print("========================================================")
                with open('weights.txt', 'r') as file:
                    contents = file.read()
                    print(contents)
                print("========================================================")

            elif choice == 3:
                os.system('clear')
                dates, weights, BMIs = read_weights_from_file('weights.txt')
                plot_weights(dates, weights)
                plot_BMI(dates, BMIs)

            elif choice == 4:
                sys.exit("Exiting fitness_tracker.py")

        except ValueError:
            print("Please enter a number only")

if __name__ == "__main__":
    main()