def addRuleToGUI(switchNo,portNo,HostNumber):
	print "Import custom msg" 
	print switchNo
	print portNo
	with open("output.txt","a") as myfile:
		myfile.write(str(switchNo)+" "+str(HostNumber)+" "+str(portNo)+"\n")	
	print "End of message"
	myfile.close()	
