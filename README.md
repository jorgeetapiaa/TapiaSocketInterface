# TapiaSocketInterface
Interface using Python socket module
Program contains two files:
  theClient file is a client requesting a specific file through the interface from the server,
  if the file exists:
    it creates a folder, catches and decodes the file sent from the server, 
    and stores the data in a text file
  
  theServer file recieves the request from theclient, 
  if the file exists: 
    it sends the data encoded and line by line
    
