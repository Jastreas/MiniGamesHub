//Possible Updates:
    /*
        Solve the traspassing pressing sd sa or dw ds which makes player loose
        Add different foods that buff or debuff the player
        Break the code in different files so its more readable
        Make the player have 3 lifes
        When player reach n points make a character congratulate or add pressure to the player
    */

#include <iostream>
#include <raylib.h>
#include <deque> //linked list
#include <raymath.h> //needed for the body push front method where we sum vector2 + vector2

using namespace std;

Color light_Green = {173, 204, 95, 255};
Color dark_Green = {43, 51, 24, 255};
bool Running = true;

//25 cells of 30 px size which = 750x750
int cellSize = 30; //grid cellsize
int cellCount = 25; //quantity of cells that will be displayed
int offset = 75;

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

bool element_In_Deque(Vector2 element, deque<Vector2> deque){

    for(unsigned int i = 0; i < deque.size(); i++){
        if(Vector2Equals(deque[i], element)){
            return true;
        }
    }
    return false;
}

class Snake{
    public:
        deque<Vector2> body = {Vector2{6, 9}, Vector2{5, 9}, Vector2{4, 9}}; //initial snake will be 3 squares long
        Vector2 direction {1, 0};
        bool addSegment = false;

    void Draw(){
        for(unsigned int i = 0; i < body.size(); i++){
            float x = body[i].x;
            float y = body[i].y;
            Rectangle segment = Rectangle{offset + x*cellSize,offset + y*cellSize, (float)cellSize, (float)cellSize};
            DrawRectangleRounded(segment, 0.5, 6, dark_Green);
        }
    }

    void Update(){
        body.push_front(Vector2Add(body[0], direction));//this function returns a vector2 with the new coordinates of snake
        if(addSegment == true){
            addSegment = false;
        } else{
            body.pop_back();
        }
    }

    void Reset(){
        body = {Vector2{6, 9}, Vector2{5, 9}, Vector2{4, 9}};
        direction = {1, 0};
    }
};

class Food{
    public:
        Vector2 position; //x, y --> this will represent cells not pixels
        Texture2D apple_Texture;

        //since I don't have the food png i will not load one, ill just use the square draw

        Food(deque<Vector2> snakeBody){ //constructor
            Image image = LoadImage("resources/ingameassets/appleResized.png");
            apple_Texture = LoadTextureFromImage(image);
            UnloadImage(image);
            position = generate_Random_Position(snakeBody);
        }

        ~Food(){ //destructor
            UnloadTexture(apple_Texture);
        }

        void Draw(){
            //constructor of DrawRectangles -> (pos.x, pos.y, width, height, color)
            //DrawRectangle(position.x * cellSize, position.y * cellSize, cellSize, cellSize, dark_Green); //we multiply x and y with the cellsize to make x and y the cell not pixel

            DrawTexture(apple_Texture, offset + position.x * cellSize, offset + position.y * cellSize, /*tint*/ WHITE);
        }

        Vector2 generate_Random_Cell(){
                float x = GetRandomValue(0, cellCount - 1); //integrated raylib function to generate random numbers
                float y = GetRandomValue(0, cellCount - 1); //integrated raylib function to generate random numbers
                return Vector2{x, y};
        }

        Vector2 generate_Random_Position(deque<Vector2> snakeBody){
                
                Vector2 position = generate_Random_Cell();

                while(element_In_Deque(position, snakeBody)){
                    position = generate_Random_Cell();
                }
                return position;
        }
};

class Game{ //better for mantainable code
    public:
        Snake snake = Snake();
        Food food = Food(snake.body);
        int score = 0;
        Sound eatSound;
        Sound borderSound;

        Game(){
            InitAudioDevice();
            eatSound = LoadSound("resources/audio/sfx/eat.mp3");
            borderSound = LoadSound("resources/audio/sfx/wall.mp3");
        }

        ~Game(){
            UnloadSound(eatSound);
            UnloadSound(borderSound);
            CloseAudioDevice();
        }


        void Draw(){
            food.Draw();
            snake.Draw();
        }

        void Update(){
            if(Running){
                snake.Update();
                check_Collision_With_Food();
                check_Collision_With_Edges();
                check_Collision_With_Tail();
            }
        }

        void check_Collision_With_Food(){
            if(Vector2Equals(snake.body[0], food.position)){
                food.position = food.generate_Random_Position(snake.body);
                snake.addSegment = true;
                PlaySound(eatSound);
                score++;
            }
        }

        void check_Collision_With_Edges(){

            if(snake.body[0].x == cellCount || snake.body[0].x == -1){
                game_Over();
            }
            if(snake.body[0].y == cellCount || snake.body[0].y == -1){
                game_Over();
            }
        }

        void game_Over(){
            snake.Reset();
            food.position = food.generate_Random_Position(snake.body);
            score = 0;
            Running = false;
            PlaySound(borderSound);
        }

        void check_Collision_With_Tail(){
            deque<Vector2> headlessBody = snake.body;
            headlessBody.pop_front();

            if(element_In_Deque(snake.body[0], headlessBody)){
                game_Over();
            }

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
    InitWindow(2*offset + cellSize*cellCount, 2*offset + cellSize*cellCount, "Retro Snake"); //creating a window
    SetTargetFPS(165); //necessary before gameloop

    Game game = Game();

    //loop
    while(WindowShouldClose() == false){ //checks if escape or cross are pressed

    //event handler
    if (event_Triggered(0.15)){
        game.Update();
    }
    if((IsKeyPressed(KEY_W) || IsKeyPressed(KEY_UP)) && game.snake.direction.y != 1){ //up
        game.snake.direction = {0, -1};
    }
    if((IsKeyPressed(KEY_D) || IsKeyPressed(KEY_RIGHT)) && game.snake.direction.x != -1){ //right
        game.snake.direction = {1, 0};
    }
    if((IsKeyPressed(KEY_S) || IsKeyPressed(KEY_DOWN)) && game.snake.direction.y != -1){ //down
        game.snake.direction = {0, 1};
    }
    if((IsKeyPressed(KEY_A) || IsKeyPressed(KEY_LEFT)) && game.snake.direction.x != 1){ //left
        game.snake.direction = {-1, 0};
    }
    if(IsKeyPressed(KEY_SPACE)){
        Running = true;
    }
    if(IsKeyPressed(KEY_P)){
        Running = false;
    }

    BeginDrawing(); //Begins the canvas drawing

    ClearBackground(light_Green);
    DrawRectangleLinesEx(Rectangle{(float)offset - 5, (float)offset - 5, (float)cellSize*cellCount+10, (float)cellSize*cellCount+10}, 5, dark_Green);
    DrawText("Retro Snake", offset - 5, 20, 40, dark_Green);
    DrawText(TextFormat("%i", game.score), offset - 5, offset + cellSize * cellCount + 10, 40, dark_Green);
    game.Draw();

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