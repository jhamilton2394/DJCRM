from django.contrib import admin
from django.urls import path
from agents.views import(
    AgentListView, AgentCreateView, AgentDetailView, AgentUpdateView,
    AgentDeleteView
    )

app_name = 'agents'

urlpatterns = [
    path('', AgentListView.as_view(), name="agent-list"),
    path('create', AgentCreateView.as_view(), name="agent-create"),
    path('<int:pk>', AgentDetailView.as_view(), name="agent-detail"),
    path('<int:pk>/update', AgentUpdateView.as_view(), name="agent-update"),
    path('<int:pk>/delete', AgentDeleteView.as_view(), name="agent-delete"),
    # path('', LeadListView.as_view(), name="lead-list"),
    # path('<int:pk>/', LeadDetailView.as_view(), name="lead-detail"),
    # path('create', LeadCreateView.as_view(), name="lead-create"),
]