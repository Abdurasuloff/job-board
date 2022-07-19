from django.urls import path
from . import views

urlpatterns=[
      path('add-resume', views.addresume, name="add-resume"),
      path('edit-resume', views.edit_resume, name="edit-resume"),
      path('delete-resume/<int:pk>', views.delete_resume, name="delete-resume"),
      path('manage-hire-requests', views.manage_hire_requests, name='manage-hire-requests'),
      path('my-applications', views.my_applications, name="my-applications"),
      path('category-talends/<int:pk>', views.category_workers, name="category-talends" ),
      path('hire/<int:pk>', views.hire, name="hire" )
]