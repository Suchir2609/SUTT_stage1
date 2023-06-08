from django.urls import path
from . import views


urlpatterns = [
    path('patient_profile/', views.profile, name='patient-profile'),
    # path('patient_profile_update/', views.profile, name='patient-profile-update'),
    path('account_create/', views.AccountCreateView.as_view(), name='account-create'),
    path('account_list/', views.AccountListView.as_view(), name='account-list'),
    path('account/<int:pk>/update/', views.account_update, name='account-update'),
]