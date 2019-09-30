from django.shortcuts import render
from .forms import HashForm
from .models import Hash
import hashlib
# Create your views here.
def home(request):
    form = HashForm()
    return render(request, 'hashing/home.html', {'form': form})
