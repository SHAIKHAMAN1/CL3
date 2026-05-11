#pip instal pyro4
import Pyro4

# python -m Pyro4.naming (in terminal and leave it running)

@Pyro4.expose
class StringConcatenationServer:
    def concatenate_strings(self, str1, str2):
        result = str1 + str2
        return result

def main():
    daemon = Pyro4.Daemon()  
    ns = Pyro4.locateNS()  
    
    server = StringConcatenationServer()
    
    uri = daemon.register(server)
    ns.register("string.concatenation", uri)
    print("Server URI:", uri)
    with open("server_uri.txt", "w") as f:
        f.write(str(uri))
    daemon.requestLoop()

if __name__ == "__main__":
    main()