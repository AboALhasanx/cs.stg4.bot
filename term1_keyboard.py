from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from global_vars import (back_term1,term1_Table_of_lectures, algo_lab_title, algo_theo_title, computer_security_lab_title, 
                        computer_security_theo_title, operation_systems_lab_title, operation_systems_theo_title, image_process_lab_title, 
                        image_process_theo_title, dis_systems_lab_title, dis_systems_theo_title, web_prog_title )

def main_term1_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    button0 = KeyboardButton(term1_Table_of_lectures)
    button1 = KeyboardButton(algo_lab_title)
    button2 = KeyboardButton(algo_theo_title)
    button3 = KeyboardButton(computer_security_lab_title)
    button4 = KeyboardButton(computer_security_theo_title)
    button5 = KeyboardButton(operation_systems_lab_title)
    button6 = KeyboardButton(operation_systems_theo_title)
    button7 = KeyboardButton(image_process_lab_title)
    button8 = KeyboardButton(image_process_theo_title)
    button9 = KeyboardButton(dis_systems_lab_title)
    button10 = KeyboardButton(dis_systems_theo_title)
    button11 = KeyboardButton(web_prog_title)
    button12 = KeyboardButton("الكورس الثاني")
    button13 = KeyboardButton("تقييم البوت")
    button14 = KeyboardButton("🪧 عن البوت 🪧")
    markup.add(button0)  
    markup.add(button1, button2)
    markup.add(button3, button4)
    markup.add(button5, button6)
    markup.add(button7, button8)
    markup.add(button9, button10)
    markup.add(button11)
    markup.add(button13, button14, button12)
    return markup


def web_prog_buttons():
    button_texts = [
        "🌐 المادة في ملف واحد كاملة 📁",
        "🌐 كل جابتر في ملف 🗂",
        "🌐 ملخصات وتوضيحات 📝",
        "🌐 اسئلة وحلول 📝",
        "🌐 البرنامج الي نطبق عليه {ما ادري} 💻"
    , back_term1]
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for text in button_texts:
        button =KeyboardButton(text)
        markup.add(button)
    return markup


def algo_lab_buttons():
    button_text = [
        "📈 المادة في ملف واحد كاملة 📁",
        "📈 كل جابتر  بملف 🗂",
        "📈 مادة السنة السابقة 🕐",
        "📈 البرنامج الي نطبق عليه {ما ادري} 💻"
        , back_term1]
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for text in button_text:
        button =KeyboardButton(text)
        markup.add(button)
    return markup

def algo_theo_buttons():
    button_text = [
        "📈 المحاضرات في ملف واحد كاملة 📁",
        "📈 كل جابتر في ملف 🗂",
        "📈 المحاضرات + الترجمة في ملف واحد كاملة 🇮🇶",
        "📈 كل جابتر مترجم في ملف 🇮🇶",
        "📈 ملخصات وتوضيحات 📝",
        "📈 اسئلة وحلول 📝",
        "📈 محاضرات السنة السابقة 🕐",
        "📈 ملحقات عشوائية من السنة السابقة 🕐"
        , back_term1]
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for text in button_text:
        button =KeyboardButton(text)
        markup.add(button)
    return markup


def computer_security_lab_buttons():
    button_text = [
        "🛡️ المادة في ملف واحد كاملة 📁",
        "🛡️ كل جابتر  بملف 🗂",
        "🛡️ مادة السنة السابقة 🕐",
        "🛡️ البرنامج الي نطبق عليه {ما ادري} 💻"
    , back_term1]
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for text in button_text:
        button =KeyboardButton(text)
        markup.add(button)
    return markup

def computer_security_theo_buttons():
    button_text = [
        "🛡️ المحاضرات في ملف واحد كاملة 📁",
        "🛡️ كل جابتر في ملف 🗂",
        "🛡️ المحاضرات + الترجمة في ملف واحد كاملة 🇮🇶",
        "🛡️ ملخصات وتوضيحات 📝",
        "🛡️ اسئلة وحلول 📝",
        "🛡️ محاضرات السنة السابقة 🕐",
        "🛡️ ملحقات عشوائية من السنة السابقة 🕐"
    , back_term1]
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for text in button_text:
        button =KeyboardButton(text)
        markup.add(button)
    return markup


def operation_systems_lab_buttons():
    button_text = [
        "🐧 المادة في ملف واحد كاملة 📁",
        "🐧 كل جابتر بملف 🗂",
        "🐧 مادة السنة السابقة 🕐",
        "🐧 البرامج الي نطبق عليها {ما ادري} 💻",
        "🐧 ملحقـات عشوائية من السنة السابقة 🕐"
    , back_term1]
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for text in button_text:
        button =KeyboardButton(text)
        markup.add(button)
    return markup

def operation_systems_theo_buttons():
    button_text = [
        "🐧 المحاضرات في ملف واحد كاملة 📁",
        "🐧 كل جابتر في ملف 🗂",
        "🐧 المحاضرات + الترجمة في ملف واحد كاملة 🇮🇶",
        "🐧 كل جابتر مترجم في ملف 🇮🇶",
        "🐧 ملخصات وتوضيحات 📝",
        "🐧 اسئلة وحلول 📝",
        "🐧 محاضرات السنة السابقة 🕐",
        "🐧 ملحقات عشوائية من السنة السابقة 🕐"
    , back_term1]
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for text in button_text:
        button =KeyboardButton(text)
        markup.add(button)
    return markup


def image_process_lab_buttons():
    button_text = [
        "🖼️ المادة في ملف واحد كاملة 📁",
        "🖼️ كل جابتر  بملف 🗂",
        "🖼️ مادة السنة السابقة 🕐",
        "🖼️ البرنامج الي نطبق عليه {ما ادري} 💻",
        "🖼️ ملحقـات عشوائية من السنة السابقة 🕐"
        , back_term1]
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for text in button_text:
        button =KeyboardButton(text)
        markup.add(button)
    return markup

def image_process_theo_buttons():
    button_text = [
        "🖼️ المحاضرات في ملف واحد كاملة 📁",
        "🖼️ كل جابتر في ملف 🗂",
        "🖼️ المحاضرات + الترجمة في ملف واحد كاملة 🇮🇶",
        "🖼️ كل جابتر مترجم في ملف 🇮🇶",
        "🖼️ ملخصات وتوضيحات 📝",
        "🖼️ اسئلة وحلول 📝",
        "🖼️ محاضرات السنة السابقة 🕐",
        "🖼️ ملحقات عشوائية من السنة السابقة 🕐"
    , back_term1]
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for text in button_text:
        button =KeyboardButton(text)
        markup.add(button)
    return markup


def dis_systems_lab_buttons():
    button_text = [
        "🕸 المادة في ملف واحد كاملة 📁",
        "🕸 كل جابتر  بملف 🗂",
        "🕸 مادة السنة السابقة 🕐",
        "🕸 البرنامج الي نطبق عليه {ما ادري} 💻"
        , back_term1]
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for text in button_text:
        button =KeyboardButton(text)
        markup.add(button)
    return markup

def dis_systems_theo_buttons():
    button_text = [
        "🕸 المحاضرات في ملف واحد كاملة 📁",
        "🕸 كل جابتر في ملف 🗂",
        "🕸 المحاضرات + الترجمة في ملف واحد كاملة 🇮🇶",
        "🕸 كل جابتر مترجم في ملف 🇮🇶",
        "🕸 ملخصات وتوضيحات 📝",
        "🕸 اسئلة وحلول 📝",
        "🕸 محاضرات السنة السابقة 🕐",
        "🕸 ملحقات عشوائية من السنة السابقة 🕐"
        , back_term1]
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for text in button_text:
        button =KeyboardButton(text)
        markup.add(button)
    return markup
