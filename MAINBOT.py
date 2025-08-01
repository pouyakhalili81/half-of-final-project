import telebot
from telebot.types import ReplyKeyboardMarkup,InlineKeyboardMarkup,InlineKeyboardButton,ReplyKeyboardRemove
import pytz
import datetime
from datetime import datetime, timezone
from translate import *
from MAIN import *
from DDL import *
from DML import *
from CONFIG import *
from API import*

bot = telebot.TeleBot(BOT_TOKEN)

User_data = {}
############listener#############
def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            irantz = pytz.timezone('Asia/Tehran')
            dt = datetime.fromtimestamp(m.date, tz=timezone.utc)
            dt_iran = dt.astimezone(irantz)
            time_str = dt_iran.strftime('%Y-%m-%d -- %H:%M:%S')
            log_msg = f"{m.chat.username}--{m.chat.id}-- {time_str} : {m.text}"
            print(log_msg)

########################                         PART             ONE            (START AND HELP)            ######################################

@bot.message_handler(commands=['start'])
def all_message_handler(message):
    cid = message.chat.id
    if is_user_exists(cid):
        main_start(message)
    else:
        start_message_handler(message)
def start_message_handler(message):
    cid = message.chat.id
    User_data[cid] = {}
    bot.send_message(cid,texts['start'])
    bot.send_message(cid,texts['start1'])
    bot.register_next_step_handler(message,start2)
def start2(message):
    cid = message.chat.id
    User_data[cid]['name'] = message.text
    bot.send_message(cid,texts['start22'])
    bot.register_next_step_handler(message,start3)
def start3(message):
    cid = message.chat.id
    user_name = message.chat.username
    fullname = User_data[cid]['name']
    User_data[cid]['age'] = int(message.text)
    age = User_data[cid]['age']
    insert_data_User(cid,user_name,fullname,age)
    User_data.pop(cid)
    main_start(message)
def main_start(message):
    cid = message.chat.id
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    inline = InlineKeyboardMarkup()
    inline.add(InlineKeyboardButton(texts['btn_goal'],callback_data=texts['goal1']),InlineKeyboardButton(texts['btn_reminder'],callback_data=texts['reminder1']))
    inline.add(InlineKeyboardButton(texts['btn_daily'],callback_data=texts['daily1']),InlineKeyboardButton(texts['btn_motive'],callback_data=texts['motive1']))
    inline.add(InlineKeyboardButton(texts['btn_score'],callback_data=texts['score1']),InlineKeyboardButton(texts['btn_account'],callback_data=texts['account1']))
    keyboard.add(texts['btn_goal'],texts['btn_reminder'])
    keyboard.add(texts['btn_daily'],texts['btn_motive'])
    keyboard.add(texts['btn_score'],texts['btn_account'])
    bot.send_message(cid,texts['start'],reply_markup=keyboard)
    bot.send_message(cid,texts['start2'],reply_markup=inline)
    

@bot.message_handler(commands=['help'])
def help_message_handler(message):
    cid = message.chat.id
    firstname = message.chat.first_name
    inline = InlineKeyboardMarkup()
    inline.add(InlineKeyboardButton(texts['btn_goal'],callback_data=texts['goal1']),InlineKeyboardButton(texts['btn_reminder'],callback_data=texts['reminder1']))
    inline.add(InlineKeyboardButton(texts['btn_daily'],callback_data=texts['daily1']),InlineKeyboardButton(texts['btn_motive'],callback_data=texts['motive1']))
    inline.add(InlineKeyboardButton(texts['btn_score'],callback_data=texts['score1']),InlineKeyboardButton(texts['btn_account'],callback_data=texts['account1']))
    bot.send_message(cid,text=texts['help'],reply_markup=inline)
########################                         PART             TWO            (MAIN   COMMANDS)           ######################################
########################                         KEYBOARD                           HANDLERS                 ######################################
@bot.message_handler(func= lambda msg : msg.text == texts['btn_goal'])
def Goal1_message_handler(message):
    cid = message.chat.id
    firstname = message.chat.first_name
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    inline = InlineKeyboardMarkup()
    inline.add(InlineKeyboardButton(texts['goal_add'],callback_data=texts['goal_add1']),InlineKeyboardButton(texts['goal_remove'],callback_data=texts['goal_remove1']))
    inline.add(InlineKeyboardButton(texts['goal_edit'],callback_data=texts['goal_edit1']),InlineKeyboardButton(texts['goal_show'],callback_data=texts['goal_show1']))
    inline.add(InlineKeyboardButton(texts['goal_report'],callback_data=texts['goal_report1']),InlineKeyboardButton(texts['btn_back'],callback_data=texts['back1']))
    keyboard.add(texts['goal_add'], texts['goal_remove'])
    keyboard.add(texts['goal_edit'], texts['goal_show'])
    keyboard.add(texts['goal_report'],texts['btn_back'])
    bot.send_message(cid,texts['goal'],reply_markup=keyboard)
    bot.send_message(cid,texts['service'],reply_markup=inline)

@bot.message_handler(func = lambda msg : msg.text == texts['btn_reminder'])
def Reminder1_message_handler(message):
    cid = message.chat.id
    firstname = message.chat.first_name
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    inline = InlineKeyboardMarkup()
    inline.add(InlineKeyboardButton(texts['reminder_add'],callback_data=texts['reminder_add1']),InlineKeyboardButton(texts['reminder_remove'],callback_data=texts['reminder_remove1']))
    inline.add(InlineKeyboardButton(texts['reminder_edit'],callback_data=texts['reminder_edit1']),InlineKeyboardButton(texts['reminder_show'],callback_data=texts['reminder_show1']))
    inline.add(InlineKeyboardButton(texts['reminder_report'],callback_data=texts['reminder_report1']),InlineKeyboardButton(texts['btn_back'],callback_data=texts['back1']))
    keyboard.add(texts['reminder_add'],texts['reminder_remove'])
    keyboard.add(texts['reminder_edit'],texts['reminder_show'])
    keyboard.add(texts['reminder_report'],texts['btn_back'])
    bot.send_message(cid,texts['reminder'],reply_markup=keyboard)
    bot.send_message(cid,texts['service'],reply_markup=inline)

@bot.message_handler(func = lambda msg : msg.text == texts['btn_daily'])
def Daily_plan1_message_handler(message):
    cid = message.chat.id
    firstname = message.chat.first_name
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    inline = InlineKeyboardMarkup()
    inline.add(InlineKeyboardButton(texts['daily_add'],callback_data=texts['daily_add1']),InlineKeyboardButton(texts['daily_remove'],callback_data=texts['daily_remove1']))
    inline.add(InlineKeyboardButton(texts['daily_edit'],callback_data=texts['daily_edit1']),InlineKeyboardButton(texts['daily_show'],callback_data=texts['daily_show1']))
    inline.add(InlineKeyboardButton(texts['daily_report'],callback_data=texts['daily_report1']),InlineKeyboardButton(texts['btn_back'],callback_data=texts['back1']))
    keyboard.add(texts['daily_add'],texts['daily_remove'])
    keyboard.add(texts['daily_edit'],texts['daily_show'])
    keyboard.add(texts['daily_report'],texts['btn_back'])
    bot.send_message(cid,texts['daily_plan'],reply_markup=keyboard)
    bot.send_message(cid,texts['service'],reply_markup=inline)

@bot.message_handler(func = lambda msg : msg.text == texts['btn_score'])
def Score_Result1_message_handler(message):
    cid = message.chat.id
    firstname = message.chat.first_name
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    inline = InlineKeyboardMarkup()
    inline.add(InlineKeyboardButton(texts['score_goal'],callback_data=texts['goal_scores']),InlineKeyboardButton(texts['score_reminder'],callback_data=texts['reminder_scores']),InlineKeyboardButton(texts['btn_back'],callback_data=texts['back1']))
    keyboard.add(texts['score_goal'],texts['score_reminder'],texts['btn_back'])
    bot.send_message(cid,texts['score'],reply_markup=keyboard)
    bot.send_message(cid,texts['service'],reply_markup=inline)

@bot.message_handler(func = lambda msg : msg.text == texts['btn_motive'])
def Motive_Messages1_message_handler(message):
    cid = message.chat.id
    firstname = message.chat.first_name
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    inline = InlineKeyboardMarkup()
    inline.add(InlineKeyboardButton(texts['motive_activate'],callback_data=texts['motive_activate1']),InlineKeyboardButton(texts['motive_deactivate'],callback_data=texts['motive_deactivate1']))
    inline.add(InlineKeyboardButton(texts['motive_edit'],callback_data=texts['edit_send_time1']),InlineKeyboardButton(texts['btn_back'],callback_data=texts['back1']))
    keyboard.add(texts['motive_activate'],texts['motive_deactivate'])
    keyboard.add(texts['motive_edit'],texts['btn_back'])
    bot.send_message(cid,texts['motive'],reply_markup=keyboard)
    bot.send_message(cid,texts['service'],reply_markup=inline)

@bot.message_handler(func = lambda msg : msg.text == texts['btn_account'])
def Manange_Account1_message_handler(message):
    cid = message.chat.id
    firstname = message.chat.first_name
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    inline = InlineKeyboardMarkup()
    inline.add(InlineKeyboardButton(texts['account_add'],callback_data=texts['add_info1']),InlineKeyboardButton(texts['account_show'],callback_data=texts['show_info1']))
    inline.add(InlineKeyboardButton(texts['account_edit'],callback_data=texts['edit_info1']),InlineKeyboardButton(texts['account_remove'],callback_data=texts['remove_info1']))
    inline.add(InlineKeyboardButton(texts['btn_back'],callback_data=texts['back1']))
    keyboard.add(texts['account_add'],texts['account_show'])
    keyboard.add(texts['account_edit'],(texts['account_remove']))
    keyboard.add(texts['btn_back'])
    bot.send_message(cid,texts['account'],reply_markup=keyboard)
    bot.send_message(cid,texts['service'],reply_markup=inline)

@bot.message_handler(func = lambda msg : msg.text == texts['btn_back'])
def Back_message_handler(message):
    cid = message.chat.id
    firstname = message.chat.first_name
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    inline = InlineKeyboardMarkup()
    inline.add(InlineKeyboardButton(texts['btn_goal'],callback_data=texts['goal1']),InlineKeyboardButton(texts['btn_reminder'],callback_data=texts['reminder1']))
    inline.add(InlineKeyboardButton(texts['btn_daily'],callback_data=texts['daily1']),InlineKeyboardButton(texts['btn_motive'],callback_data=texts['motive1']))
    inline.add(InlineKeyboardButton(texts['btn_score'],callback_data=texts['score1']),InlineKeyboardButton(texts['btn_account'],callback_data=texts['account1']))
    keyboard.add(texts['btn_goal'],texts['btn_reminder'])
    keyboard.add(texts['btn_daily'],texts['btn_motive'])
    keyboard.add(texts['btn_score'],texts['btn_account'])
    bot.send_message(cid,texts['callback_back1'],reply_markup=keyboard)
    bot.send_message(cid,texts['service'],reply_markup=inline)
########################                         CALLBACK                           HANDLERS                               ########################
@bot.callback_query_handler(func=lambda call: True)
def call_handler(call):
    call_id = call.id
    cid = call.message.chat.id
    mid = call.message.message_id
    firstname = call.from_user.first_name
    data = call.data
    bot.answer_callback_query(call_id, data)
    if data.startswith(texts['goal1']):
        inline = InlineKeyboardMarkup()
        inline.add(InlineKeyboardButton(texts['goal_add'],callback_data=texts['goal_add1']),InlineKeyboardButton(texts['goal_remove'],callback_data=texts['goal_remove1']))
        inline.add(InlineKeyboardButton(texts['goal_edit'],callback_data=texts['goal_edit1']),InlineKeyboardButton(texts['goal_show'],callback_data=texts['goal_show1']))
        inline.add(InlineKeyboardButton(texts['goal_report'],callback_data=texts['goal_report1']),InlineKeyboardButton(texts['btn_back'],callback_data=texts['back1']))
        text = (texts['goal'])
        bot.edit_message_text(chat_id=cid, message_id=mid, text=text, reply_markup=inline)
    elif data.startswith(texts['reminder1']):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        inline = InlineKeyboardMarkup()
        inline.add(InlineKeyboardButton(texts['reminder_add'],callback_data=texts['reminder_add1']),InlineKeyboardButton(texts['reminder_remove'],callback_data=texts['reminder_remove1']))
        inline.add(InlineKeyboardButton(texts['reminder_edit'],callback_data=texts['reminder_edit1']),InlineKeyboardButton(texts['reminder_show'],callback_data=texts['reminder_show1']))
        inline.add(InlineKeyboardButton(texts['reminder_report'],callback_data=texts['reminder_report1']),InlineKeyboardButton(texts['btn_back'],callback_data=texts['back1']))
        text = (texts['reminder'])
        bot.edit_message_text(chat_id = cid,message_id = mid , text = text ,reply_markup=inline)

    elif data.startswith(texts['daily1']):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        inline = InlineKeyboardMarkup()
        inline.add(InlineKeyboardButton(texts['daily_add'],callback_data=texts['daily_add1']),InlineKeyboardButton(texts['daily_remove'],callback_data=texts['daily_remove1']))
        inline.add(InlineKeyboardButton(texts['daily_edit'],callback_data=texts['daily_edit1']),InlineKeyboardButton(texts['daily_show'],callback_data=texts['daily_show1']))
        inline.add(InlineKeyboardButton(texts['daily_report'],callback_data=texts['daily_report1']),InlineKeyboardButton(texts['btn_back'],callback_data=texts['back1']))
        text = (texts['daily_plan'])
        bot.edit_message_text(chat_id=cid,message_id = mid  ,text = text ,reply_markup=inline)

    elif data.startswith(texts['motive1']):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        inline = InlineKeyboardMarkup()
        inline.add(InlineKeyboardButton(texts['motive_activate'],callback_data=texts['motive_activate1']),InlineKeyboardButton(texts['motive_deactivate'],callback_data=texts['motive_deactivate1']))
        inline.add(InlineKeyboardButton(texts['motive_edit'],callback_data=texts['edit_send_time1']),InlineKeyboardButton(texts['btn_back'],callback_data=texts['back1']))
        text = (texts['motive'])
        bot.edit_message_text(chat_id=cid,message_id = mid , text = text,reply_markup=inline)

    elif data.startswith(texts['score1']):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        inline = InlineKeyboardMarkup()
        inline = InlineKeyboardMarkup()
        inline.add(InlineKeyboardButton(texts['score_goal'],callback_data=texts['goal_scores']),InlineKeyboardButton(texts['score_reminder'],callback_data=texts['reminder_scores']),InlineKeyboardButton(texts['btn_back'],callback_data=texts['back1']))
        text = (texts['score'])
        bot.edit_message_text(chat_id=cid,message_id = mid,text = text,reply_markup=inline)

    elif data.startswith(texts["account1"]):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        inline = InlineKeyboardMarkup()
        inline.add(InlineKeyboardButton(texts['account_add'],callback_data=texts['add_info1']),InlineKeyboardButton(texts['account_show'],callback_data=texts['show_info1']))
        inline.add(InlineKeyboardButton(texts['account_edit'],callback_data=texts['edit_info1']),InlineKeyboardButton(texts['account_remove'],callback_data=texts['remove_info1']))
        inline.add(InlineKeyboardButton(texts['btn_back'],callback_data=texts['back1']))
        text = (texts['account'])
        bot.edit_message_text(chat_id=cid,message_id=mid,text = text ,reply_markup=inline)

    elif data.startswith(texts['back1']):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        inline = InlineKeyboardMarkup()
        inline.add(InlineKeyboardButton(texts['btn_goal'], callback_data=texts['goal1']), InlineKeyboardButton(texts['btn_reminder'], callback_data=texts['reminder1']))
        inline.add(InlineKeyboardButton(texts['btn_daily'], callback_data=texts['daily1']), InlineKeyboardButton(texts['btn_motive'], callback_data=texts['motive1']))
        inline.add(InlineKeyboardButton(texts['btn_score'], callback_data=texts['score1']), InlineKeyboardButton(texts['btn_account'], callback_data=texts['account1']))
        text = texts['start']
        bot.edit_message_text(chat_id=cid, message_id=mid, text=text, reply_markup=inline)
    ########################                          PART             THREE           (STEP   HANDLERS )                      ########################
#                         GOAL STEP HANDLERS                         #
@bot.message_handler(func= lambda msg : msg.text == texts['goal_add'] )
def add_goal_message_handler(message):
    cid = message.chat.id
    User_data[cid] = {}
    bot.send_message(cid ,texts['goal_ask_title'])
    bot.register_next_step_handler(message,add_goal_register)
def add_goal_register(message):
    cid = message.chat.id
    User_data[cid]['title'] = message.text.strip()
    bot.send_message(cid,texts['goal_ask_description'])
    bot.register_next_step_handler(message,desc_goal_register)
def desc_goal_register(message):
    cid = message.chat.id
    User_data[cid]['desc'] = message.text.strip()
    bot.send_message(cid,texts['goal_ask_deadline'])
    bot.register_next_step_handler(message,save_goal_deadline)
def save_goal_deadline(message):
    cid = message.chat.id
    deadline = message.text.strip()
    if '/' not in deadline or not valid_date(deadline):
        bot.send_message(cid, texts['goal_ask_deadline'])
        bot.register_next_step_handler(message, save_goal_deadline)
        return

    User_data[cid]['time'] = deadline
    title = User_data[cid]['title']
    description = User_data[cid]['desc']
    time = User_data[cid]['time']
    text = f"{texts['unvan']} = {title}\n{texts['desc']} = {description}\n{texts['mohlat']} = {time}"

    
    goal_id = insert_data_Goal(cid,title,description,time)

    bot.send_message(cid, text)
    bot.send_message(cid, f"{texts['goal_saved']}\n{texts['your_goal_id']} {goal_id}")
    User_data.pop(cid, None)


    
def valid_date(date):
    part = date.strip().split('/')
    if len(part) != 3:
        return  texts['false']
    year, month, day = part
    return year.isdigit() and month.isdigit() and day.isdigit()

def valid_time(time):
    part = time.strip().split(':')
    if len(part) != 2:
        return texts['false']
    hour, minute = part
    if not (hour.isdigit() and minute.isdigit()):
        return texts['false']
    hour = int(hour)
    minute = int(minute)
    return 0 <= hour < 24 and 0 <= minute < 60

@bot.message_handler(func=lambda msg: msg.text == texts['goal_show'])
def show_goal(message):
    cid = message.chat.id
    goals = show_all_Goal(cid) 
    if goals:
        all_text = ''
        for goal in goals:
            goal_id = goal[0]
            title = goal[1]
            text_goal = goal[2]
            aim_date = goal[3]
            all_text += (
            f"{texts['id']}: {goal_id}\n"
            f"{texts['title']}: {title}\n"
            f"{texts['goal_desc']}: {text_goal}\n"
            f"{texts['date']}: {aim_date}\n"
            "-------------\n"
                            )
        bot.send_message(cid,texts['goal_show_msg'])
        bot.send_message(cid, all_text)  
    else:
        bot.send_message(cid, texts['no_goal'])


@bot.message_handler(func= lambda msg : msg.text == texts['goal_remove'])
def goal_remove(message):
    cid = message.chat.id
    User_data[cid] = {}
    show_goal(message)
    bot.send_message(cid,texts['goal_ask_remove'])
    bot.register_next_step_handler(message,goal_remove_1)
def goal_remove_1(message):
    cid = message.chat.id
    User_data[cid]['selected_goal'] = message.text
    goal_id = User_data[cid]['selected_goal']
    delete_from_Goal(goal_id)
    User_data.pop(cid)
    bot.send_message(cid,texts['goal_removed'])

@bot.message_handler(func= lambda msg : msg.text == texts['goal_edit'])
def goal_edit_handler(message):
    cid = message.chat.id
    User_data[cid] = {}
    show_goal(message)
    bot.send_message(cid,texts['your_goals'])
    bot.send_message(cid,texts['goal_ask_edit'])
    bot.register_next_step_handler(message,edit_goal)
def edit_goal(message):
    cid = message.chat.id
    User_data[cid]['id'] = int(message.text)
    bot.send_message(cid,texts['goal_ask_title'])
    bot.register_next_step_handler(message,edit_goal_title)
def edit_goal_title(message):
    cid = message.chat.id
    User_data[cid]['new_title'] = message.text
    bot.send_message(cid,texts['goal_ask_description'])
    bot.register_next_step_handler(message,edit_goal_desc)
def edit_goal_desc(message):
    cid = message.chat.id
    User_data[cid]['new_desc'] = message.text
    bot.send_message(cid,texts['goal_ask_deadline'])
    bot.register_next_step_handler(message,edit_goal_time)
def edit_goal_time(message):
        cid = message.chat.id
        deadline = message.text.strip()
        if '/' not in deadline or not valid_date(deadline):
            bot.send_message(cid, texts['goal_ask_deadline'])
            bot.register_next_step_handler(message, edit_goal_time)
            return

        User_data[cid]['time'] = deadline
        title = User_data[cid]['new_title']
        description = User_data[cid]['new_desc']
        time = User_data[cid]['time']
        text = f"{texts['unvan']} = {title}\n{texts['desc']} = {description}\n{texts['mohlat']} = {time}"
        id = User_data[cid]['id']
    
        update_data_Goal(id,title,description,aim_date=time)

        bot.send_message(cid, text)
        bot.send_message(cid, texts['goal_edited'])
        User_data.pop(cid, None)




@bot.message_handler(func= lambda msg : msg.text == texts['reminder_add'])
def reminder_add_handler(message):
    cid = message.chat.id
    User_data[cid] = {}
    bot.send_message(cid,texts['reminder_ask_title'])
    bot.register_next_step_handler(message,handler_reminder1)
def handler_reminder1(message):
    cid = message.chat.id
    User_data[cid]['title'] = message.text.strip()
    bot.send_message(cid,texts['reminder_ask_date'])
    bot.register_next_step_handler(message,reminder_date)
def reminder_date(message):
    cid = message.chat.id
    date = message.text.strip()
    if  not valid_date(date):
        bot.send_message(cid,texts['false'])
        bot.register_next_step_handler(message,reminder_date)
    User_data[cid]['date'] = date
    bot.send_message(cid,texts['reminder_ask_time'])
    bot.register_next_step_handler(message,reminder_time)
def reminder_time(message):
    cid = message.chat.id
    time = message.text.strip()
    if not valid_time(time):
        bot.send_message(cid, texts['false'])
        bot.register_next_step_handler(message, reminder_time)
        return

    User_data[cid]['time'] = time
    title = User_data[cid]['title']
    date = User_data[cid]['date']

    text = f"{texts['unvan']} = {title}\n{texts['zaman']} = {time}\n{texts['tarikh']} = {date}"


    remi_datetime = f"{date} {time}"

    
    reminder_id = insert_data_Reminder(cid, title, None, remi_datetime)

    bot.send_message(cid, text)
    bot.send_message(cid, f"{texts['reminder_saved']}\n{texts['your_reminder_id']} {reminder_id}")
    User_data.pop(cid, None)


@bot.message_handler(func=lambda msg: msg.text == texts['daily_add'])
def daily_step_handler(message):
    cid = message.chat.id
    User_data[cid] = {'daily_tasks': []}
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(texts['btn_stop'])
    bot.send_message(cid, texts['daily_ask_task'], reply_markup=keyboard)
    bot.send_message(cid,texts['stop'])
    bot.register_next_step_handler(message, save_daily)

def save_daily(message):
    cid = message.chat.id
    if message.text == texts['btn_stop']:
        tasks = User_data[cid].get('daily_tasks', [])
        if not tasks:
            bot.send_message(cid, texts['notask'])
        else:
            msg = ""
            for i, task in enumerate(tasks, 1):
                msg += f"{i}. {task['task']} ⏰ {task['time']}\n"
            bot.send_message(cid, msg)
            bot.send_message(cid,texts['daily_task_saved'])
        User_data.pop(cid, None)
        return

    User_data[cid]['current_task'] = message.text
    bot.send_message(cid, texts['daily_ask_time'])
    bot.register_next_step_handler(message, save_daily_time)

def save_daily_time(message):
    cid = message.chat.id
    time = message.text
    task_text = User_data[cid].pop('current_task')
    User_data[cid]['daily_tasks'].append({'task': task_text, 'time': time})
    bot.send_message(cid, texts['next_task'])
    bot.register_next_step_handler(message, save_daily)

@bot.message_handler(func= lambda msg : msg.text == texts['motive_activate'])
def motive_activate(message):
    cid = message.chat.id
    User_data[cid] = {}
    bot.send_message(cid,texts['motive_edit_time'])
    bot.register_next_step_handler(message,save_motive_time)
def save_motive_time(message):
    cid = message.chat.id
    User_data[cid]['time'] = message.text
    bot.send_message(cid,texts['motive_activate_msg'])
    User_data.pop(cid)

@bot.message_handler(func= lambda msg : msg.text == texts['motive_deactivate'] )
def motive_deactivate(message):
    cid = message.chat.id
    bot.send_message(cid,texts['motive_deactivate_msg'])


@bot.message_handler(func= lambda msg : msg.text == texts['motive_edit'])
def edit_motive_time(message):
    cid = message.chat.id
    User_data[cid] = {}
    bot.send_message(cid,texts['motive_edit_time'])
    bot.register_next_step_handler(message,edit_motive)
def edit_motive(message):
    cid = message.chat.id
    User_data[cid]['time'] = message.text
    bot.send_message(cid,texts['motive_service_text'])
    User_data.pop(cid)


    
        
bot.set_update_listener(listener)
bot.infinity_polling()