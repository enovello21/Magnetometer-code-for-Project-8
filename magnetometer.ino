/*
    This sketch combines a hardware ethernet connection
      with I2C MLX90393 magnetometer communication.
*/

#include <ETH.h>
#include <MLX90393.h>
#include<time.h>
#define N_Mag 4
MLX90393 mlx[N_Mag];
//Define telnet server parameters
#define MAX_SRV_CLIENTS 4
const byte charLim = 32;
const char terminator = '\n';

void setup()
{
  Serial.begin(115200);

  Serial.println("network and server setup initialized");
  
  Wire.begin(17, 16);
  delay(1000);
  //uint8_t status;
  for(uint8_t j = 0; j < 2; j++){
    for(uint8_t i = 0; i < N_Mag; i++){
      Serial.println(mlx[i].begin(i/2, i%2)); // 255 return is BAD!!!
      delay(500);
    }
  }
  Serial.println("setup done");
}


// function to record measurements from a magnetometer
void measurement(uint8_t magID)
{
  MLX90393::txyz data;
  
  mlx[magID].readData(data);
  Serial.print("[");
  Serial.print(data.x);
  Serial.print(" x,");
  Serial.print(data.y);
  Serial.print(" y,");
  Serial.print(data.z);
  Serial.print(" z,");
  Serial.print(data.t);
  Serial.println(" C]");
}

void loop()
{
  for (uint8_t i=0; i < 2; i++) {
    
    measurement(i);
  }
  delay(5000);
  Serial.print(millis()); 
  Serial.println(" ms");
}
