from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .utils import generate_chatbot_response

def index(request):
    chatbot_response = None

    if request.method == "POST":
        user_input = request.POST["user_input"]
        chatbot_response = generate_chatbot_response(user_input)

    return render(request, "index.html", {"chatbot_response": chatbot_response})
