from django.urls import path
from .views import index, about, latest_pos, detail, latest_com, postCreateView, postupdateView, PostDeleteView

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('lastes_post/', latest_pos),
    path('latest_comment/', latest_com),
    path('detail/<int:post_id>/', detail, name='detail'),
    path('new_post/', postCreateView.as_view(), name='new_post'),
    path('detail/<slug:pk>/update/', postupdateView.as_view(), name='post_update'),
    path('detail/<slug:pk>/deleate/', PostDeleteView.as_view(), name='post_delete'),
]
