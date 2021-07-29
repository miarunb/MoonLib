from django.core.mail import send_mail

def send_activation_mail(email, activation_code):
    activation_url = f'http://localhost:8000/account/activate/{activation_code}'
    message = f'Спасибо, что присоединились!\nПожалуйста, перейдите по ссылке ниже для активации вашего аккаунта:\n{activation_url}'
    send_mail(
        'Добро пожаловать на MoonLib!',
        message,
        'test@gmail.com',
        [email, ],
        fail_silently=False
    )