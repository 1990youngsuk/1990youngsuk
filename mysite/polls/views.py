from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.db.models import F
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

from accounts.decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.decorators import login_required

# Create your views here.
'''
# Generic view version (notice we are using 'class' rather than 'def')
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    model = Question

    def get_queryset(self):
        # return the last five published questions
        return Question.objects.order_by('-pub_date')[:9]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# same as before


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice",
        })
    else:
        # fixed the race condition using 'F' method and then refreshing
        # F() objects assigned to model fields persist after saving the model instance and will be applied on each save(). For example:
        # stories_filed will be updated twice in this case. If it’s initially 1, the final value will be 3. This persistence can be avoided by reloading the model object after saving it, for example, by using refresh_from_db().
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        selected_choice.refresh_from_db()
        # Always return an HttpResponseRedirect after successfully dealing
        # with Post data. This prevents data from being poseted twice if a
        # user hits the Back button
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def get_queryset(self):
    # return the last five published questions
    return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
'''

# original view version


def index(request):
    questions = Question.objects.all()
    latest_question_list = Question.objects.order_by('-pub_date')[:9]

    context = {
        'questions': questions,
        # 'li': li,
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)


@login_required(login_url='login')
def survey(request):
    questions = Question.objects.all()
    choices = list(Question.objects.all()[0].choice_set.all())

    class CS:
        def results(self):
            return list(Question.objects.all()[self].choice_set.all())

    context = {'questions': questions, 'choices': choices}
    return render(request, 'polls/survey.html', context)


@login_required(login_url='login')
def detail(request, question_id):
    # return HttpResponse("You are looking at question %s." % question_id)
    '''  using original tech of try render and else raise 404
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/details.html', {'question': question})
    '''
    # below uses get_object_or_404 shortcut API, which return 404 if data does not exist

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


@login_required(login_url='login')
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


@login_required(login_url='login')
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice",
        })
    else:
        # fixed the race condition using 'F' method and then refreshing
        # F() objects assigned to model fields persist after saving the model instance and will be applied on each save(). For example:
        # stories_filed will be updated twice in this case. If it’s initially 1, the final value will be 3. This persistence can be avoided by reloading the model object after saving it, for example, by using refresh_from_db().
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        selected_choice.refresh_from_db()
        # Always return an HttpResponseRedirect after successfully dealing
        # with Post data. This prevents data from being poseted twice if a
        # user hits the Back button
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
