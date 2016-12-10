from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}: {}'.format(self.pk, self.title)


class Question(models.Model):
    quiz = models.ForeignKey(Quiz)
    title = models.CharField(max_length=200)
    sequence = models.IntegerField()
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.pk)



class Answer(models.Model):
    question = models.ForeignKey(Question)
    content = models.CharField(max_length=250)
    sequence = models.IntegerField()
    code = models.CharField(max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.pk)


class Result(models.Model):
    quiz = models.ForeignKey(Quiz)
    content = models.TextField()
    code = models.CharField(max_length=1)
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.pk)


class UserScore(models.Model):
    session_key = models.CharField(max_length=32)
    previous = models.OneToOneField('self', null=True)
    quiz = models.ForeignKey(Quiz)
    answer = models.ForeignKey(Answer)
    created_at = models.DateTimeField(auto_now_add=True)



