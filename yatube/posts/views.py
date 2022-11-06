from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    context = {
        'title': title,
    }
    return render(request, template, context)


def group_posts(request, slug):
    title = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title': title,
    }
    return HttpResponse(context['title'])
