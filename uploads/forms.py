from django import forms

MAX_UPLOAD_SIZE = 5 * 1024 * 1024  # 5MB
ALLOWED_CONTENT_TYPES = {
    "image/jpeg",
    "image/png",
    "application/pdf",
}

class UploadForm(forms.Form):
    file = forms.FileField()

    def clean_file(self):
        f = self.cleaned_data["file"]

        # size check
        if f.size > MAX_UPLOAD_SIZE:
            raise forms.ValidationError("حجم الملف كبير. الحد الأقصى 5MB.")

        # content-type check (basic)
        content_type = getattr(f, "content_type", "")
        if content_type not in ALLOWED_CONTENT_TYPES:
            raise forms.ValidationError("نوع الملف غير مسموح. فقط JPG/PNG/PDF.")

        return f
