# from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect  # tutorial 04
from django.urls import reverse  # tutorial 04
# from django.template import loader  # tutorial 03.1 - com template index.html
from django.shortcuts import render  # 3.2 com o atalho render(r..,t..,c..)
# from django.http import Http404 # 3.3
from django.shortcuts import get_object_or_404  # 3.4 com o atalho


from polls.models import Question, Choice

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


""" def detail(request, question_id):
    return HttpResponse('Você está olhabdo para a questão %s'% question_id) """


""" def detail(request, question_id):  # tutorial 03.3
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return render(request, 'polls/detail.html', {'question': question}) """


def detail(request, question_id):  # tutorial 03.4 com atalho
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


""" def results(request, question_id):
    response = 'Você está vendo o resultado da questão %s'
    return HttpResponse(response % question_id) """


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


""" def vote(request, question_id):
    return HttpResponse('Você está votando na questão %s' % question_id) """

# view ajustada para ser chamada pelo formulario de votacao


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # captura o valor passado pelo widget do formulario de nome choice
        # e busca se ele exite entre as opções da enquete / pergunta
        selected_choice = question.choices.get(pk=request.POST['choice'])
        # tenta encontar a chave passada em caso de chave não exite, lança
        # erro de opção não exite
    except (KeyError, Choice.DoesNotExist):
        # retorna para o formulário de detalhe informando o erro
        return render(request, 'polls/detail.html',
                      {
                          'question': question,
                          'error_message': "You didn't select a choice.",
                      })
    else:
        # funcao do model Choice crida para registrar o voto
        selected_choice.register_vote()

        # Sempre retorne um HttpResponseRedirect depois de lidar com os dados
        # POST com sucesso. Isso evita que os dados sejam postados duas vezes
        # se um usuário clicar no botão Voltar.
        return HttpResponseRedirect(reverse('polls:results',
                                    args=(question.id,)))
