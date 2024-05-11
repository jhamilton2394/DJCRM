from django.contrib import admin
from django.urls import path
from leads.views import (
    lead_detail, lead_list, lead_create, lead_update, lead_delete,
    LeadCreateView, LeadListView, LeadUpdateView, LeadDetailView,
    LeadDeleteView, DropdownView)   

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name="lead-list"),
    path('<int:pk>/', LeadDetailView.as_view(), name="lead-detail"),
    path('create', LeadCreateView.as_view(), name="lead-create"),
    path('<int:pk>/update', LeadUpdateView.as_view(), name="lead-update"),
    path('<int:pk>/delete', LeadDeleteView.as_view(), name="lead-delete"),
    path('dropdownview', DropdownView.as_view(), name="dropdownview"),
]