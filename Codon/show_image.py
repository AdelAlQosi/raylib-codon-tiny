from bindings import *

def main():
    init_window(1280, 720, 'Show Image')
    set_target_FPS(60)
    
    path = __file__[:__file__.rfind('/')] + '/assets/car_.png'

    image = load_image(path)
    texture = texture2d(image)
    unload_image(image)

    while not window_should_close():
        begin_drawing()
        clear_background(white)
        draw_texture(texture, 0, 0, white)
        draw_FPS(10, 10)
        end_drawing()
    
    unload_texture(texture)
    close_window()

main()