from django.urls import path, re_path
from . import views

app_name = 'donate'

urlpatterns = [
    path('', views.index, name='index'),

    # donate/id/
    #re_path(r'^(?P<donation_id>[0-9]+)/$', views.detail, name='detail'),

    path('MakeDonation/', views.detail, name='detail'),
]