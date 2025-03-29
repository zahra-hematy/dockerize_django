from django.urls import path, include, reverse_lazy
from .views import(
    HomeView,
    CreateImageView, 
    SignupView, 
    LoginView, 
    DetailHomeView,
    DownloaddetailView,
    download_image,
    # LogoutView,
)
from django.conf import settings  # new
from django.conf.urls.static import static 
from django.contrib.auth.views import (
    LoginView,
    LogoutView, 
    PasswordResetView,
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from upimg import views
from django.contrib.auth import views as auth_views 

app_name = "upimg"
urlpatterns = [

    path('', HomeView.as_view(), name='home'),
    path('add/', CreateImageView.as_view(), name='add' ),
    path('<int:pk>/', DetailHomeView.as_view(), name='detail' ),
    # path('<int:pk>/download/', DownloaddetailView.as_view(), name='download' ),



    path('<int:pk>/download/', download_image, name='download_image'),

    # path('ratings/', include('star_ratings.urls', namespace='ratings')),


    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.SignupView, name="register"),
    path('password_reset/', PasswordResetView.as_view(template_name='registration/password_reset.html', 
    html_email_template_name='registration/password_reset_email.html'), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done1'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html',
    success_url=reverse_lazy('upimg:password_reset_complete')),name='password_reset_confirm'),
    path('password_reset_complete/',PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),
]














    # path('login/', UserLoginAPIView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('register/', views.SignupView, name="register"),
    # path(r'^api-token-auth/', obtain_jwt_token),
    # path(r'^api-token-refresh/', refresh_jwt_token),
    # path(r'^api-token-verify/', verify_jwt_token),
    # path(r'^register/$', UserCreateAPIView.as_view(), name='register'),


    

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)