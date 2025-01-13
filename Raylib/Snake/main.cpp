#include <iostream>
#include <raylib.h>

using namespace std;


Color light_Green = {173, 204, 95, 255};
Color dark_Green = {43, 51, 24, 255};

//25 cells of 30 px size which = 750x750
int cellSize = 30; //grid cellsize
int cellCount = 25; //quantity of cells that will be displayed






class Food{
    public:
        Vector2 position; //x, y --> this will represent cells not pixels
        Texture2D apple_Texture;

        //since I don't have the food png i will not load one, ill just use the square draw

        Food(){ //constructor
            Image image = LoadImage("resources/ingameassets/appleResized.png");
            apple_Texture = LoadTextureFromImage(image);
            UnloadImage(image);
            position = generate_Random_Position();
        }

        ~Food(){ //destructor
            UnloadTexture(apple_Texture);
        }

        void Draw(){
            //constructor of DrawRectangles -> (pos.x, pos.y, width, height, color)
            //DrawRectangle(position.x * cellSize, position.y * cellSize, cellSize, cellSize, dark_Green); //we multiply x and y with the cellsize to make x and y the cell not pixel

            DrawTexture(apple_Texture, position.x * cellSize, position.y * cellSize, /*tint*/ WHITE);
        }


        Vector2 generate_Random_Position(){
                float x = GetRandomValue(0, cellCount - 1); //integrated raylib function to generate random numbers
                float y = GetRandomValue(0, cellCount - 1); //integrated raylib function to generate random numbers

                return Vector2{x ,y};
        }
};



int main () {

    /*
    Removed this because they can be calculated with the cellSize and count since
    they are the main grid in the window

    window vars
    int window_Height = 750;
    int window_Width = 750;
    */

    cout << "Starting the game..." << endl;

    //Window Properties
    InitWindow(cellSize*cellCount, cellSize*cellCount, "Retro Snake"); //creating a window
    SetTargetFPS(60); //necessary before gameloop

    Food food = Food();

    while(WindowShouldClose() == false){ //checks if escape or cross are pressed

    BeginDrawing(); //Begins the canvas drawing

    ClearBackground(light_Green);
    food.Draw();


    EndDrawing(); //Ends the canvas drawing 

    }






    //closing the window
    CloseWindow();

    return 0;
}

//structure of main:
/*
    event handling
    updating positions
    drawing objects
*/

//raylib uses structs for colors with rgb -> struct Color {red, green, blue, alpha} -> Color pure_White {255, 255, 255, 255}
//vector2 also are structs