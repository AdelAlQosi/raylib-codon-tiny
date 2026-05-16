# raylib-codon-tiny

> "What if I could write raylib games in Python syntax but compile them to native binaries and get C FPS?"

This is a tiny experiment: hand-rolled FFI bindings so [Codon](https://github.com/exaloop/codon) can talk to raylib. No code generators, no massive wrappers — just a thin C shim and some `from C import` magic.

Currently covers **16 functions** (windowing, drawing, textures, and some math types). Enough to make things move on screen.

---

## Demos

### Image viewer
![Image Demo](https://raw.githubusercontent.com/AdelAlQosi/raylib-codon-tiny/main/demos/demo_image.png)

### 5k particles @ 60 FPS (slow gif)
![Image Demo](https://raw.githubusercontent.com/AdelAlQosi/raylib-codon-tiny/main/demos/demo_particles.gif)

---

## How it works

Codon can call C functions directly with `from C import`, but raylib's API is full of structs and pointers that don't map cleanly. So there are three layers talking to each other:

### 1. Direct FFI (`bindings/__init__.py`)
For simple functions that only use primitives, Codon calls raylib straight up:

```python
from C import rl.InitWindow(int, int, cobj) -> None
from C import rl.WindowShouldClose() -> bool as window_should_close
```

`cobj` is Codon's way of passing a C string pointer, so `init_window` just forwards the title string directly to raylib.

### 2. The C Bridge (`bindings/bindings.c`)
Raylib loves structs. `Color` is `{r, g, b, a}`. `Image` and `Texture2D` are full structs with internal pointers. Codon can't pass these by value easily, so a tiny C shim sits in the middle:

- **Colors**: Instead of passing a `Color` struct, Codon passes four `u8` values. The shim reconstructs `Color {r, g, b, a}` and calls the real raylib function.
- **Pointers**: For images and textures, the shim `malloc`s the actual struct on the C heap, calls `LoadImage` / `LoadTextureFromImage` to fill it, then returns an opaque `void*` (which Codon sees as `Ptr[byte]`). Codon holds that opaque handle and passes it back to the shim for drawing or unloading. The shim casts it back to `Image*` or `Texture2D*`, does the work, then `free`s the memory.

This means Codon never has to know what an `Image` struct looks like in memory — it just babysits a pointer.

### 3. The Pythonic Layer (`bindings/raylib.py`)
Nobody wants to write `c_clear_background(255, 255, 255, 255)`. So there's a friendly Python wrapper that unpacks your `Color` object into the four `u8`s the shim expects:

```python
def clear_background(color: Color):
    c_clear_background(color.r, color.g, color.b, color.a)
```

Same for `draw_circle`, `draw_rectangle`, etc. This layer also gives you:
- Struct classes: `Vector2`, `Vector3`, `Color`, `Rectangle`, `Image`
- Predefined colors: `white`, `black`, `red`, `sky_blue`, `ray_white`, `blank`... all the raylib defaults.

**The full data flow looks like this:**

```
Your script (Codon syntax)
    ↓
Pythonic API (raylib.py) — unpacks Color/Vector2 into primitives
    ↓
FFI imports (__init__.py) — routes to either raylib directly or the shim
    ↓
C Bridge (bindings.c) — rebuilds structs, manages pointers, calls raylib
    ↓
libraylib.so — talks to the GPU
```

---

## What's inside?

```
raylib-codon-tiny/
├── C/
│   └── particles.c              # Same particle demo in pure C, for comparison
├── Codon/
│   ├── assets/
│   │   └── car_.png             # Demo asset
│   ├── bindings/
│   │   ├── __init__.py          # FFI imports (raylib + bridge)
│   │   ├── shared/              # Shared C code, like raylib itself, as a shared library (.so)
│   │   ├── bindings.c           # C shim for colors & pointer lifecycle
│   │   ├── raylib.py            # Pythonic structs, colors, and helpers
│   │   └── comp_bind.sh         # Build helper
│   ├── particles.py             # 5,000 bouncing particles at 60 FPS
│   └── show_image.py            # Texture loading demo
├── builds/
│   ├── particles                # Native binary (C version)
│   └── particles_codon          # Native binary (Codon version)
└── demos/
    ├── demo_image.png           # Screenshot of image demo
    └── demo_particles.webm      # Video of particles demo
```

---

## Quick start

```bash
# 1. Build the C bridge
cd Codon/bindings
gcc -shared -fPIC bindings.c -o shared/bindings.so -lraylib

# 2. Run stuff
cd ../..
codon run -release Codon/particles.py
codon run -release Codon/show_image.py
```

Or just use the pre-built binaries in `builds/` if you're lazy.

---

## Example

```python
from bindings import *

def main():
    init_window(800, 600, "hi mom")
    set_target_FPS(60)

    while not window_should_close():
        begin_drawing()
        clear_background(black)
        draw_circle(400, 300, 50, red)
        end_drawing()

    close_window()

main()
```

---

## Extending it

Adding a new raylib function is usually one of three paths:

**Path A — no arguments:**
If the function takes no arguments at all, import it with `as` to rename it:

```python
from C import rl.CloseWindow() -> None as close_window
from C import rl.WindowShouldClose() -> bool as window_should_close

**Path B — simple primitives with a string argument:**
If the function takes a string, add it directly in `bindings/__init__.py`, then add it to the API in `raylib.py`:
```python
# __init__.py
from C import rl.InitWindow(int, int, cobj) -> None

# raylib.py
def init_window(w, h, title):
    InitWindow(w, h, title.c_str()) # title.ptr works too
```

**Path C — structs or pointers:**
If it needs a `Color`, `Rectangle`, `Image*`, etc., write a thin wrapper in `bindings/bindings.c` that takes primitives or `void*` handles, rebuilds the raylib struct, and calls the real function. Then expose it in `__init__.py` and wrap it in `raylib.py` for a nice API.

Rinse and repeat until you have the full raylib API (or at least the parts you actually use).

(Path C can actually go in many ways, but they are not all explored here.)
---
## Experiments in progress

This is mostly me poking at how Codon talks to C. I have a few more FFI experiments I want to run — struct passing, callback bridging, overhead benchmarks. If they don't catch fire, they'll end up in here.

---
## License

Same as raylib: zlib/libpng. Basically — do whatever, just don't blame me if it breaks