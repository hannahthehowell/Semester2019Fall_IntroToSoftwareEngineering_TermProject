from django.urls import path
import django.contrib.auth.views as auth_views
from django.urls import reverse_lazy
from django.views.generic.base import RedirectView
from django.contrib.auth.decorators import login_required
from .decorators import anon_required, redirected_from
from django.urls import reverse
from . import views

app_name = 'auction'
urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('auction:home'))),
    path('home/', login_required(views.home), name='home'),
]

# Account management urls
urlpatterns += [
    path('login/', auth_views.LoginView.as_view(template_name='auction/account/login.html', redirect_authenticated_user=True),
         name='login'),
    path('logout/', login_required(auth_views.logout_then_login),
         name='logout'),
    path('signup/', anon_required(views.SignUpView.as_view()),
         name='signup'),
    path('account/', login_required(views.ViewAccountView.as_view()),
         name='account'),
    path('account/edit/', login_required(views.EditAccountView.as_view()),
         name='edit_account'),
    path('account/change_password/', login_required(auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('auction:change_password_done'))),
         name='change_password'),
    path('account/change_password/done/', redirected_from('auction:change_password')(auth_views.PasswordChangeDoneView.as_view(template_name='auction/account/change_password_done.html')),
         name='change_password_done'),
    path('account/reset_password/', auth_views.PasswordResetView.as_view(email_template_name='auction/account/temp_reset_password.html', success_url=reverse_lazy('auction:reset_password_done')),
         name='reset_password'),
    path('account/reset_password/done/', redirected_from('auction:reset_password')(auth_views.PasswordResetDoneView.as_view()),
         name='reset_password_done'),
    path('account/reset_password/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('auction:reset_password_complete')),
         name='reset_password_confirm'),
    path('account/reset_password/complete/', redirected_from('auction:reset_password_confirm')(auth_views.PasswordResetCompleteView.as_view()),
         name='reset_password_complete'),
]

urlpatterns += [
  path('create_auction/', login_required(views.create_auction), name='create_auction'),
  path('enter_local_code/', login_required(views.enter_local_code), name='enter_local_code'),
  path('auction-detail/<int:pk>', views.auction_detail, name='auction-detail')
]
