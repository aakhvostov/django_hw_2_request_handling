import os
from datetime import datetime
from django.shortcuts import render
from django.conf import settings


def date_conv(date):
    return datetime.utcfromtimestamp(int(date)).strftime('%d-%m-%Y')


def file_list_view(request, date=None):
    template_name = 'index.html'
    files_list = os.listdir(settings.FILES_PATH)
    files = []
    for file in files_list:
        file_info = os.stat(os.path.join(settings.FILES_PATH, file))
        files.append({'name': file, 'ctime': date_conv(file_info.st_atime), 'mtime': date_conv(file_info.st_mtime)})
    context = {
        'files': files,
        'date': date.strftime("%d-%m-%Y") if date else None,
    }
    return render(request, template_name, context)


def file_content_view(request, name):
    template_name = 'file_content.html'
    file_content = []
    with open(os.path.join(settings.FILES_PATH, name)) as file:
        for line in file:
            file_content.append(line[:-1])

    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    context = {
        'file_name': name,
        'file_content': file_content,
    }
    return render(request, template_name, context)
