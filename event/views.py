# Django imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from django.core.serializers.json import DjangoJSONEncoder

from django.forms.models import model_to_dict

# Local imports
from event.models import Event


class EventView(APIView):

    def get(self, request):

        date = request.data['date']

        event_list = []

        events_qs = Event.objects.filter(date=date)

        for event in events_qs:
            event_dict = model_to_dict(event)
            event_list.append(event_dict)

        return Response(data=event_list, status=status.HTTP_200_OK)
