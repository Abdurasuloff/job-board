from django.shortcuts import render, redirect
from accounts.models import User
from .models import Massage
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.

def massage(request, username):
      user = request.user
      user2  = User.objects.get(username=username)
      massages = Massage.objects.filter(Q(sender=user, receiver=user2)|Q(sender=user2, receiver=user)).order_by('-id')
      Massage.objects.filter(sender=user, receiver = user2, is_seen = False).update(is_seen=True)

      if request.method == "POST":
            if request.POST.get("massage") or request.POST.get("file"):
                  if request.POST['massage']:
                        massage = request.POST['massage']
                  else:
                        massage = "" 
                  if  request.POST['file']: 
                        file = request.POST['file']
                  else:
                        file = None    
                  Massage.objects.create(
                        sender = user,
                        receiver = user2,
                        massage = massage,
                        file = file
            
                  )
                  return redirect('chat', user2.username)
      return render(request, 'massage/chat.html')            



      

