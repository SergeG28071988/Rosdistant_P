from django.urls import path
from .views import IndexView, AddAutoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add_auto/', AddAutoView.as_view(), name='add_auto'),
]
