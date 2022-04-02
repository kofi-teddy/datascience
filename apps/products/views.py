from django.shortcuts import render


def chart_select_view(request):
    return render(request, 'products/main.html', {})