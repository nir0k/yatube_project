from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('Главная страница')


def group_posts(request, slug):
    return HttpResponse(f'Список постов группы: {slug}')
