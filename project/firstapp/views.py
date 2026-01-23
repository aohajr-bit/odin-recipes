from django.shortcuts import render


def index(request):
    """Render a simple template for the app index."""
    context = {
        'title': 'Welcome to FirstApp',
        'message': 'This is your first view rendered from a template.'
    }
    return render(request, 'firstapp/index.html', context)
