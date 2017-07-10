from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.views.generic import View
from .models import Patient
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = 'patient/index.html'

    def get_queryset(self):
        return Patient.objects.all()

class DetailView(generic.DetailView):
    model=Patient
    template_name = 'patient/detail.html'

class UserFormView(View):
    form_class = UserForm
    template_name = 'patient/registration_form.html'
    
    #displays blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    #process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
  
            user = form.save(commit=False)
            #clean (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # return User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:                
                    login(request, user)
                    return redirect('patient:index')
        return render(request, self.template_name, {'form': form})



def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'patient/login.html', context)



def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('patient:index')
            else:
                return render(request, 'patient/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'patient/login.html', {'error_message': 'Invalid login'})
    return render(request, 'patient/login.html')
