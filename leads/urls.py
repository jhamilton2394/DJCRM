from django.contrib import admin
from django.urls import path
from leads.views import lead_detail, lead_list, lead_create, lead_update, lead_delete, LeadCreateView

app_name = "leads"

urlpatterns = [
    path('', lead_list, name="lead-list"),
    path('<int:pk>/', lead_detail, name="lead-detail"),
    path('create', LeadCreateView.as_view(), name="lead-create"),
    path('<int:pk>/update', lead_update, name="lead-update"),
    path('<int:pk>/delete', lead_delete, name="lead-delete"),
]