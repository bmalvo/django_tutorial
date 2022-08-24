from django.urls import path
from myapp.views import hello, helo


urlpatterns = [
    path('hello/', hello, name='hello'),
    path('helo/', helo, name='helo'),

]
