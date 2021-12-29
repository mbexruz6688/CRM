from django.contrib import admin
from django.urls import path
from tolov.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tolov/', TolovListCreateAPIView.as_view(), name="tolovlar"),
    path("tolov/<int:pk>", TolovGetUpdateAPIView.as_view())
]
