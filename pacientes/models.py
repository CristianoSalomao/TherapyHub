from django.db import models
from django.urls import reverse

# Create your models here.

class Pacientes(models.Model):
    queixa_choices = (
        ('TDAH', 'Transtorno do déficit de atenção com hiperatividade'),
        ('TDA', 'Transtorno do Déficit de Atenção'),
        ('DEP', 'Depressão'),
        ('ANS', 'Ansiedade'),
        ('TAG', 'Transtorno de Ansiedade Generalizada'),
        ('TOC', 'Transtorno Obsessivo-Compulsivo'),
        ('TEPT', 'Transtorno de Estresse Pós-Traumático'),
        ('BIP', 'Transtorno Bipolar'),
        ('TPB', 'Transtorno de Personalidade Borderline'),
        ('ESQ', 'Esquizofrenia')
    )

    nome = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    telefone = models.CharField(max_length=255, null=True, blank=True)
    queixa = models.CharField(max_length=4, choices=queixa_choices, default='TDAH')
    foto = models.ImageField(upload_to='fotos')
    pagamento_em_dia = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
    
class Tarefas(models.Model):
    frequencia_choices = (
        ('DI', 'Diariamente'),
        ('1X', '1x por semana'),
        ('2X', '2x por semana'),
        ('3X', '3x por semana'),
        ('4X', '4x por semana'),
        ('SN', 'Somente quando necessário')
    )

    tarefa = models.CharField(max_length=255)
    instrucoes = models.TextField()
    frequencia = models.CharField(max_length=2, choices=frequencia_choices, default='DI')

    def __str__(self):
        return self.tarefa
    
class Consultas(models.Model):
    humor = models.PositiveIntegerField()
    registro_geral = models.TextField()
    video = models.FileField(upload_to="video")
    tarefas = models.ManyToManyField(Tarefas)
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.paciente.nome
    
    @property
    def link_publico(self):
        return f"http://127.0.0.1:8000{reverse('consulta_publica', kwargs={'id': self.id})}"
    
    @property
    def views(self):
        views = Visualizacoes.objects.filter(consulta=self)
        totais = views.count()
        unicas = views.values('ip').distinct().count()
        return f'{totais} - {unicas}'
    

class Visualizacoes(models.Model):
    consulta = models.ForeignKey('Consultas', on_delete=models.CASCADE)
    ip = models.GenericIPAddressField()
    
    def __str__(self):
        return f"{self.consulta} - {self.ip}"
