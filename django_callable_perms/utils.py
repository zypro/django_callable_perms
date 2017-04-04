def autoload_permission_checks():
    from django.conf import settings
    from importlib import import_module
    from django.utils.module_loading import module_has_submodule
    
    for app in settings.INSTALLED_APPS:
        mod = import_module(app)
        try:
            import_module('%s.permissions' % app)
        except:
            if module_has_submodule(mod, 'permissions'):
                raise

