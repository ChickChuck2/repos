import valve.rcon

server_address = ("192.168.1.104", 25577)
password = "top_secret"

with valve.rcon.RCON(server_address, password) as rcon:
    print(rcon("echo Hello, world!"))