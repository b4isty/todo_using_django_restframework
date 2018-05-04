from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from . import views
from .views import ToDoView

#
# router = DefaultRouter()
# router.register('todo/api', views.ToDoViewSet)

urlpatterns = [
    path('', TemplateView.as_view(template_name='todo/index.html')),
    # path('todo/api', ToDoView.as_view())
    path('todo/api/', ToDoView.as_view()),
    # path('', include(router.urls))

]
