from .models import Work
from django.shortcuts import render


def works(request):
    works = Work.objects.filter(is_visible=True)
    return render(request, "work/work.html", {'works': works})
