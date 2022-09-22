# Custom Inventory Seller Script
# Author: Clueless Cow
# Custom Server Script

from net.swordie.ms.loaders import ItemData
from net.swordie.ms.constants import ItemConstants
from net.swordie.ms.enums import InvType

def disposeAll():
    sm.dispose()
    chr.dispose()

def sellItemsFromTab(invType = InvType.EQUIP):
    # Query inv info
    inventory = chr.getInventoryByType(invType)
    invItems = inventory.getItems()
    tabName = ""

    if invType == InvType.CONSUME:
        tabName = "CONSUME"
    elif invType == InvType.ETC:
        tabName = "ETC"
    else:
        tabName = "EQUIPMENT"

    # Empty inv
    if len(invItems) == 0:
        sm.sendSayOkay("You have no item to sell in your selected inventory.")
        disposeAll()
        return

    # Has at least 1 item in inv
    if len(invItems) == 1:
        # Only has 1 item, proceed to ask for confirmation
        sellingItems = list(invItems)
        _itemId = invItems.get(0).getItemId()
        confirmed = sm.sendAskYesNo("Are you sure you want to sell #i{}# #z{}#".format(_itemId, _itemId))
    else:
        # Has more than 1 item, prompt mode selection
        optionList = "Please select what you want to sell in your {} tab:\r\n#L1##rEverything#k#l\r\n#L2##gSell between selected items#k#l\r\n#L3#Maybe later#l\r\n".format(tabName)
        option = sm.sendNext(optionList)
        if option:
            if option == 1:
                # Sell everything
                sellingItems = list(invItems)
                confirmed = sm.sendAskYesNo("Are you sure you want to sell #rEVERYTHING#k in your Equipment inventory?")
            elif option == 2:
                # Sell from/to
                sortedItems = list(invItems)
                sortedItems.sort(key=lambda x: x.getBagIndex())
                itemListTemplate = "This option will sell all available items between STARTING item and ENDING item.\r\nPlease select #r<order>#k item:\r\n"
                for item in sortedItems:
                    itemListTemplate += "#L{}##i{}# #z{}##l\r\n".format(item.getBagIndex(), item.getItemId(), item.getItemId())
                startIndex = sm.sendNext(itemListTemplate.replace("<order>", "STARTING"))
                endIndex = sm.sendNext(itemListTemplate.replace("<order>", "ENDING"))
                if startIndex > endIndex:
                    startIndex, endIndex = endIndex, startIndex
                sellingItems = filter(lambda x: (startIndex <= x.getBagIndex() <= endIndex), sortedItems)
                soldItemsTemplate = "You will sell the following items:\r\n"
                for item in sellingItems:
                    soldItemsTemplate += "#i{}# #z{}#\r\n".format(item.getItemId(), item.getItemId(), item.getBagIndex())
                confirmed = sm.sendAskYesNo(soldItemsTemplate)
            else:
                # 'Maybe later' option / no response
                disposeAll()
                return

    # Finish asking for selling items, proceed to actually sell it
    if not confirmed:
        sm.sendSayOkay("Thank you for using my service!")
        disposeAll()
        return

    # Player confirmed
    totalMesos = 0
    for item in sellingItems:
        cost = 0
        id = item.getItemId()
        quantity = item.getQuantity()
        if ItemConstants.isEquip(id):
            cost = item.getPrice() * quantity
        else:
            info = ItemData.getItemInfoByID(id)
            if info:
                cost = info.getPrice() * quantity
            else:
                continue
        totalMesos += cost

    if chr.canAddMoney(totalMesos):
        # Remove item from inv
        for soldItem in sellingItems:
            _id = soldItem.getItemId()
            _quantity = soldItem.getQuantity()
            if ItemConstants.isEquip(_id):
                chr.consumeItem(soldItem)
            else:
                chr.consumeItem(_id, _quantity)
        # Add money
        chr.addMoney(totalMesos)
        sm.sendSayOkay("You've received {} mesos. Thank you for using my service!".format(totalMesos))
        disposeAll()
        return
    else:
        sm.sendSayOkay("#rYou've reached maximum meso cap.#k Please deposit at least {} mesos and run the command again!".format(totalMesos))
        disposeAll()
        return

inventoryList = "Please which inventory you want to sell:\r\n#L1#Equipment#l\r\n#L2#Consume#l\r\n#L3#ETC#l\r\n"
selectedInv = sm.sendNext(inventoryList)

if selectedInv == 1:
    sellItemsFromTab(InvType.EQUIP)
elif selectedInv == 2:
    sellItemsFromTab(InvType.CONSUME)
elif selectedInv == 3:
    sellItemsFromTab(InvType.ETC)
else:
    sm.sendSayOkay("Invalid inventory. Please run the command again!")
    disposeAll()
