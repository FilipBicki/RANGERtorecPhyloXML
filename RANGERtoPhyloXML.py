import sys, xml.etree.cElementTree as ET
from collections import defaultdict

inputFile = sys.argv[1]

#Finds where Reconcliation starts and ends
#This is the section underneath the "Reconcilation:" and
#right above the whitespace after the last event
def findRec(lines) :
    start = 0
    end = 0
    for lineNum, current in enumerate(lines) :
        if (current.find("Reconciliation:") != -1) :
           start = lineNum+1
        if (not current.strip() and (start != 0)) :
            end = lineNum
            return (start,end)

#This takes the locations of each event and creates the appropriate XML
def buildXML(recLines) :
    root = ET.Element("recGeneTree")
    rooted = ET.SubElement(root, "phylogeny", rooted="true")
    events = ("Transfer", "Duplication", "Speciation")

    for line in recLines :
        #if any(x in line for x in events) :
        if events[0] in line :
            #Transfer XML
            print(events[0])
        elif events[1] in line :
                #Duplication XML
                print(events[1])
        elif events[2] in line :
                #Speciation XML
                print(events[2])
        else :
            print("Leaf")
    #hardcoded example
    clade = ET.SubElement(rooted, "clade")
    name = ET.SubElement(clade, "name").text = "m3"

    tree = ET.ElementTree(root)
    tree.write("file.xml")
        
with open(inputFile, 'r') as file :
    xmlLines = []
    lines = file.readlines()
    s, e = findRec(lines)[0], findRec(lines)[1]
    recLines = lines[s:e]
    buildXML(recLines)