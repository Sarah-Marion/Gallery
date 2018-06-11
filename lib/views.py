from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
import json
from .models import LibGroup, Technique, Location, Category, Image


# Create your views here.
def libs(request):
    lib_groups = LibGroup.objects.all().order_by('title')
    categories = Category.objects.all()
    location = Location.objects.all()
    images = Image.objects.all()

    return render(request, 'lib/libs.html', {'libGroups': lib_groups, 'categories':categories, 'location':location, 'images':images})


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


def about_me(request):
    return render(request, 'lib/about_me.html')


def all_images(request):
    images = Image.objects.all()
    categories = Category.objects.all()
    location = Location.objects.all()

    return render(request,'lib/libs.html',{'images':images,'categories':categories,'location':location})


def image_by_location(request, location):
    # if request.method == "GET" and 'location_name' in request.GET and request.is_ajax():
    # location = request.GET['location_name']
    images_location = Image.get_image_by_location(location)

    return render_to_response('lib/location.html', {'images_location':images_location})

    # return redirect(all_images)


def image_by_category(request):
    # if request.method == "GET" and 'category_name' in request.GET and request.is_ajax():
    #     category = request.GET['category_name']
    images_category1 = Image.get_image_by_category1(category)

    return render_to_response('lib/category.html',{'images_category1':images_category1})

    # return redirect(all_images)



def display_details(request,image_id):
    categories = Category.objects.all()
    location = Location.objects.all()
    this_image = Image.get_image_by_id(image_id)

    return render(request,'lib/image.html',{'this_image':this_image,'categories':categories,'location':location})


def search_image(request):
    categories = Category.objects.all()
    location = Location.objects.all()
    
    if 'image-search' in request.GET and request.GET['image-search']:
        search_category = request.GET.get('image-search')
        images_result = Image.get_image_by_category(search_category)
        message = f'{search_category}'

        return render(request,'lib/search.html',{'images_result':images_result,'message':message,'categories':categories,'location':location})

    else:
        return render(request,'lib/search.html')