# id 940200207 (Arcana : Grove of the Spirit Tree), field 940200207
sm.lockInGameUI(True, False)
sm.removeAdditionalEffect()
sm.blind(True, 255, 0, 0, 0, 0)
sm.zoomCamera(0, 1000, 0, 272, 30)
sm.spawnNpc(3003350, 272, 100)
sm.showNpcSpecialActionByTemplateId(3003350, "summon", 0)
sm.spawnNpc(3003351, 390, 100)
sm.showNpcSpecialActionByTemplateId(3003351, "summon", 0)
sm.sendDelay(1000)
sm.blind(False, 0, 0, 0, 0, 1000)
sm.sendDelay(1000)
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(3003302) # Wind Spirit
sm.sendNext("#face1#We're here. And now, I vanish as I appear, just like the wind!")
sm.sendSay("#face2#Never fear~ Whenever you need help, I will be near~")
sm.resetNpcSpecialActionByTemplateId(3003351)
sm.showNpcSpecialActionByTemplateId(3003351, "wind3", 1920)
sm.playSound("Sound/SoundEff.img/ArcaneRiver/wind", 100)
sm.sendDelay(1900)
sm.setInnerOverrideSpeakerTemplateID(3003301) # Small Spirit
sm.sendNext("#face1#Well... That's Wind Spirit for you.")
sm.sendSay("#face1#Oh well. Let's check on the Spirit Tree.")
sm.sendSay("#face1#...")
sm.sendSay("#face4#...")
sm.sendSay("#face5#(Sniffs) The Floral Flute was restored, but nothing's changed.")
sm.sendSay("#face7#(Sniffs) Hold on a little longer, Spirit Tree. We'll get you back to normal! Don't give up.")
sm.setParam(57)
sm.sendSay("#b(You try and cheer the Small Spirit up.)#k")
sm.setParam(37)
sm.sendSay("#face1#...")
sm.sendSay("#face2#T-thanks. You're right, we've made a good start. Okay,  let's do this! ")
sm.lockInGameUI(False, True)
sm.warp(450005000)