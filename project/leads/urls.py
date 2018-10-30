from django.urls import path
from . import views
urlpatterns = [
    path('api/lead/create', views.LeadListCreate.as_view() ),
    path('api/lead/update', views.LeadListUpdate.as_view() ),
    path('api/lead/delete', views.LeadListDelete.as_view() ),
]