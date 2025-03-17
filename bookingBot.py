import discord
from discord.ext import commands, tasks
import datetime
import json

# get_json_data function
def get_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data

# debug_data function
def debug_data(TOKEN, CHANNEL_ID, USER_DICT, BOOKING_DICT, TAG_RESET, message0, message1, emoji_id, debug_user_id):
    print('TOKEN:', TOKEN)
    print('CHANNEL_ID:', CHANNEL_ID)
    print('USER_DICT:', USER_DICT)
    print('BOOKING_DICT:', BOOKING_DICT)
    print('TAG_RESET:', TAG_RESET)
    print('message0:', message0)
    print('message1:', message1)
    print('emoji_id:', emoji_id)
    print('debug_user_id:', debug_user_id)

# set up the bot
def setup_bot():
    # Set up intents
    intents = discord.Intents.default()
    intents.members = True
    bot = commands.Bot(command_prefix='!', intents=intents)
    return bot

# main function
if __name__ == '__main__':
    file_path = 'bookingBot.json'
    data = get_data(file_path)

    TOKEN = data["TOKEN"]
    CHANNEL_ID = data["CHANNEL_ID"]
    USER_DICT = data["USERS_DICT"]
    BOOKING_DICT = data["BOOKING_DICT"]
    booking_time = data["BOOKING_TIME"]
    TAG_RESET = data["TAG_RESET"]
    message0 = data["MESSAGE0"]
    message1 = data["MESSAGE1"]
    emoji_id = data["EMOJI_ID"]
    debug_user_id = data["DEBUG_USER_ID"]

    # 
    # 
    # 
    debug_testingMode = data["DEBUG_TESTING_MODE"]
    if debug_testingMode:
        debug_data(TOKEN, CHANNEL_ID, USER_DICT, BOOKING_DICT, TAG_RESET, message0, message1, emoji_id, debug_user_id)
    # 
    # 
    # 

    bot = setup_bot()

    # bot setup
    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user}')
        send_booking_message.start()  # Start the scheduled task

    @tasks.loop(minutes=15)  # Check every 15 minutes
    async def send_booking_message():
        now = datetime.datetime.now()
        future_date = now + datetime.timedelta(days=14)
        print(now)

        # debug_testingMode = True
        if debug_testingMode:
            channel = bot.get_channel(CHANNEL_ID)
            if channel == None:
                print("Channel not found.")
                return
            member = channel.guild.get_member(debug_user_id) # put your dc user id here
            if channel:
                await channel.send(f"testing!")
                await channel.send(f"see if i can {member.mention} here")
                await channel.send(f"{message0}")
                await channel.send(f"{message1}")
                if emoji_id:
                    await channel.send(f"{bot.get_emoji(emoji_id)}")
            else:
                print("Channel not found.")
        # booking mode
        else:
            if now.hour < 23:
                for now_hour in booking_time:
                    if str(now.hour) == now_hour:
                        channel = bot.get_channel(CHANNEL_ID)
                        if channel == None:
                            print("Channel not found.")
                            return
                        member_id = USER_DICT[BOOKING_DICT[now_hour][now.weekday()]]
                        if member_id == 0:
                            print("Nothing to book now.")
                            return
                        member = channel.guild.get_member(member_id)
                        if channel:
                            if TAG_RESET[now_hour] == 1:
                                await channel.send(f"{member.mention} https://app.usthing.xyz/booking/new?date={future_date.year}-{future_date.month}-{future_date.day}&time={now.hour}00&size=medium")
                                await channel.send(f"{message0}")
                                await channel.send(f"https://lbbooking.hkust.edu.hk/calendar/edit_entry.php?area=3&room=89&hour={now.hour}&minute=0&year={future_date.year}&month={future_date.month}&day={future_date.day}")
                                await channel.send(f"{message1}")
                                if emoji_id:
                                    await channel.send(f"{bot.get_emoji(emoji_id)}")
                                TAG_RESET[now_hour] = 0
                        else:
                            print("Channel not found.")
            else:
                for now_hour in booking_time:
                    TAG_RESET[now_hour] = 1

    @send_booking_message.before_loop
    async def before_send_booking_message():
        await bot.wait_until_ready()  # Wait until the bot is ready

    # Run the bot
    bot.run(TOKEN)
