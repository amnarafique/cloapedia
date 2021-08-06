from django.contrib.auth.decorators import login_required
from django.shortcuts import render


from blog.forms import PostCreateForm
from blog.models import Post, Category


def main_page(request):
    categories = Category.objects.all()

    context = {
        'categories':categories,

    }
    return render(request, 'blog/index.html')


def create_post(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
    form = PostCreateForm()
    return render(request, 'blog/post_create.html',
                  context={'form': form})

@login_required
def user_posts(request):
    posts = Post.objects.filter(author=request.user)
    context = {
        'posts': posts
    }
    return render(request, 'blog/user_posts.html', context)

def category_posts(request, pk):
    category = Category.objects.filter(id=pk).first()
    posts = Post.objects.filter(category=category, published=True)
    return render(request, 'blog/category_posts.html',
                  context={'category': category, 'posts': posts})


def search(request):
    query = request.GET.get('q')
    posts = Post.objects.filter(title__icontains=query, published=True)
    return render(request, 'blog/search.html',
                           context={'posts': posts})

def post_detail(request, pk):
    owner = None

    post = Post.objects.filter(id=pk).first()

    if request.user and request.user == post.author:
        owner = request.user

    elif request.user or not request.user:
        post.seen_amount += 1
        post.save()

    context = {
        'post': post,
        'owner': owner
    }

    return  render(request, 'blog/post_detail.html', context)

