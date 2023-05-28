from booking_service.domain.booking.exceptions import CheckInDateCannotBeAfterCheckoutDate
from booking_service.domain.customers.exceptions import CustomerCannotBeBlank
from .booking_dto import BookingDto
from booking_service.domain.booking.enums import ErrorCodesBooking
from booking_service.domain.customers.enums import ErrorCodesCustomer
 
class BookingManager(object):
    def create_new_booking(self, bookingDto: BookingDto):
        domain_object = bookingDto._to_domain()

        try:
            if domain_object.is_valid():
                return "save" 
        except CheckInDateCannotBeAfterCheckoutDate as e:
            return {"message": e.message, "code": ErrorCodesBooking.CHECKINAFTERCHECKOUT}
        except CustomerCannotBeBlank as e:
            return {"message": e.message, "code": ErrorCodesCustomer.CUSTOMERISREQUIRED}            
        except Exception as e:
            return {"message": e.message, "code": ErrorCodesBooking.UNDEFINED}

