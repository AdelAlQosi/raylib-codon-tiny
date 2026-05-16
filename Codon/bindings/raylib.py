from . import *

# Parts before basic colors in raylib.h were skipped

# structs
# basic structs
class Vector2:
    def __init__(self, x, y):
        self.x = float32(x)
        self.y = float32(y)

class Vector3:
    def __init__(self, x, y, z):
        self.x = float32(x)
        self.y = float32(y)
        self.z = float32(z)

class Vector4:
    def __init__(self, x, y, z, w):
        self.x = float32(x)
        self.y = float32(y)
        self.z = float32(z)
        self.w = float32(w)

Quaternion = Vector4

class Matrix:
    def __init__(self, m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15):
        self.m0 = float32(m0)
        self.m1 = float32(m1)
        self.m2 = float32(m2)
        self.m3 = float32(m3)
        self.m4 = float32(m4)
        self.m5 = float32(m5)
        self.m6 = float32(m6)
        self.m7 = float32(m7)
        self.m8 = float32(m8)
        self.m9 = float32(m9)
        self.m10 = float32(m10)
        self.m11 = float32(m11)
        self.m12 = float32(m12)
        self.m13 = float32(m13)
        self.m14 = float32(m14)
        self.m15 = float32(m15)

class Color:
    def __init__(self, r, g, b, a = 255):
        self.r = u8(r)
        self.g = u8(g)
        self.b = u8(b)
        self.a = u8(a)

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = float32(x)
        self.y = float32(y)
        self.width = float32(width)
        self.height = float32(height)

# pointers structs
class Image:
    def __init__(self, data, width, height, mipmaps, _format):
        self.data = data
        self.width = int32(width)
        self.height = int32(height)
        self.mipmaps = int32(mipmaps)
        self.format = int32(_format)

    def __init__(self, width, height, mipmaps, _format):
        # TODO: add/solve data
        self.width = int32(width)
        self.height = int32(height)
        self.mipmaps = int32(1)
        self.format = int32(_format)

# end of structs

# Predefined colors
light_gray = Color(200, 200, 200, 255)
gray = Color(130, 130, 130, 255)
dark_gray = Color(80, 80, 80, 255)
yellow = Color(253, 249, 0, 255)
gold = Color(255, 203, 0, 255)
orange = Color(255, 161, 0, 255)
pink = Color(255, 109, 194, 255)
red = Color(230, 41, 55, 255)
maroon = Color(190, 33, 55, 255)
green = Color(0, 228, 48, 255)
lime = Color(0, 158, 47, 255)
dark_green = Color(0, 117, 44, 255)
sky_blue = Color(102, 191, 255, 255)
blue = Color(0, 121, 241, 255)
dark_blue = Color(0, 82, 172, 255)
purple = Color(200, 122, 255, 255)
violet = Color(135, 60, 190, 255)
dark_purple = Color(112, 31, 126, 255)
beige = Color(211, 176, 131, 255)
brown = Color(127, 106, 79, 255)
dark_brown = Color(76, 63, 47, 255)
white = Color(255, 255, 255, 255)
black = Color(0, 0, 0, 255)
blank = Color(0, 0, 0, 0)
magenta = Color(255, 0, 255, 255)
ray_white = Color(245, 245, 245, 255)

# Functions redefinition
def clear_background(color: Color):
    r = color.r
    g = color.g
    b = color.b
    a = color.a
    c_clear_background(r, g, b, a)

def init_window(screen_width, screen_height, title):
    InitWindow(screen_width, screen_height, title.c_str())

def set_target_FPS(target_fps):
    SetTargetFPS(int(target_fps))

def draw_FPS(x, y):
    DrawFPS(int(x), int(y))

def draw_rectangle(x, y, width, height, color: Color):
    x, y, width, height = int(x), int(y), int(width), int(height)
    r, g, b, a = color.r, color.g, color.b, color.a
    c_draw_rectangle(x, y, width, height, r, g, b, a)

def draw_circle(x, y, radius, color: Color):
    x, y = int(x), int(y)
    radius = float32(radius)
    r, g, b, a = color.r, color.g, color.b, color.a
    c_draw_circle(x, y, radius, r, g, b, a)

def draw_text(text: str, x, y, font_size, color: Color):
    x, y = int(x), int(y)
    font_size = int(font_size)
    r, g, b, a = color.r, color.g, color.b, color.a
    c_draw_text(text.c_str(), x, y, font_size, r, g, b, a)

def load_image(file_path: str):
    return c_load_image(file_path.c_str())

def unload_image(image: Ptr[byte]):
    c_unload_image(image)

def texture2d(image: Ptr[byte]):
    return c_texture2d(image)

def unload_texture(texture: Ptr[byte]):
    c_unload_texture(texture)

def draw_texture(texture: Ptr[byte], x, y, color: Color):
    x, y = int(x), int(y)
    r, g, b, a = color.r, color.g, color.b, color.a
    c_draw_texture(texture, x, y, r, g, b, a)