from django.shortcuts import render
from django.views.generic.list import ListView
# from django.views.generic.edit import UpdateView
from .models import UserProfile
from .forms import ProfileForm

# Create your views here.

class ProfileView(ListView):
    """List User Profile Model objects to display in template"""

    model = UserProfile
    # form_class = ProfileForm
    # initial = {'key': 'value'}
    template_name = 'profiles/userprofile.html'

    
    # def get_queryset(self, *args, **kwargs):
    #     return UserProfile.objects.filter(tags__slug=self.kwargs['slug'])


    # def user_profile(self, request):
    #     """User profile views with objects"""

    #     def get(self, request, *args, **kwargs):
    #         form = self.form_class(initial=self.initial)
    #         return render(request, self.template_name, {'form': form})

    #     def post(self, request, *args, **kwargs):
    #         form = self.form_class(request.POST)
    #         if form.is_valid():
    #             # <process form cleaned data>
    #             form_class.save()

    #         return render(request, self.template_name, {'form': form})

# class UpdateProfile(UpdateView):
#     """List User Profile Model objects to display in template"""

#     model = UserProfile
#     form_class = ProfileForm
#     template_name = 'profiles/userprofile.html'

#     def get(self, request, *args, **kwargs):
#             """User profile views with objects"""
#             form = self.form_class(initial=self.initial)
#             return render(request, self.template_name, {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             # <process form cleaned data>
#             form_class.save()

#         return render(request, self.template_name, {'form': form})

# def user_profile(request):
#     """User profile views with objects"""

#     users_profile = UserProfile.objects.get(user=request.user)
#     profile_form = ProfileForm(request.POST or None, request.FILES or None, instance=users_profile)
#     form_update = False
#     image_update = False

#     if request.method == 'POST' and profile_form.is_valid():
#         profile_form.save()
#         form_update = True

#     if request.FILES:
#         profile_form.save()
#         form_update = False
#         image_update = True
#         print("Image done!")

#     context = {
#         'users_profile': users_profile,
#         'profile_form': profile_form,
#         'form_update': form_update,
#         'image_update': image_update,
#     }
#     return render(request, 'profiles/userprofile.html', context)
