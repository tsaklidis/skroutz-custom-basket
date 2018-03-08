import re
# import json
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST

from skroutzbasket.list.models import List

from scrape import get_items


def _clean_search_post(data):
    """Ensure data are valid."""
    if not re.match(r'(^http\S+)', data, re.UNICODE):
        return None
    # correct comparsion
    # link = data.split('/')
    # if link[2] != 'skroutz.gr' or link[2] != 'www.skroutz.gr':
    #     return None
    return data


def home(request):

    data = {
    }
    return render(request, 'public/home.html', data)


def list_view(request, list_name=None):
    lst = get_object_or_404(List, name=list_name)

    total_sum = 0
    for item in lst.items.all():
        total_sum = total_sum + item.price

    data = {
        'items_list': lst,
        'total_sum': total_sum,
    }
    return render(request, 'public/list.html', data)


@require_POST
def item_add(request):
    link = _clean_search_post(request.POST.get('link'))
    if link:
        items = get_items(link)
    else:
        items = {}

    return HttpResponse(items, content_type='application/json; charset=utf8')
