import os
import requests
import base64
import json
from PIL import Image

import env

session = requests.Session()


def check_dir(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)


def check_file(file):
    if not os.path.exists(file):
        open(file, 'x').close()


def get_b64_image(path: str):
    with open(path, 'rb') as image:
        b64 = base64.b64encode(image.read())
    return b64.decode()


def download_image(url, dest_file) -> Image.Image:
    response = session.get(url)
    if response.status_code == 200:
        check_file(dest_file)
        with open(dest_file, 'wb') as file:
            file.write(response.content)

        image = Image.open(dest_file)
        image.filename = dest_file
        return image


def image_url(path: str) -> str:
    json_array = env.JSON
    json_array['images'] = [get_b64_image(path)]

    response = session.post(
        url=env.URL,
        headers=env.HEADERS,
        cookies=env.COOKIES,
        json=json_array
    )
    content = json.loads(response.text)
    if 'extra' not in content:
        return ''

    extra = json.loads(content['extra'])
    for url in list(set(extra['img_urls'])):
        if str(url).startswith(env.GENERATED):
            return url


def generate(photo: str, array: list[str]):
    for i in array:
        image = download_image(
            url=image_url(photo),
            dest_file=i
        )

        left = 25
        top = 25
        right = image.width - 25
        bottom = image.height - 205
        box = (left, top, right, bottom)

        area = image.crop(box)
        area.save(i)
