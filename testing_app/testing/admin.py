from django.contrib import admin
from .models import Question, TestCase, Option
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

# Register your models here.
class OptionInline(NestedStackedInline):
	min_num=1
	extra=0
	model = Option
class QuestionInline(NestedStackedInline):
	min_num=1
	extra=0
	model = Question
	inlines = [OptionInline,]

class TestCaseAdmin(NestedModelAdmin):
	model = TestCase
	inlines = [QuestionInline,]

admin.site.register(TestCase, TestCaseAdmin)