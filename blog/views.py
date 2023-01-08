from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django_filters.views import FilterView

from .filters import PostFilter
from .forms import PostCommentForm
from .models import Post, PostComment
from accounts.mixins import CustomerAuthMixIn


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post/detail.html'


class PostListView(FilterView):
    context_object_name = 'posts'
    filterset_class = PostFilter
    queryset = Post.objects.active()
    template_name = 'blog/post/list.html'
    paginate_by = 1


class CreatePostCommentView(CustomerAuthMixIn, CreateView):
    model = PostComment
    form_class = PostCommentForm
    template_name = "blog/post_comment/create.html"
    extra_context = {
        'title': 'Add Post Comment'
    }

    def get_success_url(self):
        return reverse('blog:post_detail', args=[self.get_object().pk])

    def get_object(self, queryset=None):
        return get_object_or_404(Post, pk=self.request.POST.get('post', None))

    def form_valid(self, form):
        form.instance.customer = self.request.user
        form.instance.post = self.get_object()
        return super().form_valid(form)


class UpdatePostCommentView(CustomerAuthMixIn, UpdateView):
    model = PostComment
    form_class = PostCommentForm
    template_name = "blog/post_comment/update.html"
    extra_context = {
        'title': 'Update Post Comment'
    }

    def get_success_url(self):
        return reverse('blog:post_detail', args=[self.get_object().post.pk])

    def get_queryset(self):
        return self.model.objects.filter(customer=self.request.user)


class DeleteCommentView(CustomerAuthMixIn, DeleteView):
    model = PostComment
    form_class = PostCommentForm
    template_name = "blog/post_comment/delete.html"
    success_url = '/'
    extra_context = {
        'title': 'Delete Post Comment'
    }

    def get_queryset(self):
        return self.model.objects.filter(customer=self.request.user)
