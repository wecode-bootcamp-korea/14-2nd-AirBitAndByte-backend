import jwt
import re
import json

from datetime           import datetime

from django.http        import JsonResponse

from my_settings        import SECRET_KEY_JWT, ALGORITHM
from user.models        import User
from property.models    import Property
from reservation.models import Reservation
from django.db.models   import Count, Avg


def login_decorator(required=True):
    def decorator(func):
        def wrapper(self, request, *args, **kwargs):

            access_token = request.headers.get('Authorization', None)

            if not required and not access_token:
                request.user = None
                return func(self, request, *args, **kwargs)

            payload      = jwt.decode(access_token, SECRET_KEY_JWT, algorithm=ALGORITHM)
            user         = User.objects.get(id=payload['id'])
            request.user = user
    
            return func(self, request, *args, **kwargs)
    
        return wrapper
    return decorator


def validate_email(email):
    return re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z]+\.[a-z.]+$', email)

def validate_password(password):
    return len(password) > 5

def validate_phone_number(phone_number):
    return re.match('^[0-9]{3}-[0-9]{3,4}-[0-9]{4}$', phone_number)

def validate_date_format(date):
    return re.match('^[0-9]{4}-[0-9]{2}-[0-9]{2}$', date)

def validate_check_in_out_date(check_in, check_out):
    if check_out <= check_in:
        return False
    return True

def date_parser(date):
    date_list = date.split('-')
    year      = int(date_list[0])
    month     = int(date_list[1])
    day       = int(date_list[2])
    date_time = datetime(year, month, day)
    return date_time

def check_availability(property, check_in, check_out):
    bookings      = Reservation.objects.filter(property_id=property.id)
    check_in      = datetime.date(check_in)
    check_out     = datetime.date(check_out)
    availability = []
    for booking in bookings:
        # check_in: 2020-01-09,         check_out: 2020-01-11
        # booking check_in: 2020-01-05, booking check_out: 2020-01-08
        if booking.check_in > check_out or booking.check_out < check_in:
            availability.append(True)
        else:
            availability.append(False)
    return all(availability)

def validate_review_set(property):

    # 숙소가 존재하지 않는경우 키에러가 발생하기 때문에 존재하는지 먼저 체크해준다.
    if property.review_set.exists():
        rate = {}
        rate['propertyCleanliness']   = property.review_set.aggregate(cleanliness=Avg('cleanliness'))['cleanliness']
        rate['propertyCommunication'] = property.review_set.aggregate(communication=Avg('communication'))['communication']
        rate['propertyCheckIn']       = property.review_set.aggregate(check_in=Avg('check_in'))['check_in']
        rate['propertyAccuracy']      = property.review_set.aggregate(accuracy=Avg('accuracy'))['accuracy']
        rate['propertyLocation']      = property.review_set.aggregate(location=Avg('location'))['location']
        rate['propertyAffordability'] = property.review_set.aggregate(affordability=Avg('affordability'))['affordability']

        rate['propertyRate'] = (rate['propertyCleanliness'] +\
                rate['propertyCommunication'] +\
                rate['propertyCheckIn'] +\
                rate['propertyAccuracy'] +\
                rate['propertyLocation'] +\
                rate['propertyAffordability'])/6
        return rate
    return False
