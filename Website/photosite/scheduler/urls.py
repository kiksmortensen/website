from django.urls import path

from . import views

app_name = 'scheduler'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:appointment_id>', views.view_appointment, name='view'),
    path('make', views.make_appointment, name='make'),
    path('cancel/<int:appointment_id>', views.cancel_appointment, name='cancel'),
    path('cancel_list', views.cancel_list, name='cancel_list')
]