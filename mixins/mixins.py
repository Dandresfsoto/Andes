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

class AndesMixin(object):

    def check_permissions(self, request):
        user = request.user
        region = Region.objects.get(pk=self.kwargs['pk'])
        checker = ObjectPermissionChecker(user)
        response = checker.has_perm('region_acceso_andes',region)
        return response

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs
        response = self.check_permissions(request)
        if not response:
            return render(request, 'permisos.html')
        return super(AndesMixin, self).dispatch(request, *args,**kwargs)

class AdministrativoMixin(object):

    def check_permissions(self, request):
        user = request.user
        region = Region.objects.get(pk=self.kwargs['pk'])
        checker = ObjectPermissionChecker(user)
        response = checker.has_perm('administrativo',region)
        return response

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs
        response = self.check_permissions(request)
        if not response:
            return render(request, 'permisos.html')
        return super(AdministrativoMixin, self).dispatch(request, *args,**kwargs)

class AccesoMixin(object):

    def check_permissions(self, request):
        user = request.user
        region = Region.objects.get(pk=self.kwargs['pk'])
        checker = ObjectPermissionChecker(user)
        response = checker.has_perm('acceso',region)
        return response

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs
        response = self.check_permissions(request)
        if not response:
            return render(request, 'permisos.html')
        return super(AccesoMixin, self).dispatch(request, *args,**kwargs)

class FinancieroMixin(object):

    def check_permissions(self, request):
        user = request.user
        region = Region.objects.get(pk=self.kwargs['pk'])
        checker = ObjectPermissionChecker(user)
        response = checker.has_perm('financiero',region)
        return response

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs
        response = self.check_permissions(request)
        if not response:
            return render(request, 'permisos.html')
        return super(FinancieroMixin, self).dispatch(request, *args,**kwargs)

class FormacionMixin(object):

    def check_permissions(self, request):
        user = request.user
        region = Region.objects.get(pk=self.kwargs['pk'])
        checker = ObjectPermissionChecker(user)
        response = checker.has_perm('formacion',region)
        return response

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs
        response = self.check_permissions(request)
        if not response:
            return render(request, 'permisos.html')
        return super(FormacionMixin, self).dispatch(request, *args,**kwargs)