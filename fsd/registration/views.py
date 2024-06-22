from django.http import JsonResponse
from django.shortcuts import redirect, render

from .forms import StudentForm


def student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    else:
        form = StudentForm()
    return render(request, 'register_student.html', {'form': form})