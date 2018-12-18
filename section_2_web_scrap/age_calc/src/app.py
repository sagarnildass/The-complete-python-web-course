
def ask_age():
    age = input("Enter your age: ")
    return int(age)

def calculate_seconds_from_years(age_years):
    return age_years * 365 * 24 * 60 * 60

def prompt_user_and_ask_age():
    age = ask_age()
    seconds_lived = calculate_seconds_from_years(age)
    print("You have lived for {} seconds.".format(seconds_lived))

prompt_user_and_ask_age()
