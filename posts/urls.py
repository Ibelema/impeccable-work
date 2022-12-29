from django.urls import path
from .views import ArticleListView, ArticleDetailView, PostCreateView, EditPostView, DeletePostView

app_name = 'posts'

urlpatterns= [
    #Homepage
    path('', ArticleListView.as_view(), name='homepage'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_create'),
    path('article/new_post/', PostCreateView.as_view(), name='new_article'),
    #Editing posts
    path('article/<int:pk>/edit/', EditPostView.as_view(), name='edit'),
    path('article/<int:pk>/delete/', DeletePostView.as_view(), name='delete'),
]
