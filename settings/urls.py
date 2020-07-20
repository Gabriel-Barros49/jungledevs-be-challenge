"""
backend-challenge-001 URL Configuration
"""
###
# Libraries
###
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework_nested import routers

from helpers.health_check_view import health_check

from topics.views import TopicViewset
from posts.views import PostViewSet
from comments.views import CommentViewSet

###
# Routers
###

router = routers.DefaultRouter()
router.register(r'topics', TopicViewset, basename='topics')

posts_router = routers.NestedSimpleRouter(router, r'topics', lookup='topic')
posts_router.register(r'posts', PostViewSet, basename='posts')

comments_router = routers.NestedSimpleRouter(posts_router, r'posts', lookup='post')
comments_router.register(r'comments', CommentViewSet, basename='comments')


###
# URLs
###
urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),

    # Health Check
    url(r'health-check/$', health_check, name='health_check'),

    # Applications
    url(r'^', include('accounts.urls')),
    url(r'^', include(router.urls)),
    url(r'^', include(posts_router.urls)),
    url(r'^', include(comments_router.urls)),

]
