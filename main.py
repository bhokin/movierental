# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie, PriceCode
from rental import Rental
from customer import Customer


def make_movies():
    movies = [
        Movie("The Irishman", PriceCode.NEW_RELEASE),
        Movie("CitizenFour", PriceCode.REGULAR),
        Movie("Frozen", PriceCode.CHILDRENS),
        Movie("El Camino", PriceCode.NEW_RELEASE),
        Movie("Particle Fever", PriceCode.REGULAR)
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days))
        days += 1
    print(customer.statement())
