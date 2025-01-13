#include <iostream>
#include <raylib.h>
#include <deque> //linked list
#include <raymath.h> //needed for the body push front method where we sum vector2 + vector2

using namespace std;


Color light_Green = {173, 204, 95, 255};
Color dark_Green = {43, 51, 24, 255};

//25 cells of 30 px size which = 750x750
int cellSize = 30; //grid cellsize
int cellCount = 25; //quantity of cells that will be displayed

//used to slow down the snake
double last_Update_Time = 0; 
bool event_Triggered(double interval){
    double current_Time = GetTime();

    if(current_Time - last_Update_Time >= interval){
        last_Update_Time = current_Time;
        return true;
    } else {
        return false;
    }
}


class Snake{
    public:
        deque<Vector2> body = {Vector2{6, 9}, Vector2{5, 9}, Vector2{4, 9}}; //initial snake will be 3 squares long
        Vector2 direction {1, 0};

    void Draw(){
        for(unsigned int i = 0; i < body.size(); i++){
            float x = body[i].x;
            float y = body[i].y;
            Rectangle segment = Rectangle{x*cellSize, y*cellSize, (float)cellSize, (float)cellSize};
            DrawRectangleRounded(segment, 0.5, 6, dark_Green);
        }
    }

    void Update(){
        body.pop_back();
        body.push_front(Vector2Add(body[0], direction));//this function returns a vector2 with the new coordinates of snake
    }
};



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


    Snake snake = Snake();
    Food food = Food();


    //loop
    while(WindowShouldClose() == false){ //checks if escape or cross are pressed

    //event handler
    if (event_Triggered(0.2)){
        snake.Update();
    }
    if((IsKeyPressed(KEY_W) || IsKeyPressed(KEY_UP)) && snake.direction.y != 1){ //up
        snake.direction = {0, -1};
    }
    if((IsKeyPressed(KEY_D) || IsKeyPressed(KEY_RIGHT)) && snake.direction.x != -1){ //right
        snake.direction = {1, 0};
    }
    if((IsKeyPressed(KEY_S) || IsKeyPressed(KEY_DOWN)) && snake.direction.y != -1){ //down
        snake.direction = {0, 1};
    }
    if((IsKeyPressed(KEY_A) || IsKeyPressed(KEY_LEFT)) && snake.direction.x != 1){ //left
        snake.direction = {-1, 0};
    }

    BeginDrawing(); //Begins the canvas drawing

    ClearBackground(light_Green);
    snake.Draw();
    food.Draw();


    EndDrawing(); //Ends the canvas drawing 

    }






    //closing the window
    CloseWindow();

    return 0;
}

//structure of main:
/*
    1. event handling
    2. updating positions
    3. drawing objects
*/

//raylib uses structs for colors with rgb -> struct Color {red, green, blue, alpha} -> Color pure_White {255, 255, 255, 255}
//vector2 also are structs