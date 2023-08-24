from django.shortcuts import render
from .models import TestCase, Question, Option, Answer, Completed
from .serializers import TestCaseSerializer, QuestionSerializer, OptionSerializer, CompletedSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes


# Create your views here.

class TestCaseList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        test_cases = TestCase.objects.all()
        serializer = TestCaseSerializer(test_cases, context={'user_id': request.user.id}, many=True)
        return Response(serializer.data)

class TestCaseDetail(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, testcase_slug, format=None):
        test_case = TestCase.objects.get(slug=testcase_slug)
        serializer = TestCaseSerializer(test_case, context={'user_id': request.user.id})
        return Response(serializer.data)

class CompletedList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        completed = Completed.objects.all()
        serializer = CompletedSerializer(completed, many=True)
        return Response(serializer.data)
    def post(self, request):
        data = request.data
        data["user"] = {"id": request.user.id}
        serializer = CompletedSerializer()
        serializer.create(data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
class CompletedDetail(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, testcase_slug):
        completed = Completed.objects.filter(test_case__slug=testcase_slug).get(user__id=request.user.id)
        serializer = CompletedSerializer(completed)
        print(serializer.data)
        return Response(serializer.data)