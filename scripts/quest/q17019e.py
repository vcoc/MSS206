# id 17019 ([Commerci Trade] Ten Trades for Luna), field 865000001
sm.setSpeakerID(9390220) # Maestra Fiametta
sm.setParam(1)
sm.sendNext("I see you've completed your voyage to Dolce. ")
sm.sendSay("You've unlocked a new destination. Open your Voyage Map and you'll see that Luna is now selectable.")
sm.sendSay("Trade more and we'll all be rich. Everybody wins.")
sm.setParam(0)
res = sm.sendNext("Hello, #e#b#h0##k#n. Welcome to the Commerci Trade Center. \r\n#b\r\n#L0#Enter trade#l#b\r\n#L1#Stimulus System#l#b\r\n#L2#Move to the Merchant Union trade location#l#b\r\n#L3#The vessel's energy will be recharged manually.#l#b\r\n#L4#The goods will be manually restocked.#l")
sm.sendNext("You've earned #r#e1267167#k#n EXP through your trades. You also have #b#e12#k#n Commerci Denaros and #d#e325638#k#n Mesos waiting for you.")
res = sm.sendAskYesNo("Do you want your voyage earnings right now?")
sm.createQuestWithQRValue(17011, "")
sm.createQuestWithQRValue(17012, "")
sm.createQuestWithQRValue(17013, "")
sm.createQuestWithQRValue(17014, "")
sm.createQuestWithQRValue(17015, "")
sm.sendNext("There you go, allotment complete. ")
sm.openUI(189)
sm.createQuestWithQRValue(17011, "")
sm.createQuestWithQRValue(17011, "C=15")
sm.createQuestWithQRValue(17011, "C=15;S=0")
sm.warp(865000101)
