from django.conf.urls import url
from django.contrib import admin

from quiz.views import helloworld
from quiz.views import helloworld2
from quiz.views import toppage
from quiz.views import list_quizzes
from quiz.views import start_quiz


urlpatterns = [
    url(r'^quiz/(?P<pk>[0-9]+)/$', start_quiz),
    url(r'^$', list_quizzes),
#    url(r'^$', toppage),
    url(r'^hello2/$', helloworld2),
    url(r'^hello/$', helloworld),
    url(r'^admin/', admin.site.urls),
]
