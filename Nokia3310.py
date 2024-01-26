def mainMenu():

	number = int(input("Enter option"))

	match(number):
		case 1:
			return phoneBook()
		case 2:
			return messages()
		case 3:
			return chat()
		case 4:
			return callRegister()
		case 5:
			return tones()
		case 6:
			return settings()
		case 7:
			return callDivert()
		case 8:
			return games()
		case 9:
			return calculator()
		case 10:
			return reminders()
		case 11:
			return clock()
		case 12:
			return profile()
		case 13:
			return simServices()
		case 99:
			return System.exit(0)
		





def mainMenu():
	print("""
		1.Phone book
		2.Messages
		3.Chat
		4.Call Register
		5.Tones
		6.Settings
		7.Call Divert
		8.Games
		9.Calculator
		10.Reminders
		11.Clock
		12.Profile
		13.SIM services
		99. Exit""")




def phoneBook():
	print("""
		1.Search
		2.Service
		3.Add Name
		4.Erase
		5.Edit
		6.Assign tone
		7.Send B' Card
		8.Options
		9.Speed Dials
		10.Voice Tags
		0. Exit""")


	number = int(input("Enter option"))

	match(number):
		case 1:
			return search()
		case 2:
			return service()
		case 3:
			return addName()
		case 4:
			return erase()
		case 5:
			return edit()
		case 6:
			return assignTone()
		case 7:
			return sendBCard()
		case 8:
			return options()
		case 9:
			return speedDials()
		case 10:
			return voiceTags()
		case 0 :
			return mainMenu()





def options():
	print("""
		1. Type Of View
		2. Memory Status

		0. Exit""")

	number = int(input("Enter option"))

	match(number):
		case 1:
			return typeOfView()
		case 2:
			return memoryStatus()
		case 0:
			return phoneBook()

	



def search():
	print("0. Exit")


	number = int(input("Enter option"))

	if(number == 0):
		phoneBook()
	


def service():
	print("0. Exit")

	number = int(input("Enter option"))

	if(number == 0):
		phoneBook()
	

																						
def addName():
	print("0.Exit")

	number = int(input("Enter option"))

	if(number == 0):
		phoneBook()
	


def erase():
	print("0.Exit")

	number = int(input("Enter option"))

	if(number == 0):
		phoneBook()

	

def edit():
	print("0.Exit"):

	number = int(input("Enter option"))

	if(number == 0):
		phoneBook()

	


def assignTone():
	print("0.Exit"):

	number = int(input("Enter option"))

	if(number == 0):
		phoneBook()
	


def sendBCard():
	print("0.Exit")

	number = int(input("Enter option"))

	if(number == 0):
		phoneBook()
		





def typeOfView():

	print("""
	      ***Type Of View***

		0.Exit""")

	number = int(input("Enter option"))

	if(number == 0):
		options()
	




def memoryStatus():
	print("""
	    ****Memory Status***
		0.Exit""")

	number = int(input("Enter option"))

	if(number == 0):
		options()

	


def speedDials():
	print("0.Exit")

	number = int(input("Enter option"))

	if(number == 0):
		phoneBook()
	


def voiceTags() :
	print("0.Exit")

	number = int(input("Enter option"))

	if(number == 0):
		phoneBook()
	




def messages():
	print("""
	1.Write messages
	2.Inbox
	3.Outbox
	4.Picture messages
	5.Templates
	6.Smileys
	7.Messages Setting
	8.Info service
	9.Voice mailbox number
	10.Service command editor
	0. Exit""")


	number = int(input("Enter option"))

	match(number):
		case 1:
			return writeMessages()
		case 2:
			return inbox()
		case 3:
			return outbox()
		case 4:
			return pictureMessages()
		case 5:
			return templates()
		case 6:
			return smileys()
		case 7:
			return messagesSetting()
		case 8:
			return infoService()
		case 9:
			return voiceMailboxNumber()
		case 10:
			return serviceCommandEditor()
		case 0:
			return mainMenu()

	


def messagesSetting():
	print("""

	 1. set1
	 2. common
	 0. Exit""")

	 
	number = int(input("Enter option"))

	match(number):
		case 1:
			return set1()
		case 2:
			return common()
		case 0:
			return messages()

	

	




	


def writeMessages():
	print("0.Exit")

	number = int(input("Enter option"))

	if(number == 0):
		messages()

	

def inbox():
	print("0.Exit"):

	number = int(input("Enter option"))


	if(number == 0):
		messages()

	

def outbox():
	print("0.Exit")

	number = int(input("Enter option"))

	if(number == 0):
		messages()

	


def pictureMessages():
	print("0.Exit")

	number = int(input("Enter option"))

	if(number == 0):
		messages()

	


def templates():
	print("0.Exit")

	number = int(input("Enter option"))

	if(number == 0):
		messages()

	


def smileys():
	print("0.Exit")

	number = int(input("Enter option"))

	if(number == 0):
		messages()
	



def set1():
	print("""
	1.Message centre number
	2.Messages sent as
	3.Message validity
	0. Exit""")

	number = int(input("Enter option"))

	match(number):	
		case 1:
			return messageCentreNumber()
		case 2:
			return messagesSentAs()
		case 3:
			return messageValidity()
		case 0:
			return messagesSetting()
	
	

					

def messageCentreNumber():
	print("0.Exit")

	number = int(input("Enter option"))

	if(number == 0):
		set1()

	

def messagesSentAs():
	print("0.Exit"):

	number = int(input("Enter option"))

	if(number == 0):
		set1()

	


def messageValidity():
	print("0.Exit")

	number = int(input("Enter option"))

	if(number == 0):
		set1()

	




def common():
	print("""
	1.Delivery reports
	2.Reply via same centre
	3.Character support
	0. Exit""")

	number = int(input("Enter option"))

	match(number):
		case 1:
			return deliveryReports()
		case 2:
			return replyViaSameCentre()
		case 3:
			return characterSupport()
		case 0:
			return messagesSetting()



	



def deliveryReports():
	print("0.Exit")

	number = int(input("Enter option"))

	if(number == 0):
		common()
	


def replyViaSameCentre():
	print("0.Exit")

	number = int(input("Enter number: "))

	if(number == 0):
		common()



def characterSupport():
	print("0.Exit")

	number = int(input("Enter number: "))

	if(number == 0):
		common()



def infoService():
	print("0.Exit")

	number = int(input("Enter number: "))

	if(number == 0):
		messages()


def voiceMailboxNumber():
	print("0.Exit")

	number = int(input("Enter number: "))

	if(number == 0):
		messages()



def serviceCommandEditor():
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
		messages()






def chat(){
	print("0.Exit")

	number = int(input("Enter number: "))

	if(number == 0):
		mainMenu()


def callRegister():
	print("""
	1.Missed calls
	2.Received calls
	3.Dialed numbers
	4.Erase recent call lists
	5.Show call duration
	6.Show call costs
	7.call cost settings
	8.Prepaid credit
	0. Exit""")


	number = int(input("Enter number: "))

	match(number):
		case 1:
			return missedCalls()
		case 2:
			return receivedCalls()
		case 3:
			return dialedNumbers()
		case 4:
			return eraseRecentCallLists()
		case 5:
			return showCallDuration()
		case 6:
			return showCallCosts()
		case 7:
			return callCostSettings()
		case 8:
			return prepaidCredit()
		case 0:
			return mainMenu()
	

	
def showCallDuration():
	print("""
	1.Last call duration
	2.All calls duration
	3.Received calls duration
	4.Dialed calls duration
	5.Clear timers
	0. Exit""")

	number = int(input("Enter number: "))

	match(number):
		case 1:
			return lastCallDuration()
		case 2:
			return allCallsDuration()
		case 3:
			return receivedCallsDuration()
		case 4:
			return dialedCallsDuration()
		case 5:
			return clearTimers()
		case 0:
			return callRegister()
	


def lastCallDuration():
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
		showCallDuration()
	


def allCallDuration():
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
		showCallDuration()
	


def receivedCallDuration():
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
		showCallDuration();
	


def dialedCallsDuration():
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
		showCallDuration();
	


def clearTimers():
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
		showCallDuration();
	


def showCallCosts():
	print("""
	1.Last call cost
	2.All calls cost
	3.Clear counters
	0. Exit""")


	number = int(input("Enter number: "))

	match(number){
		case 1:
			return lastCallCost()
		case 2:
			return allCallsCost()
		case 3:
			return clearCounters()
		case 0:
			return callRegister()
	

def lastCallCost():
	print("0.Exit")

	number = int(input("Enter number: "))

	if(number == 0)
		showCallCosts()
	

def allCallCost():
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
		showCallCosts();
	

def clearCounter():
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
		showCallCosts()
	


def callCostSettings(): 
	print("""
	1.Call cost limit
	2.Show costs in
	0. Exit""")

number = int(input("Enter number: "))

match(number){
	case 1:
		return callCostLimit()
	case 2:
		return showCostsIn()
	case 0:
		return callRegister()
	

def CallCostLimit()
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
		callCostSettings()
	}
}

def showCostIn():
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
		callCostSettings()



def missedCalls():
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
		callRegister()
	




def receivedCalls():
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
		callRegister()
	



def dialedNumbers():
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
		callRegister()
	



def eraseRecentCallLists():
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
		callRegister()





def allCallsDuration():
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
		callRegister()
	

def receivedCallsDuration():
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
		callRegister()
	


def allCallsCost():
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
		callRegister()

	



def clearCounters():
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
		callRegister()



def callCostLimit():
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
		callRegister()
	


def showCostsIn():
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
		callRegister()
	

def prepaidCredit():
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0)
		callRegister()

	




def tones():
	print("""
		1.Ringing tone
		2.Ringing volume
		3.Incoming call alert
		4.Composer
		5.Message alert tone
		6.Keypad tones
		7.Warning and game tones
		8.Vibration alert
		9.Screen saver
		0. Exit""")


	number = int(input("Enter number: "))

	match(number):
		case 1:	
			return ringingTone()
		case 2:
			return ringingVolume()
		case 3:	
			return incomingCallAlert()
		case 4:	
			return composer()
		case 5:	
			return messagesAlertTone()
		case 6:	
			return keypadTones()
		case 7:	
			return warningAndGameTones()
		case 8:	
			return vibratingAlert()
		case 9:	
			returnscreenSaver()
		case 0:	
			return mainMenu()
	
	

def ringingTone():
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
		tones()

	


def ringingVolume():
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
		tones()

	


def incomingCallAlert():
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
		tones()

	


def composer():
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
		tones()

	


def messagesAlertTone():
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
		tones()

	
def keypadTones():
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
		tones()

	


def warningAndGameTones():
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
		tones()

	


def vibratingAlert():
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
		tones()

	


def screenSaver():
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
		tones()



def settings():
	print("""
		1.Call settings
		2.Phone settings
		3.Security settings
		4.Restore factory settings
		0.Exit""")

	number = int(input("Enter number: "))
	match(number):
		case 1:
			return callSettings()
		case 2:
			return phoneSettings()
		case 3:
			return securitySettings()
		case 4:
			return restoreFactorySettings()
		case 0:
			return mainMenu()

	




def callSettings():
	print("""
		1.Automatic redial
		2.Speed dialing
		3.Call waiting options
		4.Own number sending
		5.Phone line in use
		6.Automatic answer
		0. Exit""")


	number = int(input("Enter number: "))
	match(number):
		case 1:
			return automaticRedial()
		case 2:
			return speedDialing()
		case 3:
			return callWaitingOptions()
		case 4:
			return ownNumberSending()
		case 5:
			return phoneLineInUse()
		case 6:
			return automaticAnswer()
		case 0:
			return settings()

	


def automaticRedial();
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
		callSettings()
	


def speedDialing():
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
		callSettings()
	

def callWaitingOptions():
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
	callSettings()
	


def ownNumberSending():
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
		callSettings()
	


def phoneLineInUse():
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
		callSettings()
	



def automaticAnswer():
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
		callSettings()
	



def phoneSettings():
	print("""
		1.Language
		2.Cell info display
		3.Welcome Notes
		4.Network selection
		5.Lights
		6.Confirm SIM service actions
		0. Exit""")

	number = int(input("Enter number: "))
	match(number){
		case 1:
			return language()
		case 2:
			return cellInfoDisplay()
		case 3: 
			return welcomeNote()
		case 4:
			return networkSelection()
		case 5:
			return lights()
		case 6:
			return confirmSimServiceActions()
		case 0:
			return settings()
	


def language():
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
		phoneSettings()
	


def cellInfoDisplay():
	print("0.Exit")

	number = int(input("Enter number: "))
	if(number == 0):
		phoneSettings()
	


def welcomeNote():
	print("0.Exit")

 number = int(input("Enter number: "))
	if(number ==0):
		phoneSettings()

	


def networkSelection():
	print("0.Exit")

 	number = int(input("Enter number: "))

        if(number == 0):
		phoneSettings()
	


def lights():
	println("0.Exit")

	number = int(input("Enter number: "))

	if(number == 0):
		phoneSettings()



def confirmSimServiceActions():
	print("0.Exit")
	number = int(input("Enter number: "))

	if(number == 0):
		phoneSettings()
	
	
def securitySettings():

	print("""
		1.Pin code request
		2.Call barring service
		3.Fixed dialing
		4.Closed user group
		5.Phone security
		6.Change access codes
		0. Exit""");

	number = int(input("Enter number: "))

switch(number){
	case 1->pinCodeRequest();
	case 2->calBarringService();
	case 3->fixedDialing();
	case 4-> closedUserGroup();
	case 5->phoneSecurity();
	case 6->changeAccessCodes();
	case 0->settings();
	}
}

public static void pinCodeRequest() {
System.out.println("0.Exit");

System.out.println("Enter option: ");
int number = input.nextInt();

if(number == 0){
	securitySettings();
	}
}

public static void callBarringService() {
System.out.println("0.Exit");

System.out.println("Enter option: ");
int number = input.nextInt();

if(number == 0){
	securitySettings();
	}
}




public static void fixedDialing() {
System.out.println("0.Exit");

System.out.println("Enter option: ");
int number = input.nextInt();

if(number == 0){
	securitySettings();
	}
}


public static void closedUserGroup() {
System.out.println("0.Exit");

System.out.println("Enter option: ");
int number = input.nextInt();

if(number == 0){
	securitySettings();
	}
}



public static void phoneSecurity() {
System.out.println("0.Exit");

System.out.println("Enter option: ");
int number = input.nextInt();

if(number == 0){
	securitySettings();
	}
}


public static void changeAccessCodes() {
System.out.println("0.Exit");

System.out.println("Enter option: ");
int number = input.nextInt();

if(number == 0){
	securitySettings();
	}
}




public static void restoreFactorySettings() {
System.out.println("0.Exit");

System.out.println("Enter option: ");
int number = input.nextInt();

if(number == 0){
	settings();
	}
}



public static void callDivert() {
System.out.println("0.Exit");

System.out.println("Enter number: ");
int number = input.nextInt();

if(number == 0){
	mainMenu();

	}
}

public static void games() {
System.out.println("0.Exit");

System.out.println("Enter number: ");
int number = input.nextInt();

if(number == 0){
	mainMenu();

	}
}

public static void calculator() {
System.out.println("0.Exit");

System.out.println("Enter number: ");
int number = input.nextInt();

if(number == 0){
	mainMenu();

	}
}

public static void reminders() {
System.out.println("0.Exit");

System.out.println("Enter number: ");
int number = input.nextInt();

if(number == 0){
	mainMenu();

	}
}



public static void clock() {
System.out.println("""
	1.Alarm clock
	2.Clock settings
	3.Date settings
	4.StopWatch
	5.Countdown timer
	6.Auto update of date and time
	0. Exit""");


System.out.println("Enter option:");
int number = input.nextInt();

switch(number){
	case 1->alarmClock();
	case 2->clockSettings();
	case 3->dateSettings();
	case 4->stopWatch();
	case 5->countdownTimer();
	case 6-> autoUpdateOfDateAndTime();
	case 0->mainMenu();
	}
}


public static void alarmClock() {
System.out.println("0.Exit");

System.out.println("Enter option: ");
int number = input.nextInt();

if(number == 0){
	clock();
	}
}

public static void clockSettings() {
System.out.println("0.Exit");

System.out.println("Enter option: ");
int number = input.nextInt();

if(number == 0){
	clock();
	}
}

public static void dateSettings() {
System.out.println("0.Exit");

System.out.println("Enter option: ");
int number = input.nextInt();

if(number == 0){
	clock();
	}
}

public static void stopWatch() {
System.out.println("0.Exit");

System.out.println("Enter option: ");
int number = input.nextInt();

if(number == 0){
	clock();
	}
}

public static void countdownTimer() {
System.out.println("0.Exit");

System.out.println("Enter option: ");
int number = input.nextInt();

if(number == 0){
	clock();
	}
}

public static void autoUpdateOfDateAndTime() {
System.out.println("0.Exit");

System.out.println("Enter option: ");
int number = input.nextInt();

if(number == 0){
	clock();
	}
}


public static void profile() {
System.out.println("0. Exit");

System.out.println("Enter number: ");
int number = input.nextInt();

if(number == 0){
	mainMenu();

	}
}



public static void simServices() {
System.out.println("0.Exit");

System.out.println("Enter number: ");
int number = input.nextInt();

if(number == 0){
	mainMenu();

	}
}

}#
