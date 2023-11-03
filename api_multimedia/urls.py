from django.urls import path

from .  views import MultimediaListView


urlpatterns = [
    path('list/', MultimediaListView.as_view())
]