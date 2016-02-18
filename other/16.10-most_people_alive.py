# 16.10 year with most people alive

# people = [(1910, 1950), (1920, 1970)]

# assume sorted lists of birth_years and death_years

def find_best_year(start, end, birth_years, death_years):
    max_alive = 0
    max_year = start

    people_alive = 0

    while len(birth_years) > 0 or len(death_years) > 0:
        try:
            next_birth = birth_years[0]
        except IndexError:
            next_birth = end + 1
        try:
            next_death = death_years[0]
        except IndexError:
            next_death = end + 1

        if next_birth <= next_death:
            # add to people_alive
            year = birth_years.pop(0)
            people_alive += 1
            if people_alive > max_alive:
                max_alive = people_alive
                max_year = year
        else:
            # subtract from people_alive
            year = death_years.pop(0)
            people_alive -= 1


    return max_year
