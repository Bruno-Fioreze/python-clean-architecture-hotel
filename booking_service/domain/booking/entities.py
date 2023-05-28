from .exceptions import CheckInDateCannotBeAfterCheckoutDate, CustomerCannotBeBlank
from datetime import datetime
from domain.customers.entities import Customer
from domain.rooms.entities import Room

class Booking(object):
    checkin: datetime
    checkout: datetime
    customer: Customer
    room: Room

    def __init__(self, checkin:datetime, checkout:datetime, customer: Customer) -> None:
        self.checkin = checkin
        self.checkout = checkout
        self.customer = customer

    def close_booking(self):
        pass

    def is_valid(self):
        if self.checkin > self.checkout:
            raise CheckInDateCannotBeAfterCheckoutDate("Checkin cannot be after checkout")
        elif not self.customer:
            raise CustomerCannotBeBlank("Customer cannot be blank")

        return True