# Custom Beginnings - Explorer
# Custom Server Script

from net.swordie.ms.constants import JobConstants

speaker = 2007 # Maple Administrator

# JobOptions: { string jobName, string jobDesc, int jobId }
options = [
    ["Warrior", "powerful and defensive", 100],
    ["Magician", "intelligent and magical", 200],
    ["Bowman", "long-ranged and controlled", 300],
    ["Thief", "speedy and sneaky", 400],
    ["Pirate", "fancy and unique", 500]
]

# 2ndJobOptions: { string jobName, int jobId }
warrior2ndJob = [
    ["Fighter", 110],
    ["Page", 120],
    ["Spearman", 130]
]

magician2ndJob = [
    ["Wizard (Fire, Poison)", 210],
    ["Wizard (Ice, Lightning)", 220],
    ["Cleric", 230]
]

bowman2ndJob = [
    ["Hunter", 310],
    ["Crossbowman", 320]
]

thief2ndJob = [
    ["Assassin", 410],
    ["Bandit", 420]
]

pirate2ndJob = [
    ["Brawler", 510],
    ["Gunslinger", 520]
]

currentJobID = chr.getJob()

if chr.getLevel() == 10 and currentJobID == 0: # Beginner

    sm.removeEscapeButton()

    if chr.getSubJob() == 1: # Dual Blade
        sm.jobAdvance(JobConstants.JobEnum.THIEF.getJobId())
        sm.doJobEnd()

    elif chr.getSubJob() == 2: # Cannoneer
        sm.jobAdvance(JobConstants.JobEnum.PIRATE_CANNONEER.getJobId())
        sm.doJobEnd()

    elif chr.getSubJob() == 3: # Path Finder
        sm.jobAdvance(JobConstants.JobEnum.PATHFINDER_1.getJobId())
        sm.doJobEnd()

    elif chr.getSubJob() == 10: # Jett
        sm.jobAdvance(JobConstants.JobEnum.JETT_1.getJobId())
        sm.doJobEnd()

    else:

        optionText = "It's time for you to pick a job!\r\nAs an #bExplorer#k, you have the option of the " + str(len(options)) + " following options:"

        for idx, job in enumerate(options):
            optionText += "\r\n#b#L" + str(job[2]) + "#" + job[0] + "#k, " + job[1] + "#l"
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
                    sm.startScript("job_explorer", "npc")

elif chr.getLevel() == 30 and JobConstants.isAdventurerBeginner(currentJobID):

    sm.removeEscapeButton()

    optionText = "It's time for you to pick a job!\r\nAs an #b" + JobConstants.getJobEnumById(currentJobID).getJobName() + "#k, you have these following options:"

    if currentJobID == 100: # Warrior

        for idx, job in enumerate(warrior2ndJob):
            optionText += "\r\n#b#L" + str(job[1]) + "#" + job[0] + "#k#l"
        choice = sm.sendNext(optionText)

        for job in warrior2ndJob:
            if (choice == job[1]):
                response = sm.sendAskYesNo("So, you wish to become a #b" + job[0] + "#k?")
                if response:
                    sm.jobAdvance(job[1])
                    sm.sendSayOkay("You are now a #b" + job[0] + "#k!")
                else:
                    # executes the current script again
                    sm.dispose()
                    sm.startScript("job_explorer", "npc")

    elif currentJobID == 200: # Magician

        for idx, job in enumerate(magician2ndJob):
            optionText += "\r\n#b#L" + str(job[1]) + "#" + job[0] + "#k#l"
        choice = sm.sendNext(optionText)

        for job in magician2ndJob:
            if (choice == job[1]):
                response = sm.sendAskYesNo("So, you wish to become a #b" + job[0] + "#k?")
                if response:
                    sm.jobAdvance(job[1])
                    sm.sendSayOkay("You are now a #b" + job[0] + "#k!")
                else:
                    # executes the current script again
                    sm.dispose()
                    sm.startScript("job_explorer", "npc")

    elif currentJobID == 300: # Bowman

        for idx, job in enumerate(bowman2ndJob):
            optionText += "\r\n#b#L" + str(job[1]) + "#" + job[0] + "#k#l"
        choice = sm.sendNext(optionText)

        for job in bowman2ndJob:
            if (choice == job[1]):
                response = sm.sendAskYesNo("So, you wish to become a #b" + job[0] + "#k?")
                if response:
                    sm.jobAdvance(job[1])
                    sm.sendSayOkay("You are now a #b" + job[0] + "#k!")
                else:
                    # executes the current script again
                    sm.dispose()
                    sm.startScript("job_explorer", "npc")

    elif currentJobID == 400: # Thief

        for idx, job in enumerate(thief2ndJob):
            optionText += "\r\n#b#L" + str(job[1]) + "#" + job[0] + "#k#l"
        choice = sm.sendNext(optionText)

        for job in thief2ndJob:
            if (choice == job[1]):
                response = sm.sendAskYesNo("So, you wish to become a #b" + job[0] + "#k?")
                if response:
                    sm.jobAdvance(job[1])
                    sm.sendSayOkay("You are now a #b" + job[0] + "#k!")
                else:
                    # executes the current script again
                    sm.dispose()
                    sm.startScript("job_explorer", "npc")

    elif currentJobID == 500: # Pirate

        for idx, job in enumerate(pirate2ndJob):
            optionText += "\r\n#b#L" + str(job[1]) + "#" + job[0] + "#k#l"
        choice = sm.sendNext(optionText)

        for job in pirate2ndJob:
            if (choice == job[1]):
                response = sm.sendAskYesNo("So, you wish to become a #b" + job[0] + "#k?")
                if response:
                    sm.jobAdvance(job[1])
                    sm.sendSayOkay("You are now a #b" + job[0] + "#k!")
                else:
                    # executes the current script again
                    sm.dispose()
                    sm.startScript("job_explorer", "npc")