from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from .forms import RepairForm
from .models import Repair, User
from .decorators import login_required_message
from django.db.models import Count


@login_required_message
def home(request):
    if request.user.is_staff:  # 僅限管理員可以查看以及刪除報修
        if request.method == 'POST':
            repair_ids = request.POST.getlist('repair_ids')
            Repair.objects.filter(id__in=repair_ids).delete()
            return redirect('home')
        else:
            repairs = Repair.objects.all()
            user_ids_with_repairs = repairs.values_list('user_id', flat=True).distinct()
            users_with_repairs = User.objects.filter(id__in=user_ids_with_repairs)
            categories = repairs.values_list('category', flat=True).distinct()

            # 過濾條件
            user_id = request.GET.get('user')
            category = request.GET.get('category')

            if user_id:
                repairs = repairs.filter(user_id=user_id)
            if category:
                repairs = repairs.filter(category=category)

            category_counts = repairs.values('category').annotate(count=Count('category'))
            context = {
                'repairs': repairs,
                'users': users_with_repairs,
                'categories': categories,
                'category_counts': category_counts,
            }
            return render(request, 'home.html', context)
    else:
        return redirect('submit_report')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required_message
def submit_report(request):
    if request.method == 'POST':
        form = RepairForm(request.POST)
        if form.is_valid():
            repair = form.save(commit=False)
            repair.user = request.user  # 將報修項目關聯到當前使用者
            repair.save()
            return redirect('report_success')
    else:
        form = RepairForm()
    return render(request, 'submit_report.html', {'form': form})

@login_required_message
def report_success(request):
    return render(request, 'report_success.html')

@login_required_message
def complete_repair(request, repair_id):
    repair = Repair.objects.get(pk=repair_id)
    repair.completed = True
    repair.save()
    return redirect('home')

@login_required_message
def view_reports(request):
    user_repairs = Repair.objects.filter(user=request.user)
    return render(request, 'view_reports.html', {'user_repairs': user_repairs})
