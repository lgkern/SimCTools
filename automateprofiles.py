import sys
from optparse import OptionParser
from sbprocess import call
from os import path
from itertools import combinations_with_replacement
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
# Okay so string formatting
# In python both ' and " can be used, but try to always use ' due to better practices
# If you have ' or " in text, you gotta put a \ before so it doesn't finish the string
top = 'priest=\'No_Talents\'\nreport_details=0\nlevel=110\nrace=troll\nrole=spell\nposition=back\n'+ 'artifact=47:139251:139257:139251:0:764:1:765:1:766:1:767:3:768:1:769:1:770:1:771:3:772:3:773:3:774:3:775:3:776:3:777:3:778:3:779:1:1347:1\nspec=shadow'
talents = "talents=0000000"

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

    #Never start variable names with numbers, otherwise the program will think they are numbers.
    h8k = "8000"
    m8k = "6636"
    v8k = "0"
    c8k = "6636"

    h10k = "10000"
    m10k = "5536"
    v10k = "0"
    c10k = "5536"

    h12k = "12000"
    m12k = "4536"
    v12k = "0"
    c12k = "4536"

    for "8k" in stattotal:
        haste = haste + h8k
        mast = mast + m8k
        vers = vers + v8k
        crit = crit + c8k

        gearsum = haste + \n + mast + \n + vers + \n + crit

    for "10k" in stattotal:
        haste = haste + h10k
        mast = mast + m10k
        vers = vers + v10k
        crit = crit + c10k

        gearsum = haste + \n + mast + \n + vers + \n + crit

    for "12k" in stattotal:
        haste = haste + h12k
        mast = mast + m12k
        vers = vers + v12k
        crit = crit + c12k

        gearsum = haste + \n + mast + \n + vers + \n + crit

#1/2 Targets
bigadd = "raid_events+=/adds,count=1,first=30,cooldown=60,duration=20"
noadd = ""
smalladd = "raid_events+=/adds,count=3,first=45,cooldown=45,duration=10,distance=5"

#2Ts
bigaddT = "enemy=Memetop" + \n + "raid_events+=/move_enemy,name=Memetop,cooldown=2000,duration=1000,x=-27,y=-27" + \n + "raid_events+=/adds,count=1,first=30,cooldown=60,duration=20"
noaddT = "enemy=Memetop" + \n + "raid_events+=/move_enemy,name=Memetop,cooldown=2000,duration=1000,x=-27,y=-27"
smalladdT = "enemy=Memetop" + \n + "raid_events+=/move_enemy,name=Memetop,cooldown=2000,duration=1000,x=-27,y=-27" + \n + "raid_events+=/adds,count=3,first=45,cooldown=45,duration=10,distance=5"

def generateProfile(baseProfile, talentCombo=None, mask='1111111', encounterTypes):
    # Saving file
    
    # Placeholder, gotta build a fileName based on talent and encounterTypes
    data = 'ptr = 1'
    fileName = 'kek'
    with open(fileName, "w") as outFile:
        print(data, file=outFile)
    

def genProfiles(base, iterateTalents, mask, encounterTypes):
    # Opening file
    with open(base, "r") as baseProfile:
        # Code
        # Here you can either extract the data from the profile and use it after
        # Or use the data nested here as well
        if iterateTalents:
            for talentCombo in list(combinations_with_replacement('123',7)):
                # combinations_with_replacement generates all talent options
                # each talentCombo will have a list with 7 elements
                generateProfile(baseProfile, talentCombo, mask, encounterTypes)
        else:
            # If the user doesn't want to iterate on talents
            generateProfile(baseProfile, encounterTypes=encounterTypes)
    # Saving file
    

def main():
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option("-b", "--base", dest="base", default = None, help="the base APL for all profiles")
    parser.add_option("-m", "--mask", dest="mask", default = '1111111', help="mask that shows which talents should be iterated")
    parser.add_option("-t", "--iterate-talents",  action="store_true", dest="iterateTalents", default = False, help="tells the generator to iterate between different talents")
    parser.add_option("-e", "--encounter-types", dest="encounterTypes", default = None, help="list of different encounter types to be generated")    
    (options, args) = parser.parse_args()
    
    genProfiles(options.base, options.iterateTalents, options.mask, options.encounterTypes)

if __name__ == "__main__":
    main()  
