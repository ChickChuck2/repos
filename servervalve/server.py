import valve.source
import valve.source.a2s
import valve.source.master_server

with valve.source.master_server.MasterServerQuerier() as msq:
    try:
        for address in msq.find(region=[u"eu", u"as"],
                                gamedir=u"GarrysMod",
                                map=u"gm_flatgrass"):
            with valve.source.a2s.ServerQuerier(address) as server:
                info = server.info()
                players = server.players()
            print("{player_count}/{max_players} {server_name}".format(**info))
            for player in sorted(players["players"],
                                 key=lambda p: p["score"], reverse=True):
                print("{score} {name}".format(**player))
    except valve.source.NoResponseError:
        print ("Master server request timed out!")