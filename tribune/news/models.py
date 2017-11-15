from django.db import models
import datetime as dt

class Editor(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10, blank = True)

    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save()

    def delete_editor(self):
        self.delete()

    def display_editor():
        editor = Editor.objects.all()

        return editor


        class Meta:
            ordering = ['first_name']
    # def update_editor():
    #     editor = Editor.objects.filter(id).update()
    #
    #     return editor

    # try:
    #     editor = Editor.objects.get(email = 'pork&wedges@gmail.com')
    #     print('Editor found')
    # except DoesNotExist:
    #     print('Editor was not found')

class Tags(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length = 60)
    post = models.TextField()
    editor = models.ForeignKey(Editor)
    tags = models.ManyToManyField(Tags)
    pub_date = models.DateTimeField(auto_now_add = True)
    article_image = models.ImageField(upload_to = 'articles/')

    def __str__(self):
        return self.post

    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news

    @classmethod
    def days_news(cls, date):
        news = cls.objects.filter(pub_date__date = date)
        return news

    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news
