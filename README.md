# Dialogflow-bot
Google Dialogflow system in Django Project

A custom chatbot that works through Google Dialogflow. As soon as a notification is written to the bot, it compares 
the content by keywords with its database. And when there is a match, the answer is returned.

If necessary, the bot can switch to a manager who will conduct live correspondence with the user. For this, a support 
function has been developed that disables automatic dialog responses. There is a separate page for the manager with a 
list of chats. All correspondence between users and the bot is available in these chats.