import os
from main import photos


def upload_profile_image(username, image, jwt_image):
    user_folder = os.path.join(username, "Profile_Image")
    if image:
        previous_image_name = jwt_image.split("/")[-1] if jwt_image else None
        print(previous_image_name)
        if previous_image_name:
            existing_image_path = os.path.join(
                "static", "images", user_folder, previous_image_name
            )
            print(existing_image_path)
            if os.path.exists(existing_image_path):
                os.remove(existing_image_path)
        filename = photos.save(image, folder=user_folder)
        return filename
    else:
        return "No se ha podido guardar la imagen"


def save_image(file, username, room_id):
    if file:
        file_path = os.path.join(username, room_id)
        filename = photos.save(file, file_path)
        return filename
    else:
        raise ValueError("Invalid file type.")


def delete_image(path):
    if path:
        new_path = path.replace("\\\\", "/")
        file_path = os.path.join("static", "images", new_path)
    if os.path.exists(file_path):
        os.remove(file_path)

    return "No se ha podido borrar la imagen"
