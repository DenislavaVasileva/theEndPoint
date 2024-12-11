from django.urls import path, include

from theEndPoint.posts.views import (
    DashboardView,
    AddPostView,
    DetailPostView,
    EditPostView,
    DeletePostView,
    DetailCommentView,
    EditCommentView,
    DeleteCommentView,
    LikePostView,
    AddCommentView,
)

urlpatterns = [
    # Dashboard-related path
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    # Post-related paths
    path('add_post/', AddPostView.as_view(), name='add-post'),
    path('<int:post_id>/', include([
        path('details/', DetailPostView.as_view(), name='details-post'),
        path('edit/', EditPostView.as_view(), name='edit-post'),
        path('delete/', DeletePostView.as_view(), name='delete-post'),
        path('like/', LikePostView.as_view(), name='like-post'),

        # Comment-related paths
        path('add_comment/', AddCommentView.as_view(), name='add_comment'),
        path('comment/<int:comment_id>/details/', DetailCommentView.as_view(), name='details_comment'),
        path('comment/<int:comment_id>/edit/', EditCommentView.as_view(), name='edit_comment'),
        path('comment/<int:comment_id>/delete/', DeleteCommentView.as_view(), name='delete_comment'),
    ])
         ),
]
