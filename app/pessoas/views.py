from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm, PessoaForm, DocumentoForm
from .models import Documento

def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        pessoa_form = PessoaForm(request.POST)
        if user_form.is_valid() and pessoa_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            pessoa = pessoa_form.save(commit=False)
            pessoa.user = user
            pessoa.save()
            return redirect('login')
    else:
        user_form = UserRegisterForm()
        pessoa_form = PessoaForm()
    return render(request, 'register.html', {'user_form': user_form, 'pessoa_form': pessoa_form})

def dashboard(request):
    documentos = Documento.objects.filter(pessoa__user=request.user)
    return render(request, 'dashboard.html', {'documentos': documentos})

def upload_documento(request):
    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.pessoa = request.user.pessoa
            doc.save()
            return redirect('dashboard')
    else:
        form = DocumentoForm()
    return render(request, 'upload.html', {'form': form})
