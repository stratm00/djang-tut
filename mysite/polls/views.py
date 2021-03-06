from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Choice, Question
# Create your views here.

#def index(request):
#	latest_questions = Question.objects.order_by('-pub_date')[:5]
#	template = loader.get_template("polls/index.html")
#	context = {
#		'latest_question_list' : latest_questions
#	}
#	return HttpResponse(template.render(context, request))

#def detail(request, question_id):
#	question = get_object_or_404(Question, pk = question_id)
#	template = loader.get_template("polls/detail.html")
#	return HttpResponse(template.render({"question":question}, request))


#def results(request, question_id):
#	question = get_object_or_404(Question, pk=question_id)
#	return render(request, 'polls/results.html', {'question':question})

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)

	try: 
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
		selected_choice.votes+= 1
		selected_choice.save()

		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
	except (KeyError, Choice.DoesNotExist):

		return render(request, 'polls/detail.html', {
			'question':question,
			'error_message': "You didn't select a choice."
			}) 
	else:
		pass

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'