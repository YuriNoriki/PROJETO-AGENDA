from django.urls import path
from contact import views

'''
O app_name no Django é usado para organizar e identificar URLs de um aplicativo específico em um projeto com múltiplos aplicativos.
Ele é utilizado principalmente para criar nomes de URL com escopo,
 evitando conflitos entre URLs que possam ter o mesmo nome em diferentes apps.
'''
'''
Se você quiser referenciar a URL index no template, você usaria o app_name seguido de index
'''
app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index' ),
]
