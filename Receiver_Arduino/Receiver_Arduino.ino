//For serial comm
char serialData;

//Robots main motor pins
const int leftpwm = 6;
const int leftf = 10;
const int leftb = 9;
const int rightf = 8;
const int rightb = 7;
const int rightpwm = 11;

String readString;

int constantspeed = 175;

void setup() {
  //Normal setup
  Serial.begin(9600);
  pinMode(leftpwm, OUTPUT);
  pinMode(leftf, OUTPUT);
  pinMode(leftb, OUTPUT);
  pinMode(rightf, OUTPUT);
  pinMode(rightb, OUTPUT);
  pinMode(rightpwm, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    serialData = Serial.read();
    if (serialData == 'a') {
      forward();
    }
    else if (serialData == 'b') {
      backward();
    }
    else if (serialData == 'e') {
      left();
    }
    else if (serialData == 'f') {
      right();
    }
    else if (serialData == 'c') {
      leftp();
    }
    else if (serialData == 'd') {
      rightp();
    }
    else if (serialData == 'g') {
      stopp();
    }
  }
}

void forward() {
  analogWrite(leftpwm, constantspeed);
  digitalWrite(leftf, HIGH);
  digitalWrite(leftb, LOW);
  digitalWrite(rightf, HIGH);
  digitalWrite(rightb, LOW);
  analogWrite(rightpwm, constantspeed);
}
void backward() {
  analogWrite(leftpwm, constantspeed);
  digitalWrite(leftf, LOW);
  digitalWrite(leftb, HIGH);
  digitalWrite(rightf, LOW);
  digitalWrite(rightb, HIGH);
  analogWrite(rightpwm, constantspeed);
}
void left() {
  analogWrite(leftpwm, constantspeed);
  digitalWrite(leftf, LOW);
  digitalWrite(leftb, HIGH);
  digitalWrite(rightf, HIGH);
  digitalWrite(rightb, LOW);
  analogWrite(rightpwm, constantspeed);
}
void right() {
  analogWrite(leftpwm, constantspeed);
  digitalWrite(leftf, HIGH);
  digitalWrite(leftb, LOW);
  digitalWrite(rightf, LOW);
  digitalWrite(rightb, HIGH);
  analogWrite(rightpwm, constantspeed);
}
void leftp() {
  analogWrite(leftpwm, constantspeed);
  digitalWrite(leftf, LOW);
  digitalWrite(leftb, LOW);
  digitalWrite(rightf, HIGH);
  digitalWrite(rightb, LOW);
  analogWrite(rightpwm, constantspeed);
}
void rightp() {
  analogWrite(leftpwm, constantspeed);
  digitalWrite(leftf, HIGH);
  digitalWrite(leftb, LOW);
  digitalWrite(rightf, LOW);
  digitalWrite(rightb, LOW);
  analogWrite(rightpwm, constantspeed);
}
void stopp() {
  analogWrite(leftpwm, 0);
  digitalWrite(leftf, LOW);
  digitalWrite(leftb, LOW);
  digitalWrite(rightf, LOW);
  digitalWrite(rightb, LOW);
  analogWrite(rightpwm, 0);
}
