from django.urls import path
from . import views


urlpatterns = [
   path('', views.home, name="home"),
   path('notes/', views.notes, name="notes"),
   path('notes/<int:note_id>', views.note, name='note'),
   path('categories/', views.categories, name="categories"),
   path('categories/<str:pk>/update', views.CategoryUpdateView.as_view(), name='category-update'),
   path('categories/<str:pk>/delete', views.CategoryDeleteView.as_view(), name='category-delete'),
   # path('tools/', views.tools, name="tools"),
   # path('tools/<int:tool_id>', views.tool, name='tool'),
   # path('mytools/', views.mytools, name='user-tools'),
   path('accounts/sign_up/', views.sign_up, name='sign_up'),
   path('accounts/user_profile/', views.user_profile, name='user_profile'),
   path('category/new/', views.CategoryCreateView.as_view(), name='category-new'),
   # path('toolcopy/<str:pk>/update', views.ToolCopyUpdateView.as_view(), name='toolcopy-update'),
   # path('toolcopy/<str:pk>/reserve', views.ToolCopyUpdateView_reserve.as_view(), name='toolcopy-update-reserve'),
   # path('toolcopy/<str:pk>/cancel_reserve', views.ToolCopyUpdateView_cancel_reserve.as_view(), name='toolcopy-update-cancel-reserve'),
   # path('toolcopy/<str:pk>/delete', views.ToolCopyDeleteView.as_view(), name='toolcopy-delete'),
   # path('search/', views.search, name='search'),

]

