"""Identify Image Type from the first few bytes. PNG, JPEG, and GIF."""

def image_type(file):
    """Returns str of file type. 'jpeg', 'png', 'gif'.
    Returns None if unable to identify file type"""
    if isinstance(file, str):
        f = open(file, 'rb')
        binary_string = f.read(32)
    else:
        binary_string = file.read(32)
    if binary_string[6:10] in (b'JFIF', b'Exif'):
        return 'jpeg'
    elif binary_string.startswith(b'\211PNG\r\n\032\n'):
        return 'png'
    elif binary_string[:6] in (b'GIF87a', b'GIF89a'):
        return 'gif'
    else:
        return None
