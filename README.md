# HKUST-library-roomBooking-reminder-bot
If you and your friends need a study room every weekday, you can use this Discord bot to remind you to book it.
# How to use
1. go to https://discord.com/developers/applications
2. create a new bot, copy its token in "setting" -> "bot" and place it in bookingBot.json's "TOKEN"
3. back to the bot page, turn on "Presence Intent" and "Server Members Intent"
4. go to "setting" -> "installation" -> "Default Install Settings" -> "Guild Install" -> "Scopes" add "bot"
5. "Guild Install" -> "Permissions" add "embed links", "mention everyone", "read message history" and "send messages"
6. copy the link in "setting" -> "installation" -> "Install Link", access it in your browser, add the bot into your server
7. go to bookingBot.json, set the "CHANNEL_ID", "USERS_DICT", "room_name" and "BOOKING_DICT"
8. ```bash pip install discord```
9. run your bookingBot.py 24/7, or you can start it on every morning and stop it at night
