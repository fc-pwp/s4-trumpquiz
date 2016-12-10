from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from quiz.views import helloworld
from quiz.views import helloworld2
from quiz.views import toppage
from quiz.views import list_quizzes
from quiz.views import start_quiz
from quiz.views import view_question
from quiz.views import result


urlpatterns = [
    url(r'^quiz/(?P<pk>[0-9]+)/$', start_quiz, name='start_quiz'),
    url(r'^quiz/(?P<quiz_pk>[0-9]+)/result/$', result, name='result'),
    url(r'^quiz/(?P<quiz_pk>[0-9]+)/question/(?P<question_seq>[0-9]+)/$',
        view_question, name='view_question'),
    url(r'^$', list_quizzes, name='list_quizzes'),
#    url(r'^$', toppage),
    url(r'^hello2/$', helloworld2),
    url(r'^hello/$', helloworld),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

