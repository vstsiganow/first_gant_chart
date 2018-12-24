from django.conf.urls import url
from . import views

urlpatterns = {
    url(r'^$', views.project_list, name='project_list'),
    # url(r'^$', views.calendarplan_list, name='calendarplan_list'),
    # url(r'^$', views.task_list, name='task_list'),
}