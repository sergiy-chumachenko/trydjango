from django.shortcuts import render
from django.views import View

# BASE VIEW Class = VIEW


class CourseView(View):
    template_name = 'about.html'
    def get(self, request, *args, **kwargs):
        data = {
            "my_number": 1,
            "my_list": ['Item 1', 'Item 2', 'Item3']
        }
        # GET METHOD
        return render(request, self.template_name, context=data)

# HTTP METHODS
def my_fbv(request, *args, **kwargs):
    data = {
        "my_number": 1,
        "my_list": ['Item 1', 'Item 2', 'Item3']
    }
    return render(request, 'about.html', context=data)
