from django.shortcuts import render

'''
    O request é um objeto que contém todos os dados da requisição HTTP enviada pelo navegador (ou qualquer cliente) para o servidor. 
    Ele armazena informações sobre o método da requisição (GET, POST, etc.), os cabeçalhos, os dados enviados pelo usuário, entre outros.
      No exemplo que você mostrou, ele é passado como argumento para a função index, que representa a view responsável por lidar com essa requisição.
'''

'''
A função render combina um template com um contexto e retorna uma resposta HTTP que será enviada de volta ao navegador.
    O primeiro parâmetro, request, é o objeto de requisição que você passou para a view.
    O segundo parâmetro é o caminho para o arquivo de template, no seu caso, 'contact/index.html' (cuidado com o espaço no caminho que pode causar erro).
    O terceiro parâmetro (opcional) seria um dicionário contendo o contexto (dados) que você deseja passar para o template.
'''
# Isso retornará o template index.html dentro da pasta contact, localizada em um dos diretórios de templates definidos no settings.py.
def index(request):
    return render (
        request,
        'contact/index.html'
    )
