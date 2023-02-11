# instaparse

* Instaparse 0.5.5
* Instaparse 0.5.1
* Instaparse 0.4.7

*What if context-free grammars were as easy to use as regular expressions?*

## Description
This project was created in order to simplify the acquisition of customer data, we are not responsible for what you will do.

## Features

Instaparse aims to be the simplest way to build parsers in Instagram.

+ Authorization, viewing and liking stories by hashtag, geolocation and subscribers of the selected profile. By possible limits and imitation of actions to avoid detection of insta
+ Views and likes go from the latest posts to older posts
+ Work with mobile proxies and from multiple accounts
+ Authorization and task setting for each account
+ Profile subscriber analysis script.
+ Send private messages to users.
+ Full collection of data during the work process for use on the site or elsewhere.

## Quickstart

Instaparse requires Python 3+, 
selenium 4.8.0, instaloader, datetime, langdetect, tabulate
os windows 10 - 11 
chromedriver 


Download the project to your machine:

	git clone https://github.com/VladimirGorin/Instaparse.git

Or:

	download zip

Download Dependencies:

    pip install -r requirements.txt

## Documentation

First of all, go to `/settings/users-settings.json` and set up your accounts there, below you can find a detailed description of what each parameter is responsible for

| Key | Value | 
| ------ | ------ | 
| email | `type:str`your instagram login |
| pass | `type:str`your instagram passwd |
| step | `type:int`For each function there is a step below, I painted in detail each step |
| stories_hastag_scroll | `type:int` Block scroll for step 1 |
| stories_geo_scroll | `type:int` Block scroll for step 3  |
| followes_scroll | `type:int` Block scroll for step 7 |
| scroll_on_sub |  `type:int` Block scroll for step 5 |
| on_sub | `type:str` Specify a category here ```(all available categories are listed below)``` and all users who do not match this category will be unsubscribed from you. |
| sub |`type:dict` Specify users here to analyze their followers |
| hastages |`type:dict` List all the hashtags here, and further on the posts in these hash tags, profiles will be taken and their stories will be viewed  |
| geolocation |`type:dict` List here all geolocations and further on posts in these geopositions, profiles will be taken and their stories will be viewed |
| subscriber |`type:dict` List here all users of the followers you want to view stories |
| auth_id |`type:int` The unique ID allows you to run each listed profile in the settings separately. |
| msg_limit |`type:int` Specify here the number of users to whom you want to unsubscribe, if you want to unsubscribe to everyone, write 0, so if you write 1, then the first user from your chats will not receive messages, the same if you specify 2, then the first two users will not receive a message and then. |
| message_send |`type:str`Enter your message to be sent here|


> Note: Each step starts in order if you specified step 2 for two users, then both of these accounts will work only for them, but if you specified a unique id, then it will launch only one account with the specified id `DO NOT SPECIFY A UNIQUE ID FOR TWO USERS`

## Step Options
    
    step null: Account will be skipped
    
    step 1: By specifying step 1, your account will perform all actions with stories only on hashtag posts.

    step 2: By specifying step 2, your account will perform all actions with stories only on posts with geolocation.
    
    step 3: By specifying step 3, your account will perform all actions with stories only with the followers of the user you specified in the sub array..
    
    step 4: By specifying step 4, your account will perform analytics on the user you specified in the subscriber array..
    
    step 5: By specifying step 5, your account will unsubscribe from the collected audience (the collected audience is analytics) by category, the category and users can be specified in on_sub and the user in the subscriber array.

    step 6: After specifying step 6, ATTENTION THIS STEP SHOULD BE RUN ALWAYS AFTER CHANGE THE USER SETTINGS FILE, this step creates the necessary sessions and json files for recording.
    
    step 7: After specifying step 7, you will send a message to users.

## Analytics Options
All parameters can be viewed after running the analytics along the way `/analytics/users_analytics.json`
    
    commercial: instagram business account
    
    foreign: the language in the profile is not Russian

    massfollowers: the number of subscriptions is more than 1500
    
    inactive: Haven't posted anything for more than 3 months and haven't liked the account's posts
    
    profile_activity:liked or commented in the last 3 months
    
    available_audience:Profiles with less than 1000 followers

    genuine_audience:Profiles with less than 1000 followers

>  If there are errors / bugs / questions, write to me in telegram s.m. profile. You were Vladimir thank you for your attention!

## Output
I have added a full activity tracking function, you can go make tea and when you return look into the `/tracker/your_account_name.json` directory, open the file with the accounts you want and see all the logs.


## License
MIT

**Free Software, Hell Yeah!**
