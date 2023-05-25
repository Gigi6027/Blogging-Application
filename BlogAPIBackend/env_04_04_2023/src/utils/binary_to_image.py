# importing base64 module
import base64
import os
from datetime import datetime as dt


def convert_binary_to_image(base64_binary, image_path=None, filename=None):
    encoded_data = base64_binary
    decoded_data = base64.b64decode((encoded_data))

    os.makedirs(image_path, exist_ok=True)
    img_file_path = os.path.join(image_path, filename)
    today_datetime = dt.now().strftime('%Y-%m-%d-%H-%M-%S-%f')

    filename, file_extension = os.path.splitext(img_file_path)
    img_file_path = filename + '_' + today_datetime + file_extension

    # write the decoded data back to original format in  file
    img_file = open(img_file_path, 'wb')
    img_file.write(decoded_data)
    img_file.close()
    return img_file_path


def convert_image_to_base64(image_file_path):
    with open(image_file_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    return encoded_string


def delete_image_file(image_file_path):
    if os.path.exists(image_file_path):
        os.remove(image_file_path)
    else:
        return "Invalid file path"
    return "File deleted."
