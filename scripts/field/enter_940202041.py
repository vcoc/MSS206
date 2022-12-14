# id 940202041 (null), field 940202041
sm.lockInGameUI(True, False)
sm.hideUser(True)
sm.blind(True, 255, 0, 0, 0, 0)
sm.spawnNpc(3001378, 800, 30)
sm.showNpcSpecialActionByTemplateId(3001378, "summon", 0)
sm.spawnNpc(3001379, 440, 30)
sm.showNpcSpecialActionByTemplateId(3001379, "summon", 0)
sm.spawnNpc(3001380, 1250, 30)
sm.showNpcSpecialActionByTemplateId(3001380, "summon", 0)
sm.spawnNpc(3001381, 1600, 30)
sm.showNpcSpecialActionByTemplateId(3001381, "summon", 0)
sm.spawnNpc(3001306, 1320, 30)
sm.showNpcSpecialActionByTemplateId(3001306, "summon", 0)
sm.spawnNpc(3001306, 1370, 30)
sm.showNpcSpecialActionByTemplateId(3001306, "summon", 0)
sm.spawnNpc(3001313, 1440, 30)
sm.showNpcSpecialActionByTemplateId(3001313, "summon", 0)
sm.showNpcSpecialActionByTemplateId(3001378, "dot", -1)
sm.showNpcSpecialActionByTemplateId(3001379, "dot", -1)
sm.showNpcSpecialActionByTemplateId(3001380, "dot", -1)
sm.showNpcSpecialActionByTemplateId(3001381, "dot", -1)
sm.sendDelay(5000)
sm.createFieldTextEffect("#fnﾳﾪﾴﾮﾰ￭ﾵ￱ ExtraBold##fs18#Several Hours Earlier, Village Square", 100, 2200, 6, -50, -50, 1, 4, 0, 0, 0)
sm.blind(True, 255, 0, 0, 0, 0)
sm.sendDelay(1200)
sm.blind(False, 0, 0, 0, 0, 1000)
sm.sendDelay(1400)
sm.sendDelay(1000)
sm.showNpcSpecialActionByTemplateId(3001378, "open", 0)
sm.playSound("Sound/SoundEff.img/illium/cg_open", 100)
sm.sendDelay(1500)
sm.flipNpcByTemplateId(3001306, True)
sm.flipNpcByTemplateId(3001306, True)
sm.flipNpcByTemplateId(3001313, True)
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, -20, 0, 81030125, 0, 0)
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, -20, 0, 81030126, 0, 0)
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, -20, 0, 81030127, 0, 0)
sm.sendDelay(1500)
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(3001306) # Soldier
sm.sendNext("#face1#Why is the gate opening?")
sm.spawnNpc(3001372, 1052, 4)
sm.showNpcSpecialActionByTemplateId(3001372, "summon", 0)
sm.sendDelay(300)
sm.spawnNpc(3001372, 1002, 4)
sm.showNpcSpecialActionByTemplateId(3001372, "summon", 0)
sm.sendDelay(300)
sm.spawnNpc(3001372, 952, 4)
sm.showNpcSpecialActionByTemplateId(3001372, "summon", 0)
sm.sendDelay(300)
sm.spawnNpc(3001372, 902, 4)
sm.showNpcSpecialActionByTemplateId(3001372, "summon", 0)
sm.sendDelay(300)
sm.spawnNpc(3001372, 702, 4)
sm.showNpcSpecialActionByTemplateId(3001372, "summon", 0)
sm.sendDelay(300)
sm.spawnNpc(3001372, 652, 4)
sm.showNpcSpecialActionByTemplateId(3001372, "summon", 0)
sm.sendDelay(300)
sm.spawnNpc(3001372, 602, 4)
sm.showNpcSpecialActionByTemplateId(3001372, "summon", 0)
sm.sendDelay(300)
sm.spawnNpc(3001372, 552, 4)
sm.showNpcSpecialActionByTemplateId(3001372, "summon", 0)
sm.sendDelay(2000)
sm.sendNext("#face1#S-Specters?!")
sm.setInnerOverrideSpeakerTemplateID(3001313) # Curly
sm.sendSay("#face1#How could we have been discovered...?")
sm.sendSay("#face1#Stay calm! If we can manage to close the gate, we'll be safe.")
sm.spawnNpc(3001309, 800, 4)
sm.showNpcSpecialActionByTemplateId(3001309, "summon", 0)
sm.setInnerOverrideSpeakerTemplateID(3001309) # Darius
sm.sendSay("#face2#Don't be so sure.")
sm.setInnerOverrideSpeakerTemplateID(3001313) # Curly
sm.sendSay("#face1#Darius?")
sm.sendDelay(1000)
sm.showNpcSpecialActionByTemplateId(3001379, "open", 0)
sm.playSound("Sound/SoundEff.img/illium/cg_open", 100)
sm.sendDelay(1000)
sm.showNpcSpecialActionByTemplateId(3001380, "open", 0)
sm.playSound("Sound/SoundEff.img/illium/cg_open", 100)
sm.sendDelay(1000)
sm.showNpcSpecialActionByTemplateId(3001381, "open", 0)
sm.playSound("Sound/SoundEff.img/illium/cg_open", 100)
sm.sendDelay(1500)
sm.sendNext("#face1#What's gotten into you?")
sm.sendSay("#face1#Why would you...")
sm.sendSay("#face1#How could you betray your own people?")
sm.setInnerOverrideSpeakerTemplateID(3001309) # Darius
sm.sendSay("#face2#I would rather destroy everything than see our future tainted\r\nby the abominations created by engineers like you.")
sm.sendSay("#face3#What are you waiting for? Eliminate them!")
sm.moveNpcByTemplateId(3001372, False, 500, 100)
sm.moveNpcByTemplateId(3001372, False, 500, 100)
sm.moveNpcByTemplateId(3001372, False, 500, 100)
sm.moveNpcByTemplateId(3001372, False, 500, 100)
sm.moveNpcByTemplateId(3001372, False, 500, 100)
sm.moveNpcByTemplateId(3001372, False, 500, 100)
sm.moveNpcByTemplateId(3001372, False, 500, 100)
sm.moveNpcByTemplateId(3001372, False, 500, 100)
sm.sendDelay(1500)
sm.blind(True, 255, 0, 0, 0, 500)
sm.sendDelay(500)
sm.lockInGameUI(False, True)
sm.warp(940202029)
