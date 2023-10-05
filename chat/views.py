from django.core.files.storage import default_storage
from django.shortcuts import render
from django.http import JsonResponse  # Import JsonResponse
from .models import ChatMessage
from django.contrib.auth.decorators import login_required
from core.ai.Brain.brain import ReplyBrain


@login_required
def chat_page(request):
    user = request.user
    print(user.name)
    print("User is logged in")
    if request.method == 'POST':
        # Check if it's a text message
        print("Post request Found")
        question = request.POST.get('question')
        print("Question is: ", question)
        if question:
            print("Question is being asked")
            try:
                print("Trying to get answer")
                answer = ReplyBrain(user.name, question)
                print("Answer is: ", answer)
                ChatMessage.objects.create(user=user, message=question)
                ChatMessage.objects.create(user=user, message=answer)

                # Return a JsonResponse when the message is sent successfully
                print("Sending Json Response")
                return JsonResponse({'status': 'success', 'message': 'Your message was sent successfully'})
                print("Json Response Sent")
            except Exception as exc:
                print("Exception is: ", exc)
                # Handle exceptions here, you may want to log them or provide an error message
                answer = f"Sorry, I don't understand.{exc}"
                print("Answer is: ", answer)
                ChatMessage.objects.create(user=user, message=question)
                ChatMessage.objects.create(user=user, message=answer)
                return JsonResponse({'status': 'success', 'message': answer})
                print("Json Response Sent")
        else:
            # Handle image upload
            image = request.FILES.get('image')
            if image:
                # Save the uploaded image to a unique path
                image_path = default_storage.save(f"chat/images/{user.username}/{image.name}", image)

                # Handle the comment
                comment = request.POST.get('comment')

                # Save the image and comment in the database
                ChatMessage.objects.create(user=user, message=f"Image: {image_path}")
                if comment:
                    ChatMessage.objects.create(user=user, message=f"Comment: {comment}")

    chat_history = ChatMessage.objects.filter(user=user)
    return render(request, 'chat_page.html', {'chat_history': chat_history})
