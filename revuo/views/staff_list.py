from django.views.generic import ListView

from revuo.models import Staff


class StaffList(ListView):
    model = Staff
    queryset = Staff.objects.all()
    template_name = 'revuo/staff.html'
