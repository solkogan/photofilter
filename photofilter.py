# Импортируем Pillow
from PIL import Image

# Функция bright отвечает за изменение яркости
# Первым параметром идёт имя jpg файла с фото
# вторым - имя под которым надо сохранить результат
# третьим параметром - значение яркости - если оно меньше единицы
# то будет затемнение, если больше - осветление картинки
def bright(source_name, result_name, brightness):
    source = Image.open(source_name)
    result = Image.new('RGB', source.size)
    for x in range(source.size[0]):
        for y in range(source.size[1]):
            r, g, b = source.getpixel((x, y))
            red = int(r * brightness)
            red = min(255, max(0, red))
            green = int(g * brightness)
            green = min(255, max(0, green))
            blue = int(b * brightness)
            blue = min(255, max(0, blue))
            result.putpixel((x, y), (red, green, blue))
    result.save(result_name, "JPEG")

# Функция negative преобразует фотографию в негатив
# Первым параметром идёт имя jpg файла с фото
# вторым - имя под которым надо сохранить результат
def negative(source_name, result_name):
    source = Image.open(source_name)
    result = Image.new('RGB', source.size)
    for x in range(source.size[0]):
        for y in range(source.size[1]):
            r, g, b = source.getpixel((x, y))
            result.putpixel((x, y), (255 - r, 255 - g, 255 - b))
    result.save(result_name, "JPEG")

# Функция white_black преобразует фото в черно белое
# Первым параметром идёт имя jpg файла с фото
# вторым - имя под которым надо сохранить результат
# третьим - яркость картинки
def white_black(source_name, result_name, brightness):
    source = Image.open(source_name)
    result = Image.new('RGB', source.size)
    separator = 255 / brightness / 2 * 3
    for x in range(source.size[0]):
        for y in range(source.size[1]):
            r, g, b = source.getpixel((x, y))
            total = r + g + b
            if total > separator:
                result.putpixel((x, y), (255, 255, 255))
            else:
                result.putpixel((x, y), (0, 0, 0))
    result.save(result_name, "JPEG")

# Функция gray_scale преобразует фото в оттенки серого
# Первым параметром идёт имя jpg файла с фото
# вторым - имя под которым надо сохранить результат 
def gray_scale(source_name, result_name):
    source = Image.open(source_name)
    result = Image.new('RGB', source.size)
    for x in range(source.size[0]):
        for y in range(source.size[1]):
            r, g, b = source.getpixel((x, y))
            gray = int(r * 0.2126 + g * 0.7152 + b * 0.0722)
            result.putpixel((x, y), (gray, gray, gray))
    result.save(result_name, "JPEG")

# Функция sepia преобразует фото в сепию
# Первым параметром идёт имя jpg файла с фото
# вторым - имя под которым надо сохранить результат
def sepia(source_name, result_name):
    source = Image.open(source_name)
    result = Image.new('RGB', source.size)
    for x in range(source.size[0]):
        for y in range(source.size[1]):
            r, g, b = source.getpixel((x, y))
            red = int(r * 0.393 + g * 0.769 + b * 0.189)
            green = int(r * 0.349 + g * 0.686 + b * 0.168)
            blue = int(r * 0.272 + g * 0.534 + b * 0.131)
            result.putpixel((x, y), (red, green, blue))
    result.save(result_name, "JPEG")

# Функция contrast меняет контраст
# Первым параметром идёт имя jpg файла с фото
# вторым - имя под которым надо сохранить результат
# третий - коэффициент контраста - больше единицы чтобы повысить контрастность
def contrast(source_name, result_name, coefficient):
    source = Image.open(source_name)
    result = Image.new('RGB', source.size)
    avg = 0
    for x in range(source.size[0]):
        for y in range(source.size[1]):
            r, g, b = source.getpixel((x, y))
            avg += r * 0.299 + g * 0.587 + b * 0.114
    avg /= source.size[0] * source.size[1]
    palette = []
    for i in range(256):
        temp = int(avg + coefficient * (i - avg))
        if temp < 0:
            temp = 0
        elif temp > 255:
            temp = 255
        palette.append(temp)
    for x in range(source.size[0]):
        for y in range(source.size[1]):
            r, g, b = source.getpixel((x, y))
            result.putpixel((x, y), (palette[r], palette[g], palette[b]))
    result.save(result_name, "JPEG")

# Тестируем функции
contrast("source.jpg", "contrast.jpg", 2)
sepia("source.jpg", "sepia.jpg")
bright("source.jpg", "bright_0.5.jpg", 0.5)
bright("source.jpg", "bright_1.5.jpg", 1.5)
negative("source.jpg", "negative.jpg")
white_black("source.jpg", "white_black_0.8.jpg", 0.8)
white_black("source.jpg", "white_black_1.2.jpg", 1.2)
gray_scale("source.jpg", "gray_scale.jpg")
