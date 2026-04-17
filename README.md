# TrabalhoWeb-Para criar e utilizar o **Django Forms**, o processo segue uma lógica de três passos: definir a classe do formulário, processá-la na View e exibi-la no Template. Esse método é superior ao HTML puro porque o Django cuida da validação de dados e da segurança automaticamente.
Aqui está o passo a passo técnico:
### 1. Criar o arquivo forms.py
Dentro da pasta do seu app (onde está o models.py), crie um novo arquivo chamado forms.py. Nele, você define quais campos o seu formulário terá.
```python
from django import forms

class SugestaoForm(forms.Form):
    nome = forms.CharField(label="Seu Nome", max_length=100)
    email = forms.EmailField(label="E-mail")
    comentario = forms.CharField(label="Comentário", widget=forms.Textarea)

```
### 2. Configurar a View (views.py)
A função na view precisa lidar com dois momentos: quando o usuário entra na página (método GET) e quando ele envia os dados (método POST).
```python
from django.shortcuts import render
from .forms import SugestaoForm

def enviar_sugestao(request):
    if request.method == 'POST':
        form = SugestaoForm(request.POST) # Preenche o form com os dados enviados
        if form.is_valid():
            # Se os dados forem válidos, você pode acessá-los:
            nome = form.cleaned_data['nome']
            # Aqui você faria algo com o dado (salvar no banco, enviar e-mail, etc)
            return render(request, 'sucesso.html')
    else:
        form = SugestaoForm() # Cria um formulário vazio para o método GET

    return render(request, 'contato.html', {'form': form})

```
### 3. Exibir no Template (.html)
No seu arquivo HTML, você utiliza a DTL para renderizar o formulário. O Django transforma sua classe Python em campos HTML de forma automática.
```html
<form method="post">
    {% csrf_token %} {{ form.as_p }} <button type="submit">Enviar Dados</button>
</form>

```
### Por que usar o Django Forms em vez de HTML manual?
 * **Renderização Automática:** O Django gera o HTML correto para cada tipo de dado (ex: EmailField vira um <input type="email">).
 * **Validação de Dados:** Se o usuário deixar um campo obrigatório vazio ou digitar um e-mail inválido, o Django recarrega a página automaticamente com mensagens de erro, sem você precisar escrever código extra.
 * **Segurança (CSRF):** Ao usar o {% csrf_token %}, o Django garante que os dados estão vindo do seu próprio site, protegendo contra invasões.
 * **Limpeza de Dados:** O atributo cleaned_data garante que o que você está recebendo no Python é um dado seguro e já convertido para o formato correto (ex: transforma uma string de data em um objeto datetime do Python).
Se você já tiver um **Model** criado e quiser que o formulário seja exatamente igual aos campos do seu banco de dados, você pode usar o **ModelForm**, que simplifica ainda mais esse processo. Quer que eu te mostre como converter esse exemplo para um ModelForm?
