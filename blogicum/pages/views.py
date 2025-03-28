from django.shortcuts import render

def about_page(request):
    return render(request, 'about.html')

def rules_page(request):
    return render(request, 'rules.html')
