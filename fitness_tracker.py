from datetime import date, datetime





def get_weight():
    while True:
        try:
            weight = float(input("What is your weight? "))
            return weight
        except ValueError:
            print("Please enter a number only.")


def get_weight_str(weight, date):
    return f"Your weight was {weight}kg on {date}."

def get_date():
    date = datetime.today()
    date = date.strftime("%A, %d %B %Y at %I:%M%p")
    return date

def main():

    date = get_date()
    weight = get_weight()
    weight_str = get_weight_str(weight, date)
    
    print(weight_str)

if __name__ == "__main__":
    main()