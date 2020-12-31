from datetime import datetime
from django.urls import path, register_converter
from app.views import file_list_view, file_content_view, test_conv_view
from django.conf import settings


class DateConverter:
    regex = "[0-9]{2}-[0-9]{2}-[0-9]{4}"
    day_format = settings.DAY_FORMAT

    def to_python(self, value):
        return datetime.strptime(value, self.day_format)

    def to_url(self, value):
        print(f'\n\nValue = {value}\nvalue_type = {type(value)}\n\n')
        return value.strftime(self.day_format)


register_converter(DateConverter, 'dtc')


urlpatterns = [
    path("", file_list_view, name='file_list'),
    path("<dtc:date>/", file_list_view, name='file_list'),
    path("test/<dtc:date>/", test_conv_view, name='test_conv'),
    path("file/<str:name>/", file_content_view, name='file_content'),
]
