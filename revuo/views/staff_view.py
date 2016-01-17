from django.shortcuts import get_object_or_404, render
from django.views.generic import View

from revuo.models import Staff


class StaffView(View):
    def get(self, request, staff_id):
        author = get_object_or_404(Staff, id=staff_id)
        template = 'revuo/staff_view.html'
        return render(request, template, {'author': author})
