from django.shortcuts import render


def dashboard_view(request):
    context = {
    }
    return render(request, "sampleapp/index.html", context)


def about_view(request):
    context = {

    }
    return render(request, "sampleapp/about.html",context)
