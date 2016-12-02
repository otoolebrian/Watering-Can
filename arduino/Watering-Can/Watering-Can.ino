#include<SoftwareSerial.h>
#include"dht.h"
SoftwareSerial softSerial(10,11); //RX,TX

//Flag to check if there is an open connection
bool isConnectionOpen = false;

int pinSoil=18;

int pinTemp=12;

dht DHT;


void setup() 
{
  //Set the softSerial connection to be 9600
  softSerial.begin(9600);

  //Serial for debugging
  Serial.begin(9600);
  
  //Give the ESP module time to boot
  
  
  delay(3000);

  //Set the soil pin to read
  pinMode(pinSoil, INPUT);

}

void loop() 
{

  
  int soil = analogRead(pinSoil);
  Serial.print(String(soil)+" soil condition\n\r");
  /*int chk = DHT.read11(pinTemp);
  Serial.print("\r\nTemperature = ");
  Serial.println(DHT.temperature);
  Serial.print("\r\nHumidity = ");
  Serial.println(DHT.humidity);
  */
  delay(5000);
}

/*
 * Function to send a message to an open connection
 * Returns true if successful, false otherwise
 */
bool sendInfo(String message, String IP, String port)
{
  
  if(isConnectionOpen)
  {
    //Send the message, and delay for one second to allow the
    //operation to complete
    softSerial.print("AT+CIPSEND="+String(message.length())+"\r\n");
    delay(1000);
   
    //Send the message
    softSerial.print(message+"\r\n");
    delay(1000);

    return true;
  }
  else
  {
    return false;
  }

}

/*
 * Function to open connection to an IP and Port 
 */
void openConnection(String IP, String port)
{
  //if the connection is open, then close it
  if(isConnectionOpen)
  {
    closeConnection();
  }
  
  //Create the connection to the listening server
  softSerial.print("AT+CIPSTART=\"TCP\",\""+IP+"\","+port+"\r\n");

  //Delay to allow it to set up
  delay(1000);

  //Set flag to true
  isConnectionOpen = true;
}

//Close an open connection
void closeConnection()
{
  if(isConnectionOpen)
  {
    //Close the connection
    softSerial.print("AT+CIPCLOSE\r\n");
  }
  //Set the flag to be close
  isConnectionOpen = false;
}

int checkSoilDampness()
{
  
}

