from django.contrib import admin
from .models import Question, Choice
# Register your models here.

admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('question_text', 'pub_date', 'was_pubd_recently')
	fieldsets = [
		(None, {'fields': ['question_text']}),
		('Date information', {'fields':['pub_date'],
								'classes':['collapse']})
	]
	#fields = ['pub_date', 'question_text']
	inlines = [ChoiceInline]
admin.site.register(Question, QuestionAdmin)