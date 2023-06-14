from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm

def home_page(request):
    return render(request, "leads/home_page.html")

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, "leads/lead_detail.html", context)

def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads/lead_list.html", context)

def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        print(request.POST)
        form.save()
        return redirect("/leads")
    context = {
        "form": LeadModelForm()
    }
    return render(request, "leads/lead_create.html", context)

# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadForm()
#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             f_name = form.cleaned_data['first_name']
#             l_name = form.cleaned_data['last_name']
#             ag = form.cleaned_data['age']
#             lead.first_name = f_name
#             lead.last_name = l_name
#             lead.age = ag
#             lead.save()
#             return redirect("/leads")
#     context = {
#         "lead": lead,
#         "form": form
#     }
#     return render(request, "leads/lead_update.html", context)

def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "lead": lead,
        "form": form
    }
    return render(request, "leads/lead_update.html", context)

def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")