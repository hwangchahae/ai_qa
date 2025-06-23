import openai
from django.shortcuts import render
import os 
from dotenv import load_dotenv

load_dotenv()
def qa_view(request):
    answer = None
    if request.method == 'POST':
        question = request.POST.get('question') # 폼에서 가져옴
        response = openai.chat.completions.create(
            model = 'gpt-4o',
            messages = [
                {'role':'user', 'content':question}
            ]
        )
        answer = response.choices[0].message.content
        print(f'answer : {answer}')
    return render(request, 'qa/index.html', {'answer':answer})
