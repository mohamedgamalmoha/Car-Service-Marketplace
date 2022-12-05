from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from django_filters.views import FilterView

from .models import WorkShop
from .filters import WorkShopFilter

# List Of Work
# TODO:  Workshop List With Filters                                 1
# TODO:  Create & Update & Delete Rate         <int:pk workshop>    3
# TODO:  Create & Update & Delete Comment      <int:pk workshop>    3
# TODO:  Create & Update & Delete ReportIssue  <int:pk workshop>    3
# TODO:  Delete Car                            <int:pk car>         1
# TODO:  Info Views                                                 6


class WorkShopList(FilterView):
    context_object_name = 'workshops'
    filterset_class = WorkShopFilter
    queryset = WorkShop.objects.active()
    template_name = 'workshop/workshop_list.html'
    paginate_by = 2


class WorkShopDetail(DetailView):
    model = WorkShop
    context_object_name = 'workshop'
    template_name = 'workshop/workshop_detail.html'
