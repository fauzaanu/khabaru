from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .forms import NewsArticleForm
from sampleapp.models import NewsArticle


def is_editor(user):
    return user.is_staff or user.is_superuser


@user_passes_test(is_editor)
def dashboard(request):
    recent_articles = NewsArticle.objects.order_by('-created_at')[:5]
    return render(request, 'newsadmin/dashboard.html', {'recent_articles': recent_articles})


@user_passes_test(is_editor)
def article_list(request):
    articles = NewsArticle.objects.all().order_by('-date')
    return render(request, 'newsadmin/article_list.html', {'articles': articles})


@user_passes_test(is_editor)
def article_create(request):
    if request.method == 'POST':
        form = NewsArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            form.save_m2m()  # Save tags
            messages.success(request, 'Article created successfully.')
            return redirect('newsadmin:article_list')
    else:
        form = NewsArticleForm()
    return render(request, 'newsadmin/article_form.html', {'form': form})


@user_passes_test(is_editor)
def article_edit(request, pk):
    article = get_object_or_404(NewsArticle, pk=pk)
    if request.method == 'POST':
        form = NewsArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article updated successfully.')
            return redirect('newsadmin:article_list')
    else:
        form = NewsArticleForm(instance=article)
    return render(request, 'newsadmin/article_form.html', {'form': form, 'article': article})


@user_passes_test(is_editor)
def article_delete(request, pk):
    article = get_object_or_404(NewsArticle, pk=pk)
    if request.method == 'POST':
        article.delete()
        messages.success(request, 'Article deleted successfully.')
        return redirect('newsadmin:article_list')
    return render(request, 'newsadmin/article_confirm_delete.html', {'article': article})
