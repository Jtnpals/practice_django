from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from default.models import Question, Choice


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'default/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

    return HttpResponseRedirect(reverse('default:results', args=(question.id,)))


class IndexView(generic.ListView):
    template_name = 'default/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five publishd question."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'default/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'default/results.html'
