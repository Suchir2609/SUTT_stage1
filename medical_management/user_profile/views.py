from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Account
from users.forms import ProfileUpdateForm, AccountUpdateForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView


def profile(request):
    pfile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your Account has been successfully updated! ')
            return redirect('patient-profile')
    else:
        p_form = ProfileUpdateForm()
    context = {'pfile': pfile, 'p_form':p_form}

    return render(request, 'users/patient_profile.html', context)


class AccountCreateView(LoginRequiredMixin, CreateView):
    model = Account
    fields = ['patient', 'bill', 'status']
    template_name = 'users/account_create.html'
    success_url = '/staff_home'


class AccountListView(ListView):
    model = Account
    template_name = 'users/accounts.html'
    context_object_name = 'accounts'


def account_update(request, pk):
    account = get_object_or_404(Account, pk=pk)
    if request.method == 'POST':
        form = AccountUpdateForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your Account has been successfully updated! ')
            return redirect('patient-home')
    else:
        form = AccountUpdateForm(instance=account)
    return render(request, 'users/account_update.html', {'form': form})
