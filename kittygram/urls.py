from django.urls import include, path

# from cats.views import cat_list
from cats import views

urlpatterns = [
   path('cats/', views.cat_list),
   path('cats/<int:pk>/', views.cat_detail),
]


