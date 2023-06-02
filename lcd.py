import serial
import time

#create an instance of the serial object for the arduino.
# Replace the hashtag w/ the COM port that the arduino is on. The second parameter is the baud rate, adjust as needed.
arduinocom = serial.Serial('COM3', 9600)

while(True):

    inp = input('Enter a string to be displayed, or x to exit.\n')

    if(inp !=  'x'):
        pass
    else:
        print('You have exited')
        break

    if(len(inp) > 32):
        print("ERROR: String too long")
        inp = "Error"
    #Cond for if length is less than 16
    #elif(len(inp) < 16):
    else:
        null = ""
        cond = 0

        arduinocom.write(inp.encode()) #encode the data into bytes for the arduino to accept it, then write it
        arduinocom.write(cond) #encode the data into bytes for the arduino to accept it, then write it
        arduinocom.write(null.encode()) #encode the data into bytes for the arduino to accept it, then write it

"""
    else:
        inp1 = inp[0:16]
        inp2 = inp[16:]

        print(inp1)
        print(inp2)

        cond = 1

        arduinocom.write(inp1.encode()) #encode the data into bytes for the arduino to accept it, then write it
        arduinocom.write(cond) #encode the data into bytes for the arduino to accept it, then write it
        arduinocom.write(inp2.encode()) #encode the data into bytes for the arduino to accept it, then write it


"""
arduinocom.close()