from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import  render
from django.views import generic
from login.forms import UserRegistrationForm, UserEditForm, AvatarForm
from django.contrib.auth.decorators import login_required
from .models import Avatar, Usuario
from django.contrib.auth.models import User

# Create your views here.
@login_required
def UpdateProfile(request):
    
    usuario = request.user  #instanciamos el login
    
    #si es POST hago lo mismo que agregar.
    if request.method == "POST":
        form =UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            #Datos a modificar
            usuario.email = informacion['email']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            #usuario.avatar = informacion['avatar']
            usuario.descripcion = informacion['descripcion']
            usuario.web_link = informacion['web_link']
            usuario.save()

            return render(request, 'index.html')
    else:
        #Creo el formulario que voy a modificar.
        form = UserEditForm(initial= { 'email':usuario.email, 'first_name':usuario.first_name,  'last_name':usuario.last_name})
    return render(request, 'profile_detail.html', {"form":form, "usuario":usuario})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username = username, password = password)

            if user is not None:
                login(request, user)
                
                #return render(request, '', {"mensaje":f"Bienvenido {user}"})
                return render(request, 'index.html')
            else:
                #return render(request, '', {"mensaje":"Error, datos incorrectos"})
                return HttpResponse("Error, datos incorrectos")
        else:
            #return render(request, '', {"mensaje":"Error, formulario erróneo"})
            return HttpResponse("Error, formulario erróneo")
        
    form = AuthenticationForm()

    return render(request, 'login.html', {'form':form})

def register(request):

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'registration/register_confirm.html', {'message': f"Usuario {username} Creado"})
    else:
        form = UserRegistrationForm()
    
    return render(request, 'registration/register.html', {"form": form})

class UserDetail(generic.ListView):
    queryset = Usuario.objects.all
    template_name = 'profile.html'

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)        
            avatar = Avatar(user=u, image=form.cleaned_data['image'])
            avatar.save()
            return render(request, 'index.html')
    else:
        form = AvatarForm()
    return render(request, "avatar_form.html", {"form":form})