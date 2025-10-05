from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('booklist/',views.book_list,name='book_list'),
    path('book/',views.add_book,name='add_book'),
    path('book/<int:books_id>/',views.update_book,name='update_book'),
     path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.home_view,name='home'),
    path('book/<int:books_id>/delete/', views.delete_book, name='delete_book'),
]
