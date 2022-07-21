from django.urls import path
from . import views


urlpatterns= [
      path('chat/<str:username>', views.massage, name='chat')
]