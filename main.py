import telebot
import random
import json
from config import (ADMIN_ID, BOT_TOKEN, cs_stg4, cs_stg4_onefile, cs_stg4_deleted, cs_apps)
from global_vars import (done_forward, not_post_yet, about_bot_msg)
#---------------------
#استدعائات الكورس الاول
from global_vars import  (back_term1,term1_Table_of_lectures,chose_from, algo_lab_title, algo_theo_title, 
                        computer_security_lab_title, computer_security_theo_title,image_process_lab_title, 
                        image_process_theo_title, operation_systems_lab_title, operation_systems_theo_title, 
                        dis_systems_lab_title, dis_systems_theo_title, web_prog_title )

from term1_keyboard import ( main_term1_keyboard, computer_security_lab_buttons, computer_security_theo_buttons, 
                            image_process_lab_buttons, image_process_theo_buttons, operation_systems_lab_buttons, 
                            operation_systems_theo_buttons, algo_lab_buttons, algo_theo_buttons, dis_systems_lab_buttons, 
                            dis_systems_theo_buttons, web_prog_buttons)
#---------------------
#---------------------
#استدعائات الكورس الثاني
from global_vars import (back_term2,term2_Table_of_lectures, cloud_computing_lab_title, cloud_computing_theo_title,
                        iot_lab_title,iot_theo_title,design_and_analyze_systems_lab_title,design_and_analyze_systems_theo_title,
                        mobile_applications_lab_title,mobile_applications_theo_title, english_title)

from term2_keyboard import (give_rating, main_term2_keyboard, cloud_computing_lab_buttons, cloud_computing_theo_buttons, 
                            design_and_analyze_systems_lab_buttons, design_and_analyze_systems_theo_buttons, mobile_applications_lab_buttons, 
                            mobile_applications_theo_buttons, iot_lab_buttons, iot_theo_buttons, english_buttons)

#------------------------------------------------------
#---------- initialize bot and files process ----------
#------------------------------------------------------
bot = telebot.TeleBot(BOT_TOKEN, parse_mode=None)

file_path = 'terms_cmd2values.json'
commands_file_path = 'terms_btn2cmd.json'

def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def load_commands():
    with open(commands_file_path, 'r') as file:
        return json.load(file)

#----------------------------------------
#---------- check join process ----------
#----------------------------------------
def is_user_member(user_id, chat_id):
    try:
        chat_member = bot.get_chat_member(chat_id, user_id)
        return chat_member.status in ['member', 'administrator', 'creator']
    except Exception as e:
        print(f"Error checking membership: {e}")
        return False

def check_and_respond(message, response_function, *args):
    user = message.from_user
    first_name = user.first_name
    user_id = message.from_user.id
    required_channels = ["@cs_stg4", "@cs_stg4_onefile", "@cs_stg4_deleted", "@cs_apps"]
    
    all_membership_valid = all(is_user_member(user_id, chat_id) for chat_id in required_channels)
    
    if all_membership_valid:
        response_function(message, *args)
    else:
        bot.send_message(message.chat.id,f"⤦ اوكف {first_name} شو ما مشترك بالقنوات ⁉️🫣\nاشترك وارجع اضغط على /start\n• قناة الملازم: @cs_stg4\n• قناة الملخصات: @cs_stg4_onefile\n• قناة المهملات: @cs_stg4_deleted\n• قناة البرامج: @cs_apps")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    def respond(message):
        welcome_text = ("<b>• هلا بالخريج مالتنا 😌🎓✨\n\n• اختار من القائمة 🎛⚡️\n\n<blockquote>👨🏻‍💻المطور : @ab0_alhasan</blockquote></b>"
        )
        bot.reply_to(message, welcome_text, parse_mode='HTML', reply_markup = main_term1_keyboard())
    check_and_respond(message, respond)

def chose_from_markup(message, reply_markup):
    bot.reply_to(message, chose_from, parse_mode='HTML', reply_markup = reply_markup)
@bot.message_handler(commands = ['about'])
@bot.message_handler(func=lambda message: message.text == "🪧 عن البوت 🪧")
def about_bot(message):
    bot.reply_to(message, about_bot_msg, parse_mode='HTML')
    
    
def respond_to_rating(message):
    bot.reply_to(message, "<b>شنو تقييمك للبوت 👀❔</b>", parse_mode='HTML', reply_markup = give_rating())
@bot.message_handler(func=lambda message: message.text == "تقييم البوت")
@bot.message_handler(commands=['rating'])
def replay(message):
    respond_to_rating(message)

import random

@bot.message_handler(func=lambda message: message.text in ["🎖🏆 واحد عراق 😶‍🌫✋🏻", "عاش يسطا 👀🔥", "الله على الروقان ✨😌", "جيد 👍🙂", "تحجي صدك 🦦؟"])
def handle_rating(message):
    rating = message.text
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    username = message.from_user.username or "غير معروف"
    
    good_response = ["حبيب اخوك 😇", "حبيبي نورتني 😌", "صدك جذب تدلل 😊"]
    veryGood_response = ["اخويا ياسطا 😎🤙🏻", "تسلم يالقالي 😴🫶", "نورك هذا لو الشمس؟ عمي منورنا 😔❤️‍🔥", "يا هلا وغلا بالعزيز 🫂❤️‍🔥", "شهادة اعتزُ بيها 😌🤝🏻", "هاي الوردة تستاهلك 🌹🫴"]
    ok_response = ["خوش 🤨", "تمام 🙄", "ماشي 🙃", "اوك 🌚", "شوكران يمحترم 😒", "مثل تقديرك 🫠"]

    if rating == "تحجي صدك 🦦؟":
        response_text = "هاي ليش 💔🗿؟ \n راسلني وكلي اذا اكو مشكلة بالبوت @ab0_alhasan"
    elif rating == "الله على الروقان ✨😌":
        response_text = random.choice(good_response)
    elif rating == "جيد 👍🙂":
        response_text = random.choice(ok_response)
    else:
        response_text = random.choice(veryGood_response)
    bot.send_message(
        ADMIN_ID,
        f"اكلك هذا {user_name} الي معرفه (@{username}) يكول \n\"{rating}\" على البوت 🫣"
    )

    bot.send_message(
        message.chat.id, response_text, reply_markup= main_term1_keyboard()
    )


@bot.message_handler(commands=['term1'])
@bot.message_handler(func=lambda message: message.text in ["الرجوع الى الكورس الأول ⬅", back_term1])
def to_term1_menu(message):
    def respond(message):
        chose_from_markup(message, main_term1_keyboard())
    check_and_respond(message, respond)


@bot.message_handler(func=lambda message: message.text == computer_security_lab_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, computer_security_lab_buttons())    
    check_and_respond(message, respond)
    
@bot.message_handler(func=lambda message: message.text == computer_security_theo_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, computer_security_theo_buttons())    
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == image_process_lab_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, image_process_lab_buttons())    
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == image_process_theo_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, image_process_theo_buttons())    
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == operation_systems_lab_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, operation_systems_lab_buttons())    
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == operation_systems_theo_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, operation_systems_theo_buttons())    
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == algo_lab_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, algo_lab_buttons())    
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == algo_theo_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, algo_theo_buttons())    
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == dis_systems_lab_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, dis_systems_lab_buttons())    
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == dis_systems_theo_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, dis_systems_theo_buttons())    
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == web_prog_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, web_prog_buttons())    
    check_and_respond(message, respond)



@bot.message_handler(func=lambda message: message.text == term1_Table_of_lectures) 
def redirect(message):
    def respond(message):
        bot.forward_message(message.chat.id, cs_stg4, 39)    
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == back_term2)
def return_to_term2_menu(message):
    def respond(message):
            bot.reply_to(message, chose_from, parse_mode='HTML', reply_markup=main_term2_keyboard())
    check_and_respond(message, respond)

@bot.message_handler(commands=['term2']) 
@bot.message_handler(func=lambda message: message.text == "الكورس الثاني") 
def to_term2_menu(message):
    def respond(message):
        chose_from_markup(message, main_term2_keyboard())
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == english_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, english_buttons())    
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == cloud_computing_lab_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, cloud_computing_lab_buttons())    
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == cloud_computing_theo_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, cloud_computing_theo_buttons())    
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == mobile_applications_lab_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, mobile_applications_lab_buttons())    
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == mobile_applications_theo_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, mobile_applications_theo_buttons())    
    check_and_respond(message, respond)
    
@bot.message_handler(func=lambda message: message.text == iot_lab_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, iot_lab_buttons())    
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == iot_theo_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, iot_theo_buttons())    
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == design_and_analyze_systems_lab_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, design_and_analyze_systems_lab_buttons())    
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == design_and_analyze_systems_theo_title)
def redirect(message):
    def respond(message):
        chose_from_markup(message, design_and_analyze_systems_theo_buttons())    
    check_and_respond(message, respond)

@bot.message_handler(func=lambda message: message.text == term2_Table_of_lectures ) 
def redirect(message):
    def respond(message):
        bot.forward_message(message.chat.id, cs_stg4, 40)    
    check_and_respond(message, respond)
    
#--------------------------------------------------------


@bot.message_handler(func=lambda message: message.text in ["القائمة الرئيسية","خروج من التقييم"])
def return_to_main_menu(message):
    def respond(message):
        bot.reply_to(message, "<b>القائمة الرئيسية</b>", parse_mode='HTML', reply_markup=main_term1_keyboard())
    check_and_respond(message, respond)

#--------------------------------------
#---------- Get file process ----------
#--------------------------------------
# Load the command mappings
button_to_command = load_commands()

@bot.message_handler(func=lambda message: message.text in button_to_command.keys())
def handle_button(message):
    command = button_to_command.get(message.text)
    get_file_command(message, command)

def get_file_command(message, command):
    data = load_data(file_path)
    post_id_or_list = data['commands'].get(command)
    
    if '_full' in command:
        CHANNEL_ID = cs_stg4
    elif '_lectures' in command:
        CHANNEL_ID = cs_stg4_onefile
    elif '_old' in command:
        CHANNEL_ID = cs_stg4_deleted
    elif '_app' in command:
        CHANNEL_ID = cs_apps
    else:
        bot.reply_to(message, not_post_yet)
        return

    if post_id_or_list:
        try:
            if isinstance(post_id_or_list, list):
                for post_id in post_id_or_list:
                    bot.forward_message(message.chat.id, CHANNEL_ID, post_id)
                bot.reply_to(message, done_forward)
            else:
                bot.forward_message(message.chat.id, CHANNEL_ID, post_id_or_list)
                bot.reply_to(message, done_forward)
                
        except Exception as e:
            bot.reply_to(message, "اما تكون الرسالة ممسوحة من القنوات او غير موجودة🚫")
    else:
        bot.reply_to(message, not_post_yet)

bot.polling()