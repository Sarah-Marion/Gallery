from django.shortcuts import render, get_object_or_404
from .models import LibGroup


# Create your views here.
def libs(request):
    lib_groups = LibGroup.objects.all().order_by('title')
    return render(request, 'lib/libs.html', {'libGroups': lib_groups})