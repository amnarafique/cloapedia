from blog.models import Category, Post


def get_categories(request):
    categories = Category.objects.all()
    return {'categories': categories}


def get_footer(request):
    recent_posts = Post.objects.filter(published=True).order_by('-date_created')[:3]
    popular_posts = Post.objects.all().order_by('-rating')[:3]
    return {
        'recent_posts': recent_posts,
        'popular_posts': popular_posts
    }

