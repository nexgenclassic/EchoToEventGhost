import random

GOODBYE_RESPONSES = ["talk to you later", \
                    "the girls in this household have to do all the hard work",\
                    "peace out", \
                    "All done", "Catch ya later!", \
                    "I am happy to help", \
                    ",POW!, the job is done", \
                    ", You are lucky I dont charge by the hour", \
                    ", phew, no rest for the wicked!", \
                    ", I wonder why I bother", \
                    ", would you like me to wipe your bum next time too?", \
                    "Smell ya later", \
                    "next time, do it yourself lazy guts", \
                    "talk to you next time", \
                    "Done, did you know I like cheese?", \
                    "I live to serve", \
                    "good bye", \
                    "Next time get smudge to do it"]
PLAY_RESPONSES = ["Lets get rocking", \
                    "Lets get this party started"]

eg.globals.bb_cmd = ''
eg.globals.bb_location = ''                                                                                                                                                         
eg.globals.bb_skillid = ''
eg.globals.bb_session = ''
eg.globals.bb_request = ''
ReturnMsg = ''
EndSession = 'yes'



if len(eg.event.payload) > 2:
    
    eg.globals.bb_cmd = eg.event.payload[0]
    eg.globals.bb_location =  eg.event.payload[1] #Location (deviceID)
    eg.globals.bb_skillid = eg.event.payload[2] #SkillID
    eg.globals.bb_session = eg.event.payload[3] #SessionID
    eg.globals.bb_request = eg.event.payload[4] #RequestID

	#Example 1
    if eg.globals.bb_cmd == 'skip' or eg.globals.bb_cmd == 'skip track':
        eg.TriggerEvent('Alexa-skip track')
        ReturnMsg = 'Lets find a better track, ' 
        EndSession = 'yes'
    
    #Example 2 This is a configured example used in the tutorial of the configuration of option 1.
    #elif eg.globals.bb_cmd.startswith('LightsOnIn'):
    #                eg.TriggerEvent('Alexa.' + eg.globals.bb_cmd)
    #                ReturnMsg = 'Bing! the ' + eg.globals.bb_cmd.partition(' ')[2] + ' lights are on.'
    #                EndSession = 'yes'

    #Example 3
	elif   eg.globals.bb_cmd == 'play':
                    eg.TriggerEvent('Alexa.Play/Pause')
                    ReturnMsg = 'Got it, ' + random.choice(PLAY_RESPONSES)
                    EndSession = 'yes'
        
    #Example 4 Using multiple slots to trigger an event (usful when using configuration option 3 without configuring specific slots)
	elif   eg.globals.bb_cmd == 'turn off' or \
                    eg.globals.bb_cmd == 'shutdown' or \
                    eg.globals.bb_cmd == 'switch off' or \
                    eg.globals.bb_cmd == 'volume down' or \
                    eg.globals.bb_cmd == 'volume up' or \
                    eg.globals.bb_cmd == 'volume max':
        #Action
        eg.TriggerEvent('Alexa.TurnOff')
        ReturnMsg = 'Got it, ' + random.choice(GOODBYE_RESPONSES)
        EndSession = 'yes' 
    
    else:
        
        #Option 1: If you only want to process configured commands remove "#" from lines below and add "#" to Option 2 code lines.
        #ReturnMsg = 'I did not understand the command ' + eg.globals.bb_cmd + ' , please try a command like lights on'
        #EndSession = 'no'
        
        #Option 2: to attempt command as interpruted. Allows you to quickly setup multiple commands, but prone to miscommunication
        ReturnMsg = 'Trying command ' + eg.globals.bb_cmd
        eg.TriggerEvent('Alexa.' +eg.globals.bb_cmd)
        EndSession = 'yes'
else:
    print 'Something went wrong, not enough objects in the payload'
    ReturnMsg = 'There was an error, ' + random.choice(GOODBYE_RESPONSES)
    EndSession = 'yes'
    

#Format the response message to Alexa
eg.globals.bb_msg = 'Return Msg: ' + ReturnMsg + \
' \nEndSession: ' + EndSession
print ReturnMsg

#This will pass a formated response to the index.html page which is read by your Alexa skill as a response.
eg.plugins.Webserver.SetValue(u'bb_response', u'{eg.globals.bb_msg}', False, False)
