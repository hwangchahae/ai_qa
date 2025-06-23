from django.urls import path, include
from .views import qa_view


urlpatterns = [
    path('', qa_view, name ='qa'),
]