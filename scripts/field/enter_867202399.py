# id 867202399 (Abrup Basin : Training Grounds), field 867202399
sm.lockInGameUI(True, False)
sm.spawnNpc(9400582, -110, -70)
sm.showNpcSpecialActionByTemplateId(9400582, "summon", 0)
sm.spawnNpc(9400602, -170, -70)
sm.showNpcSpecialActionByTemplateId(9400602, "summon", 0)
sm.sendDelay(1000)
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(9400602) # Einar
sm.sendNext("#face3#Huff, huff...")
sm.sendDelay(2000)
sm.setInnerOverrideSpeakerTemplateID(9400582) # Cayne
sm.sendNext("#face0#Einar, you can't be tired. Lots of people are counting on you. ")
sm.setInnerOverrideSpeakerTemplateID(9400602) # Einar
sm.sendSay("#face0#Did... Sanaan... talk to you...?")
sm.setInnerOverrideSpeakerTemplateID(9400582) # Cayne
sm.sendSay("#face0#Of course she did. ")
sm.setInnerOverrideSpeakerTemplateID(9400602) # Einar
sm.sendSay("#face0#Is that... why you're being nice to me? ")
sm.setInnerOverrideSpeakerTemplateID(9400582) # Cayne
sm.sendSay("#face0#Nope. She asked me to treat you like anyone else. ")
sm.sendDelay(500)
sm.showEffect("Effect/OnUserEff.img/emotionBalloon/noSpeak", 2000, 0, 0, 0, 0, 0, 0)
sm.setInnerOverrideSpeakerTemplateID(9400602) # Einar
sm.sendNext("#face0#... ")
sm.sendDelay(1500)
sm.setParam(57)
sm.sendNext("#bSanaan is worried about you. ")
sm.setParam(37)
sm.sendSay("#face1#I know... I owe her so much. ")
sm.sendSay("#face1#To return her favor, I must... ")
sm.sendSay("#face0#This armor Sanaan gave me... I can never repay her. ")
sm.sendSay("#face0#...I'm guessing you don't think much of me right now. ")
sm.setInnerOverrideSpeakerTemplateID(9400582) # Cayne
sm.sendSay("#face0#Why would you say that? No judgments here. ")
sm.setParam(57)
sm.sendSay("#bNo one's going to give you a hard time with all the effort you're putting in. ")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400602) # Einar
sm.sendSay("#face0#Honestly, #h0#, I heard your speech from my home. One part stood out to me... 'I realized that there were always people who helped me, for everything I thought I accomplished on my own.' ")
sm.sendSay("#face1#You're right. I wouldn't be here if it weren't for the townspeople. ")
sm.sendDelay(1000)
sm.sendNext("#face0#...Please, will you listen to my story? ")
sm.setParam(57)
sm.sendSay("#bOf course. ")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400582) # Cayne
sm.sendSay("#face1#Just keep it under three minutes. We've got a training schedule to stick to! ")
sm.setParam(57)
sm.sendSay("#bNot now, Cayne...")
sm.setParam(37)
sm.sendSay("#face1#Hey, I've just got plenty of energy to burn. You talk, I'll stretch. ")
sm.setInnerOverrideSpeakerTemplateID(9400602) # Einar
sm.sendSay("#face0#For almost my whole life, Julieta was my only family. There's a big age gap between us, but soon after she was born, our parents... ")
sm.sendSay("#face0#I did any kind of work I could find to make a living for my sister and I. There wasn't much I could do, but I chopped wood and fixed roofs and cleaned barns as best I could. I still do, honestly. ")
sm.sendSay("#face0#Then came the day that everyone disappeared into the forest. They vanished, and never returned. ")
sm.sendSay("#face0#That morning, I was supposed to cut trees on my own in the deep forest. I was terrified. My sister told me not to go, but I knew I had to work for use to survive. ")
sm.sendSay("#face0#As I was leaving, the Chief stopped me and asked me to help with something else in town. I don't even remember what it was now...")
sm.sendSay("#face0#Julieta didn't know that. She packed me a lunch and came to find me in the forest... ")
sm.sendSay("#face1#It's... it's my fault that she's gone. ")
sm.sendSay("#face1#My whole family is gone... and it's my fault. I know it's my fault. It's like I'm cursed... ")
sm.setInnerOverrideSpeakerTemplateID(9400582) # Cayne
sm.sendSay("#face0#That's ridiculous. ")
sm.sendDelay(3000)
sm.setInnerOverrideSpeakerTemplateID(9400602) # Einar
sm.sendNext("#face1#You know what's worse than that, though? ")
sm.sendSay("#face1#I never even considered looking for my sister. All I could think about was my regret... if I had stayed home that day... if I had gone to the forest... if I had told Julieta that I was going...")
sm.sendSay("#face0#I always think like that, but now it's the other way. If Elva didn't bring me food every day... if the Chief didn't make me take charge of my life...")
sm.sendSay("#face0#And if Sanaan never made this armor, or find Julieta's necklace...")
sm.spineScreen(False, False, True, 0, "Map/EffectPL.img/MONAD1/spine/scene3/d2","0","scene3")
sm.sendSay("#face0#If any of those things didn't happen, I'd still be wallowing at home in my guilt and remorse. ")
sm.setInnerOverrideSpeakerTemplateID(9400582) # Cayne
sm.sendSay("#face0#Is she your sister? She doesn't look like you. ")
sm.setParam(57)
sm.sendSay("#b... ")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400602) # Einar
sm.sendSay("#face0##h0#, you were right. I'm still here because I had help from everyone. ")
sm.sendSay("#face0#I'm so happy I've finally realized this, before it's too late. I want to do everything I can to help you. It's the only way I can atone for abandoning my sister. ")
sm.setInnerOverrideSpeakerTemplateID(9400582) # Cayne
sm.sendSay("#face0#Great! That means it's time for action, not words. And if you want to act, you've got to learn to fight! ")
sm.offSpineScreen("scene3", 0, "", 0)
sm.sendDelay(1000)
sm.moveNpcByTemplateId(9400582, True, 120, 100)
sm.sendDelay(2000)
sm.flipNpcByTemplateId(9400582, False)
sm.sendDelay(500)
sm.sendNext("#face0##h0#, Einar, are you ready? ")
sm.setInnerOverrideSpeakerTemplateID(9400602) # Einar
sm.sendSay("#face2#Yes... I'm ready! ")
sm.setParam(57)
sm.sendSay("#bI'm ready too. ")
sm.lockInGameUI(False, True)
sm.completeQuestNoCheck(64129)
sm.startQuest(64130)
sm.warp(867202500)
