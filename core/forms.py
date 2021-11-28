from django import forms
from django.core.mail.message import EmailMessage  # Importando biblioteca para envio de email
from .models import Contato, Senhas, Dependente, Filiacao, Paciente, Endereco, Agenda

"""
class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):  # Método para o emvio de e-mail usando o formulario

        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\n E-mail: {email}\n Assunto: {assunto}\n Mensagem: {mensagem}\n'

        mail = EmailMessage(
            subject='Email enviado pelo sistema Django_Ubs',
            body=conteudo,
            from_email='rodrigochagas@gmail.com.br',  # Inserir email em dominio próprio
            to={email},  # Destinatario
            headers={'Reply-to': email},
        )

        mail.send()
"""


class ContatoModelForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['tel_fixo', 'celular', 'tel_comercial', 'tel_conhecidos']


class SenhasModelForm(forms.ModelForm):
    class Meta:
        model = Senhas
        fields = ['usuario', 'senha']


class DependenteModelForm(forms.ModelForm):
    class Meta:
        model = Dependente
        fields = ['nome', 'sobrenome', 'sexo', 'data_nascimento', 'idade', 'relacionamento']


class FiliacaoModelForm(forms.ModelForm):
    class Meta:
        model = Filiacao
        fields = ['nome_pai', 'sobrenome_pai', 'nome_mae', 'sobrenome_mae']


class PacienteModelForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'sobrenome', 'sexo', 'email', 'rg', 'cartão_sus', 'dt_nascimento', 'idade', 'lactante',
                  'imagemsus', 'imagemrg']


class EnderecoModelForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['rua', 'numero', 'bairro', 'cep', 'cidade', 'estado_uf', 'país']


class AgendaModelForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ['data_ag']
