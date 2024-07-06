from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages

def proveedorRequerido(view_func):
    
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if request.user.groups.filter(name='proveedor').exists():
            return view_func(request, *args, **kwargs)
        else:
            messages.error(request, 'Acceso denegado. No tienes permiso para acceder a esta página.')
            return redirect('loginProveedor')
    return _wrapped_view
