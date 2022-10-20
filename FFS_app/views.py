from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.contrib.auth import login
from .models import User, Category, Note
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView


def home(request):
    return render(request, 'home.html')


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('home'))
    else:
        form = SignUpForm()
    return render(request, 'registration/sign_up.html', context={'form': form})


@login_required
def user_profile(request):
    return render(request, 'registration/user_profile.html')


@login_required
def notes(request):
    notes = Note.objects.filter(owner__exact=request.user)
    categories = Category.objects.filter(owner__exact=request.user)

    context = {
        'notes': notes,
        'categories': categories,
    }
    return render(request, 'notes.html', context=context)


@login_required
def note(request, note_id):
    single_note = get_object_or_404(Note, pk=note_id)
    return render(request, 'note.html', {'note': single_note})


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['name']
    success_url = "/notes"
    template_name = 'category_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


@login_required
def categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'categories.html', context=context)


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    fields = ['name']
    success_url = "/categories"
    template_name = 'category_update_form.html'

    def form_valid(self, form):
        form.owner = self.request.user
        return super().form_valid(form)


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    fields = ['name']
    success_url = "/categories"
    template_name = 'category_delete_form.html'

    def form_valid(self, form):
        form.owner = self.request.user
        return super().form_valid(form)