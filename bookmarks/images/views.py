from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
from .models import Image
from django.http import JsonResponse
from django.views.decorators.http import require_POST


@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Image added successfully')
            return redirect(new_item.get_absolute_url())
    else:
        form = ImageCreateForm(request.GET)
    return render(request, 'images/image/create.html', {'section': 'images',
                                                        'form': form})


def image_detail(request, id, slug):
    # png/jpg/jpeg
    image = get_object_or_404(Image, id=id, slug=slug)
    """
    Using the {% with %} template tag is useful to prevent Django from evaluating QuerySets multiple times.
    """
    return render(request, 'images/image/detail.html',{'section':'images','image':image})


@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_likes.add(request.user)
            else:
                """
                Another useful method of the many-to-many manager is clear(), which removes all objects from the related
                object set.
                """
                image.users_likes.remove(request.user)
            return JsonResponse({'status':'ok'})
        except:
            pass
    return JsonResponse({'status':'ko'})
