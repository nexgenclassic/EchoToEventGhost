# Getting Started with EchoToEG for Amazon Alexa

# Overview

EchoToEG allows you to trigger events in EventGhost using voice commands through Amazon Alexa.

There are 3 ways to interact which are configured in Alexa skills.

There is a detailed step-by-step instruction with screenshots in the repo should you get stuck. It&#39;s perhaps a little too detailed for experienced users, but should be useful for trouble shooting.

## Option 1 – Invocation, intent and action:-

-  (Invocation, Intent, Action)
   - Example 1: Alexa, &quot;Event ghost&quot;, &quot;perform action&quot;, &quot;lights on&quot;
    - Example 2: Alexa, &quot;ask Event ghost to perform action lights on&quot;
   - Example 3: Alexa, &quot;Event ghost&quot;, &quot;Dim lights&quot;, &quot;in dining room&quot;
- Benefits:
  - The actions can be configured with all sorts of pre-configured structure using the Alexa toolkit. This is useful if you want content like numbers, dates, weekdays etc...
  - Can be configured with lots of commands without spending a lot of time configuring Alexa skills.
  - The example is configured with Action slot defined as a search query, this allows you to pass any command to EG to trigger events (i,e Alexa, &quot;Event ghost&quot;, &quot;perform action&quot;, whatever you say)
- Drawback:
  - Lots of words to initiate actions

## Option 2 - Invocation and intent:-

- Shorter (Invocation, Intent)
  - Example 1: Alexa, &quot;Event ghost&quot;, &quot; play music&quot;
  - Example 2: Alexa, &quot;ask Event ghost to play music&quot;
- Benefits:
  - Requires a little effort to configure
  - Provides restricted options to ensure Alexa understands the command.
  - Can be configured with multiple utterances (word variances)
- Drawbacks:
  - Not as short as it can be

## Option 3 - Invocation only:-

- Shortest (Invocation)
  - Example 1: Alexa, &quot;initiate music&quot;
- Benefits:
  - Few words required
- Drawbacks:
  - Most effort to configure, requires an Alexa skill per command, linked by the skillID to the EG python code.

You have to stay clear of Alexa&#39;s trigger commands (and there are loads which you will stumble over lots! For example &quot;Play&quot; or &quot;start&quot; would have been the obvious choice rather than &quot;initiate music&quot;, if they weren&#39;t restricted!)

# Setup Tutorial

## Step 1 (Create your AWS Lambda function that your skill will use)

1. Download or clone my EchoToEventGhost github project [https://github.com/nexgenclassic/EchoToEventGhost](https://github.com/nexgenclassic/EchoToEventGhost)
2. Make sure you have your EventGhost Webserver is running and you can post to from outside your network.
   - Get Your External IP, [https://whatismyipaddress.com/](https://whatismyipaddress.com/)
    - Plus the post that your have configured for the Event Ghost webserver to run on (80 is default). If you need help with configuring port forwardinglook here [http://www.wikihow.com/Set-Up-Port-Forwarding-on-a-Router](http://www.wikihow.com/Set-Up-Port-Forwarding-on-a-Router)
   - To test goto [http://ip:port/page?event](http://ip:port/page?event) ie. [http://192.168.1.1:80/index.html?EG\_Event](http://192.168.1.1/index.html?EG_Event) and a event should be logged in EventGhost
3. If you do not already have an account on AWS, go to Amazon Web Services and create an account.
4. Log in to the AWS Management Console and navigate to AWS Lambda.
5. Click the region drop-down in the upper-right corner of the console and select either **US East (N. Virginia)** or **EU (Ireland)**. Lambda functions for Alexa skills must be hosted in either the **US East (N. Virginia)** or **EU (Ireland)** region.
6. If you have no Lambda functions yet, click  **Create a Lambda Function**.
7. Select **Author from scratch**.
8. Click in the empty box and select  **Alexa Skills Kit** , then next.
9. For the function name enter  **EchoToEGv3** , the Description can be left blank, and for the runtime select  **Node.js 6.10**

Note: If Node.js 6.10 is not available select a later version. You will be presented with more options later on.

10. Select **Create a new role with basic Lambda permissions** from the drop down.
11. Under the Lambda **function**   **code** section leave as  **Edit code inline.**
12. Delete the existing code and then **copy in the code** from [\EchoToEventGhost\AlexaSkillKit\_Code\EchoToEGv2.js](https://github.com/nexgenclassic/EchoToEventGhost/blob/master/AlexaSkillKit_Code/EchoToEGv2.js)
13. Edit the variables in the code:-
    - Line 17: Is your EventGhost Webserver using **http** and https
    - Line 19: **Enter your External IP** or domain name
    - Line 22: Enter the **port number** you configured in the EventGhost Webserver
    - Lines 30 &amp; 31 are your EventGhost Webserver user name and password

Note: There are other variables that can be set for added security or personalisation. It is recommended you get the function working before exploring these.

14. Under the  **Lambda function handler and role**  section, leave  **Handler**  and  **Role**  as is and for  **Existing role**  select &quot;lamba\_basic\_execution&quot;
15. Leave the other sections as is and click  **Next**  and then on the next page click  **Create Function**
16. Under  **Actions**  you can test your function by using the  **Configure test event** , change the name of  **Hello World**  as needed and pasted the contents of [\EchoToEventGhost\AlexaSkillKit\_Code\EchoToEG\_TestEvent.xml](https://github.com/nexgenclassic/EchoToEventGhost/blob/master/AlexaSkillKit_Code/EchoToEG_TestEvent.xml)  (Line 23 is the command that is passed) and then  **Save and Test**  If all works you could see an event in your EventGhost log.

## Step 2 (Create your Alexa Skill and link your Lambda function)

1. Sign in to the  **Amazon developer portal**. If you haven&#39;t done so already, you&#39;ll need to create a free account. [https://developer.amazon.com/edw/home.html#/](https://developer.amazon.com/edw/home.html#/)
2. From the top navigation bar, select  **Alexa**.
3. Under  **Alexa Skills Kit** , choose  **Create Skill**.
4. Choose  **Add a New Skill**.
5. Name your skill. This is the name displayed to users in the Alexa app.  **Event Ghost**  is a good choice.
6. Leave **Custom** and **provision your own** ptions selected.
7. Click **create skill**.
8. Leave from scratch selected, click **choose**
9. Select **Invocation** in the left side column.
10. Create an invocation name. This is the word or phrase that users will speak to activate the skill.  **Event Ghost**  is a good choice. Amazon recommends against signal word invocation name.
11. Click **JSON Editor**  in the left side column, paste the JSON code from [\EchoToEventGhost\AlexaSkillKit\_Code\IntentSchema.txt](https://github.com/m19brandon/EchoToEventGhost/blob/master/AlexaSkillKit_Code/IntentSchema.txt)
12. Click **Endpoint**  in the left side column and then select **AWS Lambda ARN**.
13. Click Copy to Clipboard to **copy your skill id**.
14. Go **back the AWS Console tab** and paste the skill ID into the **Skill ID box** and click **Add** and then **Save**.
15. Return to the **Alexa skill site** and paste your **ARN number** into the **Default Region**.
16. Click Save **Endpoints** , then **Save Model** and then **Build Model**.

## Step 3 (Ensure your skill is linked to your Alexa)

1. Open the **Alexa app** on your **mobile phone**.
    - Click on the burger menu on the top left and select **SKILLS &amp; GAMES**.
    - Goto **Your Skills** and **select Dev**.
   - **Open the skill** (Event Ghost or whatever your name it) and select **ENABLE TO USE**.

## Step 4 (EventGhost, add some code to make stuff happen)

1. Create a new Python Script Macro, Name it EG Alexa Welcome Script, copy in the contents of  [\EchoToEventGhost\EventGhost\_Code\PythonWelcomeScript.py](https://github.com/nexgenclassic/EchoToEventGhost/blob/master/EventGhost_Code/PythonWelcomeScript.py)
2. Create a second new Python Script Macro, Name it EG Alexa Action Script, copy in the contents of [\EchoToEventGhost\EventGhost\_Code\PythonActionScript.py](https://github.com/nexgenclassic/EchoToEventGhost/blob/master/EventGhost_Code/PythonActionScript.py)
3. Copy [\EchoToEventGhost\EventGhost\_Code\index.html](https://github.com/m19brandon/EchoToEventGhost/blob/master/EventGhost_Code/index.html) into your webserver folder.
4. Now it&#39;s time to talk to Alexa! Say: &quot;Alexa, Event Ghost&quot;. It will error, this is normal.
5. From your EventGhost log, drag the HTTP.EchoToEGWelcome[etc…]. event into the welcome script macro.
6. Now talk to Alexa again! Say: &quot;Alexa, ask Event Ghost to perform action test&quot;. It will error again.
7. From your EventGhost log, drag the EchoToEG [etc…]. event into the action script macro.
8. Test your Skill.

## Setting up your commands

### Example of Option 1 Configuration – Invocation, intent and action:-

The following steps are very similar to the steps completed previously, the main differences are:-

    - You are going to set the skill name to something relevant to the command you are making
    - Choosing your skill name will require more thought to avoid use of Alexa trigger words.

1. Open the alexa development console webpage [https://developer.amazon.com/alexa/console/ask](https://developer.amazon.com/alexa/console/ask) and edit your Event Ghost skill.

Note: If you want to use an invocation name other than &quot;Event Ghost&quot; create a new skill as before.

1. Add a new **Intent** and name it **LightsOnIn** is used in this example.
2. Click on **Create a new slot** and enter a slot name called &quot;room&quot;. Change the Select a slot type to **AMAZON.Room**.
3. Add Sample Utterances &quot;turn the {room} lights on&quot;, &quot;lights on in {room}&quot; and lights on {room}
4. Turn the &quot; **Does this intent require confirmation?&quot;** slider to the **on** position.
5. Add the **Alexa prompt,**&quot;Do you want to turn the {room} lights on?&quot;.
6. Change the &quot; **Is this slot required to fulfil the intent?**&quot; slide to the **on** position.
7. Click **Save Model** and then **build model**. Confirm the build is successful.
8. Test your skill works. Say &quot;Alexa, event ghost&quot;, Alexa will respond with a welcome response, reply &quot;lights on&quot;, Alexa should respond &quot;in which room&quot;, reply &quot;Dining room&quot;, should prompt &quot;do you want to turn the dining room lights on&quot;, reply &quot;Yes&quot;, Alexa should respond &quot;trying command lights on in dining room&quot;.

Note: You can shorten the Alexa command request in a number of ways when the skill is configured in this way. Example &quot;Alexa, ask event ghost to turn the dining room lights on&quot;

Note: You can change the acknowledgement to be relevant to the command. Open the EG Alexa Actions Script python script and you will see # section as an example.

### Example of Option 2 Configuration– Invocation and intent:-

The following steps are mostly a reduced version of the steps in option 1.

1. Open the alexa development console webpage [https://developer.amazon.com/alexa/console/ask](https://developer.amazon.com/alexa/console/ask) and edit your Event Ghost skill.

Note: If you want to use an invocation name other than &quot;Event Ghost&quot; create a new skill as before.

1. Add a new **Intent** and name it **Play** is used in this example.
2. Add Sample Utterances &quot;play music&quot; and &quot;play&quot;
3. Click **Save Model** and then **build model**. Confirm the build is successful.
4. Test your skill works.
  - Say &quot; **Alexa, event ghost**&quot;, Alexa should respond with one of the welcome responses configure in the event ghost python script.
  - Reply &quot; **play**&quot; Alexa should respond &quot;got it, let&#39;s get rocking&quot; or &quot;got it let&#39;s get this party started&quot;.

Note: The play command has already got a preconfigured response in the EventGhost action python script. Take a look at it and review the script for understanding.

### Example of Option 3 Configuration– Invocation only:-

1. The following steps are very similar to the steps completed previously, the only differences are:-
    - You are going to set the skill name to something relevant to the command you are making
    - Choosing your skill name will require more thought to avoid use of Alexa trigger words.
2. Open the **alexa developer console** web page and Click  **Create**  **Skill** within the  **Alexa Skills Kit**
3. Name your skill. This is the name displayed to users in the Alexa app. In this example I have used **welcome me home**.
4. Leave **Custom** and **provision your own** ptions selected. Click **create skill**.
5. Create an invocation name. This is the word or phrase that users will speak to activate the skill. I have used **welcome me home**  in the example. Amazon recommends against signal word invocation name.

Note: Invocation name cannot contain the launch words &quot;ask&quot;, &quot;begin&quot;, &quot;launch&quot;, &quot;load&quot;, &quot;open&quot;, &quot;play&quot;, &quot;resume&quot;, &quot;run&quot;, &quot;start&quot;, &quot;talk to&quot;, or &quot;tell&quot;.

6. Enter a name for the intent. **WelcomeMeHome** is used in the example.
7. Add Sample Utterances. In this example I have used &quot;welcome home&quot;.

Note: No spaces are allowed.

8. Copy your skill id from the **AWS Lambda ARN** within the **Endpoint**  section.
9. Go back the AWS Console tab and add a new **Alexa Skills Kit** and paste the skill ID into the **Skill ID box** and click **Add**. Then **Save**.
10. Copy the ARN address to clipboard. Return to the Alexa skill tab and paste your **ARN number** into the **Default Region**.
11. Click Save **Endpoints** , **Save Model** and then **Build Model**. A message box confirming the build was successful should appear.

Note: There is no need to Publish the skill.

12. Open the **Alexa app** on your **mobile phone**.
   - Click on the burger menu on the top left and select **SKILLS &amp; GAMES**.
   - Goto **Your Skills** and **select Dev**.
   - **Open the skill** (Event Ghost or whatever your name it) and select **ENABLE TO USE**.
13. Return to EventGhost and open the Python script associated to the **EG Alexa Welcome Script.**
14. Paste the skill ID over the amzn1.ask.skill.xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx text on line 28 of the example skill script. Ensure the apostrophes (&#39;) remain either side of the ID.

15. Customise the trigger command and return message to suit your needs. Examples:-
    - Existing code: eg.TriggerEvent(&#39;Invocation action example 1&#39;)
    - Example altered code: eg.TriggerEvent(&#39;Welcome me home&#39;)

    - Existing code: ReturnMsg = random.choice(WELCOME\_RESPONSES)
    - Example altered code: ReturnMsg = &quot;Welcome home. Hasn&#39;t it been a lovely day&quot;

16. Test your skill works. &quot;Alexa, welcome me home&quot;.
