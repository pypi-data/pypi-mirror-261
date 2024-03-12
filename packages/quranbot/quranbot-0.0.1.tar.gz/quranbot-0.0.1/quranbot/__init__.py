from PIL import Image, UnidentifiedImageError
from io import BytesIO
from datetime import time as T
import pytz
import requests

class Pages:
    def __init__(self):
        self.style = 1
        self.pagesList = 0
        self.time = 0
        self.current_day = 0
        self.khatmaNum = 0
    
    ######################################################################################################

    def __getImage(self, style, pageNum):
        try:
            url = f"http://www.islamicbook.ws/{style}/{pageNum}.jpg"
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
        except UnidentifiedImageError:
            url = f"http://www.islamicbook.ws/{style}/{pageNum}.png"
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
        
        return img

    ######################################################################################################

    def sample(self, style):
        if type(style) != type(1):
            raise ValueError("style numbers can only be integers")
        if style < 1 or style > 4:
            raise ValueError("only choose styles between 1 and 4")
        
        if style >= 3:
            style += 3

        img1 = self.__getImage(style, pageNum=2)
        img2 = self.__getImage(style, pageNum=3)
        
        img1.show()
        img2.show()

    ######################################################################################################

    def khatma(self, khatma: int, time, style=1, startingDay=1):

        error = ValueError("Time format is invalid. Format should be XX:XX (e.g. 8:00 or 15:00)")

        if ":" not in time or time.count(":") != 1:
            raise error
        hour, minute = time.split(":")
        if len(hour) not in [1, 2] or len(minute) != 2 or not (hour.isdigit() and minute.isdigit()):
            raise error
        hour, minute = int(hour), int(minute)
        if not (0 <= hour <= 23) or not (0 <= minute <= 59):
            raise error
        
        if type(style) != type(1):
            raise ValueError("style numbers can only be integers")
        if style < 1 or style > 4:
            raise ValueError("only choose styles between 1 and 4")
        
        if style >= 3:
            style += 3
        

        quranPages = 604
        totalPages = quranPages*khatma
        
        oneDayPages = totalPages//29
        remainingPages = totalPages%29

        currentPage = 1

        dailyPageCounts = [oneDayPages] * 29

        for day in range(remainingPages):
            dailyPageCounts[day] += 1

        pagesList = []

        for dayNum, numOfPages in enumerate(dailyPageCounts):
            pagesList.append([])
            for _ in range(numOfPages):
                pagesList[dayNum].append(currentPage)
                currentPage = 1 if currentPage == 604 else currentPage + 1

        self.pagesList = pagesList
        self.time = T(hour=hour, minute=minute, tzinfo=pytz.timezone('Asia/Riyadh'))
        self.style = style
        self.khatmaNum = khatma
        self.current_day = startingDay-1

    ######################################################################################################

    def send_daily_images(self, bot, chat_id, endMessage):
        """Sends the images for the current day to the specified chat."""
        if self.current_day >= len(self.pagesList):
            bot.send_message(chat_id=chat_id, text=endMessage)
            self.current_day = 0  # Reset or handle completion as needed
            return

        # Retrieve the pages for the current day
        day_pages = self.pagesList[self.current_day]

        # Send each page as an image
        for page_num in day_pages:
            try:
                url = f"http://www.islamicbook.ws/{self.style}/{page_num}.jpg"
                bot.send_photo(chat_id=chat_id, photo=url)
                print(url)
            except Exception:
                url = f"http://www.islamicbook.ws/{self.style}/{page_num}.png"
                bot.send_photo(chat_id=chat_id, photo=url)
                print(url)

        # Move to the next day
        self.current_day += 1
        bot.send_message(chat_id=chat_id, text=f"تم ارسال صفحات اليوم {self.current_day} في خطة انهاء {self.khatmaNum} ختمة خلال شهر رمضان المبارك\nسيتم ارسال بقية الصفحات غدا الساعة {self.time} بأذن الله\n\n تقبل الله منا ومنكم صالح الاعمال 🌙🤍")