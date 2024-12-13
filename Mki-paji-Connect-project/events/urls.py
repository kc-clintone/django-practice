from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('', views.index, name='index'),
    path('events/', views.events, name='events'),
    path('register/', views.register, name='register'),
    path('accounts/logout/', views.mylogout, name='logout'),
    path('myevents/', views.user_events, name='myevents'),
    path('cancel-event/<int:event_id>/', views.cancel_event, name='cancel_event'),
]
