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
8. 
```bash
pip install discord
```
10. run your bookingBot.py 24/7, or you can start it on every morning and stop it at night
# Booking Link
You will notice that two links are sent simultaneously. The first link is from the Usthing website, allowing you to book a room two hours earlier than the library link. However, the trade-off is that this link does not take you directly to your desired room; you will need to search for it manually. Additionally, there can occasionally be a glitch where the link fails to allow bookings for dates 14 days in advance. In such cases, you'll need to click the link again to access that option.

On the other hand, the second link, provided by the library, guarantees direct access to the specific date and time you wish to book. The drawback, however, is that you must wait two hours before you can reserve a room for a date 14 days from now.
