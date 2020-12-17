from collections import Counter
from django.http import HttpResponse
from django.shortcuts import render


counter_show = Counter()
counter_click = Counter()


def index(request):
    landing_type = request.GET.get('from-landing')
    if landing_type == 'test':
        counter_click['test'] += 1
    elif landing_type == 'original':
        counter_click['original'] += 1
    return render(request, 'index.html')


def landing(request):
    print(request.GET)
    if request.GET.get('ab-test-arg') == 'original':
        counter_show['original'] += 1
        return render(request, 'landing.html')
    elif request.GET.get('ab-test-arg') == 'test':
        counter_show['test'] += 1
        return render(request, 'landing_alternate.html')
    else:
        return HttpResponse('Вы ввели неверные данные')


def stats(request):
    test_stats = counter_click['test'] / counter_show['test']
    original_stats = counter_click['original'] / counter_show['original']
    return render(request, 'stats.html', context={
        'test_conversion': test_stats,
        'original_conversion': original_stats,
    })
