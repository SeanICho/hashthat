from django.shortcuts import render
from .forms import HashForm
from .models import Hash
import hashlib

# Create your views here.
def home(request):

    if request.mothod == 'POST':
        filled_form = HashForm(request.POST)
        if filled_form.is_valid():
            text = filled_form.cleaned_data['text']

    form = HashForm()
    return render(request, 'hashing/home.html', {'form': form})
