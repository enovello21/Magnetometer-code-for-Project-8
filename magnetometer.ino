/*
    This sketch combines a Serial connection
      with I2C MLX90393 magnetometer communication. This is to be used with the
      magnetometer_readings python program, which writes the data to a txt file
      Magnetometer readings are in units of microTesla.
*/
#include <MLX90393.h>
#define N_Mag 4
MLX90393 mlx[N_Mag];

void setup()
{
  Serial.begin(115200);

  
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
 
  if (Serial.available()){
    Serial.read();
    for (uint8_t i=0; i < 2; i++) {
      measurement(i);
    }

  }

}
