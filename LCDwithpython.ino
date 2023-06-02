
#include <LiquidCrystal.h>
#include <string.h>
#include <stdlib.h>

const int regSel = 3, enable = 2, dp0 = 4, dp1 = 5, dp2 = 6, dp3 = 7;
LiquidCrystal lcd(regSel, enable, dp0, dp1, dp2, dp3);

void setup() {
  // put your setup code here, to run once:
  //Define baud rate 
  Serial.begin(9600);
  //Defines the LCD's columns and rows
  lcd.begin(16, 2);
}

void loop() {
  // put your main code here, to run repeatedly:

  lcd.print("Enter a string");
  while(Serial.available() == 0) { }
  lcd.clear();

  String string1 = Serial.readString();

  int cond = Serial.read();

  if(cond == 1) {
    while(Serial.available() == 0) { }

    String string2 = Serial.readString();

    lcd.print(string1);
    lcd.setCursor(0,1);
    lcd.print("hey there");
  }
  else {
    lcd.print(string1);
  }

  delay(3000);
  lcd.clear();

}
