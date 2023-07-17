from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name="home"),
    path('snippets/add/', views.add_snippet_page, name="snippets-add"),
    path('snippets/list', views.snippets_page, name="snippets-list"),
    # path('snippets/my/', views.snippets_page, {'my': True}, name="snippets-my"),
    path('snippet/<int:snippet_id>/', views.snippet_detail, name="snippet-detail"),
    path('snippet/<int:snippet_id>/delete/', views.snippet_delete, name="snippet-delete"),
    path('comment/add/', views.comment_add, name="comment_add"),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('registration/', views.registration, name='registration'),
    path('mysnippet/', views.my_snippet, name='mysnippet'),
    path('snippet/<int:snippet_id>/snippet_detail_edit/', views.snippet_edit, name='snippet-edit'),
    path('index.html', views.snippet_search, name="snippet-search"),
    path('snippet/<int:snippet_id>/mysnippet/', views.snippet_hide, name='hide'),
    path('home', views.snippet_show, name='show_snippet'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
