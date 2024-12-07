from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from theEndPoint.posts.forms import AddPostForm, EditPostForm, DeletePostForm, AddCommentForm, SearchForm, \
    EditCommentForm, DeleteCommentForm
from theEndPoint.posts.models import Post, Category, Comment, Like
from django.db.models import Q


class DashboardView(ListView):
    template_name = 'posts/dashboard.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = self.model.objects.all()

        if 'category' in self.request.GET:
            category = self.request.GET.get('category')
            queryset = queryset.filter(category__name__iexact=category)

        if 'search' in self.request.GET:
            search = self.request.GET.get('search')
            queryset = queryset.filter(Q(content__icontains=search) | Q(title__icontains=search))

        return queryset.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['search_form'] = SearchForm()
        return context


class AddPostView(CreateView):
    model = Post
    form_class = AddPostForm
    template_name = 'posts/add_post.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)


class DetailPostView(DetailView):
    model = Post
    template_name = 'posts/details_post.html'
    pk_url_kwarg = 'post_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = AddCommentForm()
        context['comments'] = Comment.objects.filter(post=self.object).order_by('-created_at')
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user.username
            comment.save()
            return redirect('details-post', post_id=post.id)

            # If form is not valid, render the page with errors
        return self.render_to_response({'form': form, 'post': post})


class EditPostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'posts/edit_post.html'
    pk_url_kwarg = 'post_id'
    success_url = reverse_lazy('dashboard')


class DeletePostView(DeleteView):
    model = Post
    form_class = DeletePostForm
    template_name = 'posts/delete_post.html'
    pk_url_kwarg = 'post_id'
    success_url = reverse_lazy('dashboard')

    def form_invalid(self, form):
        return self.form_valid(form)


class DetailCommentView(DetailView):
    model = Comment
    template_name = 'comments/details_comment.html'
    pk_url_kwarg = 'comment_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.object.post
        return context


class EditCommentView(UpdateView):
    model = Comment
    form_class = EditCommentForm
    template_name = 'comments/edit_comment.html'
    pk_url_kwarg = 'comment_id'

    def get_success_url(self):
        return reverse_lazy('details-post', kwargs={'post_id': self.object.post.id})


class DeleteCommentView(DeleteView):
    model = Comment
    form_class = DeleteCommentForm
    template_name = 'comments/delete_comment.html'
    pk_url_kwarg = 'comment_id'
    success_url = reverse_lazy('dashboard')

    def form_invalid(self, form):
        return self.form_valid(form)


class LikePostView(LoginRequiredMixin, View):
    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        user = request.user

        if Like.objects.filter(user=user, post=post).exists():
            Like.objects.filter(user=user, post=post).delete()
        else:
            Like.objects.create(user=user, post=post)

        return redirect('details-post', post_id=post.id)
