import sys
from optparse import OptionParser
from sbprocess import call
from os import path
#To DO:
# Automagically build seperate stat profiles if given a total stat amount, should base around haste and then keep mastery and crit even, overfill into vers.
# Use if statements for other classes not shadow to input other classes into mass profiles ie mage, shaman, etc.
# figure out how to save it as .simc, should be able to via os, just need to figure out syntax.
# make it all fit together
# enable PTR switch, cmd line argument would be best.
# talent automation built into API?
#



def profile(stats, adds, outputFile=None): #cmd line arguments?
    print ("creating profiles!")

    arguments="stats={0} adds={1}".format(outputFile)
    if stats:
        arguments+= stattotal
    if adds:
        adds+= addtype
    if outputFile:
        arguments+= (".simc".format(outputFile+"_"+adds+'_'+stats)
    arguments+=' {0}'.format(stats)

top = "priest='No_Talents'" +\n + "report_details=0" + \n + "level=110" + \n + "race=troll" + \n + "role=spell" + \n + "position=back" + \n + "artifact=47:139251:139257:139251:0:764:1:765:1:766:1:767:3:768:1:769:1:770:1:771:3:772:3:773:3:774:3:775:3:776:3:777:3:778:3:779:1:1347:1" + \n + "spec=shadow"
talents = "talets=0000000"

#PTR line:




'''def stats(statotal):
    statstotal= 0
    haste = 10000
    crit = 6000
    mastery = 2000
    versatility = statstotal-haste+crit+mastery

    for h in haste:
        haste = 10000
        haste = '''

#latest shadow APL - 12/20/2016
apl = " " 


#Needs work
def stats(stattotal): #attempt at automating some stat stuffs
    print("Adding stats")
    int = "gear_intellect=33212"
    haste = "gear_haste_rating="
    mast = "geat_mastery_rating="
    vers = "gear_versatility_rating=" 
    cirt = "gear_crit_rating="

    8kh = "8000"
    8km = "6636"
    8kv = "0"
    8kc = "6636"

    10kh = "10000"
    10km = "5536"
    10kv = "0"
    10kc = "5536"

    12kh = "12000"
    12km = "4536"
    12kv = "0"
    12kc = "4536"

    for "8k" in stattotal:
        haste = haste + 8kh
        mast = mast + 8km
        vers = vers + 8kv
        crit = crit + 8kc

        gearsum = haste + \n + mast + \n + vers + \n + crit

    for "10k" in stattotal:
        haste = haste + 10kh
        mast = mast + 10km
        vers = vers + 10kv
        crit = crit + 10kc

        gearsum = haste + \n + mast + \n + vers + \n + crit

    for "12k" in stattotal:
        haste = haste + 12kh
        mast = mast + 12km
        vers = vers + 12kv
        crit = crit + 12kc

        gearsum = haste + \n + mast + \n + vers + \n + crit

#1/2 Targets
bigadd = "raid_events+=/adds,count=1,first=30,cooldown=60,duration=20"
noadd = ""
smalladd = "raid_events+=/adds,count=3,first=45,cooldown=45,duration=10,distance=5"

#2Ts
bigaddT = "enemy=Memetop" + \n + "raid_events+=/move_enemy,name=Memetop,cooldown=2000,duration=1000,x=-27,y=-27" + \n + "raid_events+=/adds,count=1,first=30,cooldown=60,duration=20"
noaddT = "enemy=Memetop" + \n + "raid_events+=/move_enemy,name=Memetop,cooldown=2000,duration=1000,x=-27,y=-27"
smalladdT = "enemy=Memetop" + \n + "raid_events+=/move_enemy,name=Memetop,cooldown=2000,duration=1000,x=-27,y=-27" + \n + "raid_events+=/adds,count=3,first=45,cooldown=45,duration=10,distance=5"

    


    
