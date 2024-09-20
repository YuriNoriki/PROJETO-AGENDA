from django.db import models
from django.utils import timezone

# id (primary key - automático)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)

# Depois
# category (foreign key), show (boolean), owner (foreign key)
# picture (imagem)

# Criado a tabela(base da dados)
class Contact(models.Model):
    # Campos Obrigatorios 
    # Blank = Nao obrigatorio a preencher
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    create_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    
    #No Django, quando você define um campo ImageField ou FileField com o parâmetro upload_to, 
    # o caminho que você define será relativo ao diretório configurado em MEDIA_ROOT no seu arquivo de configurações (settings.py).
    picture = models.ImageField(blank=True, upload_to='picture/%Y/%m/')
    
    '''esse método é especialmente útil quando você quer que os objetos do seu modelo sejam apresentados 
    de maneira legível, tanto no terminal quanto na interface administrativa.'''
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    