# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import socket
import struct

port=37 #port needed for RFC 868
bufferSize= 32   #the time returned is a 32 bit unsigned integer
servers=["time-c-g.nist.gov", "utcnist.colorado.edu"]  #list that stores names of servers
ServersTimes=[]  #list that stores the actual time of each server in the list Servers

for i in range (2):#This implementation is helpful when we want to work with several servers 
    #and compare their time
    
    #Create a socket at each iteration,one for each server
    mysocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM ) 
    
    #Connect to each server with the corresponding port (port #37)
    mysocket.connect(( servers[i], port ))
    
    #Receive response: time of the server
    time_string=mysocket.recv( bufferSize )
    data, = struct.unpack('!I', time_string) 
    #This is used to convert the time from hexadecimal to seconds
    
    #Record the values of servers' times and store them in the Times array
    ServersTimes.append(data)
    
    #close each socket
    mysocket.close 








#Displays and conclusions:
print("When it comes to the IPs:")
print("The IP of the first server is:",socket.gethostbyname(servers[0]))
print("The IP of the second server is:", socket.gethostbyname(servers[1]))
print("")
print("When it comes to the servers' times:")
print("The actual time of the first server in seconds is:", ServersTimes[0],"secs or",ServersTimes[0]//(365*24*3600), "years since 1 JAN 1900", "-> in year", 1900+ServersTimes[0]//(365*24*3600))
print("The actual time of the second server in seconds is:", ServersTimes[1],"secs or",ServersTimes[1]//(365*24*3600), "years since 1 JAN 1900", "-> in year", 1900+ServersTimes[1]//(365*24*3600))
print("The difference in time between the two times retrieved is:",abs(ServersTimes[1]-ServersTimes[0]),"s"  )
print("")
print("")
print("")
print("Conclusion:")
print("")
print("The 2 servers' names are: time-c-g.nist.gov and utcnist.colorado.edu")
print("This slight difference is expected since the two servers are at 2 different locations, but not that considerable since these 2 servers are still located in the US.")
print("However, if we take two servers in the exact same location,having close IP adresses, we will get a 0s of time difference.")

 