from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.blogListView, name='home'),
    url(r'^write/new/$', views.createBlogView, name='create_blog'),
    url(r'^blog/(?P<id>\d+)/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[\w-]+)/$',views.blogDetailView, name='blog_detail'),
    url(r'^likes/$', views.likeBlogView, name='like_blog'),
    url(r'^tags/(?P<tag_slug>[\w-]+)/$', views.blogListView, name='blog_list_by_tag_name'),
    url(r'^share/blog/(?P<id>\d+)/$', views.shareBlogView, name='share_blog'),
    url(r'^myblogs/$', views.myBlogsView, name='my_blogs'),
    url(r'myblogs/edit/(?P<id>\d+)/$', views.myBlogEditView, name='edit_myblog'),
    url(r'myblogs/delete/(?P<id>\d+)/$', views.myBlogDeleteView, name='delete_myblog'),
]
