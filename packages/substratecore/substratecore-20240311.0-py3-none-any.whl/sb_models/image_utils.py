def resize_to_resolution(input_image, resolution: int):
    from PIL import Image as PILImage

    input_image = input_image.convert("RGB")
    W, H = input_image.size
    minHW = min(H, W)
    if resolution is None:
        resolution = minHW * 2
    k = float(resolution) / minHW
    H *= k
    W *= k
    H = int(round(H / 64.0)) * 64
    W = int(round(W / 64.0)) * 64
    img = input_image.resize((W, H), resample=PILImage.Resampling.LANCZOS)
    return img


def crop_to_dimensions(input_image, width: int, height):
    from PIL import Image as PILImage

    target_ratio = width / height
    img_ratio = input_image.width / input_image.height

    if img_ratio > target_ratio:
        # If the image is wider than the target, resize based on height
        new_height = height
        new_width = int(new_height * img_ratio)
    else:
        new_width = width
        new_height = int(new_width / img_ratio)
    input_image = input_image.resize((new_width, new_height), resample=PILImage.Resampling.LANCZOS)

    # Calculate coordinates to crop the image at the center
    left = (new_width - width) / 2
    top = (new_height - height) / 2
    right = (new_width + width) / 2
    bottom = (new_height + height) / 2
    input_image = input_image.crop((left, top, right, bottom))
    return input_image
