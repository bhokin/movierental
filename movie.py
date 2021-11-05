from enum import Enum


class PriceCode(Enum):
    """An enumeration for different kinds of movies and their behavior"""
    new_release = {"price": lambda days: 3.0 * days,
                   "frp": lambda days: days
                   }
    normal = {"price": lambda days: 2 if days <= 2 else 2 + (1.5 * (days - 2)),
              "frp": lambda days: 1
              }
    childrens = {"price": lambda days: 1.5 if days <= 3 else 1.5 + (1.5 * (days - 3)),
                 "frp": lambda days: 1
                 }

    def price(self, days: int) -> float:
        """Return the rental price for a given number of days"""
        pricing = self.value["price"]  # the enum member's price formula
        return pricing(days)

    def point(self, days: int) -> int:
        """Return the award renter points for a given number of days."""
        point = self.value["frp"]
        return point(days)


class Movie:
    """
    A movie available for rent.
    """

    def __init__(self, title: str, price_code: PriceCode):
        # Initialize a new movie.
        self.title = title
        self.price_code = price_code

    def get_price_code(self):
        # get the price code
        return self.price_code

    def get_title(self):
        return self.title
