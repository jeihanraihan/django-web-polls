import datetime
from django.utils import timezone
from django.test import TestCase
from . models import Question
from django.urls import reverse
# Create your tests here.
class QuestionModelTest(TestCase):
    def test_was_published_recently(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTest(TestCase):
    def test_no_question(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No Polls are Available')
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        past_question = create_question(question_text='Past Question', days=-30)
        url = reverse('polls:details', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
        #response = self.client.get(reverse('polls:index'))
        #self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past Question>'])

    def test_future_question(self):
        future_question = create_question(question_text='Future Question', days=30)
        url = reverse('polls:details', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        #response = self.client.get(reverse('polls:index'))
        #self.assertContains(response, 'No Polls are Available')
        #self.assertQuerysetEqual(response.context['latest_question_list'], [])
