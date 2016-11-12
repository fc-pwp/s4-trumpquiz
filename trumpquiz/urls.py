from django.conf.urls import url
from django.contrib import admin

from quiz.views import helloworld
from quiz.views import helloworld2
from quiz.views import toppage


urlpatterns = [
    url(r'^$', toppage),
    url(r'^hello2/$', helloworld2),
    url(r'^hello/$', helloworld),
    url(r'^admin/', admin.site.urls),
]
