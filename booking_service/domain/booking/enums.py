from enum import Enum

class ErrorCodesBooking(Enum):
    CHECKINAFTERCHECKOUT = "CheckIn date cannot be after checkout"
    UNDEFINED = "Undefined"
 