from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='my_index'),
    path('about/', views.about , name='my_about'),
    path('contact/',views.contact, name='my_contact'),
    path('exam_list/', views.exam_list, name='exam_list'),
    path('create/', views.exam_create, name='exam_create'),
    path('update/<int:pk>/', views.exam_update, name='exam_update'),
    path('delete/<int:pk>/', views.exam_delete, name='exam_delete'),
    path('register/', views.student_register, name='student_register'),
    path('my-exams/', views.my_exams, name='my_exams'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='my_index'), name='logout'),
]
