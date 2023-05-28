from datetime import datetime
from booking_service.domain.booking.entities import Booking
from booking_service.domain.customers.entities import Customer

class BookingDto(object):
    checkin: datetime
    checkout: datetime
    customer: Customer

    def __init__(self, checkin:datetime, checkout:datetime, customer: Customer) -> None:
        self.checkin = checkin
        self.checkout = checkout
        self.customer = customer

    def _to_domain(self):
        return Booking(self.checkin, self.checkout, self.customer)
    