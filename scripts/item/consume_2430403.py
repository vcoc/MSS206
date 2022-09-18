# 1.3x Exp Coupon

if sm.canHold(5211067):
    sm.giveItemWithExpireDate(5211067, 1, False, 60) # 60 Minutes
    sm.consumeItem(2430403)
else:
    sm.setSpeakerID(1540809)
    sm.sendSayOkay("Please make room in your inventory.")