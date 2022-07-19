from django.urls import path
from . import views

urlpatterns = [
      path('new-vacancy', views.NewVacancy.as_view(), name='new-vacancy' ),
      path('edit-vacancy/<int:pk>', views.EditVacancy.as_view(), name='edit-vacancy' ),
      path('vacancy-detail/<int:pk>', views.vacancy_detail, name='vacancy-detail' ),
      path('manage-vacancies', views.manage_vacancies, name='manage-vacancies' ),
      path('hire-requests', views.hire_requests, name='hire-requests' ),
      path('manage-applications/<int:pk>', views.show_applications, name='manage-applications' ),
      path('category-jobs/<int:pk>', views.category_jobs, name='category-jobs' ),
      
      path('',views.index, name='index'),
]