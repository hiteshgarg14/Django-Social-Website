from django.http import HttpResponseBadRequest, HttpResponse

"""
Build custom decorators for your views if you find that you are repeating
the same checks in multiple views.
"""

def ajax_required(f):
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            #return HttpResponse("hi")
            return HttpResponseBadRequest()
        return f(request, *args, **kwargs)
    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap
