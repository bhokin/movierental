import unittest
from customer import Customer
from rental import Rental
from movie import Movie


class RentalTest(unittest.TestCase):
	
	def setUp(self):
		self.new_movie = Movie("Mulan", Movie.NEW_RELEASE)
		self.regular_movie = Movie("CitizenFour", Movie.REGULAR)
		self.childrens_movie = Movie("Frozen", Movie.CHILDRENS)

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("CitizenFour", Movie.REGULAR)
		self.assertEqual("CitizenFour", m.get_title())
		self.assertEqual(Movie.REGULAR, m.get_price_code())

	def test_rental_price(self):
		rental_price = [
			(self.new_movie, 1, 3.0),
			(self.new_movie, 5, 15.0),
			(self.new_movie, 10, 30.0),
			(self.regular_movie, 1, 2.0),
			(self.regular_movie, 2, 2.0),
			(self.regular_movie, 5, 6.5),
			(self.childrens_movie, 1, 1.5),
			(self.childrens_movie, 3, 1.5),
			(self.childrens_movie, 9, 10.5),
		]
		for movie, days_rented, price in rental_price:
			with self.subTest():
				self.assertEqual(
					Rental(movie, days_rented).get_price(), price
				)

	@unittest.skip("TODO add test of frequent renter points when you add it to Rental")
	def test_rental_points(self):
		self.fail("TODO add  test of frequent renter points")
