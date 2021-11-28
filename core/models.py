# Models é responsavel pelo Banco de Dados da página

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agenda(models.Model):
    id_agenda = models.AutoField(db_column='ID_Agenda', primary_key=True)  # Field name made lowercase.
    id_paciente_agd = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='ID_Paciente_AGD', blank=True,
                                        null=True)  # Field name made lowercase.
    id_posto_agd = models.ForeignKey('Ubs', models.DO_NOTHING, db_column='ID_Posto_AGD', blank=True,
                                     null=True)  # Field name made lowercase.
    id_medico_agd = models.ForeignKey('MedicoUbs', models.DO_NOTHING, db_column='ID_Medico_AGD', blank=True,
                                      null=True)  # Field name made lowercase.
    id_especialidade_agd = models.ForeignKey('Especialidades', models.DO_NOTHING, db_column='ID_Especialidade_AGD',
                                             blank=True, null=True)  # Field name made lowercase.
    data_ag = models.DateTimeField('Data de Agendamento: dd/mm/yyyy hh:mm', db_column='Data_AG', blank=True,
                                   null=True)  # Field name made lowercase.
    horario_ag = models.DateTimeField('Horario de Agendamento', db_column='Horario_AG', blank=True,
                                      null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'agenda'

    def __str__(self):
        return self.data_ag  # O que será apresentado no link dos dados listados no admin


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Contato(models.Model):
    id_contato = models.AutoField(db_column='ID_Contato', primary_key=True)  # Field name made lowercase.
    num_titular = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='Num_Titular', blank=True,
                                    null=True)  # Field name made lowercase.
    tel_fixo = models.IntegerField('Numero do Telefone Fixo', blank=True, null=True)
    celular = models.IntegerField('Numero do Celular', db_column='Celular', blank=True,
                                  null=True)  # Field name made lowercase.
    tel_comercial = models.IntegerField('Numero do Telefone Comercial', db_column='Tel_comercial', blank=True,
                                        null=True)  # Field name made lowercase.
    tel_conhecidos = models.IntegerField('Contato de Conhecidos', db_column='Tel_Conhecidos', blank=True,
                                         null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contato'

    def __str__(self):
        return f'{self.tel_fixo} Celular: {self.celular}'


class Dependente(models.Model):
    id_dependente = models.AutoField(db_column='ID_Dependente', primary_key=True)  # Field name made lowercase.
    id_responsavel = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='ID_Responsavel', blank=True,
                                       null=True)  # Field name made lowercase.
    nome = models.CharField('Nome do Dependente', db_column='Nome', max_length=30, blank=True,
                            null=True)  # Field name made lowercase.
    sobrenome = models.CharField('Sobrenome do Dependente', db_column='Sobrenome', max_length=30, blank=True,
                                 null=True)  # Field name made lowercase.
    sexo = models.CharField('Sexo(Gênero)', db_column='Sexo', max_length=1, blank=True,
                            null=True)  # Field name made lowercase.
    data_nascimento = models.DateTimeField('Data de Nascimento: dd/mm/yyyy', db_column='Data_Nascimento', blank=True,
                                           null=True)  # Field name made lowercase.
    idade = models.TextField('Idade do Dependente: yy', db_column='Idade', blank=True,
                             null=True)  # Field name made lowercase. This field type is a guess.
    relacionamento = models.CharField('Grau de Relacionamento', db_column='Relacionamento', max_length=10, blank=True,
                                      null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dependente'

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Endereco(models.Model):
    id_endereço = models.AutoField(db_column='ID_Endereço', primary_key=True)  # Field name made lowercase.
    num_dono = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='Num_Dono', blank=True,
                                 null=True)  # Field name made lowercase.
    rua = models.CharField('Nome da Rua', db_column='Rua', max_length=30, blank=True,
                           null=True)  # Field name made lowercase.
    numero = models.IntegerField('Numero da Casa', db_column='Numero', blank=True,
                                 null=True)  # Field name made lowercase.
    bairro = models.CharField('Bairro', db_column='Bairro', max_length=30, blank=True,
                              null=True)  # Field name made lowercase.
    cep = models.IntegerField('CEP', db_column='CEP', blank=True, null=True)  # Field name made lowercase.
    cidade = models.CharField('Cidade', db_column='Cidade', max_length=20, blank=True,
                              null=True)  # Field name made lowercase.
    estado_uf = models.CharField('Estado(UF)', db_column='Estado_UF', max_length=2, blank=True,
                                 null=True)  # Field name made lowercase.
    país = models.CharField('País', db_column='País', max_length=10, blank=True,
                            null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'endereco'

    def __str__(self):
        return f'{self.rua} Número: {self.numero}'


class EnderecoUbs(models.Model):
    id_endereço = models.AutoField(db_column='ID_Endereþo', primary_key=True)  # Field name made lowercase.
    id_posto = models.ForeignKey('Ubs', models.DO_NOTHING, db_column='ID_Posto', blank=True,
                                 null=True)  # Field name made lowercase.
    rua = models.CharField('Rua da UBS', db_column='Rua', max_length=30, blank=True,
                           null=True)  # Field name made lowercase.
    numero = models.IntegerField('Número', db_column='Numero', blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField('Bairro', db_column='Bairro', max_length=30, blank=True,
                              null=True)  # Field name made lowercase.
    cep = models.IntegerField('CEP', db_column='CEP', blank=True, null=True)  # Field name made lowercase.
    cidade = models.CharField('Cidade', db_column='Cidade', max_length=20, blank=True,
                              null=True)  # Field name made lowercase.
    estado_uf = models.CharField('Estado(UF)', db_column='Estado_UF', max_length=2, blank=True,
                                 null=True)  # Field name made lowercase.
    país = models.CharField('País', db_column='País', max_length=20, blank=True,
                            null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'endereco_ubs'

    def __str__(self):
        return f'Rua UBS: {self.rua} Número: {self.numero}'


class Especialidades(models.Model):
    id_especialidade = models.AutoField(db_column='ID_Especialidade', primary_key=True)  # Field name made lowercase.
    id_posto_spec = models.ForeignKey('Ubs', models.DO_NOTHING, db_column='ID_Posto_Spec', blank=True,
                                      null=True)  # Field name made lowercase.
    id_medico_spec = models.ForeignKey('MedicoUbs', models.DO_NOTHING, db_column='ID_Medico_Spec', blank=True,
                                       null=True)  # Field name made lowercase.
    nome_especialidade = models.CharField('Especialidade do Profissional', db_column='Nome_Especialidade',
                                          max_length=20, blank=True, null=True)  # Field name made lowercase.
    sobrenome = models.CharField(db_column='Sobrenome', max_length=20, blank=True,
                                 null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'especialidades'

    def __str__(self):
        return f'Especialidade: {self.nome_especialidade}'


class Filiacao(models.Model):
    id_filiacao = models.AutoField(db_column='ID_Filiacao', primary_key=True)  # Field name made lowercase.
    num_filho = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='Num_filho', blank=True,
                                  null=True)  # Field name made lowercase.
    nome_pai = models.CharField('Nome do Pai', db_column='Nome_Pai', max_length=10, blank=True,
                                null=True)  # Field name made lowercase.
    sobrenome_pai = models.CharField('Sobrenome do Pai', db_column='Sobrenome_Pai', max_length=20, blank=True,
                                     null=True)  # Field name made lowercase.
    nome_mae = models.CharField('Nome da Mãe', db_column='Nome_Mae', max_length=10, blank=True,
                                null=True)  # Field name made lowercase.
    sobrenome_mae = models.CharField('Sobrenome da Mãe', db_column='Sobrenome_Mae', max_length=20, blank=True,
                                     null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'filiacao'

    def __str__(self):
        return f'Pai: {self.nome_pai} {self.sobrenome_pai} e Mãe: {self.nome_mae} {self.sobrenome_mae}'


class MedicoUbs(models.Model):
    id_medico = models.AutoField(db_column='ID_Medico', primary_key=True)  # Field name made lowercase.
    id_posto_med = models.ForeignKey('Ubs', models.DO_NOTHING, db_column='ID_Posto_Med', blank=True,
                                     null=True)  # Field name made lowercase.
    nome = models.CharField('Nome do Médico', db_column='Nome', max_length=10, blank=True,
                            null=True)  # Field name made lowercase.
    sobrenome = models.CharField('Sobrenome do Médico', db_column='Sobrenome', max_length=20, blank=True,
                                 null=True)  # Field name made lowercase.
    email = models.CharField('E-mail', db_column='Email', max_length=50, blank=True,
                             null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medico_ubs'

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'


class Paciente(models.Model):
    id_cadastro = models.AutoField(db_column='ID_Cadastro', primary_key=True)  # Field name made lowercase.
    nome = models.CharField('Nome do Paciente', db_column='Nome', max_length=30)  # Field name made lowercase.
    sobrenome = models.CharField('Sobrenome do Paciente', db_column='Sobrenome',
                                 max_length=30)  # Field name made lowercase.
    sexo = models.CharField('Sexo(Gênero)', db_column='Sexo', max_length=1, blank=True,
                            null=True)  # Field name made lowercase.
    email = models.CharField('E-mail', db_column='Email', max_length=50, blank=True,
                             null=True)  # Field name made lowercase.
    rg = models.IntegerField('R.G.', db_column='RG', blank=True, null=True)  # Field name made lowercase.
    cartão_sus = models.IntegerField('Número do Cartão do SUS', db_column='Cartão_SUS', blank=True,
                                     null=True)  # Field name made lowercase.
    dt_nascimento = models.DateTimeField('Data de Nascimento', db_column='Dt_Nascimento', blank=True,
                                         null=True)  # Field name made lowercase.
    idade = models.IntegerField('Idade do Paciente', db_column='Idade', blank=True,
                                null=True)  # Field name made lowercase.
    lactante = models.IntegerField('É Lactante?', db_column='Lactante', blank=True,
                                   null=True)  # Field name made lowercase.
    imagemsus = models.TextField('Imagem do Cartão do SUS', db_column='imagemSUS', blank=True,
                                 null=True)  # Field name made lowercase.
    imagemrg = models.TextField('Imagem do R.G.', db_column='imagemRG', blank=True,
                                null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'paciente'

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'


class Senhas(models.Model):
    id_senha = models.AutoField(db_column='ID_Senha', primary_key=True)  # Field name made lowercase.
    id_proprietario = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='ID_Proprietario', blank=True,
                                        null=True)  # Field name made lowercase.
    usuario = models.CharField('Usuário:', db_column='Usuario', max_length=20, blank=True,
                               null=True)  # Field name made lowercase.
    senha = models.CharField('Senha:', db_column='Senha', max_length=20, blank=True,
                             null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'senhas'

    def __str__(self):
        return self.usuario


class Ubs(models.Model):
    id_ubs = models.AutoField(db_column='ID_UBS', primary_key=True)  # Field name made lowercase.
    nome_unidade = models.CharField('Nome Descritivo da Unidade', db_column='Nome_unidade', max_length=30, blank=True,
                                    null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ubs'

    def __str__(self):
        return self.nome_unidade
