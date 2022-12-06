from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django_filters.views import FilterView

from .filters import WorkShopFilter
from accounts.mixins import CustomerAuthMixIn
from .models import WorkShop, Rate, Comment, ReportIssue
from .forms import RateForm, CommentForm, ReportIssueForm


# List Of Work
# TODO:  List   & Detail          Workshop     <int:pk workshop>    2
# TODO:  Create & Update & Delete Rate         <int:pk workshop>    3
# TODO:  Create & Update & Delete Comment      <int:pk workshop>    3
# TODO:  Create & Update & Delete ReportIssue  <int:pk workshop>    3
# TODO:  Delete Car                            <int:pk car>         1
# TODO:  Info Views                                                 6


class WorkShopList(FilterView):
    context_object_name = 'workshops'
    filterset_class = WorkShopFilter
    queryset = WorkShop.objects.active()
    template_name = 'workshop/workshop/list.html'
    paginate_by = 2


class WorkShopDetail(DetailView):
    model = WorkShop
    context_object_name = 'workshop'
    template_name = 'workshop/workshop_detail.html'


class CreateRateView(CustomerAuthMixIn, CreateView):
    model = Rate
    form_class = RateForm
    template_name = "workshop/rate/create.html"
    extra_context = {
        'title': 'Add Rate'
    }

    def get_success_url(self):
        return reverse('workshop:workshop_detail', pk=self.get_object().pk)

    def get_object(self, queryset=None):
        return get_object_or_404(WorkShop, pk=self.kwargs.get('pk', None))

    def form_valid(self, form):
        form.instance.customer = self.request.user
        form.instance.workshop = self.get_object()
        return super().form_valid(form)


class UpdateRateView(CustomerAuthMixIn, UpdateView):
    model = Rate
    form_class = RateForm
    template_name = "workshop/rate/update.html"
    extra_context = {
        'title': 'Update Rate'
    }

    def get_queryset(self):
        return self.model.objects.filter(customer=self.request.user)


class DeleteRateView(CustomerAuthMixIn, DeleteView):
    model = Rate
    form_class = RateForm
    template_name = "workshop/rate_delete.html"
    extra_context = {
        'title': 'Delete Rate'
    }

    def get_queryset(self):
        return self.model.objects.filter(customer=self.request.user)


class CreateCommentView(CustomerAuthMixIn, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "workshop/comment/create.html"
    extra_context = {
        'title': 'Add Comment'
    }

    def get_success_url(self):
        return reverse('workshop:workshop_detail', pk=self.get_object().pk)

    def get_object(self, queryset=None):
        return get_object_or_404(WorkShop, pk=self.kwargs.get('pk', None))

    def form_valid(self, form):
        form.instance.customer = self.request.user
        form.instance.workshop = self.get_object()
        return super().form_valid(form)


class UpdateCommentView(CustomerAuthMixIn, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "workshop/comment/update.html"
    extra_context = {
        'title': 'Update Comment'
    }

    def get_queryset(self):
        return self.model.objects.filter(customer=self.request.user)


class DeleteCommentView(CustomerAuthMixIn, DeleteView):
    model = Comment
    form_class = CommentForm
    template_name = "workshop/comment/delete.html"
    extra_context = {
        'title': 'Delete Comment'
    }

    def get_queryset(self):
        return self.model.objects.filter(customer=self.request.user)


class CreateReportIssueView(CustomerAuthMixIn, CreateView):
    model = ReportIssue
    form_class = ReportIssueForm
    template_name = "workshop/report/create.html"
    extra_context = {
        'title': 'Add Report'
    }

    def get_success_url(self):
        return reverse('workshop:workshop_detail', pk=self.get_object().pk)

    def get_object(self, queryset=None):
        return get_object_or_404(WorkShop, pk=self.kwargs.get('pk', None))

    def form_valid(self, form):
        form.instance.customer = self.request.user
        form.instance.workshop = self.get_object()
        return super().form_valid(form)


class UpdateReportIssueView(CustomerAuthMixIn, UpdateView):
    model = ReportIssue
    form_class = ReportIssueForm
    template_name = "workshop/report/update.html"
    extra_context = {
        'title': 'Update Report'
    }

    def get_queryset(self):
        return self.model.objects.filter(customer=self.request.user)


class DeleteReportIssueView(CustomerAuthMixIn, DeleteView):
    model = ReportIssue
    form_class = ReportIssueForm
    template_name = "workshop/report/delete.html"
    extra_context = {
        'title': 'Delete Report'
    }

    def get_queryset(self):
        return self.model.objects.filter(customer=self.request.user)
