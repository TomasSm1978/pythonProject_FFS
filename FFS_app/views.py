from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, NewNoteForm, UpdateNoteForm
from django.contrib.auth import login
from .models import User, Category, Note
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.db.models import Q


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
    success_url = "/categories"
    template_name = 'category_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


@login_required
def categories(request):
    categories = Category.objects.filter(owner__exact=request.user)
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
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    fields = ['name']
    success_url = "/categories"
    template_name = 'category_delete_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


@login_required
def category(request, category_id):
    categories = Category.objects.filter(owner__exact=request.user)
    single_category = get_object_or_404(Category, pk=category_id)
    context = {
        'single_category': single_category,
        'categories': categories,
    }
    return render(request, 'category.html', context=context)


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NewNoteForm
    success_url = "/notes"
    template_name = 'note_new_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display categories that belong to a given user"""

        kwargs = super(NoteCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = UpdateNoteForm
    success_url = "/notes"
    template_name = 'note_update_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display categories that belong to a given user"""

        kwargs = super(NoteUpdateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    fields = ['title', 'text', 'category', 'image']
    success_url = "/notes"
    template_name = 'note_delete_form.html'

    def form_valid(self, form):
        return super().form_valid(form)

@login_required
def search(request):
    query = request.GET.get('query')
    search_results = Note.objects.filter(Q(title__icontains=query) | Q(text__icontains=query))
    return render(request, 'search.html', {'notes': search_results, 'query': query})