import datetime, random

def get_birthdays(number_of_bdays: int):
    """Return a list of random birthdays."""
    birthdays = []
    for i in range(number_of_bdays):
        start_of_year = datetime.date(2002, 1, 1)
        random_no_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + random_no_of_days

        birthdays.append(birthday.strftime("%B %d"))
    
    return birthdays

def get_match(birthdays: list):
    if len(birthdays) == len(set(birthdays)):
        return None
    
    repeated = []

    for birthday in birthdays:
        if birthday in repeated:
            continue
        else:
            counts = birthdays.count(birthday)
            if counts > 1:
                repeated.append(birthday)
    
    return repeated

def main():
    print('''Birthday Paradox, by Shreyash Raj.
  
    The birthday paradox shows us that in a group of N people, the odds
    that two of them have matching birthdays is surprisingly large.
    This program does a Monte Carlo simulation (that is, repeated random
    simulations) to explore this concept.
    
    (It's not actually a paradox, it's just a surprising result.)
    ''')

    while True:
        print("How many birthdays shall I genereate? (Max: 100)")
        total_no_of_bday = input('> ')

        if total_no_of_bday.isdecimal() and 0 < int(total_no_of_bday) <= 100:
            total_no_of_bday = int(total_no_of_bday)
            break
        else:
            print("Wrong input! Please try an integer between [1, 100]")
    
    print()
    birthdays = get_birthdays(total_no_of_bday)
    matches = get_match(birthdays)

    print("Running #1 simulation...")
    print(f"Total no. of birthday requested to generate are {str(total_no_of_bday)}.")
    print("Date of births generated are:")
    print(", ".join(birthdays))

    if matches != None:
        print("Matching birthdays are: {}".format(" ".join(matches)))
    else:
        print("There are no matching birthday in this simulation")
    print("Let's run another 100,000 simulations.")

    num_matches = 0

    for i in range(100_000):
        if i % 10_000 == 0 and i > 0:
            print(f"Completed #{str(i)} simulations...")
        
        birthdays = get_birthdays(total_no_of_bday)
        matches = get_match(birthdays)

        if matches != None:
            num_matches += 1
    
    print("Completed #100000 simulations.")
    print(f"Total no. of matches={str(num_matches)}.")
    print(f"""
    Out of 100,000 simulations of {str(total_no_of_bday)} people, there was a
    matching birthday in that group {str(num_matches)} times. This means
    that {str(total_no_of_bday)} people have a {str(round(num_matches*100/10**5, 2))}% chance of
    having a matching birthday in their group.
    That's probably more than you think.
    """)

if __name__ == '__main__':
    main()
