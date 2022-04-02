from django.urls import path
from .views import *
urlpatterns = [
    path('category', ListCategory.as_view()),
    path('category/<int:pk>/', DetailCategory.as_view()),
    path('book', ListBook.as_view()),
    path('book/<int:pk>/', DetailBook.as_view()),
    path('products', ListProduct.as_view()),
    path('product/<int:pk>/', DetailProduct.as_view())
]