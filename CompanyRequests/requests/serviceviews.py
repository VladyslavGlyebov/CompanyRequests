from django.contrib.auth.hashers import make_password
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView, ContextMixin
from django.views.generic.list import ListView
from requests.models import Department, Activ, Category
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator

#Departments
class DepartmentListView(ListView):
    model = Department
    template_name = "service/departments.html"
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        return super(DepartmentListView, self).get(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
        context = super(DepartmentListView, self).get_context_data(**kwargs)
        try:
            context["pn"] = self.request.GET["page"]
        except KeyError:
            context["pn"] = "1"
        return context

    def get_queryset(self):
        return Department.objects.all()

@method_decorator(permission_required("request.department.can_add_department"), name='dispatch')
class CreateDepartmentView(CreateView):
    model = Department
    fields = ["name"]

    def post(self, request, *args, **kwargs):
        self.success_url = reverse("services")
        return super().post(request, *args, **kwargs)  

@method_decorator(permission_required("request.department.can_change_department"), name='dispatch')
class UpdateDepartmentView(UpdateView):
    model = Department
    fields = ["name"]
    template_name = "service/department_edit.html"
    pk_url_kwarg = "department_id"

    def post(self, request, *args, **kwargs):
        self.success_url = reverse("services")
        return super().post(request, *args, **kwargs)  
    
@method_decorator(permission_required("request.department.can_delete_department"), name='dispatch')
class DeleteDepartmentView(DeleteView):
    model = Department
    template_name = "service/department_delete.html"
    pk_url_kwarg = "department_id"

    def post(self, request, *args, **kwargs):
        self.success_url = reverse("services")
        return super().post(request, *args, **kwargs) 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context["department"] = Department.objects.get(pk = self.kwargs["department_id"])
        return context;

#Activs
class ActivListView(ListView):
    model = Activ
    template_name = "service/activs.html"
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        return super(ActivListView, self).get(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
        context = super(ActivListView, self).get_context_data(**kwargs)
        context["departments"] = Department.objects.all()
        try:
            context["pn"] = self.request.GET["page"]
        except KeyError:
            context["pn"] = "1"
        return context

    def get_queryset(self):
        return Activ.objects.all()

@method_decorator(permission_required("request.activ.can_add_activ"), name='dispatch')
class CreateActivView(CreateView):
    model = Activ
    fields = ["cub_number"]

    def form_valid(self, form):
        form.instance.department = Department.objects.get(pk = self.request.POST["department_id"])
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        self.success_url = reverse("activs")
        return super().post(request, *args, **kwargs)  

@method_decorator(permission_required("request.activ.can_change_activ"), name='dispatch')
class UpdateActivView(UpdateView):
    model = Activ
    fields = ["cub_number", "department"]
    template_name = "service/activ_edit.html"
    pk_url_kwarg = "activ_id"

    def post(self, request, *args, **kwargs):
        self.success_url = reverse("activs")
        return super().post(request, *args, **kwargs)  

@method_decorator(permission_required("request.activ.can_delete_activ"), name='dispatch')
class DeleteActivView(DeleteView):
    model = Activ
    template_name = "service/activ_delete.html"
    pk_url_kwarg = "activ_id"

    def post(self, request, *args, **kwargs):
        self.success_url = reverse("activs")
        return super().post(request, *args, **kwargs) 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context["activ"] = Activ.objects.get(pk = self.kwargs["activ_id"])
        return context;

#Categories
class CategoryListView(ListView):
    model = Category
    template_name = "service/categories.html"
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        return super(CategoryListView, self).get(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        try:
            context["pn"] = self.request.GET["page"]
        except KeyError:
            context["pn"] = "1"
        return context

    def get_queryset(self):
        return Category.objects.all()

@method_decorator(permission_required("request.category.can_add_category"), name='dispatch')
class CreateCategoryView(CreateView):
    model = Category
    fields = ["name"]

    def post(self, request, *args, **kwargs):
        self.success_url = reverse("categories")
        return super().post(request, *args, **kwargs)  

@method_decorator(permission_required("request.category.can_change_category"), name='dispatch')
class UpdateCategoryView(UpdateView):
    model = Category
    fields = ["name"]
    template_name = "service/category_edit.html"
    pk_url_kwarg = "category_id"

    def post(self, request, *args, **kwargs):
        self.success_url = reverse("categories")
        return super().post(request, *args, **kwargs)  

@method_decorator(permission_required("request.category.can_delete_category"), name='dispatch')
class DeleteCategoryView(DeleteView):
    model = Category
    template_name = "service/category_delete.html"
    pk_url_kwarg = "category_id"

    def post(self, request, *args, **kwargs):
        self.success_url = reverse("categories")
        return super().post(request, *args, **kwargs) 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context["category"] = Category.objects.get(pk = self.kwargs["category_id"])
        return context;
