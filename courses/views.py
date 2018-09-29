from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Course
# BASE VIEW Class = VIEW


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
