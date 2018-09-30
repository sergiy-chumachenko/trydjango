from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import CourseModelForm
from .models import Course
# BASE VIEW Class = VIEW


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


class CourseView(View):
    template_name = 'courses/course_detail.html'

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(Course, id=id)
            context['object'] = obj
            # GET METHOD
        return render(request, self.template_name, context=context)


# HTTP METHODS
def my_fbv(request, *args, **kwargs):
    data = {
        "my_number": 1,
        "my_list": ['Item 1', 'Item 2', 'Item3']
    }
    return render(request, 'about.html', context=data)
