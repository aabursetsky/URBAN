# -*- coding: utf-8 -*-

# Пример использования сторонней библиотеки на примере Pillow

# Задача: сделать поздравительную открытку другу на Halloween

import os
from PIL import Image, ImageDraw, ImageFont, ImageColor


class PostCardMaker:

    def __init__(self, name, template=None, font_path=None):
        self.name = name
        self.template = "post_card.jpg" if template is None else template           # имя файла исходника, если не template не указан
        if font_path is None:
            self.font_path = os.path.join("fonts", "ofont_ru_DS Eraser2.ttf")       # подкаталог шрифтов, если не указан - ./fonts
        else:
            self.font_path = font_path

    def make(self, resize=False, out_path=None, bw=False):
        im = Image.open(self.template)                                              # открытие файла исходника
        if resize:                                                                  # если нужно изменить размер
            w, h = im.size                                                          # получение текущего - высота x ширина (pic)
            im = im.resize((w // 2, h // 2))                                        # resize(), уменьшение в два раза
        draw = ImageDraw.Draw(im)                                                   # получение нового объекта на основе исходника
        font = ImageFont.truetype(self.font_path, size=26)

        y = im.size[1] - 10 - (10 + font.size) * 2
        message = f"Привет, {self.name}!"
        draw.text((10, y), message, font=font, fill=ImageColor.colormap['white'])     # верхняя строка

        y = im.size[1] - 20 - font.size                                                 # нижняя строка
        message = f"С праздником тебя!"
        draw.text((10, y), message, font=font, fill=ImageColor.colormap['green'])

        if bw:                                                                      # при желании конвертировать в серый
            im = im.convert('L')

        out_path = out_path if out_path else 'probe.jpg'
        im.save(out_path)
        print(f'Post card saved as {out_path}')


if __name__ == '__main__':
    maker = PostCardMaker(name='Михаил Юрьевич Лермонтов')
    maker.make(resize=True)
    maker.make(out_path='probebw.jpg', bw=True)
