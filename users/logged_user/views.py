import json
from django.http import HttpResponse
from oauth2_provider.decorators import protected_resource


@protected_resource()
def get_user(request):
    user = request.user
    return HttpResponse(
        json.dumps({'username': user.username,
                   'email': user.email, 'id': user.id}),
        content_type='application/json')
