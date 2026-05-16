#include <raylib.h>
#include <stdlib.h>

void c_clear_background(
    unsigned char r,
    unsigned char g,
    unsigned char b,
    unsigned char a
) {
    Color background_color = {r, g, b, a};
    ClearBackground(background_color);
}

void c_draw_rectangle(
    int x,
    int y,
    int width,
    int height,
    unsigned char r,
    unsigned char g,
    unsigned char b,
    unsigned char a
) {
    Color rec_color = {r, g, b, a};
    DrawRectangle(x, y, width, height, rec_color);
}

void c_draw_circle(
    int x,
    int y,
    float radius,
    unsigned char r,
    unsigned char g,
    unsigned char b,
    unsigned char a
) {
    Color circle_color = {r, g, b, a};
    DrawCircle(x, y, radius, circle_color);
}

void c_draw_text(
    const char *text,
    int x,
    int y,
    int font_size,
    unsigned char r,
    unsigned char g,
    unsigned char b,
    unsigned char a
) {
    Color text_color = {r, g, b, a};
    DrawText(text, x, y, font_size, text_color);
}

// Functions with pointers

// Images
void* c_load_image(const char* file_name) {
    Image* img = (Image*)malloc(sizeof(Image));
    *img = LoadImage(file_name);
    return (void*)img;
}

void c_unload_image(void* handle) {
    Image* img = (Image*)handle;
    UnloadImage(*img);
    free(img);
}

// Textures
void* c_texture2d(void* image) {
    Image* img = (Image*)image;
    Texture2D* texture = (Texture2D*)malloc(sizeof(Texture2D));
    *texture = LoadTextureFromImage(*img);
    return (void*)texture;
}

void c_unload_texture(void* texture_pointer) {
    Texture2D* texture = (Texture2D*)texture_pointer;
    UnloadTexture(*texture);
    free(texture);
}

void c_draw_texture(
    void* texture_pointer,
    int x,
    int y,
    unsigned char r,
    unsigned char g,
    unsigned char b,
    unsigned char a
) {
    Texture2D* texture = (Texture2D*)texture_pointer;
    Color color = {r, g, b, a};
    DrawTexture(*texture, x, y, color);
}