
// void setup() {
// 	Serial.begin(921600);
// }

// void loop() {
// 	Serial.println("hello world !");
// }




void setup() {
	pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {

    // LED on
	digitalWrite(LED_BUILTIN, HIGH);
    // 1초 대기
    delay(1000);


    // LED off
    digitalWrite(LED_BUILTIN, LOW);
    // 1초 대기
    delay(1000);
}




