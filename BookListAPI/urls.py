from django.urls import path
from . import views
from .views import books

urlpatterns = [
    path('books/', books, name='books'),
]