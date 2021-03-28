from django.core.exceptions import ValidationError
from django.db.models import ImageField


class SizeRestrictedImageField(ImageField):
    """
        Custom ImageField to restrict the maximum size of the image file.
        500MB - 429916160

        required: max_upload_size
    """

    def __init__(self, max_upload_size=429916160, *args, **kwargs):
        self.max_upload_size = max_upload_size
        super().__init__(*args, **kwargs)

    def clean(self, value, model_instance):
        data = super().clean(value=value, model_instance=model_instance)
        uploaded_file = data.file
        if uploaded_file._size > self.max_upload_size:
            raise ValidationError("Uploaded file size is {}. Size limit: {}". \
                format(uploaded_file._size, self.max_upload_size), code="Invalid size")
        return data
