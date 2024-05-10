from django.urls import path
from . import views


urlpatterns =[

    path('',views.home, name='home'),
    #path('drinks/<str:drink_name>', views.drinks, name='drink_name'),
    path('about/',views.about, name='about'),
    path('menu/',views.menu, name='menu'),
    path('book/', views.book, name='book'),
    path('menu_item/<int:pk>/', views.display_menu_items, name="menu_item"),
]