from django.urls import path
from . import views


urlpatterns = [
   path('', views.home, name="home"),
   path('notes/', views.notes, name="notes"),
   path('notes/<int:note_id>', views.note, name='note'),
   path('categories/', views.categories, name="categories"),
   path('categories/<int:category_id>', views.category, name='category'),
   path('categories/<str:pk>/update', views.CategoryUpdateView.as_view(), name='category-update'),
   path('categories/<str:pk>/delete', views.CategoryDeleteView.as_view(), name='category-delete'),
   path('accounts/sign_up/', views.sign_up, name='sign_up'),
   path('accounts/user_profile/', views.user_profile, name='user_profile'),
   path('category/new/', views.CategoryCreateView.as_view(), name='category-new'),
   # path('search/', views.search, name='search'),

]

