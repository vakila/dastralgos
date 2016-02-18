# Given list of movie running times and the length of a flight,
# determine whether there are 2 movies that will take up exactly the flight length.


def are_there_2(movie_lengths, flight_length):
    complements = dict()

    for movie in movie_lengths:
        if movie in complements:
            return True

        complements[flight_length - movie] = True

    return False


if __name__ == "__main__"

    lengths = [2.5, 2.5, ]
    flight_length = 2

    complements = {2.5:True, 3.4:True, 1.5:True, 3:True}
