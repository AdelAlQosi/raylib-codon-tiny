rl = __file__[:-11] + '/shared/raylib/libraylib.so'
bnd = __file__[:-11] + '/shared/bindings.so'

# From rl
from C import rl.InitWindow(int, int, cobj) -> None
from C import rl.SetTargetFPS(int) -> None
from C import rl.DrawFPS(int, int) -> None

# From rl referencing
from C import rl.CloseWindow() -> None as close_window
from C import rl.WindowShouldClose() -> bool as window_should_close
from C import rl.BeginDrawing() -> None as begin_drawing
from C import rl.EndDrawing() -> None as end_drawing

# From bnd
from C import bnd.c_clear_background(u8, u8, u8, u8) -> None
from C import bnd.c_draw_rectangle(int, int, int, int, u8, u8, u8, u8) -> None
from C import bnd.c_draw_circle(int, int, float32, u8, u8, u8, u8) -> None
from C import bnd.c_draw_text(cobj, int, int, int, u8, u8, u8, u8) -> None
from C import bnd.c_draw_texture(Ptr[byte], int, int, u8, u8, u8, u8) -> None

from C import bnd.c_load_image(cobj) -> Ptr[byte]
from C import bnd.c_unload_image(Ptr[byte]) -> None
from C import bnd.c_texture2d(Ptr[byte]) -> Ptr[byte]
from C import bnd.c_unload_texture(Ptr[byte]) -> None

# Serve
from raylib import *