from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from sampleapp.models import NewsArticle


@require_POST
def post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        slug = request.POST.get('slug')
        date = request.POST.get('date')
        intro = request.POST.get('intro')
        content = request.POST.get('content')
        main_image = request.FILES.get('main_image')
        og_image = request.FILES.get('og_image')
        featured_media = request.FILES.get('featured_media')
        featured_youtube = request.POST.get('featured_youtube')
        tags = request.POST.get('tags')

        # Validate required fields
        if not title or not slug or not date or not main_image:
            print("Please fill in all required fields.")
            messages.error(request, "Please fill in all required fields.")
            return render(request, 'newsadmin/index.html')

        article = NewsArticle(
            title=title,
            slug=slug,
            date=date,
            intro=intro,
            body=content,
            main_image=main_image,
            og_image=og_image,
            featured_media=featured_media,
            featured_youtube=featured_youtube
        )

        try:
            article.save()
            print("Post saved successfully.")
        except Exception as e:
            print(f"Error saving post: {e}")
            messages.error(request, "There was an error saving the post.")
            return render(request, 'newsadmin/index.html')

        if tags:
            article.tags.add(*tags.split(','))  # Assuming tags are comma-separated

        return redirect('index')  # Redirect to the index page after saving

    return render(request, 'newsadmin/index.html')
