from django.shortcuts import render

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-pk')
    return render(
        request,
        'blog/index.html',
        {
            'posts':posts,
        }
    )
