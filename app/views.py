from django.shortcuts import render
from .models import *
from .forms import *


def not_ok_comment(comment: str):
    stop_list = ('кот', 'котик')
    for word in stop_list:
        if word in comment.lower().split():
            return True
    return False


def movie(request, movie_id: int):
    form = NewCommentForm()
    all_comments = Comment.objects.filter(active=True, movie_id=movie_id)
    movie_to_page = Movie.objects.get(id=movie_id)
    data = {
        'comments': all_comments,
        'form': form,
        'movie': movie_to_page,
        'cat_filter': False
    }
    if request.POST:
        data['cat_filter'] = not_ok_comment(request.POST.get('body'))
        if not data['cat_filter']:
            Comment.objects.create(
                author=request.POST.get('author'),
                body=request.POST.get('body'),
                movie_id=movie_id,
                active=True
            ).save()
    return render(request, 'movie.html', context=data)
