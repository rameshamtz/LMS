from django.shortcuts import render,redirect
from app.models import *
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db.models import Sum

def baseView(request):
    return render(request,'base.html')

def homeView(request):
    categories=Categories.objects.all().order_by('id')[0:5]
    course=Course.objects.filter(status='PUBLISH').order_by('-id')
    context={
        'category':categories,
        'course':course
    }
    return render(request,'Main/home.html',context)

def singleCourseView(request):
    categories=Categories.get_all_category(Categories)
    level=Level.objects.all()
    course=Course.objects.all()
    freecourse_count=Course.objects.filter(price=0).count()
    paidcourse_count=Course.objects.filter(price__gte=1).count()
    context={
        'category':categories,
        'level':level,
        'course':course,
        'freecourse_count':freecourse_count,
        'paidcourse_count':paidcourse_count
    } 
    return render(request,'Main/single_course.html',context)

def search(request):
    query=request.GET['query']
    course=Course.objects.filter(title__icontains=query)
    context={
        'course':course
    }
    return render(request,'search/search.html',context)


def filter_data(request):
    categories = request.GET.getlist('category[]')
    level = request.GET.getlist('level[]')
    price = request.GET.getlist('price[]')

    if price == ['pricefree']:
       course = Course.objects.filter(price=0)
    elif price == ['pricepaid']:
       course = Course.objects.filter(price__gte=1)
    elif price == ['priceall']:
       course = Course.objects.all()
    elif categories:
       course = Course.objects.filter(category__id__in=categories).order_by('-id')
    elif level:
       course = Course.objects.filter(level__id__in = level).order_by('-id')
    else:
       course = Course.objects.all().order_by('-id')

    t = render_to_string('ajax/course.html', {'course': course})

    return JsonResponse({'data': t})

def contactUsView(request):
    category=Categories.get_all_category(Categories)
    context={
        'category':category
    }
    return render(request,'Main/contact_us.html',context)

def aboutUsView(request):
    category=Categories.get_all_category(Categories)
    context={
        'category':category
    }
    return render(request,'Main/about_us.html',context)

def course_details(request,slug):
    category=Categories.get_all_category(Categories)
    time_duration=Video.objects.filter(course__slug=slug).aggregate(sum=Sum('time_duration'))
    course=Course.objects.filter(slug=slug)
    if course.exists():
        course=course.first()
    else:
        return redirect('404')
    context={
        'course':course,
        'category':category,
        'time_duration':time_duration
    }
    return render(request,'Course/course_details.html',context)

def page_not_found(request,slug):
    category=Categories.get_all_category(Categories)
    context={
        'category':category
    }
    return render(request,'Error/404.html',context)


