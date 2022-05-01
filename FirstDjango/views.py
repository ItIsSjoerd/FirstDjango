"""
To Render HTML Web Pages.
"""
from multiprocessing import context
from django.http import HttpResponse
from articles.models import Article
    
def name_printer(name):


    article_obj = Article.objects.get(id=3)

    
    context = {
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content,
        "name": name,
    }

    HTML_STRING = """
    <h1>{title} (ID: {id})</h1>
    <span>Hallo {name}, {content}.</span>
    """.format(**context)

    return HTML_STRING


def home_view(request):
    """
    Take in request.(Django sends request)
    Send HTML as response.
    """

    HTML_STRING = name_printer('sjoerd') + name_printer('sieger')

    return HttpResponse(HTML_STRING)
