# from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader  # tutorial 03.1 - com template index.html
from django.shortcuts import render  # 3.2 com o atalho render(r..,t..,c..)

from polls.models import Question

""" def index(request):
    return HttpResponse("Olá Mundo, Você esta no indice de enquetes.") """


""" def index(request):  # tutorial 03
    latest_questions_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_questions_list])
    return HttpResponse(output) """


""" def index(request):  # tutorial 03.1 - com template index.html
    latest_questions_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_questions_list,
    }
    return HttpResponse(template.render(context, request)) """


def index(request):  # tutorial 03.2 - com o atalho render(r..,t..,c..)
    latest_questions_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_questions_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse('Você está olhabdo para a questão %s' % question_id)


def results(request, question_id):
    response = 'Você está vendo o resultado da questão %s'
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse('Você está votando na questão %s' % question_id)
