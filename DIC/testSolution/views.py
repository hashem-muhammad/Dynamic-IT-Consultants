from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.conf import settings
from testSolution.Filter.filter import sortFliter
from testSolution.models import News
from .forms import NewUserForm, loginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import requests
import requests_cache


def homeView(request):
    return render(request=request, template_name='index.html', context={
        'title': 'Home'
    })


def registerRequest(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect(reverse_lazy("home"))

        messages.error(
            request, "Unsuccessful registration. Invalid information.")
        messages.error(request, form.errors)

    form = NewUserForm()
    return render(request=request, template_name="assets/pages/register.html", context={"register_form": form, "title": 'Register'})


def loginRequest(request):
    if request.method == "POST":
        form = loginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse_lazy("home"))
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")

    form = loginForm()
    return render(request=request, template_name="assets/pages/login.html", context={"login_form": form, 'title': 'Login'})


def logoutRequest(request):
    logout(request)
    return redirect(reverse_lazy("home"))


def newsRequest(request):
    url = settings.NEWS_WEBSITE
    headers = {'x-api-key': settings.X_API_KEY}

    page = request.GET.get('page', 1)
    sort_status = request.POST.getlist('sort', ['1'])
    country = request.POST.getlist('country', ['US'])

    querystring = {"q": "\"Tesla\"", "lang": "en",
                   "sort_by": "relevancy", "page": page}
    response = requests.get(url, headers=headers, params=querystring).json()

    checkNews = News.objects.count()
    if checkNews > 0:
        sort_values = sortFliter(model=News, sort=sort_status, country=country)

    # I created it in this method to test database bulk create but I can make it without store it in database
    else:
        try:
            for i in response['articles']:
                News.objects.bulk_create([
                    News(title=i['title'], image=i['media'], details=i['summary'],
                         country=i['country'], published_date=i['published_date'],
                         language=i['language']
                         )
                ])
            sort_values = News.objects.values(
                'id', 'title', 'image', 'details', 'published_date')
        except:
            sort_values = {'title': 'news not available'}
    # page will be cashe after visit
    requests_cache.install_cache('news_cache')

    # data is not to big it's around 50 items but also to test pagination
    paginator = Paginator(sort_values, 3)
    try:
        sort_values = paginator.page(page)
    except PageNotAnInteger:
        sort_values = paginator.page(1)
    except EmptyPage:
        sort_values = paginator.page(paginator.num_pages)

    return render(request, 'assets/pages/content.html', {'response': sort_values})
