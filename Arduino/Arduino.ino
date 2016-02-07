#include "pindef.h"
#include <string.h>
#include <stdint.h>

#define UP 4
#define DOWN 5
#define LEFT 6 
#define RIGHT 7

#define SELECT 8
#define START 9

#define A 10
#define B 11

#define LED 12

void setup() {
    // initialize serial communication at 9600 bits per second:
    Serial.begin(9600);

    pinMode(UP, INPUT_PULLUP);
    pinMode(DOWN, INPUT_PULLUP);
    pinMode(LEFT, INPUT_PULLUP);
    pinMode(RIGHT, INPUT_PULLUP);

    pinMode(A, INPUT_PULLUP);
    pinMode(B, INPUT_PULLUP);

    pinMode(SELECT, INPUT_PULLUP);
    pinMode(START, INPUT_PULLUP);

    pinMode(LED, OUTPUT);

    while(!Serial.available())
    {
        String challenge = Serial.readString();
        if (challenge == "Hi. Who are you?")
        {
            Serial.write("Hi. I'm HES.\n");
            break;
        }
        delay(100);
    }   
}


void loop()
{
    while(true)
    {
        if (!digitalRead(UP)) Serial.write("up\n");
        if (!digitalRead(DOWN)) Serial.write("down\n");
        if (!digitalRead(LEFT)) Serial.write("left\n");
        if (!digitalRead(RIGHT)) Serial.write("right\n");
      
        if (!digitalRead(A)) Serial.write("a\n");
        if (!digitalRead(B)) Serial.write("b\n");

        if (!digitalRead(SELECT)) Serial.write("select\n");
        if (!digitalRead(START)) Serial.write("start\n");
    
        delay(10);
    }
}

