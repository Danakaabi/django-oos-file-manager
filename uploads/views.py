import logging
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UploadForm
from .models import UploadedFile

logger = logging.getLogger(__name__)

def upload_file(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.cleaned_data["file"]
            try:
                obj = UploadedFile.objects.create(
                    original_name=f.name,
                    file=f,
                )
                messages.success(request, "تم رفع الملف بنجاح ✅")
                return redirect("upload_success", pk=obj.pk)
            except Exception:
                logger.exception("Upload failed")
                messages.error(request, "صار خطأ أثناء رفع الملف. جرّبي مرة ثانية.")
        else:
            messages.error(request, "تحقق من الملف وحاولي مرة ثانية.")
    else:
        form = UploadForm()

    return render(request, "uploads/upload.html", {"form": form})

def upload_success(request, pk: int):
    obj = UploadedFile.objects.get(pk=pk)
    return render(request, "uploads/success.html", {"obj": obj})
