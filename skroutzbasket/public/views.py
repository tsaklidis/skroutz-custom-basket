import re
# import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from scrape import get_items


def _clean_search_post(data):
    """Ensure data are valid."""
    if not re.match(r'(^http\S+)', data, re.UNICODE):
        return None
    return data


def home(request):

    data = {
    }
    return render(request, 'public/home.html', data)


@require_POST
def item_add(request):
    link = _clean_search_post(request.POST.get('link'))

    items = get_items(link)
    return HttpResponse(items, content_type='application/json; charset=utf8')
