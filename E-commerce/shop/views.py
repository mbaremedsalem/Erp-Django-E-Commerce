from django.shortcuts import render
from .models import Product,Order,Category
from django.core.paginator import Paginator
from .form import OrderForm,ProductForm
from .filters import ShopFilter

# Create your views here.
def shop_list(request):
    shop_list = Product.objects.all()
    #filters
    my_filter = ShopFilter(request.GET,queryset=shop_list)
    shop_list = my_filter.qs

    context = {'shops':shop_list,'my_filter':my_filter}
    return render(request,'shop/shop_list.html',context)
    

def shop_category(request):
    shop_category = Category.objects.all()
    context = {'category':shop_category}
    return render(request,'shop/shop_list.html',context)

def all_shops(request):
    all_shops = Product.objects.all()

    paginator = Paginator(all_shops, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'shops':page_obj}
    return render(request,'shop/all_product.html',context)

def shop_detaile(request,slug):
    shop_detail = Product.objects.get(slug=slug)   
    context = {'shop': shop_detail}
    return render(request,'shop/shop_detail.html',context)

def checkout(request):
    if request.method=="POST":
        form = OrderForm(request.POST)
        if form.is_valid():
           myform = form.save()
    else:
        form = OrderForm()
            
    return render(request,'shop/checkout.html',{'form':form})    


def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'profile':profile})
def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method=='POST':
        userform = UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(request.POST,request.FILES,instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))

    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)
    return render(request,'accounts/profile_edit.html',{'userform':userform,'profileform':profileform})      