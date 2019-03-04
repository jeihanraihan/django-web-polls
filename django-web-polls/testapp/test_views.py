from django.test import TestCase
from django.urls import reverse
from polls.models import Question

# Test views here
class IndexViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_question = 10

        for question_id in range(number_of_question):
            Question.objects.create(
                question_id=f'What is the Question {question_id}',
                pub_date=f'Date Published {question_id}',
            )

    def test_view_urls_exist(self):
        response = self.client.get('/polls/question/')
        self.assertEqual(response.status_code, 200)

    def test_urls_get_access_by_name(self):
        response = self.client.get(reverse('question'))
        self.assertEqual(response.status_code, 200)

    def test_urls_use_correct_templates(self):
        response = self.client.get(reverse('question'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'polls/index.html')

    
