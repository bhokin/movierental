import logging

from movie import *


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    But for simplicity of the example only a days_rented
    field is used.
    """

    def __init__(self, movie: Movie, days_rented: int,  price_code: PriceCode):
        """Initialize a new movie rental object for
           a movie with known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days_rented
        self.price_code = price_code

    def get_price_code(self):
        # get the price code
        return self.price_code

    def get_charge(self) -> float:
        """Compute rental change."""
        return self.get_price_code().price(self.days_rented)

    def get_point(self) -> float:
        """Award renter points."""
        return self.get_price_code().point(self.days_rented)

    def get_title(self) -> str:
        return self.movie.get_title
