from django import http

def sendfile(request, location, **kwargs):
    response = http.HttpResponse()
    response['X-Accel-Redirect'] = location
    del response['Content-Type'] # Let the proxy figure this out
    return response