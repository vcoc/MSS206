# id 4 (coll02), field 867201820
sm.lockInGameUI(True, False)
sm.createQuestWithQRValue(64088, "coll1=1;coll2=1")
sm.sendDelay(2000)
sm.setSpeakerType(3)
sm.setParam(57)
sm.setColor(1)
sm.sendNext("#b(This might be too far for a jump.)")
sm.sendDelay(2000)
sm.sendNext("#bWe can probably bounce across on that. ")
sm.spawnNpc(9400580, 1690, -500)
sm.showNpcSpecialActionByTemplateId(9400580, "summon", 0)
sm.lockInGameUI(False, True)