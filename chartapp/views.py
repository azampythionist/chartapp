from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors.as_json()}, status=400)
    else:
        form = UserCreationForm()
    return render(request, 'chartapp/registration_form.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({'status': 'ok'})
        return JsonResponse({'status': 'error', 'errors': form.errors.as_json()}, status=400)
    else:
        form = AuthenticationForm()
    return render(request, 'chartapp/login_form.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'chartapp/home.html')

@login_required
def chart(request):
    chart_type = request.session.get('chart_type')
    if not chart_type:
        return render(request, 'chartapp/chart.html', {'message': 'Please select chart type from home page.'})
    return render(request, 'chartapp/chart.html', {'chart_type': chart_type})

@login_required
def set_chart_type(request):
    if request.method == 'POST':
        chart_type = request.POST.get('chart_type')
        if chart_type:
            request.session['chart_type'] = chart_type
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'fail'}, status=400)
