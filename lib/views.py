from django.shortcuts import render, get_object_or_404
from .models import LibGroup


# Create your views here.
def libs(request):
    lib_groups = LibGroup.objects.all().order_by('title')
    return render(request, 'lib/libs.html', {'libGroups': lib_groups})


def lib_detail(request, lib_title_slug):
    context_dict = {}

    try:
        lib_groups = LibGroup.objects.get(slug=lib_title_slug)
        context_dict['libGroups'] = lib_groups
        techniques = technique.objects.filter(group=lib_groups).order_by('published_date')
        context_dict['techniques'] = techniques

    except LibGroup.DoesNotExist:
        pass

    return render(request, 'lib/lib_detail.html', context_dict)
