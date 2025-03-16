from django.urls import path
from . import views
urlpatterns = [
    path('',views.loader,name='loader'),
    path('portfolio',views.portfolio,name='portfolio'),
    path('sendmail',views.sendmail,name='sendmail'),
    path('success',views.success,name='success')
]
