from django.urls import path
from . import views
from api.views import GetData

urlpatterns = [
    path('' , GetData.as_view()),
    path('adddata/',views.addItem)
]