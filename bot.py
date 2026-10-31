import os
import telebot
# لو بتستخدم قاعدة بيانات SQL Server لبرنامج المنارة، هتحتاج تنزل مكتبة pyodbc
# وتفك التفعيل عن السطور دي وقت ربط السيرفر عندك
# import pyodbc

# توكن البوت اللي بتاخده من BotFather على تليجرام
TOKEN = "حط_التوكن_هنا"
bot = telebot.TeleBot(TOKEN)

# دالة الترحيب
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك يا ابويوسف! بوت متابعة مستودع الأبراج جاهز لخدمتك. اكتب /report لاستخراج تقرير الحركة والنواقص.")

# دالة جلب التقارير (تقدر تربطها بقاعدة بيانات المنارة لاحقاً)
@bot.message_handler(commands=['report'])
def get_inventory_report(message):
    # هنا بيتم الاتصال بقاعدة بيانات المنارة وسحب البيانات
    # مثال توضيحي لتقرير سريّع:
    report_text = (
        "📊 **تقرير حركة المستودع اليومي**\n\n"
        "🔹 إجمالي الحركات اليوم: 0\n"
        "🔹 الأصناف التي وصلت للحد الأدنى: 0\n"
        "✅ الحالة العامة للمستودع: مستقرة.\n\n"
        "تم استخراج التقرير تلقائياً."
    )
    bot.reply_to(message, report_text, parse_mode="Markdown")

# تشغيل البوت
if __name__ == '__main__':
    print("Bot is running...")
    bot.infinity_polling()
