# Custom Beginnings - Resistance
# Custom Server Script

speaker = 2007 # Maple Administrator

# JobOptions: { string jobName, string jobDesc, int jobId }
options = [
    ["Battle Mage", "", 3200],
    ["Wild Hunter", "", 3300],
    ["Mechanic", "", 3500],
    ["Blaster", "", 3700]
]

currentJobID = chr.getJob()

if chr.getLevel() == 10 and currentJobID == 3000: # Citizen

    sm.removeEscapeButton()

    optionText = "It's time for you to pick a job.\r\nAs a member of the #bResistance#k, you have the option of the " + str(len(options)) + " following options:"

    for idx, job in enumerate(options):
        optionText += "\r\n#b#L" + str(job[2]) + "#" + job[0] + "#k " + job[1] + "#l"
    choice = sm.sendNext(optionText)

    for job in options:
        if (choice == job[2]):
            response = sm.sendAskYesNo("So, you wish to become a #b" + job[0] + "#k?")
            if response:
                sm.jobAdvance(job[2])
                sm.doJobEnd()
                sm.sendSayOkay("You are now a #b" + job[0] + "#k!")
            else:
                # executes the current script again
                sm.dispose()
                sm.startScript("job_resistance", "npc")

elif chr.getLevel() == 10 and currentJobID == 3001: # Demon (Avenger/Slayer)

    sm.removeEscapeButton()

    if sm.sendAskSelectMenu(1, 0) == 1:
        sm.jobAdvance(3100) # Demon Slayer
        sm.doJobEnd()
        sm.sendSayOkay("You are now a #bDemon Slayer#k!")
    else:
        sm.jobAdvance(3101) # Demon Avenger
        sm.doJobEnd()
        sm.sendSayOkay("You are now a #bDemon Avenger#k!")