import json
from django.http.response import JsonResponse

from django.views import View

from core.utils import login_decorator
from reservation.models import Reservation


class ReservationView(View):
    
    @login_decorator(required=True)

    # 이미지를 넣어하는데 방법을 찾아야함! 
    def get(self, request):
        try:
            reservations = Reservation.objects.select_related(
                    'property',
                    'size',
                    'status',
                    'user'
                    ).filter(user=request.user)
    
            context = [{
                'reservation_id': reservation.id,
                'created_at': reservation.created_at,
                'check_in': reservation.check_in,
                'property_id': reservation.property_id,
                'title': reservation.property.title,
                'content': reservation.property.content,
                'capacity': reservation.property.capacity,
                'adult': reservation.adult,
                'child': reservation.child,
                'infant': reservation.infant,
                'price': reservation.property.price,
                'status_id': reservation.status_id,
                'status_name': reservation.status.name
                }
                for reservation in reservations
                ]
    
            return JsonResponse({'result': context}, status=200)
        except KeyError:
            return JsonResponse({'message': 'KeyError'}, status=400)
