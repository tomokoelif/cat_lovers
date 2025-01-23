from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import About

# Create your views here.

class AboutDetailView(generic.DetailView):
    model = About
    template_name = "about/about_detail.html"

def about_me(request):
    about = get_object_or_404(About, pk=1)  # 適切な主キーを使用してください
    return render(request, 'about/about.html', {'about': about})

