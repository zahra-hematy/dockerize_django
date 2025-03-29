# from django.shortcuts import render
# from django.views.generic import View
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.conf import settings  # new
# from . import forms

# # Create your views here.

# class LoginView(View, LoginRequiredMixin):
#     template_name = 'registrations/login.html'
#     form_class = forms.LoginForm
#     def get(self, request):
#         form = self.form_class
#         message = ''
#         return render(request, self.template_name, context={ 'form': form, 'message':message})

#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             user = athenticate(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password'],
                
#             )
#     if user is not None:
#         login(request, user)
#         return redirect('home')
#     message = 'Login failed!'
#     return render(request, self.template_name, context={'form': form, 'message':message})
# def SignupView(request):
#     form  = forms.SignupForm()
#     if request.method == 'POST':
#         form = forms.SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect(settings.LOGIN_REDIRECT_URL)
#     return render(request, 'registrations/register.html', context={'form': form})