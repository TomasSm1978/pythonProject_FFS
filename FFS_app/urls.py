from django.urls import path
from . import views


urlpatterns = [
   path('', views.home, name="home"),
   path('notes/', views.notes, name="notes"),
   path('notes/<int:note_id>', views.note, name='note'),
   path('note/new', views.NoteCreateView.as_view(), name='note-new'),
   path('note/<str:pk>/update', views.NoteUpdateView.as_view(), name='note-update'),
   path('note/<str:pk>/delete', views.NoteDeleteView.as_view(), name='note-delete'),
   path('categories/', views.categories, name="categories"),
   path('categories/<int:category_id>', views.category, name='category'),
   path('categories/<str:pk>/update', views.CategoryUpdateView.as_view(), name='category-update'),
   path('categories/<str:pk>/delete', views.CategoryDeleteView.as_view(), name='category-delete'),
   path('accounts/sign_up/', views.sign_up, name='sign-up'),
   path('accounts/user_profile/', views.user_profile, name='user_profile'),
   path('category/new/', views.CategoryCreateView.as_view(), name='category-new'),
   path('search/', views.search, name='search'),

]

