from django.urls import path
from . import views
app_name = 'projectapp'

urlpatterns = [
    path('', views.MyIndexView.as_view(), name="my_index_view"),
]