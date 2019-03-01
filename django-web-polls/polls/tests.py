import datetime
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from . models import Question
# Create your tests here.

class QuestionModelTest(TestCase):
    def test_was_published_recently(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), True)

    def test_was_published_old_question(self):
        time = timezone.now() - datetime.timedelta(days=29)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)


# New function to test new question
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

    def test_future_question_and_past_question(self):
        create_question(question_text='Future Question', days=30)
        create_question(question_text='Past Question', days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], ['Question: Past Question'])

    def test_two_past_question(self):
        create_question(question_text='Past Question', days=-30)
        create_question(question_text='Past Question', days=-15)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list', ['Question: Past Question']])

class QuestionDetailViewTest(TestCase):
    def test_future_question(self):
        future_question = create_question(question_text='Future Question', days=15)
        url = reverse('polls:details', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question(question_text='Past Question', days=-15)
        url = reverse('polls:details', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
