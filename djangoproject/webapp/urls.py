from django.urls import path
from . import views

# Author: P.R. Ananya, Shayak Banerjee, Vedika Pachisia
# Date: 28 Oct '19
# Version: 1.0


urlpatterns = [
    path('', views.index, name='index'),
    path('text', views.text, name='text'),
    path('simulate_calls', views.simulate_calls, name='simulate calls'),
    path('read_from_file', views.read_from_file, name='read_from_file'),
    path('read_no_connected', views.read_no_connected, name='read_no_connect'),
    path('read_sms_data', views.read_sms_data, name='read_sms_data'),
    path('revenue_data', views.revenue_data, name='revenue_data'),
    path('read_data_data', views.read_data_data, name='read_data_data'),

]
