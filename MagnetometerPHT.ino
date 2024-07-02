/*
    This sketch combines a Serial connection
      with I2C MLX90393 magnetometer communication. This is to be used with the
      magnetometer_readings python program, which writes the data to a txt file
      Magnetometer readings are in units of microTesla.
*/
#include <MLX90393.h>
#include "Adafruit_MLX90393.h"
#include <Adafruit_Sensor.h>
#include <Adafruit_MS8607.h>
Adafruit_MLX90393 sensor = Adafruit_MLX90393();
Adafruit_MS8607 ms8607;
#define N_Mag 4
MLX90393 mlx[N_Mag];
void setup()
{
  Serial.begin(115200);

  Wire.begin(17, 16);
  delay(1000);
  
 
  for(uint8_t j = 0; j < 2; j++){
    for(uint8_t i = 0; i < N_Mag; i++){
      mlx[i].I2C_BASE_ADDR = 0x18+i;
      Serial.println(mlx[i].begin(i/2, i%2)); // 255 return is BAD!!!
      delay(500);
    }
  }
  Serial.println("setup done");
  if (!ms8607.begin(&Wire,0x40)) {
    Serial.println("Failed to find MS8607 chip");
    while (1) { delay(10); }
  }
  Serial.println("MS8607 Found!");

  ms8607.setHumidityResolution(MS8607_HUMIDITY_RESOLUTION_OSR_8b);
  

  Serial.print("Humidity resolution set to ");
  switch (ms8607.getHumidityResolution()){
    case MS8607_HUMIDITY_RESOLUTION_OSR_12b: Serial.println("12-bit"); break;
    case MS8607_HUMIDITY_RESOLUTION_OSR_11b: Serial.println("11-bit"); break;
    case MS8607_HUMIDITY_RESOLUTION_OSR_10b: Serial.println("10-bit"); break;
    case MS8607_HUMIDITY_RESOLUTION_OSR_8b: Serial.println("8-bit"); break;
  }
  //ms8607.setPressureResolution(MS8607_PRESSURE_RESOLUTION_OSR_4096);
  
  Serial.print("Pressure and Temperature resolution set to ");
  switch (ms8607.getPressureResolution()){
    case MS8607_PRESSURE_RESOLUTION_OSR_256: Serial.println("256"); break;
    case MS8607_PRESSURE_RESOLUTION_OSR_512: Serial.println("512"); break;
    case MS8607_PRESSURE_RESOLUTION_OSR_1024: Serial.println("1024"); break;
    case MS8607_PRESSURE_RESOLUTION_OSR_2048: Serial.println("2048"); break;
    case MS8607_PRESSURE_RESOLUTION_OSR_4096: Serial.println("4096"); break;
    case MS8607_PRESSURE_RESOLUTION_OSR_8192: Serial.println("8192"); break;
    
  }
  Serial.println("");
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
    sensors_event_t temp, pressure, humidity;
    ms8607.getEvent(&pressure, &temp, &humidity);
    Serial.print("[");
    Serial.print(pressure.pressure); Serial.print(" hPa,");
    Serial.print(humidity.relative_humidity); Serial.print(" %rH,");
    Serial.print(temp.temperature); Serial.println(" C]");
   
  }

}
