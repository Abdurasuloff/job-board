from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Vacancy, Category, Apply
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from worker.models import Hire




#-------------------HOME PAGE--------------------------
def index(request):
      vacancies = Vacancy.objects.all()

      return render(request, 'index.html', {'vacancies':vacancies})

#---------------TO CREATE NEW VACANCY ADS------------------      

class NewVacancy(LoginRequiredMixin,  CreateView):
    model = Vacancy
    template_name = 'job/new-vacancy.html'
    fields = ('title','description','category','cost','cost_for','work_type', 'location', 'needed_experience', 'tags',  'company_name', 'tagline', 'company_email', "company_logo"   )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

   
#-----------------VACANCY DETAIL---------------------------


@login_required
def vacancy_detail(request, pk):
    vacancy  = Vacancy.objects.get(id=pk)

    #If vacancy sended by this user
    sended = False
    apply = Apply.objects.filter(vacancy = vacancy, employer = vacancy.author , worker = request.user)
    if apply:
        sended = True
    else:
        sended = False
        
    #send vacancy   
    if request.method == "POST":
        sended = True
        if request.POST['resume']:
            resume = request.POST['resume']
        else:
            resume = request.user.resume    
            
        massage = request.POST['massage']
            
        Apply.objects.create(
            vacancy = vacancy,
            employer = vacancy.author,
            worker = request.user,
            resume = resume ,
            massage = massage,
        )
        
        
    return render(request, 'job/vacancy-detail.html', {'vacancy':vacancy, 'sended':sended})    

#------------------MANAGE VACANCIES-------------------------

@login_required
def manage_vacancies(request):
    user = request.user
    massage=""
    #If user is Employer
    if user.is_employer == True and user.is_worker==False :
        my_ads = Vacancy.objects.filter(author=user).order_by("-id")

        #Count applications to this vacancy
        for ad in my_ads:
            ad.applications = Apply.objects.filter(vacancy = ad, ).count()
            ad.save()

        #Mark filled function    
        if request.method == "POST":
            id = request.POST.get['id']
            a = Vacancy.objects.get(id=id)
            a.is_closed=True
            a.save()
    
    #If user is worker
    elif user.is_worker==True and user.is_employer == False:
        massage = "You are in worker account, so you allowed to enter to this page!"

    #If user are not both of this    
    else:
        massage="Something wrong with your account"  
    
    try:
        context = {'my_ads':my_ads}
    except:
        context = {}

    context.update({'massage':massage})

    return render(request, 'job/manage-jobs.html', context)    

#------------------MANAGE VACANCIES DETAIL------------------

def show_applications(request, pk):
    user = request.user   
    massage = ""

    #if user is employer
    if user.is_employer == True and user.is_worker==False :

        try:
            vacancy = Vacancy.objects.get(id=pk, author=user)
            applications = Apply.objects.filter(vacancy=vacancy).order_by("-id")
            applications.update(new=False)
        except:
            massage="Vacancy not found or you are not owner of this vacancy"


    #if user is worker   
    elif user.is_worker==True and user.is_employer == False:
        massage = "You are in worker account, so you allowed to enter to this page!"

    #user is not both of this    
    else:
        massage="Something wrong with your account"
     
    try: 
        context = {'applications':applications, "vacancy":vacancy} 
    except:  
        context = {}

    context.update({'massage':massage})    

    return render(request, 'job/manage-applications.html', context)   


#----------------------EDIT VACANCIES ---------------------------


class EditVacancy(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = Vacancy
    template_name = 'job/edit-vacancy.html'
    fields = ('title','description','category','cost','cost_for','work_type', 'location', 'needed_experience', 'tags',  'company_name', 'tagline', 'company_email', "company_logo", 'deleted'  )

    
    # if user is owner run this view
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user



#-------------------MANAGE HIRE REQUESTS----------------

@login_required
def hire_requests(request):
    user = request.user
    hire = Hire.objects.filter(employer=user, deleted=False)
    return render(request, 'job/hire-request.html', {"hire":hire})


#------------------TO SHOW CATEGERIES IN ALL PAGES -------------

def categories(request):
    categories = Category.objects.all()
    return {"categories":categories}



def category_jobs(request, pk):
    category = Category.objects.get(id=pk)
    vacancies = Vacancy.objects.filter(category=category)
    num  = vacancies.count()
    return render(request, 'job/category-jobs.html', {'vacancies':vacancies, "cat":category, 'num':num})


