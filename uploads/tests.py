from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from .forms import UploadForm


class UploadFormTests(TestCase):
    def test_valid_png_under_limit(self):
        # ملف PNG بسيط (محتوى وهمي)
        file_obj = SimpleUploadedFile(
            "test.png",
            b"fake-image-content",
            content_type="image/png",
        )

        form = UploadForm(files={"file": file_obj})
        self.assertTrue(form.is_valid())

    def test_reject_disallowed_content_type(self):
        # ملف exe (غير مسموح)
        file_obj = SimpleUploadedFile(
            "malware.exe",
            b"fake-exe",
            content_type="application/octet-stream",
        )
        form = UploadForm(files={"file": file_obj})
        self.assertFalse(form.is_valid())
        self.assertIn("file", form.errors)

    def test_reject_large_file(self):
        # ملف أكبر من 5MB
        big_content = b"a" * (5 * 1024 * 1024 + 1)
        file_obj = SimpleUploadedFile(
            "big.pdf",
            big_content,
            content_type="application/pdf",
        )
        form = UploadForm(files={"file": file_obj})
        self.assertFalse(form.is_valid())
        self.assertIn("file", form.errors)
