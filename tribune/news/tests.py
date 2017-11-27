from django.test import TestCase
from .models import Article, Tags

# class EditorTestClass(TestCase):
#     # set up method
#     def setUp(self):
#         self.brown = Editor(first_name = 'Brown', last_name = 'Muchai', email = 'pork&wedges@gmail.com')
#         self.brown.save_editor()
#
#         # creating a new tag and saving it
#         self.new_tag = Tags(name = 'testing')
#         self.new_tag.save()
#
#         self.new_article = Article(title = 'Tests Article', post = 'This is a random test post', editor = self.brown)
#         self.new_article.save()
#
#         self.new_article.tags.add(self.new_tag)
#
#     def tearDown(self):
#         Editor.objects.all().delete()
#         Tags.objects.all().delete()
#         Article.objects.all().delete()
#
#     # testing instance
#     def test_instance(self):
#         self.assertTrue(self.brown, Editor)
#
#     # testing save method
#     def test_save_method(self):
#         self.brown.save_editor()
#         editors = Editor.objects.all()
#         self.assertTrue(len(editors) > 0)
#
#     # testing delete method
#     def test_delete_method(self):
#         self.brown.save_editor()
#         editors = Editor.objects.all()
#         self.brown.delete_editor()
#         self.assertTrue(len(editors) == 0)
#
#     def test_display_method(self):
#         self.brown.save_editor()
#         editors = Editor.objects.all()
#         self.assertTrue(Editor.display_editor())

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news) > 0)

    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.date_news(date)
        self.assertTrue(len(news_by_date) == 0)

    # def test_update_method(self):
    #     self.brown.save_editor()
    #     editors = Editor.objects.all()
    #     self.assertFalse(Editor.update_editor())
