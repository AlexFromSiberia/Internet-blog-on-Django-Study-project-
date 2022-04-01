from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    # reg new user
    if request.method != 'POST':
        # show empty form
        form = UserCreationForm()
    else:
        # process filled form
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('learning_logs:index')

    # show empty or invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)
















