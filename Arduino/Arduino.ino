#define DEBOUNCE 8 // (ms) half a frame at 60Hz
#define PRESSEDLOGICLEVEL LOW

#define GND1 4
#define GND2 15
#define GND3 11

#define SELECT 12
#define START 8
#define UP 14
#define DOWN 18
#define LEFT 16 
#define RIGHT 17
#define A 7
#define B 6

#define LED 10

byte buttons[] = {SELECT, START, UP, DOWN, LEFT, RIGHT, A, B}; // the analog 0-5 pins are also known as 14-19
#define NUMBUTTONS sizeof(buttons)

// we will track if a button is just pressed, just released, or 'currently pressed'
volatile byte pressed[NUMBUTTONS], justpressed[NUMBUTTONS], justreleased[NUMBUTTONS]; 

void setup() {
    // initialize serial communication at 9600 bits per second:
    Serial.begin(9600);

    pinMode(GND1, OUTPUT);
    pinMode(GND2, OUTPUT);
    pinMode(GND3, OUTPUT);
    digitalWrite(GND1, LOW);
    digitalWrite(GND2, LOW);
    digitalWrite(GND3, LOW);

    for (byte i=0; i < NUMBUTTONS; i++)
        pinMode(buttons[i], INPUT_PULLUP);

    pinMode(LED, OUTPUT);
    digitalWrite(LED, LOW);

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

    // Run timer2 interrupt every 15 ms
    TCCR2A = 0;
    TCCR2B = 1<<CS22 | 1<<CS21 | 1<<CS20;

    //Timer2 Overflow Interrupt Enable
    TIMSK2 |= 1<<TOIE2;

    digitalWrite(LED, HIGH);
}


void check_switches()
{
    static byte previousstate[NUMBUTTONS];
    static byte currentstate[NUMBUTTONS];
    static long lasttime;
    byte index;
  
    if (millis() < lasttime){ 
        lasttime = millis(); // we wrapped around, lets just try again
    }
   
    if (millis() < (lasttime + DEBOUNCE)) {
        return; // not enough time has passed to debounce
    }
    
    lasttime = millis(); // ok we have waited DEBOUNCE milliseconds, lets reset the timer
   
    for (index = 0; index < NUMBUTTONS; index++)
    {
        currentstate[index] = digitalRead(buttons[index]);   // read the button
       
        if (currentstate[index] != previousstate[index]) // state changed after the debounce delay
        {
          if (!pressed[index] && (currentstate[index] == PRESSEDLOGICLEVEL)) {              
              justpressed[index] = 1; // just pressed
          }
          else if (pressed[index] && (currentstate[index] == !PRESSEDLOGICLEVEL)) {              
              justreleased[index] = 1; // just released
          }
          
          if (PRESSEDLOGICLEVEL == HIGH) 
            pressed[index] = currentstate[index];   
          else 
            pressed[index] = !currentstate[index]; // the 'pressed' byte array uses HIGH to mean pressed 
        }
        previousstate[index] = currentstate[index];   // keep a running tally of the buttons
    }
}


SIGNAL(TIMER2_OVF_vect) {
  check_switches();
}


void loop()
{       
    for (byte i = 0; i < NUMBUTTONS; i++){
        if (justpressed[i]) {
            justpressed[i] = 0;
            Serial.print("P");
            Serial.println(i);            
        }
        if (justreleased[i]) {
            justreleased[i] = 0;
            Serial.print("R");
            Serial.println(i);
            
        }
        /*if (pressed[i]) {
            Serial.print(i, DEC);
            Serial.println(" pressed");
            // is the button pressed down at this moment
        }*/      
    }
    delay(1);
}

