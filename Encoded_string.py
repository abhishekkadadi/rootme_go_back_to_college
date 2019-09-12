import socket
import base64

server = "irc.root-me.org"       #settings
channel = b"#root-me_challenge"
botnick = b"AK"
sendtobot = b"candy"
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #defines the socket
def ginpong():
    while 1:    #puts it in a loop
       text1=irc.recv(2040)  #receive the text
       text=text1.decode("utf-8")
       print (text1)  #print text to console
       if text.find('PING') != -1:                          #check if 'PING' is found
          irc.send(b'PONG ' + text.split()[1].encode() + b'\r\n') #returnes 'PONG' back to the server (prevents pinging out!)
          break
def GetEm():
    irc.send(b"PRIVMSG "+sendtobot+b" :!ep2\r\n") # Start the challenge
    while 1:
        junk=b""
        junk=irc.recv(2040)
        junk = junk[(junk[1:].find(b":")) + 2:]
        string_to_decode=str(junk.rstrip().decode('utf-8'))
        if string_to_decode: # Just to make sure if we're receiving the challenge message
            try:
                decoded_string=bytes(base64.b64decode(string_to_decode))
                print(decoded_string)
                irc.send(b"PRIVMSG "+sendtobot+b" :!ep2 -rep "+decoded_string+b"\r\n") # send answer
                print(irc.recv(7000)) # Get validation password
                irc.send(b"QUIT :By3 By3!") # End up client session
                break
            except:
                print("[!] Waiting for challenge...")
print ("connecting to:"+server)
irc.connect((server, 6667))                                                         #connects to the server
irc.send(b"USER "+ botnick +b" "+ botnick +b" "+ botnick +b" :This is a fun bot!\n") #user authentication
irc.send(b"NICK "+ botnick +b"\n")                            #sets nick
irc.send(b"PRIVMSG nickserv :iNOOPE\r\n")    #auth
irc.send(b"JOIN "+ channel +b"\n")        #join the chan
print("[+] Playing PING PONG to impose our bot presence")
ginpong()
print("[+] Getting'em")
GetEm()
