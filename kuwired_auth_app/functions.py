from django.contrib.auth.models import User

def Create_user(form):
    first_name = form.cleaned_data.get('first_name')
    last_name = form.cleaned_data.get('last_name')
    email = form.cleaned_data.get('email')
    username = form.cleaned_data.get('username')
    password = form.cleaned_data.get('password')
    return  User.objects.create_user(
            username = username,
            password = password,
            email = email,
            first_name =first_name,
            last_name = last_name
        )
    
#def unique(value):
     
'''  
def insert_user_role(form,user):
    if form.cleaned_data.get('user_role') == "buyer":
        return Role.objects.create(username=user,is_buyer=True,is_seller=False)

    elif form.cleaned_data.get('user_role') == "seller":
        return Role.objects.create(username=user,is_buyer=False,is_seller=True)
    else:
        return None
          '''