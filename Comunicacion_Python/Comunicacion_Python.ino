char lectura;

void setup() {
  Serial.begin(9600);
  pinMode(13,OUTPUT);

}

void loop() {
//  Serial.println("1");
//  delay(4000);

    lectura = Serial.read();
    //Serial.println(lectura);
    if(lectura == '1'){
      /*digitalWrite(13, HIGH);
      delay(1000);
      digitalWrite(13,LOW);*/
        for(int i=0; i<100; i++){
          Serial.println(i);
          // delay(100);
          }
      }  
}
