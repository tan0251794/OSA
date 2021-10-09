from django.contrib.admin.options import csrf_protect_m
from accounts.forms import AccountForm
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

# @csrf_protect
# def account(request):
#     form = AccountForm()

#     if request.method == 'POST':
#         form = AccountForm(request.POST)
#     if form.is_valid():
#         form.save()
#         messages.success(request, 'added new user')
#         form.clean()
#         return redirect('.')
#     return render(request, 'signup.html', {'form': form})


# def home_view(request):
#     return render(request, 'home.html')