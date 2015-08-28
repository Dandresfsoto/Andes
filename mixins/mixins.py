from region.models import Region
from guardian.core import ObjectPermissionChecker
from django.shortcuts import render

class RegionMixin(object):

    def check_permissions(self, request):
        user = request.user
        region = Region.objects.get(pk=self.kwargs['pk'])
        checker = ObjectPermissionChecker(user)
        response = checker.has_perm('region_acceso',region)
        return response

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs
        response = self.check_permissions(request)
        if not response:
            return render(request, 'permisos.html')
        return super(RegionMixin, self).dispatch(request, *args,**kwargs)

class CpeMixin(object):

    def check_permissions(self, request):
        user = request.user
        region = Region.objects.get(pk=self.kwargs['pk'])
        checker = ObjectPermissionChecker(user)
        response = checker.has_perm('region_acceso_cpe',region)
        return response

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs
        response = self.check_permissions(request)
        if not response:
            return render(request, 'permisos.html')
        return super(CpeMixin, self).dispatch(request, *args,**kwargs)