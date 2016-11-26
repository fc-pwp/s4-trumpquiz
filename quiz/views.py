from django.shortcuts import render
from django.http import HttpResponse

from quiz.forms import StartQuizForm


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
#    if 'page' in request.GET:
#        page = request.GET['page']
#    else:
#        page = 1

#    page = request.GET.get('page')
#    page = request.GET.get('page', 1)
#    page = request.GET.get('page', '')
#    if page.isdigit():
#        page = int(page)
#    else:
#        page = 1

    page = request.GET.get('page', 1)
    try:
        page = int(page)
    except Exception:
        page = 1

    ctx = {
        'page': page * 1,
    }
    return render(request, 'list_quizzes.html', ctx)


def start_quiz(request, pk):
#    if http get 방식으로 접속하면?
#        퀴즈 시작 화면 출력
#    elif http post 방식으로 접속하면?
#        사용자가 이름을 전송한 걸 확인한 다음에
#        퀴즈 1번 문제로 이동.
    if request.method == 'GET':
        form = StartQuizForm()
    elif request.method == 'POST':
        form = StartQuizForm(data=request.POST)

        if form.is_valid():
            raise Exception('잘 된 상황이지만 임시로 오류 처리')

    ctx = {
        'form': form,
    }
    return render(request, 'start_quiz.html', ctx)


def view_question(request, quiz_pk, question_seq):
    ctx = {}
    return render(request, 'view_question.html', ctx)






