from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from quiz.forms import StartQuizForm
from quiz.forms import AnswerForm

from .models import Quiz
from .models import Question
from .models import Answer


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

    per_page = 2
    page = request.GET.get('page', 1)
    try:
        page = int(page)
    except Exception:
        page = 1

    start = (page - 1) * per_page
    end = page * per_page

    # contents = Quiz.objects.order_by('-created_at')
    contents = Quiz.objects.all().order_by('-created_at')

    ctx = {
        'quizzes': contents[start:end],
        'page': page * 1,
    }
    return render(request, 'list_quizzes.html', ctx)


def start_quiz(request, pk):
    # quiz = Quiz.objects.get(id=pk)
    quiz = get_object_or_404(Quiz, id=pk)
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
            #raise Exception('잘 된 상황이지만 임시로 오류 처리')
            #return redirect('/quiz/1/question/1/')
            return redirect('view_question', quiz_pk=1, question_seq=1)

    ctx = {
        'form': form,
        'quiz': quiz,
    }
    return render(request, 'start_quiz.html', ctx)


def view_question(request, quiz_pk, question_seq):
    # quiz = Quiz.objects.get(id=quiz_pk)
    quiz = get_object_or_404(Quiz, id=quiz_pk)
    question_seq = int(question_seq)
    # question = Question.objects.get(sequence=question_seq, quiz=quiz)
    question = get_object_or_404(Question, sequence=question_seq, quiz=quiz)

    answers = Answer.objects.filter(question=question).order_by('sequence')

    if request.method == 'GET':
        form = AnswerForm()
    elif request.method == 'POST':
        form = AnswerForm(request.POST)

        if form.is_valid():
            question_seq = int(question_seq) + 1
            return redirect('view_question',
                            quiz_pk=quiz_pk,
                            question_seq=question_seq)

    ctx = {
        'form': form,
        'question': question,
        'answers': answers,
    }
    return render(request, 'view_question.html', ctx)






