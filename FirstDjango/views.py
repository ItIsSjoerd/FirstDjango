"""
To Render HTML Web Pages.
"""
from django.http import HttpResponse

def name_print(name):
    
    HTML_STRING = f"""
    <h1>Hello, World!</h1>
    <span>Hallo {name}, dit is een test.</span>
    """

    return HTML_STRING


def home_view(request):

    """
    Take in request.(Django sends request)
    Send HTML as response.
    """

    HTML_STRING = name_print('sjoerd') + name_print('sieger')

    return HttpResponse(HTML_STRING)