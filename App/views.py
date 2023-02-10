from django.shortcuts import render, redirect
from .models import Candidate
from .forms import CandidateForm

# Create your views here.

# READ
def data_read(request):
    context = {'data_read':Candidate.objects.all()}
    return render(request, "data_read.html", context)

# CREATE / UPDATE
def data_form (request, id = None):
    if request.method == "POST":
        if id == None:
            form = CandidateForm(request.POST)
        else:
            candidate = Candidate.objects.get(pk = id)
            form = CandidateForm(request.POST, instance = candidate)
        if form.is_valid():
            form.save()
        return redirect('/data')
    else:
        if id == None:
            form = CandidateForm()
        else:
            candidate = Candidate.objects.get(pk = id)
            form = CandidateForm(instance = candidate)
        return render(request, "data_form.html", {'form':form})

# DELETE
def data_delete(request, candidate_id):
    candidate = Candidate.objects.get(id = candidate_id)
    candidate.delete()
    return redirect('/data')
