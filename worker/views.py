from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, DeleteView
from .models import User, Category, Resume, Hire
from job.models import Apply
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
# Create your views here.

#Make worker public

@login_required
def addresume(request):

    massage=''
    owner = request.user
    
    if owner.is_employer==True:
      massage = 'You are not in worker account so you can not create a resume'
    elif owner.is_public == True:
      massage = 'You have already created resume. You can change this resume in "My account" section. '
    else:

      if  request.method == "POST":


            category_id = request.POST['category']
            category = Category.objects.get(id = category_id)
            title = request.POST['title']
            description = request.POST['description']
            url = request.POST['url']
            cost = request.POST['cost']
            cost_for = request.POST['cost_for']

            Resume.objects.create(
           
                owner = owner,
                title = title,
                category = category ,
                description = description,
                url = url,
                cost = cost,
                cost_for = cost_for,
                )
            owner.is_public = True
            owner.save()   
            redirect('index')

    return render(request, "worker/add-resume.html", {"massage":massage}) 
      

#In category section worker list 

def category_workers(request, pk):
      category = Category.objects.get(id=pk)
      resumes = Resume.objects.filter(category=category)

      return render(request, "worker/category-workers.html", {"category": category, "resumes":resumes})


#send hire request
def hire(request, pk):
      massage=''
      user = request.user
      # check is it available or 404
      try:
        resume = Resume.objects.get(id=pk)
      except:
        resume={}  
        massage="Does not exist"

      #check is user employer
      if user.is_employer==True:

        #check is  hire request sended by this user
        try:
          Hire.objects.get(resume=resume, employer=user)
          massage = "You have already sended hire request you chan change or check it in your dashboard"
        except:  
            if request.method == "POST":
              about_company = request.POST['about_company']
              hire_massage = request.POST['hire_massage']

              Hire.objects.create(
                resume = resume,
                worker = resume.owner,
                employer = user,
                about_company = about_company,
                massage = hire_massage,

              )
              return redirect("index")


      #if user's account is not employer            
      else:
            massage = 'You are not in employer account, so you can not hire workers'

      return render(request, 'worker/hire.html', {'massage':massage, 'resume':resume})      

@login_required
def my_applications(request):
  user = request.user
  applications = Apply.objects.filter(worker=user)
  
  return render(request, 'worker/my-applications.html', {'applications':applications})
  

def manage_hire_requests(request):
  user = request.user
  hire = Hire.objects.filter(worker = user, deleted=False)
  if request.method == "POST":
    status = request.POST['status']
    id = request.POST['id']
    hire_request = Hire.objects.filter(id=id, deleted=False, worker=user)
    hire_request.update(
      status=status,
    )
    
    return redirect("manage-hire-requests")


  return render(request, "worker/manage-hire-requests.html", {'hire':hire})



def edit_resume(request):
  user = request.user
  massage = ''
  resume_data = Resume.objects.get(owner=user)
  if request.user.is_worker==True:
    resume = Resume.objects.filter(owner=user)
    if request.method == "POST":
      title = request.POST['title']
      description = request.POST['description']
      category_id = request.POST['category']
      category = Category.objects.get(id = category_id)
      cost = request.POST['cost']
      cost_for = request.POST['cost_for']
      url = request.POST['url']
      resume.update(title=title, description=description, category=category, cost=cost, cost_for=cost_for, url=url)
     

      return redirect('index')
  else:
    massage = 'Does not exist'
  return render(request, "worker/edit-resume.html", {"resume":resume_data, "massage":massage})  
    
@login_required
def delete_resume(request, pk):
  resume = Resume.objects.filter(id=pk)
  resume_a = Resume.objects.get(id=pk)
  if request.method == "POST":
    user = resume_a.owner
    user.is_public = False
    user.save()
    resume.delete()
    return redirect('index')
  return render(request, 'worker/delete-resume.html')  

