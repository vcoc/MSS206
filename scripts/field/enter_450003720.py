# id 450003720 (Lachelein Alley : Lachelein Alley), field 450003720
sm.lockInGameUI(True, False)
sm.blind(True, 255, 0, 0, 0, 0)
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(3003209) # Gray Mask
sm.sendNext("Oh! There's something important I forgot to tell you! ")
sm.sendSay("I wouldn't try to escape by following the river, if I were you. It's an extremely dangerous place.")
sm.sendSay("Those who fall in are #bsapped of their energy#k. And soon, they are #btorn apart into their component Erdas.#k Isn't that terrible?")
sm.blind(True, 255, 0, 0, 0, 0)
sm.sendDelay(1200)
sm.blind(False, 0, 0, 0, 0, 1000)
sm.sendDelay(1400)
sm.lockInGameUI(False, True)
