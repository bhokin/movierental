import csv
import datetime
from enum import Enum
from typing import List


class Movie:
    """
    A movie available for rent.
    """

    def __init__(self, title: str, year: int, genre: List[str]):
        # Initialize a new movie.
        self.__title = title
        self.__year = year
        self.__genre = genre

    @property
    def get_title(self):
        return self.__title

    @property
    def get_year(self):
        return self.__year

    @property
    def get_genre(self):
        return self.__genre

    def is_genre(self, genre) -> bool:
        return genre in self.__genre


class MovieCatalog:
    """Movie catalog knows all the movies.
    It is a factory for Movies.
    """

    def get_movie(self, title: str) -> Movie:
        file = open("movies.csv")
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[1] == title:
                movie = row
                name = movie[1]
                year = movie[2]
                genre = movie[3].split('|')
                file.close()
                return Movie(name, year, genre)


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

    def for_movie(movie: Movie):
        this_year = datetime.date.today().year
        if movie.get_year == this_year:
            return PriceCode.new_release
        elif "Children" in movie.get_genre:
            return PriceCode.childrens
        return PriceCode.normal
