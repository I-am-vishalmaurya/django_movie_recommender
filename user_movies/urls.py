from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.watch_list, name='watchlist'),

]

urlpatterns = format_suffix_patterns(urlpatterns)