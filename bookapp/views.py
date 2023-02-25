from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404, redirect

from bookapp.forms import GuestForm, SearchForm
from bookapp.models import GuestBook, StatusChoice


# Create your views here.
def index_view(request: WSGIRequest):
    guests = GuestBook.objects.exclude(status=StatusChoice.BLOCKED).order_by('created_at')
    context = {
        'guests': guests
    }
    return render(request, 'index.html', context=context)


def edit_view(request, pk):
    errors = {}
    guest = get_object_or_404(GuestBook, pk=pk)

    if request.method == 'GET':
        form = GuestForm(initial={
            'name': guest.name,
            'email': guest.email,
            'text': guest.text,
            'status': guest.status
        })
        return render(request, 'guest_edit.html',
                      context={
                          'guest': guest,
                          'choices': StatusChoice.choices,
                          'form': form
                      })
    elif request.method == 'POST':
        form = GuestForm(data=request.POST)
        if form.is_valid():
            guest.name = form.cleaned_data['name']
            guest.email = form.cleaned_data['email']
            guest.text = form.cleaned_data['text']
            guest.status = form.cleaned_data['status']
            guest.save()
            return redirect('task_detail', pk=guest.pk)

        else:
            if not request.POST.get('name'):
                errors['name'] = 'Данное поле обязательно к заполнению'
            return render(request, 'guest_edit.html',
                          context={
                              'guest': guest,
                              'choices': StatusChoice.choices,
                              'errors': errors,
                              'form': form
                          })


def delete_view(request, pk):
    guest = get_object_or_404(GuestBook, pk=pk)
    return render(request, 'guest_confirm_delete.html', context={'guest': guest})


def confirm_delete(request, pk):
    guest = get_object_or_404(GuestBook, pk=pk)
    guest.delete()
    return redirect('index')


def add_view(request: WSGIRequest):
    if request.method == "GET":
        form = GuestForm()
        return render(request, 'guest_add.html',
                      context={
                          'choices': StatusChoice.choices,
                          'form': form
                      })
    form = GuestForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'guest_add.html',
                      context={
                          'choices': StatusChoice.choices,
                          'form': form
                      })
    else:
        guest = GuestBook.objects.create(**form.cleaned_data)
        return redirect('index')


def search_view(request: WSGIRequest):
    search_form = SearchForm
    form = GuestForm
    search = request.GET.get('search', default='')
    guests = GuestBook.objects.filter(name__icontains=search).exclude(status=StatusChoice.BLOCKED).order_by('created_at')
    context = {
        'guests': guests,
        'search_form': search_form,
        'form': form
    }
    return render(request, 'index.html', context)
