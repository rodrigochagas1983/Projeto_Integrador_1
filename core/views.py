""" 'Views.py' é responsavel pelo LÓGICA DE CÓDIGO que ira rodar dentro da pagina e fazer BUSCA NO BANCO DE DADOS para
# renderizar no template(Pagina HTML)
"""
from django.contrib import messages
from django.core.mail.message import EmailMessage  # Importando biblioteca para envio de email
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404  # Biblioteca para a pagina 'Error 404'
from django.core.mail import send_mail
from .models import MedicoUbs, Agenda, Senhas, Paciente, AuthUser
from .forms import ContatoModelForm, SenhasModelForm, PacienteModelForm, DependenteModelForm, FiliacaoModelForm, \
    AgendaModelForm, EnderecoModelForm


def index(request):  # Método responsavel por renderizar código e banco de dados dentro da pagina 'index.html'
    # Context passa uma variavel para dentro do codigo HTML retornando o passado dentro do método 'index'

    if str(request.user) == 'AnonymousUser':
        messages.error(request, 'Faça o Login Digitando seu Usuario e Senha!!!')

    user = request.user
    # medico = MedicoUbs.objects.filter(nome=nome)
    medicos = MedicoUbs.objects.all()

    context = {
        'curso': 'Profissionais Plantonistas Atualmente Contratados: ',
        'user': user,
        # 'medico': medico,
        'medicos': medicos,
    }

    return render(request, 'index.html', context)  # Passar 'context' como parametro na função para funcionar


"""
def contato(request):

    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():  # Retorna true se o formulario foi preenchido corretamente(é valido)
            nome = form.cleaned_data['nome']  # Armazena o digitado no campo nome na variavel 'nome'
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print('Mensagem Enviada')
            print(f'Nome: {nome}')  # imprime o que foi armazenado na variavel 'nome'
            print(f'E-mail: {email}')
            print(f'Assunto: {assunto}')
            print(f'Mensagem: {mensagem}')

            messages.success(request, 'E-mail enviado com Sucesso!!!')  # Retorna mensagem de sucesso se não houver nenhum problema
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao Enviar Mensagem!!!')  # Retorna mensagem de erro se ocorrer problemas

    context = {
        'form': form  # passa o formulario no contexto para a pagina(ser formatado pelo bootstrap)
    }

    return render(request, 'contato.html', context)
"""


def contato(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':

            form = ContatoModelForm(request.POST, request.FILES)

            if form.is_valid():

                form.save()

                tel_fixo = form.cleaned_data['tel_fixo']  # Armazena o digitado no campo nome na variavel 'nome'
                celular = form.cleaned_data['celular']
                tel_comercial = form.cleaned_data['tel_comercial']
                tel_conhecidos = form.cleaned_data['tel_conhecidos']

                print(f'Nome: {tel_fixo}')
                print(f'E-mail: {celular}')
                print(f'Assunto: {tel_comercial}')
                print(f'Mensagem: {tel_conhecidos}')

                messages.success(request, 'Dados de Contato Salvos com Sucesso.')
                # form = ContatoModelForm()
            else:
                messages.error(request, 'Erro ao Salvar Dados de Contato.')
        else:
            form = ContatoModelForm()
    else:
        return redirect('index')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


def paciente(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':

            form = PacienteModelForm(request.POST, request.FILES)

            if form.is_valid():

                form.save()

                messages.success(request, 'Dados do Paciente foram Salvos com Sucesso.')
                # form = PacienteModelForm()

            else:
                messages.error(request, 'Erro ao Salvar Dados do Paciente.')
        else:
            form = PacienteModelForm()
    else:
        return redirect('index')

    context = {
        'form': form
    }
    return render(request, 'paciente.html', context)


def dependente(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':

            form = DependenteModelForm(request.POST, request.FILES)

            if form.is_valid():

                form.save()

                messages.success(request, 'Dados dos Dependentes Salvos com Sucesso.')
                # form = DependenteModelForm()
            else:
                messages.error(request, 'Erro ao Salvar Dados dos Dependentes.')
        else:
            form = DependenteModelForm()
    else:
        return redirect('index')

    context = {
        'form': form
    }
    return render(request, 'dependente.html', context)


def filiacao(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':

            form = FiliacaoModelForm(request.POST, request.FILES)

            if form.is_valid():

                form.save()

                messages.success(request, 'Dados de Filiação Salvos com Sucesso.')
                # form = FiliacaoModelForm()
            else:
                messages.error(request, 'Erro ao Salvar Dados de Filiação.')
        else:
            form = FiliacaoModelForm()
    else:
        return redirect('index')

    context = {
        'form': form
    }
    return render(request, 'filiacao.html', context)


def endereco(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':

            form = EnderecoModelForm(request.POST, request.FILES)

            if form.is_valid():

                form.save()

                messages.success(request, 'Endereço Salvo com Sucesso.')
                # form = EnderecoModelForm()
            else:
                messages.error(request, 'Erro ao Salvar Endereço.')
        else:
            form = EnderecoModelForm()
    else:
        return redirect('index')

    context = {
        'form': form
    }
    return render(request, 'endereco.html', context)


def senhas(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':

            form = SenhasModelForm(request.POST, request.FILES)

            if form.is_valid():

                form.save()

                messages.success(request, 'Senha Salva com Sucesso.')
                # form = SenhasModelForm()
            else:
                messages.error(request, 'Erro ao Salvar Usuario e Senha.')
        else:
            form = SenhasModelForm()
    else:
        return redirect('index')

    context = {
        'form': form
    }
    return render(request, 'senhas.html', context)


def agenda(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':

            form = AgendaModelForm(request.POST, request.FILES)

            if form.is_valid():

                data_ag = form.cleaned_data['data_ag']

                data_all = Agenda.objects.all()

                for varre_data in data_all:
                    data_ag1 = varre_data.data_ag

                if data_ag == data_ag1:
                    messages.error(request, 'Esta data ja está reservada, Escolha outra data!!!')
                else:
                    form.save()

                    messages.success(request, 'Agendamento Salvo com Sucesso.')

                    # Envio de e-mail para o usuario

                    form = AgendaModelForm(request.POST, request.FILES)

                    user1 = request.user

                    user2 = AuthUser.objects.filter(username=user1)

                    for varre_user in user2:
                        email1 = varre_user.email
                        name = varre_user.first_name
                        sobrename = varre_user.last_name

                    nome1 = f'{name} {sobrename}'
                    email_send = email1
                    assunto = 'Confirmação de Agendamento de Consulta'
                    mensagem = f'Sr. {name} {sobrename}, seu Agendamento está marcado com o Doutor (*) no dia e hora {data_ag}'

                    send_mail(
                        subject=assunto,
                        message=mensagem,
                        from_email=nome1 + "<rodrigo@meusite.com>",
                        recipient_list=[email_send]
                    )
            else:
                messages.error(request, 'Erro ao Salvar Agendamento.')
        else:
            form = AgendaModelForm()
    else:
        return redirect('index')

    context = {
        'form': form
    }
    return render(request, 'agenda.html', context)


# def send_mail_medico():
