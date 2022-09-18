# 1.5x Exp Coupon

if sm.canHold(5211068):
    sm.giveItemWithExpireDate(5211068, 1, False, 60) # 60 Minutes
    sm.consumeItem(2430404)
else:
    sm.setSpeakerID(1540809)
    sm.sendSayOkay("Please make room in your inventory.")