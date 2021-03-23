from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
from .models import Rental
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView

# Create your views here.

# def home(request):
#   obj = Rental.objects.all()
#   context = {'obj':obj}
#   return render(request,'index.html',context)


class home(ListView):
  model=Rental
  template_name='index.html'
  context_object_name='obj'
  queryset = Rental.objects.order_by('-dt')
  paginate_by = 10


class detail(DetailView):
  model=Rental
  context_object_name='obj'
  template_name='detail.html'
  # queryset = Rental.objects.all()



def profile(request):
  context = {}
  return render(request,'profile.html',context)


def login(request):
  if request.method =='POST':
    uname = request.POST['username']
    pwd = request.POST['password']

    user = auth.authenticate(username=uname,password=pwd)
    if user is not None:
      auth.login(request,user)
      messages.success(request,', Logged in successfully!')
      return redirect('/')

    else:
      messages.error(request,'invalid credentials')
      return redirect('login')
  else: 
    return render(request,'registration/login.html')


def logout(request):
  auth.logout(request)
  messages.success(request,', logged out successfully!')
  return redirect('/')



def register(request):
  if request.user.is_authenticated:
    return redirect('home')
  elif request.method == 'POST':
    fname = request.POST['fname']
    lname = request.POST['lname']
    uname = request.POST['uname']
    email = request.POST['email']
    pwd1 = request.POST['pwd1']
    pwd2 = request.POST['pwd2']

    if pwd1==pwd2:
      if User.objects.filter(username=uname).exists():
          messages.warning(request,', Username Taken!')
          return redirect('register')
      elif User.objects.filter(email=email).exists():
          messages.warning(request,', Email Taken!')
          return redirect('register')
      else:    
        user = User.objects.create_user(username=uname,password=pwd1,email=email,first_name=fname,last_name=lname)
        user.save()
        auth.login(request,user)
        messages.success(request,',  Registered and logged in successfully!')
        return redirect('/')
    else:
      messages.error(request,'Password not matching!')
      return redirect('register')  
  else:
    return render(request,'registration/register.html')



class PropertyCreateView(SuccessMessageMixin,CreateView):
    model = Rental
    fields = ('name', 'img','desc','price','type','reg_agent')
    template_name = 'create.html'
    success_url = '/'
    success_message = "%(name)s was created successfully"


class update(UserPassesTestMixin,SuccessMessageMixin,UpdateView):
    model = Rental
    fields = ('name', 'img','desc','price','type','reg_agent')
    template_name = 'update.html'
    success_url = '/'
    success_message = "%(name)s was updated successfully"
    def test_func(self):
      obj = self.get_object()
      return obj.reg_agent == self.request.user


class delete(UserPassesTestMixin,SuccessMessageMixin,DeleteView):
    model = Rental
    success_url = '/'    
    template_name = 'delete.html'
    success_message = "%(name)s was deleted successfully"
    login_url = 'login'
    def test_func(self):
      obj = self.get_object()
      return obj.reg_agent == self.request.user


    
