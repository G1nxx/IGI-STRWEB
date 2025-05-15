from django.utils import timezone
from .models import UserSession

class SessionTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            ses_key = request.session.session_key
            
            if not UserSession.objects.filter(
                user=request.user,
                session_key=ses_key,
                logout_time__isnull=True
            ).exists():
                UserSession.objects.create(
                    user=request.user,
                    session_key=ses_key,
                    login_time=timezone.now()
                )
        
        response = self.get_response(request)

        if request.user.is_authenticated:
            now = timezone.now()
            active_sessions = UserSession.objects.filter(
                user=request.user,
                session_key=request.session.session_key,
                logout_time__isnull=True
            )
            
            for session in active_sessions:
                session.duration = now - session.login_time
                session.save()
        
        return response