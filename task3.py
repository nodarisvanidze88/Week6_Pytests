def main():
    try:
        amount = int(input("What is the amount: "))
        years = int(input("What is the years: "))
        percent = int(input("What is the percentage: "))

    except ValueError as a:
        print(f"Wrong Value {a}")
    else:
        print(calculate_interest(amount, years, percent))


def calculate_interest(amoun, year, percen):
    if percen > 100:
        raise ValueError("Percent should be less than or equal to 100")
    result = (amoun * year * percen)/100
    return result

if __name__=="__main__":
    main()

