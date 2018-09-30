from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .forms import CourseModelForm
from .models import Course
# BASE VIEW Class = VIEW


class CourseObjectMixin(object):
    model = Course
    lookup = 'id'

    def get_object(self):
        lookup = self.kwargs.get(self.lookup)
        obj = None
        if lookup is not None:
            obj = get_object_or_404(self.model, id=lookup)
        return obj


class CourseDeleteView(CourseObjectMixin, View):
    template_name = 'courses/course_delete.html'

    def get(self, request, *args, **kwargs):
        # GET METHOD
        context = {}
        obj = self.get_object()
        if obj is not None:
            context = {'object': obj}
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        # POST METHOD
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('courses:courses-list')
        return render(request, self.template_name, context=context)


class CourseUpdateView(CourseObjectMixin, View):
    template_name = 'courses/course_update.html'

    def get(self, request, *args, **kwargs):
        # GET METHOD
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(request.GET, instance=obj)
            context = {"form": form, 'object': obj}
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        # POST METHOD
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            form = CourseModelForm()
            context = {"form": form,
                       "object": obj}
        return render(request, self.template_name, context=context)


class CourseCreateView(View):
    template_name = 'courses/course_create.html'

    def get(self, request, *args, **kwargs):
        # GET METHOD
        form = CourseModelForm()
        context = {"form": form}
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        # POST METHOD
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseModelForm()
        context = {"form": form}
        return render(request, self.template_name, context=context)


class CourseListView(View):
    template_name = "courses/course_list.html"
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset()}
        return render(request, self.template_name, context=context)


class CourseView(CourseObjectMixin, View):
    template_name = 'courses/course_detail.html'

    def get(self, request, id=None, *args, **kwargs):
        context = {'object': self.get_object()}
        return render(request, self.template_name, context=context)


# HTTP METHODS
def my_fbv(request, *args, **kwargs):
    data = {
        "my_number": 1,
        "my_list": ['Item 1', 'Item 2', 'Item3']
    }
    return render(request, 'about.html', context=data)
