from django.shortcuts import render
from django.db import IntegrityError
from django.http import JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import json
@csrf_exempt
def books(request):
    if request.method == 'GET':
        books = list(Book.objects.all().values())
        return JsonResponse({
            "books": books
        })

    elif request.method == 'POST':
        if request.content_type == 'application/json':
            data = json.loads(request.body)
        else:
            data = request.POST

        title = data.get('title')
        author = data.get('author')
        price = data.get('price')

        # Check if all required fields are provided
        if not title or not author or not price:
            return JsonResponse({'error': 'true', 'message': 'required field missing'}, status=400)

        # Create the Book instance
        book = Book(title=title, author=author, price=price)

        try:
            book.save()
            return JsonResponse(model_to_dict(book), status=201)
        except IntegrityError:
            return JsonResponse({'error': 'true', 'message': 'unable to save book'}, status=400)

    return JsonResponse({'error': 'true', 'message': 'method not allowed'}, status=405)
