from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.
def loader(request):
    return render(request ,'loader.html')

def portfolio(request):
    return render(request,'homepage.html')

def sendmail(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        subject = f"New Contact Form Submission from {name}"
        body = f"""
        Name: {name}
        From: {email}
        Phone: {phone}
        Message:{message}
        """

        try:
            send_mail(
                subject=subject,
                message=body,
                from_email="manmadhajayamangala@gmail.com",  # Replace with your email
                recipient_list=["manmadhajayamangala777@gmail.com"],  # Replace with your email
                fail_silently=False,
            )
            messages.info(request, "Your email has been sent successfully!")
            return render(request, "success.html", {"open_new_tab": True})
        except Exception as e:
            messages.info(request, "Failed to send email. Please try again later.")
            return render(request, "failure.html", {"open_new_tab": True})
        
def success(request):
    return render(request, 'success.html')