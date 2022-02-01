from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CustomUser
# Create your views here.


@api_view(['POST'])
def update_profile(request):
    if request.method == 'POST':
        all_data = request.data
        # Check if the proper data is sent
        email = all_data.get('email')
        gender = all_data.get('gender')
        dob = all_data.get('date_of_birth')
        first_name = all_data.get('first_name')
        last_name = all_data.get('last_name')
        if gender is not None:
            user = CustomUser.objects.get(email=email)
            user.gender = gender
            user.save()
        if dob is not None:
            user = CustomUser.objects.get(email=email)
            user.date_of_birth = dob
            user.save()
        if first_name is not None:
            user = CustomUser.objects.get(email=email)
            user.first_name = first_name
            user.save()
        if last_name is not None:
            user = CustomUser.objects.get(email=email)
            user.last_name = last_name
            user.save()
        return Response("Updated Successfully", status=200)
    else:
        return Response(status=400)
