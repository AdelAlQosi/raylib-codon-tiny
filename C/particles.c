#include<raylib.h>

#define MAX_PARTICLES 5000

typedef struct Particle {
    Vector2 position;
    Vector2 velocity;
    float radius;
    Color color;
} Particle;

int main(void) {
    const int screenWidth = 1280;
    const int screenHeight = 720;

    InitWindow(screenWidth, screenHeight, "Random Particles");
    SetTargetFPS(60);
    
    Particle particles[MAX_PARTICLES];
    for (int i = 0; i < MAX_PARTICLES; i++) {
        particles[i].position = (Vector2){ GetRandomValue(0, screenWidth), GetRandomValue(0, screenHeight) };
        particles[i].velocity = (Vector2){ GetRandomValue(-200, 200) / 100.0f, GetRandomValue(-200, 200) / 100.0f };
        particles[i].radius = (float)GetRandomValue(1, 3);
        particles[i].color = (Color){ GetRandomValue(50, 255), GetRandomValue(50, 255), 255, 255 };
    }

    while (!WindowShouldClose()) {
        BeginDrawing();
        ClearBackground(BLACK);

        for (int i = 0; i < MAX_PARTICLES; i++) {
            Particle *particle = &particles[i];

            if (particle->position.x <= 0.0f || particle->position.x >= (float)screenWidth) {
                particle->velocity.x = -particle->velocity.x;   
            }
            if (particle->position.y <= 0.0f || particle->position.y >= (float)screenHeight) {
                particle->velocity.y = -particle->velocity.y;   
            }

            particle->position.x += particle->velocity.x;
            particle->position.y += particle->velocity.y;

            DrawCircle((int)particle->position.x, (int)particle->position.y, particle->radius, particle->color);
        }

        DrawFPS(10, 10);
        EndDrawing();
    }

    CloseWindow();
    return 0;
}