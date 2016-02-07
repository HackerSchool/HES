#define PIN_START   0
#define PIN_SELECT  1
#define PIN_A       2
#define PIN_B       3
#define PIN_UP      4
#define PIN_RIGHT   5
#define PIN_DOWN    6
#define PIN_LEFT    7

void setup()
{
    Serial.begin(9600);

    // activate pull-up resistors for port D
    PORTD = ~(char)0;
}

unsigned char prev, curr=~0, diff;

void loop()
{
    prev = curr;
    curr = PIND;
    diff = curr^prev;

    for(int i=0; i<8; i++)
    {
        if(diff>>i & 1)
        {
            //Serial.println(i);
            if(curr>>i & 1) // key up
            {
                Serial.write(8 | i);
            }
            else    // key down
            {
                Serial.write(i);
            }
        }
    }

    //Serial.print(prev, BIN);
    //Serial.print(' ');
    //Serial.print(curr, BIN);
    //Serial.print(' ');
    //Serial.println(diff, BIN);
    delay(10);
}
