from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Image
from .forms import ImageForm
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings  # new
from . import forms
from django.contrib.auth import login
from django.views.generic import ListView, CreateView, DetailView
from django.contrib import messages
from django.contrib.auth import get_user_model

# Create your views here.

class HomeView(ListView):
    model = Image
    template_name = 'home.html'

class DetailHomeView(DetailView):
    model = Image
    template_name = 'detail.html'
    def get_queryset(self):
        return self.model.objects.filter(
            user=self.request.user,
            id=self.kwargs['pk']
        )
class DownloaddetailView(View):
    def get(self, request, *args, **kwargs):
        image = Image.objects.get(pk=self.kwargs['pk'])
        image_buffer = open(image.photo.url, "rb").read()
        content_type = magic.from_buffer(image_buffer, mime=True)
        response = HttpResponse(image_buffer, content_type=content_type);
        response['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(image.photo.url)
        return response


def download_image(request, pk):
    # Assuming you have a model named Image with a FileField named 'image'
    image = get_object_or_404(Image, pk=pk)
    image_path = image.photo.url

    # Open the image file
    with open(image_path, 'rb') as f:
        response = FileResponse(f)
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(os.path.basename(image_path))
        return response


class CreateImageView(CreateView):
    model = Image
    form_class = ImageForm
    template_name = 'image_create.html'
    success_url = reverse_lazy('home')

class LoginView(View, LoginRequiredMixin):
    template_name = 'registrations/login.html'
    form_class = forms.LoginForm
    def get(self, request):
        form = self.form_class
        message = ''
        return render(request, self.template_name, context={ 'form': form, 'message':message})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = athenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            message = 'Login failed!'
        return render(request, self.template_name, context={'form': form, 'message':message})


# User = get_user_model()
def SignupView(request):
    form  = forms.RegistrationForm()
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'شما با موفقیت ثبت نام شده اید.')
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            messages.error(request, 'نام کاربری شما معتبر نیست')
    else:
        form  = forms.RegistrationForm()
    return render(request, 'registration/register.html', context={'form': form})

