from django.shortcuts import render
from django.http import HttpResponse


def helloworld(request):
    text = HttpResponse('hello world')
    return text


def helloworld2(request):
    return render(request, 'hello.html')


def toppage(request):
    quizzes = [
        {
            'image_url': 'http://images.freeimages.com/images/previews/3e2/weather-vane-1424027.jpg',
            'quiz_title': '첫 번째 퀴즈',
            'quiz_description': '우앙 재밌는 퀴즈',
        },
        {
            'image_url': 'http://images.freeimages.com/images/previews/3e2/weather-vane-1424027.jpg',
            'quiz_title': '두 번째 퀴즈',
            'quiz_description': '흥미진진한 퀴즈입니다.',
        },
        {
            'image_url': 'http://images.freeimages.com/images/previews/3e2/weather-vane-1424027.jpg',
            'quiz_title': '세 번째 퀴즈',
            'quiz_description': '풀어주세요',
        },
    ]

    ctx = {
        'page_title': '트럼프 퀴즈에 오신 걸 환영합니다',
        'quizzes': quizzes,
    }
    return render(request, 'toppage.html', ctx)


def list_quizzes(request):
    return render(request, 'list_quizzes.html')


def start_quiz(request, pk):
    ctx = {
        'quiz_pk': pk,
        'pk_type': str(type(pk)),
    }
    return render(request, 'start_quiz.html', ctx)







