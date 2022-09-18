# Maple Road: Maple Tree Hill (4000011)
# Custom Beginnings - Server Start Map
# Custom Server Script

server_name = sm.getServerName()

sm.setSpeakerID(2007) # Maple Administrator

if chr.getLevel() == 10:
    sm.removeEscapeButton()
    sm.sendSayOkay("Welcome to the world of #b" + server_name + "#k!\r\n\r\n#d(I will now send you to the 'Player Hub' to start your adventure.)#k")
    sm.warpToHub()
    sm.doJobStart()
    sm.giveStartItems()