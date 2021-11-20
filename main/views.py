from django.shortcuts import render, redirect, reverse
from django.template.defaultfilters import title
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from .models import VendorProfile, Brew
from .forms import VendorSignupForm, VendorLoginForm, VendorProfileForm, VendorProfilePictureForm




from django.core.mail import EmailMessage
from .forms import CustomUserCreationForm
from django.contrib import messages

# Create your views here.


class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vendorsignupform"] = CustomUserCreationForm()
        context["vendorloginform"] = VendorLoginForm()
        return context

# # # Vendor Login

class VendorLogin(View):
    
    def get(self, request):
        form = VendorLoginForm()
        vendorsignupform = CustomUserCreationForm()
        context = {"vendorloginform": form, "vendorsignupform": vendorsignupform}
        return render(request, "vendor_registration/vendor_login.html", context)
    
    def post(self, request):
        company_name = request.POST['company_name']
        password = request.POST['password1']
        user = authenticate(request, company_name=company_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('vendor_profile', pk=user.id)
        else:
            form = VendorLoginForm()
            vendorsignupform = CustomUserCreationForm()
            error = "Invalid Credentials" 
            context = {"vendorloginform": form, "vendorsignupform": vendorsignupform, "error": error}
            return render(request, "vendor_registration/vendor_login.html", context)
        
            
# # # Vendor SignUp

class VendorSignup(View):
    
    def get(self, request):
        vendorloginform = VendorLoginForm()
        form = CustomUserCreationForm()
        context = {"vendorsignupform": form, "vendorloginform": vendorloginform}
        return render(request, "vendor_registration/vendor_signup.html", context)
    
    def post(self, request):
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile', pk=self.request.user.pk)
        else:
            vendorloginform = VendorLoginForm()
            context = {"vendorsignupform": form, "vendorloginform": vendorloginform}
            return render(request, "vendor_registration/vendor_signup.html", context)
          
# # # Vendor
          
class VendorProfilePage(TemplateView):
    model = VendorProfile
    template_name = "vendor_profile.html"
    ordering = ['created_at']

    def get_context_data(self, pk, **kwargs):
        vendorprofile = VendorProfile.objects.get(pk=pk)
        context = super().get_context_data(**kwargs)
        context["vendorprofile"] = vendorprofile
        context["posts"] = vendorprofile.post.all().order_by('-created_at')
        return context

class VendorProfileUpdate(UpdateView):
    model = User
    form_class = VendorProfileForm
    template_name = "vendor_profile_update.html"
    
    def get_success_url(self):
        return reverse('vendorprofile', kwargs={'pk': self.object.pk})

class VendorProfilePictureUpdate(UpdateView):
    model = VendorProfile
    form_class = VendorProfilePictureForm
    template_name = "vendor_profile_picture_update.html"
    
    def get_success_url(self):
        return reverse('vendorprofile', kwargs={'pk': self.object.pk})
      
      
# # # Brews      

class BrewList(TemplateView):
    template_name = "brew_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")

        if name != None:
            context["brews"] = Brew.objects.filter(name__icontains=name)
        else:
            context["brews"] = Brew.objects.all()
        return context

class BrewDetail(TemplateView):
    template_name = "brew_details.html"

    def get_context_data(self, slug, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")

        if name != None:
            context["brews"] = Brew.objects.filter(name__icontains=name)
            context["brew_details"] = Brew.objects.get(slug=slug)
        else:
            context["brews"] = Brew.objects.all()
            context["brew_details"] = Brew.objects.get(slug=slug)
        return context
