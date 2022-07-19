from django.urls import path
from . import views

urlpatterns = [
     #account pages
     path('profile/<str:username>', views.profile, name='profile'),
     path('edit-profile', views.editprofile, name="edit-profile"),
     
     #registration
     path('signup/', views.SignUpView.as_view(), name='signup'),
     path('signup-step2/<int:pk>', views.SignUp2.as_view(), name='signup-step2'),
     path('signup-worker-step3/<int:pk>', views.worker_signup, name='signup-worker'),
     path('signup-employer-step3/<int:pk>', views.employer_signup, name='signup-employer'),
     
]