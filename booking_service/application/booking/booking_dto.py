from datetime import datetime
from booking_service.domain.booking import entities


class BookingDto(object):
    checkin: datetime
    checkout: datetime
    customer: entities.Customer

    def __init__(self, checkin:datetime, checkout:datetime, customer: entities.Customer) -> None:
        self.checkin = checkin
        self.checkout = checkout
        self.customer = customer

    def _to_domain(self):
        return entities.Booking(self.checkin, self.checkout, self.customer)
    