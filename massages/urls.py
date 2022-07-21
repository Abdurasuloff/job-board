from django.urls import path
from . import views


urlpatterns= [
      path('chat/<username:str>', views, name='chat')
]