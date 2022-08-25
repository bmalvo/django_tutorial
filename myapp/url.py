from django.urls import path
from myapp.views import hello, helo, morning


urlpatterns = [
    path('', hello, name='hello'),
    path('helo/', helo, name='helo'),
    path('morning/', morning, name='morning'),


]
