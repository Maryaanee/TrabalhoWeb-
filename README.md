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

