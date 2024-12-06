from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from myApp.forms import ImageForm,ProfileForm
from myApp.models import Member, ImageModel,Profile
from django.contrib.auth import logout


def login(request):
    return render(request,'login.html')

def settings(request):
    return render(request,'settings.html')

def exploredetails(request):
    return render(request,'exploredetails.html')
def create(request):
    if request.method == "POST":
        members = Member(
            name=request.POST['name'],
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password'],

        )
        members.save()
        return redirect('/login')

    else:
        return render(request, 'createaccount.html')


def index(request):
    if request.method == 'POST':
        # Authenticate the user
        try:
            member = Member.objects.get(
                username=request.POST['username'],
                email=request.POST['email'],
                password=request.POST['password']
            )

            # Store the member's username or some unique identifier in the session
            request.session['user_id'] = member.id  # You can store the member's ID or another identifier

            # Fetch all images and render them
            images = ImageModel.objects.all()
            return render(request, 'index.html', {'images': images})

        except Member.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    # Check if user is already logged in by checking session
    if 'user_id' in request.session:
        # User is logged in, so just show the images
        images = ImageModel.objects.all()
        return render(request, 'index.html', {'images': images})

    # If not logged in, show the login page
    return render(request, 'login.html')


def faq(request):
    return render(request,'FAQS.html')

def about (request):
    return render(request,'about.html')

def explore(request):
    return render(request,'explore.html')

def forums(request):
    return render(request,'forums.html')

def profile(request):
    return render(request,'viewprofile.html')
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ImageForm()
    return render(request, 'uploadimage.html', {'form': form})

def image_list(request):
    images = ImageModel.objects.all()
    return render (request,'index.html',{'images':images})

def edit_image(request,image_id):
    image = get_object_or_404(ImageModel,id=image_id)

    if request.method == 'POST':
        form = ImageForm (request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ImageForm(instance=image)
    return render (request, 'edit_image.html',{'form':form, 'image':image})

def delete_image(request,image_id):
    image=get_object_or_404(ImageModel,id=image_id)
    if request.method=='POST':
        image.delete()
        return redirect('index')

    return render(request, 'delete_image.html', {'image':image})

def logout(request):
    request.session.flush()
    return redirect('login')


def view_profile(request):
    # Assume we have one profile, you can adjust for multiple profiles or specific profile lookup.
    profile = get_object_or_404(Profile, pk=1)  # Here pk=1 is just an example.
    return render(request, 'viewprofile.html', {'profile': profile})

def edit_profile(request):
    profile = get_object_or_404(Profile, pk=1)  # Adjust pk as needed

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'editprofile.html', {'form': form})




