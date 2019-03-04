from django.test import TestCase
from polls.models import Question

# Test Question models here
class QuestionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Question.objects.create(question_text='What is the question', pub_date=time)

    def test_question_name_label(self):
        question = Question.objects.get(id=1)
        field_label = question._meta.get_field('question_text').verbose_name
        self.assertEqual(field_label, 'question_text')

    def test_date_label(self):
        question = Question.objects.get(id=1)
        field_label = question._meta.get_field('pub_date').verbose_name
        self.assertContains(field_label, 'Date Published')

    def test_question_name_max_length(self):
        question = Question.objects.get(id=1)
        max_length = question._meta.get_field('question_text').max_length
        self.assertEqual(max_length, 200)

    def test_get_absolute_url(self):
        question = Question.objects.get(id=1)
        self.assertEqual(question.get_absolute_url(), '/polls/question/1')
