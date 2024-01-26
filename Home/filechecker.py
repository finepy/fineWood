from django.core.exceptions import ValidationError

def validate_file_size(value):
    filesize = value.size
    
    if filesize > 2097152:  # 2MB in bytes (1024 bytes * 1024 bytes * 2)
        raise ValidationError("You cannot upload a file larger than 2MB.")
    else:
        return value
