from rest_framework import serializers
from .models import TestCase, Question, Option, Answer, Completed
from django.contrib.auth.models import User

class OptionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Option
		fields = (
				"id",
				"text",
				"correct"
			)

class QuestionSerializer(serializers.ModelSerializer):
	options = OptionSerializer(many=True)
	class Meta:
		model = Question
		fields = (
				"id",
				"title",
				"options"
			)

class TestCaseSerializer(serializers.ModelSerializer):
	questions = QuestionSerializer(many=True, required=False)
	completed = serializers.SerializerMethodField('completedd')
	def completedd(self, objectt):
		return True if Completed.objects.filter(user=self.context['user_id']).filter(test_case=objectt.id) else False
		## here we will check if user has completed the test
		#return "A"
	class Meta:
		model = TestCase
		fields = (
				"id",
				"slug",
				"title",
				"questions",
				"completed",
				"get_absolute_url",
			)


class AnswerSerializer(serializers.ModelSerializer):
	question = QuestionSerializer()
	options = OptionSerializer(many=True)
	class Meta:
		model = Answer
		fields = (
				"id",
				"question",
				"options"
			)

class CompletedSerializer(serializers.ModelSerializer):
	# test_case = TestCaseSerializer()
	answers = AnswerSerializer(many=True)
	class Meta:
		model = Completed
		fields = (
				"id",
				"user",
				"test_case",
				"answers",
				"result",
				"right_answers",
				"wrong_answers"
			)
	def create(self, validated_data):
		q_number = len(validated_data['answers'])
		correct_q_number = 0
		u = User.objects.get(id=validated_data['user']['id'])
		test_case = TestCase.objects.get(id=validated_data['test_case'])
		completed = Completed.objects.create(user = u, test_case=test_case, result=0, right_answers=0, wrong_answers=0)
		for answer in validated_data['answers']:
			question = Question.objects.get(id=answer['question']['id'])
			answer_created = Answer.objects.create(question = question)
			for option in answer['options']:
				o = Option.objects.get(id=option['id'])
				answer_created.options.add(o)
			# check if answer is correct
			our_options = answer_created.options.all()
			correct_options = question.options.filter(correct=True).all()
			if set(our_options) == set(correct_options):
				correct_q_number+=1
			completed.answers.add(answer_created)
		completed.result = int((correct_q_number/q_number)*100)
		completed.right_answers = correct_q_number
		completed.wrong_answers = q_number - correct_q_number
		completed.save()
		return completed