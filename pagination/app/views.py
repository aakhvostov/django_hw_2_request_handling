from django.core.paginator import Paginator
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
import os
import csv

# на случай, если фйл будет меняться...
# p.s. а на самом деле я читал задание через строку и просто не увидел, что имя файла уже задано в settings)))
FILE = None
for element in os.listdir(settings.BASE_DIR):
    if element.endswith(".csv"):
        FILE = element
        break


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    with open(FILE, newline='') as f:
        reader = csv.DictReader(f)
        bus_stations_info = []
        for row in reader:
            bus_stations_info.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})
    paginator = Paginator(bus_stations_info, settings.ITEMS_PER_PAGE)
    page_obj = paginator.get_page(page_number)
    next_page_url = reverse(
        'bus_stations') + f'?page={page_obj.next_page_number()}' if page_obj.has_next() else None
    prev_page_url = reverse('bus_stations') + f'?page=' \
                                              f'{page_obj.previous_page_number()}' if page_obj.has_previous() else None
    return render(request, 'index.html', context={
        'bus_stations': page_obj.object_list,
        'current_page': page_number,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })
