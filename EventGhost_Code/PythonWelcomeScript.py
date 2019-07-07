    
import random

# Modify the these reponse to customise your experience
GOODBYE_RESPONSES = ["Got it, talk to you later", "Actioning", "Got it, talk to you next time", "Sure thing, I live to serve", "No problem, good bye"]
WELCOME_RESPONSES = ["Confirm your command", "What do you desire my master", "Sure thing, please confirm your command"]

eg.globals.bb_cmd = ''
eg.globals.bb_location = ''
eg.globals.bb_skillid= ''
eg.globals.bb_session = ''
eg.globals.bb_request = ''
ReturnMsg = ''
EndSession = 'yes'

if len(eg.event.payload) > 2:

    eg.globals.bb_cmd = eg.event.payload[0]
    eg.globals.bb_location =  eg.event.payload[1] #Location (deviceID)
    eg.globals.bb_skillid= eg.event.payload[2] #SkillID
    eg.globals.bb_session = eg.event.payload[3] #SessionID
    eg.globals.bb_request = eg.event.payload[4] #RequestID

    #This is an example of how to configure a triggered event from the Invocation command alone
    #In this configuration it is recognising the skill id set in line below (replace x's with your skill id),
    #then triggering an event (change "innvoation action example" to what ever event description you desire"),
    #then finally ending the session so you are not prompted for a command, or more specifically with the Welcome messages above.
    if eg.globals.bb_skillid == 'amzn1.ask.skill.xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx':
        eg.TriggerEvent('Invocation action example 1')
        ReturnMsg = random.choice(WELCOME_RESPONSES)
        EndSession = 'yes'
    
    #As above, this elif statement is provided for quick copy and pasting convience.
    elif eg.globals.bb_skillid == 'amzn1.ask.skill.xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx':
        eg.TriggerEvent('Invocation action example 2')
        #This eample has a customised confirmation message
        ReturnMsg = random.choice(WELCOME_RESPONSES)
        #ReturnMsg = random.choice(WELCOME_RESPONSES)
        EndSession = 'yes'  

    else:
        #This is the welcome response used when initiatied by a skillID not in the above if/elif statements
        ReturnMsg = random.choice(WELCOME_RESPONSES)
        EndSession = 'no'

else:
    print 'Something went wrong, not enough objects in the payload'
    ReturnMsg = 'There was an error, something is wrong!'
    EndSession = 'yes'

#Formate the response message to Alexa
eg.globals.bb_msg = 'Welcome Msg: ' + ReturnMsg + '\nEndSession: ' + EndSession
print eg.globals.bb_msg

#This will pass a formated response to the index.html page which is read by your Alexa skill as a response.
eg.plugins.Webserver.SetValue(u'bb_response', u'{eg.globals.bb_msg}', False, False)

