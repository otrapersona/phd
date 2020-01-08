# proof of concept
# manda datos via serial con el formato x,.yyyyyyyyyy
# x incremental
# y al azar

int a=0;
float randNum=0;
float randDecimal=0;

void setup() {
  randomSeed(analogRead(0));
  Serial.begin(115200);
}

void loop() {
  a++;
  randNum = random(0, 100000001);
  randDecimal = randNum/100000000;
  Serial.print(a, DEC);
  Serial.print(",");
  Serial.println(randDecimal, DEC);
  delay(1000);
}
