from typing import TypedDict


class Vehicle(TypedDict):
    make: str
    model: str
    year: int

BASE_URL="https://example.com"

def generate_token():
    """
    This function will generate a token to be used in the headers of an api request.

    """
    pass

def lookup_customer(phone_number: str):
    """
    This function will lookup a customer by phone number and return customer data including:
    - Customer ID
    - First Name
    - Last Name
    - Email
    - Phone Number
    - Appointment Statuses
    - Open Recalls on their vehicles
    - Customer Vehicles

    """
    pass

def cancel_appointment(appointment_id: str):
    """
    This function will cancel an appointment by appointment ID.

    """
    pass


def get_availability(
        start_date: str, 
        end_date: str, 
        transportation_type: str, 
        services: list[str],
        vehicle: Vehicle,
        advisor_id: str | None = None,
    ):
    """
    This function will create an appointment.

    Services are the opCodes corresponding to the services a customer wants to book.

    """
    pass

def create_customer(
        phone_number: str,
        email: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        vehicle: Vehicle | None = None,
    ):
    """Used for creating a new customer."""
    pass

def book_appointment(
        date_time: str,
        customer_phone_number: str,
        vehicle: Vehicle,
        services: list[str],
        advisor_id: str | None = None,
        customer_email: str | None = None,
        customer_first_name: str | None = None,
        customer_last_name: str | None = None,
    ):
    """Used for booking a new appointment."""

    pass

def update_appointment(
        appointment_id: str,
        date_time: str,
        customer_phone_number: str,
        vehicle: Vehicle,
        services: list[str],
        advisor_id: str | None = None,
    ):
    """Used for updating an existing appointment/rescheduling an appointment."""

    pass

def get_all_opcodes():
    """Used for getting all opcodes for the dealership."""
    pass

def get_all_advisors():
    """Used for getting all advisors for the dealership."""
    pass

def get_all_valid_vehicles():
    """Used for getting all valid vehicles for the dealership."""
    pass
