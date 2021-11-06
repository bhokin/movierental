import unittest
from customer import Customer
from rental import Rental
from movie import MovieCatalog, PriceCode


class RentalTest(unittest.TestCase):

	def setUp(self):
		catalog = MovieCatalog()
		self.c = Customer("Movie Mogul")
		self.new_movie = catalog.get_movie("ISP")
		self.price_code_new = PriceCode.for_movie(self.new_movie)

		self.normal_movie = catalog.get_movie("Sicario")
		self.price_code_normal = PriceCode.for_movie(self.normal_movie)

		self.childrens_movie = catalog.get_movie("Spotlight")
		self.price_code_childrens = PriceCode.for_movie(self.childrens_movie)

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		self.assertEqual("ISP", self.new_movie.get_title)
		self.assertEqual('2021', self.new_movie.get_year)
		self.assertEqual(['Action', 'Sci-Fi', 'Drama'], self.new_movie.get_genre)

	def test_rental_price(self):
		rental_price = [
			(self.new_movie, 1, self.price_code_new, 3.0),
			(self.new_movie, 5, self.price_code_new, 15.0),
			(self.new_movie, 10, self.price_code_new, 30.0),
			(self.normal_movie, 1, self.price_code_normal, 2.0),
			(self.normal_movie, 2, self.price_code_normal, 2.0),
			(self.normal_movie, 5, self.price_code_normal, 6.5),
			(self.childrens_movie, 1, self.price_code_childrens, 1.5),
			(self.childrens_movie, 3, self.price_code_childrens, 1.5),
			(self.childrens_movie, 9, self.price_code_childrens, 10.5),
		]
		for movie, days_rented, price_code, price in rental_price:
			with self.subTest():
				self.assertEqual(
					Rental(movie, days_rented, price_code).get_charge(), price
				)

	def test_rental_points(self):
		rental_point = [
			(self.new_movie, 1, self.price_code_new, 1),
			(self.new_movie, 3, self.price_code_new, 3),
			(self.normal_movie, 1, self.price_code_normal, 1),
			(self.normal_movie, 5, self.price_code_normal, 1),
			(self.childrens_movie, 1, self.price_code_childrens, 1),
			(self.childrens_movie, 3, self.price_code_childrens, 1),
		]
		for movie, days_rented, price_code, point in rental_point:
			with self.subTest():
				self.assertEqual(
					Rental(movie, days_rented, price_code).get_point(), point
				)
