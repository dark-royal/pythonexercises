

def mainMenu():

number = int(input("Enter option"))

match(number):
	case 1:
		return phoneBook().
	case 2:
		return messages().
	case 3:
		return chat().
	case 4:
		return callRegister().
	case 5:
		return tones().
	case 6:
		return settings().
	case 7:
		return callDivert().
	case 8:
		return games().
	case 9:
		return calculator().
	case 10:
		return reminders().
	case 11:
		return clock().
	case 12:
		return profile().
	case 13:
		return simServices().
	case 99:
		return System.exit(0).
		





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
		return search().
	case 2:
		return service().
	case 3:
		return addName().
	case 4:
		return erase().
	case 5:
		return edit().
	case 6:
		return assignTone().
	case 7:
		return sendBCard().
	case 8:
		return options().
	case 9:
		return speedDials().
	case 10:
		return voiceTags().
	case 0 :
		return mainMenu().





def options():
	print("""
		1. Type Of View
		2. Memory Status

		0. Exit""")

number = int(input("Enter option"))

match(number):
	case 1:
		return typeOfView().
	case 2:
		return memoryStatus().
	case 0:
		return phoneBook().

	



def search():
	print("0. Exit")


number = int(input("Enter option"))

if(number == 0):
	phoneBook().
	


def service():
	print("0. Exit")

number = int(input("Enter option"))

if(number == 0):
	phoneBook().
	

																						
def addName():
	print("0.Exit")

number = int(input("Enter option"))

if(number == 0):
	phoneBook().
	


def erase():
	print("0.Exit")

number = int(input("Enter option"))

if(number == 0):
	phoneBook().

	

def edit():
	print("0.Exit"):

number = int(input("Enter option"))

if(number == 0):
	phoneBook().

	


def assignTone():
	print("0.Exit"):

number = int(input("Enter option"))

if(number == 0):
	phoneBook().
	


def sendBCard():
	print("0.Exit")

number = int(input("Enter option"))

if(number == 0):
	phoneBook().
	





def typeOfView():

	print("""
	      ***Type Of View***

		0.Exit""")

number = int(input("Enter option"))

if(number == 0):
	options().
	




def memoryStatus():
	print("""
	    ****Memory Status***
		0.Exit""")

number = int(input("Enter option"))

if(number == 0):
	options().

	


def speedDials():
	print("0.Exit")

number = int(input("Enter option"))

if(number == 0):
	phoneBook().
	


def voiceTags() :
	print("0.Exit")

number = int(input("Enter option"))

if(number == 0):
	phoneBook().
	




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

match(number4):
	case 1:
		return writeMessages().
	case 2:
		return inbox().
	case 3:
		return outbox().
	case 4:
		return pictureMessages().
	case 5:
		return templates().
	case 6:
		return smileys().
	case 7:
		return messagesSetting().
	case 8:
		return infoService().
	case 9:
		return voiceMailboxNumber().
	case 10:
		return serviceCommandEditor().
	case 0:
		return mainMenu().

	


def messagesSetting():
	print("""

	 1. set1
	 2. common
	 0. Exit""")

	 
number = int(input("Enter option"))

match(number):
	case 1:
		return set1().
	case 2:
		return common().
	case 0:
		return messages().

	

	




	


def writeMessages():
	print("0.Exit")

number = int(input("Enter option"))

if(number == 0):
	messages().

	

def inbox():
	print("0.Exit"):

number = int(input("Enter option"))


if(number == 0):
	messages().

	

def outbox():
	print("0.Exit")

number = int(input("Enter option"))

if(number == 0):
	messages().

	


def pictureMessages():
	print("0.Exit")

number = int(input("Enter option"))

if(number == 0):
	messages().

	


def templates():
	print("0.Exit")

number = int(input("Enter option"))

if(number == 0):
	messages().

	


def smileys():
	print("0.Exit")

number = int(input("Enter option"))

if(number == 0):
	messages().
	



def set1():
	print("""
	1.Message centre number
	2.Messages sent as
	3.Message validity
	0. Exit""")

number = int(input("Enter option"))

match(number):	
	case 1:
		return messageCentreNumber().
	case 2:
		return messagesSentAs().
	case 3:
		return messageValidity().
	case 0:
		return messagesSetting().
	
	

					

def messageCentreNumber():
	print("0.Exit")

number = int(input("Enter option"))

if(number == 0):
	set1().

	

def messagesSentAs():
	print("0.Exit"):

number = int(input("Enter option"))

	if(number == 0):
		set1().

	


def messageValidity():
	print("0.Exit")

number = int(input("Enter option"))

	if(number == 0):
		set1().

	




def common():
	print("""
	1.Delivery reports
	2.Reply via same centre
	3.Character support
	0. Exit""")

number = int(input("Enter option"))

match(number):
	case 1:
		return deliveryReports().
	case 2:
		return replyViaSameCentre().
	case 3:
		return characterSupport().
	case 0:
		return messagesSetting().



	



def deliveryReports():
	print("0.Exit")

number = int(input("Enter option"))

	if(number == 0):
		common().
	


def replyViaSameCentre():
	print("0.Exit")

System.out.println("Enter number: ");
int number = input.nextInt();

if(number == 0){
	common();

	}
}

public static void characterSupport() {
System.out.println("0.Exit");
t5444444444444
System.out.println("Enter number: ");
int number = input.nextInt();

if(number == 0){
	common();

	}
}


public static void infoService() {
System.out.println("0.Exit");

System.out.println("Enter number: ");
int number = input.nextInt();

if(number == 0){
	messages();

	}
}

public static void voiceMailboxNumber() {
System.out.println("0.Exit");

System.out.println("Enter number: ");
int number = input.nextInt();

if(number == 0){
	messages();

	}
}

public static void serviceCommandEditor() {
System.out.println("0.Exit");

System.out.println("Enter number: ");
int number = input.nextInt();

if(number == 0){
	messages();

	}
}



public static void chat(){
System.out.println("0.Exit");

System.out.println("Enter number: ");
int number = input.nextInt();

if(number == 0){
	mainMenu();

	}

}

public static void callRegister() {
System.out.println("""
	1.Missed calls
	2.Received calls
	3.Dialed numbers
	4.Erase recent call lists
	5.Show call duration
	6.Show call costs
	7.call cost settings
	8.Prepaid credit
	0. Exit""");


System.out.println("Enter option: ");
int number = input.nextInt();

switch(number){
	case 1->missedCalls();
	case 2->receivedCalls();
	case 3->dialedNumbers();  
	case 4->eraseRecentCallLists();
	case 5->showCallDuration();
	case 6->showCallCosts();
	case 7->callCostSettings();
	case 8->prepaidCredit();
	case 0->mainMenu();
	}
}
	
public static void showCallDuration() {
System.out.println("""
	1.Last call duration
	2.All calls duration
	3.Received calls duration
	4.Dialed calls duration
	5.Clear timers
	0. Exit""");

System.out.println("Enter number: ");
int number7 = input.nextInt();

switch(number7){
	case 1->lastCallDuration();
	case 2->allCallsDuration();
	case 3->receivedCallsDuration();
	case 4->dialedCallsDuration();
	case 5->clearTimers();
	case 0->callRegister();
	}
}

public static void lastCallDuration(){
System.out.print("0.Exit");

System.out.println("Enter option: ");
int number = input.nextInt();

if(number == 0){
	showCallDuration();
	}
}

public static void allCallDuration(){
System.out.print("0.Exit");

System.out.println("Enter option: ");
int number = input.nextInt();

if(number == 0){
	showCallDuration();
	}
}

public static void receivedCallDuration(){
System.out.print("0.Exit");

System.out.println("Enter option: ");
int number = input.nextInt();

if(number == 0){
	showCallDuration();
	}
}

public static void dialedCallsDuration(){
System.out.print("0.Exit");

System.out.println("Enter option: ");
int number = input.nextInt();

if(number == 0){
	showCallDuration();
	}
}

public static void clearTimers(){
System.out.print("0.Exit");

System.out.println("Enter option: ");
int number = input.nextInt();

if(number == 0){
	showCallDuration();
	}
}


public static void showCallCosts() {
System.out.println("""
	1.Last call cost
	2.All calls cost
	3.Clear counters
	0. Exit""");


System.out.println("Enter option: ");
int number = input.nextInt();

switch(number){
	case 1->lastCallCost();
	case 2->allCallsCost();
	case 3->clearCounters();
	case 0->callRegister();
	}
}

public static void lastCallCost(){
System.out.print("0.Exit");

System.out.println("Enter option: ");
int number = input.nextInt();

if(number == 0){
	showCallCosts();
	}
}

public static void allCallCost(){
System.out.print("0.Exit");

System.out.println("Enter option: ");
int number = input.nextInt();

if(number == 0){
	showCallCosts();
	}
}

public static void clearCounter(){
System.out.print("0.Exit");

System.out.println("Enter option: ");
int number = input.nextInt();

if(number == 0){
	showCallCosts();
	}
}


public static void callCostSettings() {
System.out.println("""
	1.Call cost limit
	2.Show costs in
	0. Exit""");

System.out.println("Enter option: ");
int number = input.nextInt();

switch(number){
	case 1->callCostLimit();
	case 2->showCostsIn();
	case 0->callRegister();
	}
}

public static void CallCostLimit(){
System.out.print("0.Exit");

System.out.println("Enter option: ");
int number = input.nextInt();

if(number == 0){
	callCostSettings();
	}
}

public static void showCostIn(){
System.out.print("0.Exit");

System.out.println("Enter option: ");
int number = input.nextInt();

if(number == 0){
	callCostSettings();
	}
}




public static void missedCalls() {
System.out.println("0.Exit");

System.out.print("Enter option: ");
int number = input.nextInt();

if(number == 0){
	callRegister();
	}


}

public static void receivedCalls() {
System.out.println("0.Exit");

System.out.print("Enter option: ");
int number = input.nextInt();

if(number == 0){
	callRegister();
	}

}

public static void dialedNumbers() {
System.out.println("0.Exit");

System.out.print("Enter option: ");
int number = input.nextInt();

if(number == 0){
	callRegister();
	}

}

public static void eraseRecentCallLists() {
System.out.println("0.Exit");

System.out.print("Enter option: ");
int number = input.nextInt();

if(number == 0){
	callRegister();
	}

}





public static void allCallsDuration() {
System.out.println("0.Exit");

System.out.print("Enter option: ");
int number = input.nextInt();

if(number == 0){
	callRegister();
	}

}

public static void receivedCallsDuration(){
System.out.println("0.Exit");

System.out.print("Enter option: ");
int number = input.nextInt();

if(number == 0){
	callRegister();
	}

}







public static void allCallsCost() {
System.out.println("0.Exit");

System.out.print("Enter option: ");
int number = input.nextInt();

if(number == 0){
	callRegister();

	}

}

public static void clearCounters() {
System.out.println("0.Exit");

System.out.print("Enter option: ");
int number = input.nextInt();

if(number == 0){
	callRegister();
	}

}



public static void callCostLimit(){
System.out.println("0.Exit");

System.out.print("Enter option: ");
int number = input.nextInt();

if(number == 0){
	callRegister();
	}
}

public static void showCostsIn(){
System.out.println("0.Exit");

System.out.print("Enter option: ");
int number = input.nextInt();

if(number == 0){
	callRegister();
	}

}

public static void prepaidCredit() {
System.out.println("0.Exit");

System.out.print("Enter option: ");
int number = input.nextInt();

if(number == 0){
	callRegister();

	}
}



public static void tones() {
System.out.println("""
	1.Ringing tone
	2.Ringing volume
	3.Incoming call alert
	4.Composer
	5.Message alert tone
	6.Keypad tones
	7.Warning and game tones
	8.Vibration alert
	9.Screen saver
	0. Exit""");


System.out.println("Enter option: ");
int number = input.nextInt();

switch(number){
	case 1->ringingTone();
	case 2->ringingVolume();
	case 3->incomingCallAlert();
	case 4->composer();
	case 5->messagesAlertTone();
	case 6->keypadTones();
	case 7->warningAndGameTones();
	case 8->vibratingAlert();
	case 9->screenSaver();
	case 0->mainMenu();
	
	}
}


	


public static void ringingTone() {
System.out.println("0.Exit");

System.out.println("Enter number: ");
int number = input.nextInt();

if(number == 0){
	tones();

	}
}

public static void ringingVolume() {
System.out.println("0.Exit");

System.out.println("Enter number: ");
int number = input.nextInt();

if(number == 0){
	tones();

	}
}

public static void incomingCallAlert() {
System.out.println("0.Exit");

System.out.println("Enter number: ");
int number = input.nextInt();

if(number == 0){
	tones();

	}
}

public static void composer() {
System.out.println("0.Exit");

System.out.println("Enter number: ");
int number = input.nextInt();

if(number == 0){
	tones();

	}
}

public static void messagesAlertTone() {
System.out.println("0.Exit");

System.out.println("Enter number: ");
int number = input.nextInt();

if(number == 0){
	tones();

	}
}

public static void keypadTones() {
System.out.println("0.Exit");

System.out.println("Enter number: ");
int number = input.nextInt();

if(number == 0){
	tones();

	}
}

public static void warningAndGameTones() {
System.out.println("0.Exit");

System.out.println("Enter number: ");
int number = input.nextInt();

if(number == 0){
	tones();

	}
}

public static void vibratingAlert() {
System.out.println("0.Exit");

System.out.println("Enter number: ");
int number = input.nextInt();

if(number == 0){
	tones();

	}
}

public static void screenSaver() {
System.out.println("0.Exit");

System.out.println("Enter number: ");
int number = input.nextInt();

if(number == 0){
	tones();

	}
}



public static void settings() {
System.out.println("""
	1.Call settings
	2.Phone settings
	3.Security settings
	4.Restore factory settings
	0.Exit""");

System.out.print("Enter option: ");
int number = input.nextInt();

switch(number){
	case 1->callSettings();
	case 2->phoneSettings();
	case 3->securitySettings();
	case 4->restoreFactorySettings();
	case 0->mainMenu();

	}
}



public static void callSettings() {
System.out.println("""
	1.Automatic redial
	2.Speed dialing
	3.Call waiting options
	4.Own number sending
	5.Phone line in use
	6.Automatic answer
	0. Exit""");


System.out.println("Enter option: ");
int number = input.nextInt();

switch(number){
	case 1->automaticRedial();
	case 2->speedDialing();
	case 3->callWaitingOptions();
	case 4->ownNumberSending();
	case 5->phoneLineInUse();
	case 6->automaticAnswer();
	case 0->settings();

	}
}

public static void automaticRedial() {
System.out.println("0.Exit");

System.out.println("Enter option: ");
int number = input.nextInt();

if(number == 0){
	callSettings();
	}
}


public static void speedDialing() {
System.out.println("0.Exit");

System.out.println("Enter option: ");
int number = input.nextInt();

if(number == 0){
	callSettings();
	}
}

public static void callWaitingOptions() {
System.out.println("0.Exit");

System.out.println("Enter option: ");
int number = input.nextInt();

if(number == 0){
	callSettings();
	}
}

public static void ownNumberSending() {
System.out.println("0.Exit");

System.out.println("Enter option: ");
int number = input.nextInt();

if(number == 0){
	callSettings();
	}
}

public static void phoneLineInUse() {
System.out.println("0.Exit");

System.out.println("Enter option: ");
int number = input.nextInt();

if(number == 0){
	callSettings();
	}
}

public static void automaticAnswer() {
System.out.println("0.Exit");

System.out.println("Enter option: ");
int number = input.nextInt();

if(number == 0){
	callSettings();
	}
}



public static void phoneSettings() {
System.out.println("""
	1.Language
	2.Cell info display
	3.Welcome Notes
	4.Network selection
	5.Lights
	6.Confirm SIM service actions
	0. Exit""");

System.out.println("Enter option: ");
int number = input.nextInt();
switch(number){
	case 1->language();
	case 2->cellInfoDisplay();
	case 3-> welcomeNote();
	case 4->networkSelection();
	case 5->lights();
	case 6->confirmSimServiceActions();
	case 0->settings();
	}
}

public static void language() {
System.out.println("0.Exit");

System.out.println("Enter option: ");
int number = input.nextInt();

if(number == 0){
	phoneSettings();
	}
}

public static void cellInfoDisplay() {
System.out.println("0.Exit");

System.out.println("Enter option: ");
int number = input.nextInt();

if(number == 0){
	phoneSettings();
	}
}

public static void welcomeNote(){
System.out.println("0.Exit");

System.out.println("Enter option: ");
int number = input.nextInt();

if(number == 0){
	phoneSettings();
	}
}

public static void networkSelection() {
System.out.println("0.Exit");

System.out.println("Enter option: ");
int number = input.nextInt();

if(number == 0){
	phoneSettings();
	}
}

public static void lights() {
System.out.println("0.Exit");

System.out.println("Enter option: ");
int number = input.nextInt();

if(number == 0){
	phoneSettings();
	}
}

public static void confirmSimServiceActions() {
System.out.println("0.Exit");

System.out.println("Enter option: ");
int number = input.nextInt();

if(number == 0){
	phoneSettings();
	}
}



public static void securitySettings() {
System.out.println("""
	1.Pin code request
	2.Call barring service
	3.Fixed dialing
	4.Closed user group
	5.Phone security
	6.Change access codes
	0. Exit""");

System.out.print("Enter option: ");
int number = input.nextInt();

switch(number){
	case 1->pinCodeRequest();
	case 2->callBarringService();
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
