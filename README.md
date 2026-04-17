Dominar o Django é um excelente passo para quem já tem uma base de programação. O framework segue a filosofia "batteries included", o que significa que ele já traz quase tudo o que você precisa para criar um site robusto.
Abaixo, preparei um roteiro focado no seu ambiente Windows/VS Code, seguindo a lógica de aprendizado do CS50.
## 1. Configurando o Ambiente Virtual no Windows
No VS Code, abra o terminal (Ctrl + ') e execute os seguintes comandos:
 1. **Criar o ambiente:** python -m venv venv
 2. **Ativar o ambiente:** .\venv\Scripts\activate
 3. **Instalar Django:** pip install django
 4. **Iniciar o projeto:** django-admin startproject meu_site .
 5. **Criar um App:** python manage.py startapp principal
## 2. Model + View + Template (MVT)
O Django usa o padrão **MVT**, que é uma variação do MVC. Entender essa arquitetura é a chave para o CS50:
 * **Model:** Define a estrutura dos dados (Banco de dados).
 * **View:** A "lógica". Ela recebe uma requisição e decide o que enviar de volta.
 * **Template:** A parte visual (HTML) que o usuário vê.
## 3. Caminhos e HTML "dentro" do Python
No início, você pode retornar HTML diretamente da view, mas isso não é escalável.
No arquivo views.py do seu app:
```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bem-vindo à página inicial!</h1>")

```
Para registrar caminhos (URLs), você cria um arquivo urls.py dentro do seu app e o conecta ao urls.py principal do projeto.
## 4. Django Template Language (DTL)
A DTL permite que você coloque lógica dentro do HTML. Em vez de usar HttpResponse, usamos render.
### Estruturas de Repetição
Se você passar uma lista de nomes da View para o Template, pode exibi-los assim:
```html
<ul>
  {% for nome in lista_nomes %}
    <li>{{ nome }}</li>
  {% empty %}
    <li>Nenhum nome encontrado.</li>
  {% endfor %}
</ul>

```
## 5. Formulários: HTML puro vs Django Forms
O Django facilita muito a manipulação de dados enviados pelo usuário.
### Formulário HTML Manual
Você cria a tag <form> no HTML e, na View, captura os dados usando request.POST.get('nome_do_campo').
### Django Forms (O jeito certo)
Você define uma classe em um novo arquivo forms.py:
```python
from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(label="Seu nome", max_length=100)
    mensagem = forms.CharField(widget=forms.Textarea)

```
**Vantagens:**
 * Validação automática de dados.
 * Geração automática do HTML no template apenas usando {{ form.as_p }}.
 * Proteção contra ataques CSRF (Cross-Site Request Forgery) apenas adicionando {% csrf_token %} dentro do formulário.
## Resumo de Comandos Úteis
| Ação | Comando |
|---|---|
| Criar Migrações | python manage.py makemigrations |
| Aplicar ao Banco | python manage.py migrate |
| Rodar o Servidor | python manage.py runserver |
| Criar Admin | python manage.py createsuperuser |
Qual desses tópicos você gostaria de aprofundar primeiro criando um exemplo prático de código?


Como a atividade pede **persistência em uma lista global** (em memória) e o uso de **Django Forms**, não precisaremos configurar um banco de dados (models.py) agora. Vamos focar na lógica de visualização e no formulário.
Aqui está o passo a passo para o seu VS Code:
### 1. Criar o Formulário (forms.py)
Crie este arquivo dentro da pasta do seu app para definir os campos solicitados na imagem (Evento e Local).
```python
from django import forms

class EventoForm(forms.Form):
    nome_evento = forms.CharField(label="Evento", max_length=100)
    local_evento = forms.CharField(label="Local", max_length=100)

```
### 2. A Lógica com Lista Global (views.py)
Aqui vamos criar a lista no topo do arquivo para salvar os dados temporariamente, conforme a instrução técnica da prova.
```python
from django.shortcuts import render, redirect
from .forms import EventoForm

# Lista global para persistência em memória
eventos_db = [
    {'evento': 'Seminário de estatística', 'local': 'Laboratório 01'},
    {'evento': 'Semana da TI', 'local': 'Auditório'},
]

def home(request):
    # Lista os eventos ativos na Dashboard
    return render(request, 'home.html', {'eventos': eventos_db})

def novo_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            # Extrai os dados e adiciona na lista global
            novo = {
                'evento': form.cleaned_data['nome_evento'],
                'local': form.cleaned_data['local_evento']
            }
            eventos_db.append(novo)
            return redirect('home') # Volta para a lista após cadastrar
    else:
        form = EventoForm()
    
    return render(request, 'novo.html', {'form': form})

```
### 3. Criando os Templates (HTML)
#### home.html (A Dashboard)
Use a **DTL (Django Template Language)** para criar a tabela.
```html
<h2>Eventos em Destaque</h2>
<table border="1">
    <thead>
        <tr>
            <th>Evento</th>
            <th>Local</th>
        </tr>
    </thead>
    <tbody>
        {% for e in eventos %}
        <tr>
            <td>{{ e.evento }}</td>
            <td>{{ e.local }}</td>
        </tr>
        {% endfor %}
    </tbody>
</table>
<br>
<a href="{% url 'novo' %}">Cadastrar Novo Registro</a>

```
#### novo.html (O Formulário de Registro)
Aqui usamos o {% csrf_token %} por segurança e o {{ form.as_p }} para renderizar os campos.
```html
<h2>Novo Registro</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Confirmar Cadastro</button>
</form>
<br>
<a href="{% url 'home' %}">Cancelar e Voltar</a>

```
### 4. Configurar os Caminhos (urls.py)
No arquivo urls.py do seu app, conecte as páginas:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('novo/', views.novo_evento, name='novo'),
]

```
### Resumo do que foi aplicado:
 1. **Django Templates:** Usamos {% for %} para listar os eventos.
 2. **Django Forms:** Criamos a classe EventoForm para validar a entrada.
 3. **MVT:** A View faz a ponte entre a lista (Model improvisado) e o HTML.
 4. **Persistência:** A variável eventos_db guarda os nomes enquanto o servidor estiver rodando.
**Dica para a entrega:** Como a prova pede o repositório no GitHub, certifique-se de que o arquivo .gitignore ignore a pasta venv e que você tenha feito o pip freeze > requirements.txt antes de subir o código!

