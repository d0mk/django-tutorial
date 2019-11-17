from django.shortcuts import render

posts = [
    {
        'author': 'Autor1',
        'title': 'blog post 1',
        'content': 'first post content',
        'date_posted': '17.11.2019'
    },
    {
        'author': 'Autor2',
        'title': 'blog post 2',
        'content': 'second post content',
        'date_posted': '18.11.2019'
    }
]


def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})