#include <VirtualWire.h>

const int led_pin = 13;
//const int transmit_pin = 1;
//const int receive_pin = 2;
const int receive_pin = 2;
//const int transmit_en_pin = 3;

void setup()
{
    Serial.begin(115200);	// Debugging only
    Serial.println("Starting receiver");
    
    vw_set_rx_pin(receive_pin);
    vw_set_ptt_inverted(true); // Required for DR3100
    vw_setup(500);	 // Bits per sec
    vw_rx_start();       // Start the receiver PLL running
    pinMode(led_pin, OUTPUT);
}

void loop()
{
    uint8_t buf[VW_MAX_MESSAGE_LEN];
    uint8_t buflen = VW_MAX_MESSAGE_LEN;

    if (vw_get_message(buf, &buflen)) // Non-blocking
    {
       // Flash a light to show received good message
        digitalWrite(led_pin, HIGH); 
        for (int i = 0; i < buflen; i++) {
            Serial.print((char)buf[i]);
        }
        Serial.println();
        
        digitalWrite(led_pin, LOW);
    }
}
