from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from revuo.models import Staff
from revuo.forms import FormEditProfile


class StaffEdit(View):
    template_name = 'revuo/edit_item.html'

    @method_decorator(login_required)
    def get(self, request):
        author_info = Staff.objects.get(user=request.user)
        form = FormEditProfile(instance=author_info)
        return render(request, self.template_name, {'form': form}, context_instance=RequestContext(request))

    @method_decorator(login_required)
    def post(self, request):
        author_info = Staff.objects.get(user=request.user)
        form = FormEditProfile(request.POST, request.FILES, instance=author_info)
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        return render(request, self.template_name, {'form': form}, context_instance=RequestContext(request))
