from django.urls import path

from . import views
urlpatterns=[
    path('<int:pk>/',views.fruit_details,name="fruit_detail"),
]