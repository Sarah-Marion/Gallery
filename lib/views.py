from django.shortcuts import render, get_object_or_404
from .models import LibGroup, Technique


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


def craft_detail(request, craft_id):
    technique = get_object_or_404(Technique, id=craft_id)

    try:
        next_technique = technique.get_next_by_published_date()
        while next_technique.group != technique.group:
            next_technique = next_technique.get_next_by_published_date()
    except Technique.DoesNotExist:
        next_technique = None

    try:
        previous = technique.get_previous_by_published_date()
        while previous.group != technique.group:
            previous = previous.get_previous_by_published_date()
    except Technique.DoesNotExist:
        previous = None

    return render(request, 'lib/craft_detail.html', {'technique':technique, 'next':next_technique, 'previous':previous})