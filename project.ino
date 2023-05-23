#include <Adafruit_MPL3115A2.h>
#include <Wire.h>
#include <DHT.h>

#define DHTPIN 2          // Digital pin connected to the DHT sensor
#define DHTTYPE DHT11     // DHT 11

#define AUDIOPIN A3

#define ECHOPIN 3
#define TRIGPIN 4

#define PHOTOPIN A0

DHT dht(DHTPIN, DHTTYPE);

Adafruit_MPL3115A2 baro = Adafruit_MPL3115A2();

long duration;
int distance;

void setup() {
  dht.begin();
  baro.begin();
  
  pinMode(AUDIOPIN, INPUT);

  pinMode(ECHOPIN, INPUT);
  pinMode(TRIGPIN, OUTPUT);
  
  Serial.begin(9600);
  
  delay(10);
}

void loop() {
  float humidity = dht.readHumidity();
  float temp = dht.readTemperature();
  
  float pressure = baro.getPressure();
  float sound = analogRead(AUDIOPIN);

  int light = analogRead(PHOTOPIN);
  
  if (isnan(humidity) || isnan(temp)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  digitalWrite(TRIGPIN, LOW);
  delayMicroseconds(2);

  digitalWrite(TRIGPIN, HIGH);
  delayMicroseconds(10);

  digitalWrite(TRIGPIN, LOW);

  duration = pulseIn(ECHOPIN, HIGH);
  distance = duration * 0.0344 / 2;


  Serial.print(temp);
  Serial.print("\t");

  Serial.print(humidity);
  Serial.print("\t");
  
  Serial.print(pressure);
  Serial.print("\t");

  Serial.print(sound);
  Serial.print("\t");

  Serial.print(distance);
  Serial.print("\t");

  //Serial.print(duration);
  //Serial.print("\t");

  Serial.print(light);
  Serial.print("\t");

  Serial.println();

  delay(10); 
}
