from rental import Rental
from movie import MovieCatalog, PriceCode


class Customer:
    """
       A customer who rents movies.
       The customer object holds information about the
       movies rented for the current billing period,
       and can print a statement of his rentals.
    """

    def __init__(self, name: str):
        """ Initialize a new customer."""
        self.name = name
        self.rentals = []

    def add_rental(self, rental: Rental):
        if rental not in self.rentals:
            self.rentals.append(rental)

    def get_name(self):
        return self.name

    def compute_rental_points(self) -> int:
        """Return the rental point."""
        frequent_renter_points = 0
        for rental in self.rentals:
            frequent_renter_points += rental.get_point()
        return frequent_renter_points

    def compute_total_charge(self) -> float:
        """Return the rental charge."""
        total_amount = 0  # total charges
        for rental in self.rentals:
            # and accumulate activity
            total_amount += rental.get_charge()
        return total_amount

    def statement(self) -> str:
        """
            Print all the rentals in current period, 
            along with total charges and reward points.
            Returns:
                the statement as a String
        """
        statement = f"Rental Report for {self.name}\n\n"
        fmt = "{:32s}    {:4s} {:6s}\n"
        statement += fmt.format("Movie Title", "Days", "Price")
        fmt = "{:32s}   {:4d} {:6.2f}\n"

        total_amount = self.compute_total_charge()
        frequent_renter_points = self.compute_rental_points()

        for rental in self.rentals:
            #  add detail line to statement
            statement += fmt.format(rental.get_title(), rental.days_rented, rental.get_charge())

        # footer: summary of charges
        statement += "\n"
        statement += "{:32s} {:6s} {:6.2f}\n".format(
            "Total Charges", "", total_amount)
        statement += "Frequent Renter Points earned: {}\n".format(frequent_renter_points)

        return statement


if __name__ == "__main__":
    catalog = MovieCatalog()
    customer = Customer("Edward Snowden")
    print(customer.statement())

    movie = catalog.get_movie("Mulan")
    price_code = PriceCode.for_movie(movie)
    customer.add_rental(Rental(movie, 2, price_code))

    movie = catalog.get_movie("Steve Jobs")
    price_code = PriceCode.for_movie(movie)
    customer.add_rental(Rental(movie, 3, price_code))

    print(customer.statement())
