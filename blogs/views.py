from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# from django.http import Http404
from .models import BlogPost
from .forms import BlogPostForm


def home(request):
    # Получаем список всех блог-постов, упорядоченных по дате добавления
    posts = BlogPost.objects.order_by('-date_added')
    return render(request, 'blogs/home.html', {'posts': posts})


def post_details(request, post_id):
    # Получаем конкретный блог-пост по его идентификатору
    post = BlogPost.objects.get(id=post_id)
    return render(request, 'blogs/post_details.html', {'post': post})


@login_required
def edit_post(request, post_id):
    # Получаем конкретный блог-пост по его идентификатору
    post = BlogPost.objects.get(id=post_id)

    if request.user == post.author:
        if request.method == 'POST':
            # Если данные отправлены методом POST, создаем форму на основе полученных данных
            form = BlogPostForm(request.POST, instance=post)
            if form.is_valid():
                form.instance.author = request.user  # Установите автора перед сохранением
                # Если форма прошла валидацию, сохраняем изменения в блог-посте
                updated_post = form.save()  # Сохраняем изменения и получаем обновленный пост
                return redirect('post_details', post_id=updated_post.id)  # Перенаправляем на страницу post_details с
                # обновленным постом
        else:
            # Если данные не отправлены методом POST, показываем форму для редактирования
            form = BlogPostForm(instance=post)
        return render(request, 'blogs/edit_post.html', {'form': form, 'post': post})
    else:
        # Если текущий пользователь не является автором поста, перенаправляем на домашнюю страницу
        return redirect('home')


@login_required
def new_post(request):
    if request.method == 'POST':
        # Если данные отправлены методом POST, создаем форму на основе полученных данных
        form = BlogPostForm(request.POST)
        if form.is_valid():
            # Если форма прошла валидацию, сохраняем новый блог-пост
            # blog_post = form.save(commit=False)
            # blog_post.author = request.user  # Устанавливаем текущего пользователя как автора поста
            # blog_post.save()
            form.instance.author = request.user  # Установите автора перед сохранением
            form.save()
            return redirect('blogs:home')
    else:
        # Если данные не отправлены методом POST, показываем пустую форму
        form = BlogPostForm()
    return render(request, 'blogs/new_post.html', {'form': form})


def my_posts(request):
    user_posts = BlogPost.objects.filter(author=request.user)
    return render(request, 'blogs/my_posts.html', {'user_posts': user_posts})


def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    # Проверка, что текущий пользователь - автор поста
    if request.user == post.author:
        post.delete()

    return redirect('blogs:home')  # Перенаправление на домашнюю страницу после удаления поста
