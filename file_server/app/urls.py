from datetime import datetime
from django.urls import path, register_converter
from app.views import file_list_view, file_content_view


class DateConverter:
    regex = "[0-9]{2}-[0-9]{2}-[0-9]{4}"
    time_format = "%d-%m-%Y"

    def to_python(self, value):
        return datetime.strptime(value, self.time_format)

    def to_url(self, value):
        return value.strftime(self.time_format)


register_converter(DateConverter, 'dtc')


urlpatterns = [
    path("", file_list_view, name='file_list'),
    path("<dtc:date>/", file_list_view, name='file_list'),
    path("file/<str:name>/", file_content_view, name='file_content'),
]
