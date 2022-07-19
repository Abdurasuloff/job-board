from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.decorators import login_required
from job.models import Vacancy
from worker.models import Resume
from .models import User


# Create your views here.

class SignUpView(CreateView):
    model = User
    fields = ('first_name', 'last_name', 'username', 'email',  'password')
    template_name = 'registration/step_1.html'


class SignUp2(DetailView):
      model = User
      template_name = "registration/step_2.html"

def worker_signup(request, pk):
      
      user = User.objects.get(id=pk)
      if request.method == "POST":
            User.objects.filter(id=pk).update(
                  is_worker = True,
                  avatar = request.POST['avatar'],
                  phone_number = request.POST['phone_number'],
                  location = request.POST['location'],
                  resume = request.POST['resume'],
            )
            redirect('/accounts/login')
           
      return render(request, 'registration/worker_signup.html', {"user":user})

def employer_signup(request, pk):
    
      user = User.objects.get(id=pk)
      if request.method == "POST":
            User.objects.filter(id=pk).update(
                  is_employer = True,
                  avatar = request.POST['avatar'],
                  phone_number = request.POST['phone_number'],
                  company_name = request.POST['company_name'],
            )
            redirect('/accounts/login')

      return render(request, 'registration/employer_signup.html', {"user":user}) 

def profile(request, username):
      user = User.objects.get(username=username)
      try: 
            resume = Resume.objects.get(owner=user) 
      except:
            resume=''  

      owner = False
      if user == request.user :
            owner=True  

      vacancies = Vacancy.objects.filter(author=user)
      
      return render(request, 'accounts/profile.html', {"resume":resume, "owner":owner, 'vacancies':vacancies})


@login_required
def editprofile(request):
      userr = request.user
      user = User.objects.filter(username = request.user.username)

      if request.method == "POST":
            #avatar phone_number location resume company_name 
            username = request.POST['username']
            email = request.POST['email']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            phone_number = request.POST['phone_number']
            location = request.POST['location']
            if request.POST['resume']:
                  resume = request.POST['resume']
            else:
                  resume = request.user.resume 

            if request.POST['resume']:
                  company_name = request.POST['company_name']
            else:
                  company_name = request.user.company_name    
            
            user.update(
                  username = username,
                  email=email,
                  first_name= first_name,
                  last_name = last_name,
                  phone_number = phone_number,
                  location = location,
                  resume = resume,
                  company_name=company_name

            ) 
               

            return redirect('profile' , userr.username)      
      return render(request, "accounts/edit-profile.html", {"user":userr})            




