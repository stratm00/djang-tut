from django.test import TestCase

# Create your tests here.
import datetime 
from django.test import TestCase
from django.utils import timezone

from .models import Question


def create_question(question_text, days):

	time = timezone.now() + datetime.timedelta(days=days)
	return Questions.objects.create(question_text=question_text, pub_date=time)


class QuestionModelTests(TestCase):

	def test_was_pubd_recently_in_future(self):
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)

		self.assertIs(future_question.was_pubd_recently(), False)
class QuestionIndexViewTests(TestCase):
	def test_no_questions(self):
		response = self.client.get(reverse('polls:index'))
		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(response.context['latest_question_list'], [])
	def test_past_question(self):
		question = create_question(question_text = "PastQ. DELETETHISNOW", days=-30)

		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'], [question])

	def test_future_question(self):
		question = create_question(question_text = "FutureQ. DELETETHISNOW", days=30)

		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'], [])
