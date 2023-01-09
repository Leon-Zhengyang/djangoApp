import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):

    def test(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        question = Question.objects.all()
        self.assertEqual(question.count(), 0)
    
    def test_2(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        question = Question.objects.all()
        self.assertEqual(question.count(), 2)
    
    def test_3(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        question = Question.objects.all()
        self.assertEqual(question.count(), 3)
