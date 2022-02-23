
from django.urls import path

from applications.category.views import CategoryListView

urlpatterns = [
    path('category-list/', CategoryListView.as_view()),
]


