#define UP 18
#define DOWN 2
#define LEFT 17 
#define RIGHT 19

#define SELECT 7
#define START 12

#define A 11
#define B 6

#define GND1 4
#define GND2 14
#define GND3 15

#define LED 13

void setup() {
    // initialize serial communication at 9600 bits per second:
    Serial.begin(9600);

    pinMode(GND1, OUTPUT);
    pinMode(GND2, OUTPUT);
    pinMode(GND3, OUTPUT);
    digitalWrite(GND1, LOW);
    digitalWrite(GND2, LOW);
    digitalWrite(GND3, LOW);

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

