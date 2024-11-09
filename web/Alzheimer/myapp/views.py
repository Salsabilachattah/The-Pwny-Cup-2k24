from django.shortcuts import render

from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt
# @require_POST
def submit_comment(request):
    comment = request.POST.get('comment', '')

    if len(comment) > 50:
        raise Exception("Comment exceeds 50 characters.")

    # Process the comment (e.g., save to the database, etc.)
    return JsonResponse({'message': 'Comment submitted successfully!'})

def show_page(request, page_number):
    # Simulate page content based on page number (e.g., fetch from database)
    content = f"Content for page {page_number}"
    return JsonResponse({'page': page_number, 'content': content})

def comment_form(request):
    return render(request, 'comment_form.html')

def index(request):
    return render(request, 'index.html')