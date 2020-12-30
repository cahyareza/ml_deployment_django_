from django.urls import path

from estimate.views import home, result

urlpatterns = [
    path('', home),
    path('result/', result)
]