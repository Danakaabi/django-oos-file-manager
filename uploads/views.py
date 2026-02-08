import logging
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .forms import UploadForm
from .models import UploadedFile

logger = logging.getLogger(__name__)

# ======================================
# اختياري: تحقق بسيط (نوع/حجم)
# عدّلي القيم حسب احتياجك
# ======================================
MAX_FILE_SIZE_MB = 10
ALLOWED_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".pdf", ".docx", ".txt", ".zip"
}


def _is_allowed_file(uploaded_file) -> tuple[bool, str]:
    """
    تحقق بسيط من حجم وامتداد الملف.
    يرجع (True, "") إذا الملف مقبول، وإلا (False, سبب الرفض)
    """
    name = (uploaded_file.name or "").lower()

    # حجم الملف
    max_bytes = MAX_FILE_SIZE_MB * 1024 * 1024
    if uploaded_file.size and uploaded_file.size > max_bytes:
        return False, f"حجم الملف كبير. الحد الأقصى {MAX_FILE_SIZE_MB}MB."

    # امتداد الملف
    dot = name.rfind(".")
    ext = name[dot:] if dot != -1 else ""
    if ALLOWED_EXTENSIONS and ext not in ALLOWED_EXTENSIONS:
        return False, "نوع الملف غير مسموح."

    return True, ""


# ======================================
# Upload View
# ======================================
def upload_file(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            f = form.cleaned_data.get("file")

            if not f:
                messages.error(request, " لم يتم اختيار ملف. يرجى اختيار ملف للرفع.")
                return render(request, "uploads/upload.html", {"form": form})

            # تحقق أمان بسيط
            ok, reason = _is_allowed_file(f)
            if not ok:
                messages.error(request, reason)
                return render(request, "uploads/upload.html", {"form": form})

            try:
                obj = UploadedFile.objects.create(
                    original_name=f.name,
                    file=f,
                )
                messages.success(request, "تم رفع الملف بنجاح ✅")
                return redirect("upload_success", pk=obj.pk)

            except Exception:
                logger.exception("Upload failed")
                messages.error(request, "حدث  خطأ أثناء رفع الملف. قم بالرفع مرة اخرى.")

        else:
            messages.error(request, "تحقق من الملف وحاول مرة اخرى.")
    else:
        form = UploadForm()

    return render(request, "uploads/upload.html", {"form": form})


# ======================================
# Success View
# ======================================
def upload_success(request, pk: int):
    obj = get_object_or_404(UploadedFile, pk=pk)
    return render(request, "uploads/success.html", {"obj": obj})