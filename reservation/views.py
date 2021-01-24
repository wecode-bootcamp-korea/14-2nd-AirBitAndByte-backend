import json

from django.http        import JsonResponse
from django.views       import View

from core.utils         import date_parser, login_decorator
from .models            import Reservation



class PaymentView(View):

    @login_decorator(required=True)
    def post(self, request, property_id):
        try:
            data      = json.loads(request.body)
            check_in  = date_parser(data['checkIn'])
            check_out = date_parser(data['checkOut'])

            result = Reservation.objects.create(property_id = property_id,
                    size_id   = data['sizeId'],
                    status_id = 2,
                    user_id   = request.user.id,
                    check_in  = check_in,
                    check_out = check_out,
                    adult     = data['adult'],
                    child     = data['child'],
                    infant    = data['infant'])
            return JsonResponse({'message': 'Success'}, status=200)

        except KeyError:
            return JsonResponse({'message': 'KeyError'}, status=400)


