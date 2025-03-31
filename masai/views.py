from gc import get_objects
from django.db.models.fields import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import BlogKeyword
from masai.service.chatgptAi import ChatGptAi

def index(request):
    category_list = BlogKeyword.objects.order_by('-worked_date')
    context = {
        'category_list' : category_list,
        }
    return render(request, 'masai/index.html', context)

@csrf_exempt
def ai_request(request):
    if request.method == "POST":
        gptai = ChatGptAi()

        thema = request.POST.get('thema')
        category = request.POST.get('category')
        styleoption = request.POST.get('styleoption')
        toneoption = request.POST.get('toneoption')
        response = gptai.response_contents(category,styleoption,toneoption)

        # 여기서 AI 분석 로직 또는 기타 처리 수행
        response_data = f"'{thema}'와(과) '{category}' 분석 결과 예시입니다."

        return JsonResponse({'get_data': response})
    return JsonResponse({'error': 'Invalid request'}, status=400) 