from django.urls import path

from . import views

urlpatterns = [
    path("post/", views.PostListCreate.as_view(), name="post_list"),
    path(
        "post/<int:post_id>/",
        views.PostRetrieveUpdateDestroy.as_view(),
        name="post_details",
    ),
    path("comment/", views.CommentListCreate.as_view(), name="comments_list"),
    path(
        "comment/<int:comment_id>/",
        views.CommentRetrieveUpdateDestroy.as_view(),
        name="comment_details",
    ),
    path("vote/", views.VoteListCreate.as_view(), name="vote_create"),
]
