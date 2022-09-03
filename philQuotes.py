import instabot  # for creating an agent to post images to instagram
from PIL import Image  # use pillows image library
from PIL import ImageFont  # create pillow compatible font
from PIL import ImageDraw  # overlay font onto image
from PIL import ImageFilter  # blur image
import os.path
from os import path
import urllib
import random
import codecs
import cv2
import numpy as np

"""
Philosophy Instagram Account:
username: Daily_Philosophy_Trend
password: ^***********************S

random 1:1 high-quality photos: https://source.unsplash.com/random/1080x1080/?nature
"""

image_fetch_url = "https://source.unsplash.com/random/1080x1080/?nature"


class Agent:
    def __init__(self, _username="", _password=""):
        self._username = "Daily_Philosophy_Trend"
        self._password = "^***********************S"
        # self.acting = instabot.Bot()

    def __repr__(self) -> str:
        return "{username}, {actingAgent}".format(
            username=self._username, actingAgent=self.acting
        )

    def verifyAgentCred(self) -> bool:
        # try:
        #     self.acting.login(username=self._username, password=self._password)
        # except:
        #     return False  # something went wrong logging in
        return True

    def post(self, some_image_path):
        # logged_in = self.verifyAgentCred()
        # if logged_in == False:
        #     print("***Log-in to {agent_repr} failed...".format(agent_repr=self))
        #     return
        if path.exists(some_image_path) == False:
            print(
                "***Image path @ ({img_path})does not exist...".format(
                    img_path=some_image_path
                )
            )
            return
        # self.acting.upload_photo(
        #     some_image_path, caption="--Your Daily Philosophy -- made with love--"
        # )


class Creator:
    def __init__(self):
        self.post_path = "images/post.jpg"
        self.count = 0

    def fetchImage(self):
        # remove old image
        rem_path = self.post_path + ".REMOVE_ME"
        if os.path.exists(rem_path):
            os.remove(rem_path)
        img_path = self.post_path
        try:
            urllib.request.urlretrieve(image_fetch_url, img_path)
        except:
            print(
                "***no image retrieved from {fetch_url}... defaulting to default.jpg".format(
                    fetch_url=image_fetch_url
                )
            )
            img_path = "images/default.jpg"  # fallback if no image is fetched
        return img_path

    def formatText(self, text):
        # add a line break
        cc = 0
        for x in range(len(text)):
            cc += 1
            if cc >= 26 and text[x - 1] == " ":
                text = text[:x] + "\n " + text[x:]
                cc = 0
        return "“" + text[:-1] + "”"

    def applyVignette(self, some_image_path):
        img = cv2.imread(some_image_path)
        rows, cols = img.shape[:2]
        # generating vignette mask using Gaussian kernels
        kernel_x = cv2.getGaussianKernel(cols, 255)
        kernel_y = cv2.getGaussianKernel(rows, 255)
        kernel = kernel_y * kernel_x.T
        mask = 400 * kernel / np.linalg.norm(kernel)
        output = np.copy(img)
        # applying the mask to each channel in the input image
        for i in range(3):
            output[:, :, i] = output[:, :, i] * mask
        cv2.imwrite(some_image_path, output)
        ret_img = Image.open(some_image_path)
        return ret_img

    def modifyImage(self, some_PIL_image, text="Lorem ipsum"):
        to_post = some_PIL_image.filter(ImageFilter.GaussianBlur(3))
        to_post = some_PIL_image.filter(ImageFilter.SMOOTH_MORE())
        to_post = some_PIL_image.filter(ImageFilter.EDGE_ENHANCE())
        to_post = self.applyVignette(self.post_path)
        draw = ImageDraw.Draw(to_post)
        border_thickness = 4  # offset
        random_range = []
        font_size = 65
        if len(text) < 64:
            random_range = [(75, 220), (95, 875)]
        else:
            random_range = [(50, 220), (65, 475)]
        randx = random.randint(random_range[0][0], random_range[0][1])
        randy = random.randint(random_range[1][0], random_range[1][1])
        draw_pos = [randx, randy]

        reduce = 65 // 7
        font_size -= reduce
        _font = ImageFont.truetype("DejaVuSans.ttf", font_size)
        # _font = ImageFont.load_default()
        text = self.formatText(text)
        draw.text(
            (draw_pos[0] + border_thickness, draw_pos[1] + border_thickness),
            text,
            (0, 0, 0),
            font=_font,
        )  # drop shadow
        draw.text(draw_pos, text, (255, 255, 255), font=_font)  # white text
        # _watermark_font = ImageFont.truetype("C:/Windows/fonts/Arial.ttf", 18)
        # watermark = "@Daily_Philosophy_Trend"
        # draw.text((850, 1050), watermark, (247, 245, 251), font=_watermark_font)

        to_post.save(self.post_path)

        return self.post_path

    def fetchSentence(self) -> str:
        input = codecs.open("database/markov_quotes.txt", "r", "utf-16")
        quotes = []
        for line in input.readlines():
            quotes.append(line)
        rand_index = 0
        sentence = "0" * 128
        while len(sentence) > 127:
            rand_index = random.randint(0, len(quotes))
            sentence = quotes[rand_index]

        return sentence

    def generateContent(self):
        # 1) fetch some random sentence from markov chain
        text = self.fetchSentence()
        # 2) fetch some random image from url
        img_path = self.fetchImage()
        img = Image.open(img_path)
        # 3) now combine the image with text and add slight gaussian blur
        return self.modifyImage(img, text=text)


def main():
    philAgent = Agent()
    creator = Creator()
    content = creator.generateContent()  # returns a path to the content to be posted
    # print(f"Posting: {content}")
    # philAgent.post(content)


if __name__ == "__main__":
    main()
