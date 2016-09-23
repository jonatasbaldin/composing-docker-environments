from django.http import HttpResponse
from django.views import View
from django.db.models import F
from .models import AwesomeCounter
from django.template.defaultfilters import pluralize


class IndexView(View):
    def get(self, request):

        obj, created = AwesomeCounter.objects.get_or_create(
            name='IndexCounter',
        )

        # Increment counter
        obj.counter = F('counter') + 1
        obj.save()
        # Refresh obj from DB
        obj.refresh_from_db()
        page_views = obj.counter

        return HttpResponse(
            'This page has been accessed {} time{}'.format(
                page_views,
                pluralize(page_views)
            )
        )
