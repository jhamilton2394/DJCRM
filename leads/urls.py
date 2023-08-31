from django.contrib import admin
from django.urls import path
from leads.views import (
    lead_detail, lead_list, lead_create, lead_update, lead_delete,
    LeadCreateView, LeadListView, LeadUpdateView, LeadDetailView,
    LeadDeleteView, PassDownCreateView, EntryCreateView, EntryListView,
    EntryByPassdown)   

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name="lead-list"),
    path('<int:pk>/', LeadDetailView.as_view(), name="lead-detail"),
    path('create', LeadCreateView.as_view(), name="lead-create"),
    path('<int:pk>/update', LeadUpdateView.as_view(), name="lead-update"),
    path('<int:pk>/delete', LeadDeleteView.as_view(), name="lead-delete"),
    path('createpassdown', PassDownCreateView.as_view(), name="passdown-create"),
    path('createentry', EntryCreateView.as_view(), name="entry-create"),
    path('entrylist', EntryListView.as_view(), name="entry-list"),
    path('entrybypassdown', EntryByPassdown.as_view(), name="entry-by-passdown")
]