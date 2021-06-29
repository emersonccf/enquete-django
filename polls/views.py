# from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Olá Mundo, Você esta no indice de enquetes.")


def detail(request, question_id):
    return HttpResponse('Você está olhabdo para a questão %s' % question_id)


def results(request, question_id):
    response = 'Você está vendo o resultado da questão %s'
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse('Você está votando na questão %s' % question_id)
