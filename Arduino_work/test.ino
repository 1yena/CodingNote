

// void setup() {
// 	pinMode(LED_BUILTIN, OUTPUT);
// }


// void loop() {

//     // 두 번 깜빡이고 꺼짐.
//     // LED on
// 	digitalWrite(LED_BUILTIN, HIGH);
//     // 1초 대기
//     delay(1000);
//     // LED off
//     digitalWrite(LED_BUILTIN, LOW);
//     // 1초 대기
//     delay(1000);

//     digitalWrite(LED_BUILTIN, HIGH);
//     delay(1000);

//     while(1) {
        
//     }
	    
// }

void setup() {
    Serial.begin(9600);

    while (!Serial) {
    }

    Serial.println("hello world !");
}

void loop() {
    Serial.println("smail world !");
    delay(3000);
}




