import sys



def get_weight():
    while True:
        try:
            weight = int(input("What is your weight? "))
            return weight
        except ValueError:
            print("Please enter a number only.")
        



def main():
    weight = get_weight()
    print(f"Your weight is {weight}kg.")

if __name__ == "__main__":
    main()