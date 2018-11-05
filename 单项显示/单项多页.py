from urllib import parse,request
import requests
import json
import os,re
from tkinter import messagebox,Canvas,PanedWindow,Label,Button,Frame,PhotoImage
import tkinter
from PIL import Image,ImageTk

class First(object):
    def __init__(self, master=None):
        self.root=master
        self.root.geometry("500x600")
        self.createpage()

    def get_memory(self):
        url = 'https://gzgd.ams.ott.chinanetcenter.com:9912/ams/is/externalRank/queryRank?clientInfo= { "deviceCode":"BOX", "rankConditions":[ {"code":"new_list", "topN":5} ] }'
        res = requests.get(url)
        inp_str = res.json()
        result_bangming = []
        result_yingyongming = []
        result_yingyongtupian = []
        result_xiazaidizhi = []
        print(inp_str.items())
        for i, j in inp_str.items():
            if (i == 'content'):
                patten = re.compile(r'{"name":"(.*?)","code"')
                result_bangming = re.findall(patten, j)
                #print(result_bangming)

                patten = re.compile(r'{"name":"([\u4e00-\u9fa5_a-zA-Z0-9_]{1,10})","packageName"')
                result_yingyongming = re.findall(patten, j)
                print(result_yingyongming)

                patten = re.compile(r'"downloadUrl":"(http:.*?.apk)"')
                result_xiazaidizhi = re.findall(patten, j)
                #print(result_xiazaidizhi)

                patten = re.compile(r'"icon":"(.*?)"')
                result_yingyongtupian = re.findall(patten, j)
                print(result_yingyongtupian)
        return result_yingyongtupian,result_bangming,result_yingyongming,result_xiazaidizhi

    def createpage(self):
        result_bangming = []
        result_yingyongming = []
        result_yingyongtupian = []
        result_xiazaidizhi = []
        result_yingyongtupian,result_bangming,result_yingyongming,result_xiazaidizhi=self.get_memory()

        print(result_xiazaidizhi,result_yingyongtupian,result_yingyongming,result_bangming)

        # 主界面
        top_1 = PanedWindow(orient="vertical")
        top_1.pack(fill='both', expand=1)
        ttle=Label(top_1,text=result_bangming[0])
        top_1.add(ttle)


        # 右边界面
        top_2 = PanedWindow(top_1)
        top_1.add(top_2)

        # 左边5项
        top_3 = PanedWindow(top_2, orient="vertical")
        top_2.add(top_3)

        # 右边图片
        top_4 = PanedWindow(top_2, orient="vertical")
        top_2.add(top_4)

        # 右边文字
        top_5 = PanedWindow(top_2, orient="vertical")
        top_2.add(top_5)

        # 下方两个按钮
        top_6 = PanedWindow(top_1, orient="horizontal")
        top_1.add(top_6)

        # 左边5标签
        left1 = Label(top_1, text="1", height=5, width=15)
        top_3.add(left1)
        left2 = Label(top_1, text="2", height=5, width=15)
        top_3.add(left2)
        left3 = Label(top_1, text="3", height=5, width=15)
        top_3.add(left3)
        left4 = Label(top_1, text="4", height=5, width=15)
        top_3.add(left4)
        left5 = Label(top_1, text="5", height=5, width=15)
        top_3.add(left5)

        pic_size = 93
        w_box = pic_size
        h_box = pic_size
        LP = [0, 0, 0, 0, 0]
        pil_image = [0, 0, 0, 0, 0]
        tk_image = [0, 0, 0, 0, 0]
        pil_image_resized = [0, 0, 0, 0, 0]
        k = 0
        for i in result_yingyongtupian:
            response = request.urlopen(i)
            cat_img = response.read()
            with open('C:\\Users\\jaska\\Desktop\\cat_500_600' + str(k) + '.jpg', 'wb') as f:
                f.write(cat_img)
                f.close()
            pil_image[k] = Image.open(r'C:\Users\jaska\Desktop\cat_500_600' + str(k) + '.jpg')
            w, h = pil_image[k].size
            pil_image_resized[k] = self.resize(w, h, w_box, h_box, pil_image[k])
            tk_image[k] = ImageTk.PhotoImage(pil_image_resized[k])
            print(tk_image)
            LP[k] = Label(top_4, image=tk_image[k], height=w_box, width=h_box)
            top_4.add(LP[k])
            k += 1

        def button_1():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[0])

        def button_2():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[1])

        def button_3():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[2])

        def button_4():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[3])

        def button_5():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[4])

        def button_6():
            messagebox.showinfo(title="往前", message="但是很可惜的是这是第一页")

        def button_7():
            top_1.destroy()
            Second(self.root)

        # 右边按钮
        button1_1 = Button(top_2, text=result_yingyongming[0], height=5, width=30, command=button_1, highlightcolor="blue",
                           activebackground="blue", justify="right", compound="right")
        top_5.add(button1_1)
        button1_2 = Button(top_2, text=result_yingyongming[1], height=5, width=30, command=button_2, highlightcolor="blue",
                           activebackground="blue", justify="right", compound="right")
        top_5.add(button1_2)
        button1_3 = Button(top_2, text=result_yingyongming[2], height=5, width=30, command=button_3, highlightcolor="blue",
                           activebackground="blue", justify="right", compound="right")
        top_5.add(button1_3)
        button1_4 = Button(top_2, text=result_yingyongming[3], height=5, width=30, command=button_4, highlightcolor="blue",
                           activebackground="blue", justify="right", compound="right")
        top_5.add(button1_4)
        button1_5 = Button(top_2, text=result_yingyongming[4], height=5, width=30, command=button_5, highlightcolor="blue",
                           activebackground="blue", justify="right", compound="right")
        top_5.add(button1_5)

        # 下方左右换页按钮
        button1_6 = Button(top_6, text="←", height=2, width=30, command=button_6, highlightcolor="blue",
                           activebackground="blue", justify="right", compound="right")
        top_6.add(button1_6)
        button1_7 = Button(top_6, text="→", height=2, width=30, command=button_7, highlightcolor="blue",
                           activebackground="blue", justify="right", compound="right")
        top_6.add(button1_7)
        root.mainloop()


    def resize(self,w,h,w_box,h_box,pil_image):
        f1 = 1.0 * w_box / w  # 1.0 forces float division in Python2
        f2 = 1.0 * h_box / h
        factor = min([f1, f2])
        # print(f1, f2, factor) # test
        # use best down-sizing filter
        width = int(w * factor)
        height = int(h * factor)
        return pil_image.resize((width, height), Image.ANTIALIAS)

class Second(object):

    def __init__(self, master=None):
        self.root=master
        self.root.geometry("500x600")
        self.createpage()

    def get_memory(self):
        url = 'https://gzgd.ams.ott.chinanetcenter.com:9912/ams/is/externalRank/queryRank?clientInfo= { "deviceCode":"BOX", "rankConditions":[ {"code":"game_list", "topN":5} ] }'
        res = requests.get(url)
        inp_str = res.json()
        result_bangming = []
        result_yingyongming = []
        result_yingyongtupian = []
        result_xiazaidizhi = []
        print(inp_str.items())
        for i, j in inp_str.items():
            if (i == 'content'):
                patten = re.compile(r'{"name":"(.*?)","code"')
                result_bangming = re.findall(patten, j)
                #print(result_bangming)

                patten = re.compile(r'{"name":"([\u4e00-\u9fa5_a-zA-Z0-9_]{1,10})","packageName"')
                result_yingyongming = re.findall(patten, j)
                print(result_yingyongming)

                patten = re.compile(r'"downloadUrl":"(http:.*?.apk)"')
                result_xiazaidizhi = re.findall(patten, j)
                #print(result_xiazaidizhi)

                patten = re.compile(r'"icon":"(.*?)"')
                result_yingyongtupian = re.findall(patten, j)
                print(result_yingyongtupian)
        return result_yingyongtupian,result_bangming,result_yingyongming,result_xiazaidizhi

    def createpage(self):
        result_bangming = []
        result_yingyongming = []
        result_yingyongtupian = []
        result_xiazaidizhi = []
        result_yingyongtupian,result_bangming,result_yingyongming,result_xiazaidizhi=self.get_memory()

        print(result_xiazaidizhi,result_yingyongtupian,result_yingyongming,result_bangming)

        # 主界面
        top_1 = PanedWindow(orient="vertical")
        top_1.pack(fill='both', expand=1)
        ttle = Label(top_1, text=result_bangming[0])
        top_1.add(ttle)
        # 右边界面
        top_2 = PanedWindow(top_1)
        top_1.add(top_2)

        # 左边5项
        top_3 = PanedWindow(top_2, orient="vertical")
        top_2.add(top_3)

        # 右边图片
        top_4 = PanedWindow(top_2, orient="vertical")
        top_2.add(top_4)

        # 右边文字
        top_5 = PanedWindow(top_2, orient="vertical")
        top_2.add(top_5)

        # 下方两个按钮
        top_6 = PanedWindow(top_1, orient="horizontal")
        top_1.add(top_6)

        # 左边5标签
        left1 = Label(top_1, text="1", height=5, width=15)
        top_3.add(left1)
        left2 = Label(top_1, text="2", height=5, width=15)
        top_3.add(left2)
        left3 = Label(top_1, text="3", height=5, width=15)
        top_3.add(left3)
        left4 = Label(top_1, text="4", height=5, width=15)
        top_3.add(left4)
        left5 = Label(top_1, text="5", height=5, width=15)
        top_3.add(left5)

        pic_size = 93
        w_box = pic_size
        h_box = pic_size
        LP = [0, 0, 0, 0, 0]
        pil_image = [0, 0, 0, 0, 0]
        tk_image = [0, 0, 0, 0, 0]
        pil_image_resized = [0, 0, 0, 0, 0]
        k = 0
        for i in result_yingyongtupian:
            response = request.urlopen(i)
            cat_img = response.read()
            with open('C:\\Users\\jaska\\Desktop\\cat_500_600' + str(k) + '.jpg', 'wb') as f:
                f.write(cat_img)
                f.close()
            pil_image[k] = Image.open(r'C:\Users\jaska\Desktop\cat_500_600' + str(k) + '.jpg')
            w, h = pil_image[k].size
            pil_image_resized[k] = self.resize(w, h, w_box, h_box, pil_image[k])
            tk_image[k] = ImageTk.PhotoImage(pil_image_resized[k])
            print(tk_image)
            LP[k] = Label(top_4, image=tk_image[k], height=w_box, width=h_box)
            top_4.add(LP[k])
            k += 1

        def button_1():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[0])

        def button_2():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[1])

        def button_3():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[2])

        def button_4():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[3])

        def button_5():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[4])

        def button_6():
            top_1.destroy()
            First(self.root)

        def button_7():
            top_1.destroy()
            Third(self.root)

        # 右边按钮
        button1_1 = Button(top_2, text=result_yingyongming[0], height=5, width=30, command=button_1, highlightcolor="blue",
                           activebackground="blue", justify="right", compound="right")
        top_5.add(button1_1)
        button1_2 = Button(top_2, text=result_yingyongming[1], height=5, width=30, command=button_2, highlightcolor="blue",
                           activebackground="blue", justify="right", compound="right")
        top_5.add(button1_2)
        button1_3 = Button(top_2, text=result_yingyongming[2], height=5, width=30, command=button_3, highlightcolor="blue",
                           activebackground="blue", justify="right", compound="right")
        top_5.add(button1_3)
        button1_4 = Button(top_2, text=result_yingyongming[3], height=5, width=30, command=button_4, highlightcolor="blue",
                           activebackground="blue", justify="right", compound="right")
        top_5.add(button1_4)
        button1_5 = Button(top_2, text=result_yingyongming[4], height=5, width=30, command=button_5, highlightcolor="blue",
                           activebackground="blue", justify="right", compound="right")
        top_5.add(button1_5)

        # 下方左右换页按钮
        button1_6 = Button(top_6, text="←", height=2, width=30, command=button_6, highlightcolor="blue",
                           activebackground="blue", justify="right", compound="right")
        top_6.add(button1_6)
        button1_7 = Button(top_6, text="→", height=2, width=30, command=button_7, highlightcolor="blue",
                           activebackground="blue", justify="right", compound="right")
        top_6.add(button1_7)
        root.mainloop()

    def resize(self,w,h,w_box,h_box,pil_image):
        f1 = 1.0 * w_box / w  # 1.0 forces float division in Python2
        f2 = 1.0 * h_box / h
        factor = min([f1, f2])
        # print(f1, f2, factor) # test
        # use best down-sizing filter
        width = int(w * factor)
        height = int(h * factor)
        return pil_image.resize((width, height), Image.ANTIALIAS)
class Third(object):
    def __init__(self, master=None):
        self.root=master
        self.root.geometry("500x600")
        self.createpage()

    def get_memory(self):
        url = 'https://gzgd.ams.ott.chinanetcenter.com:9912/ams/is/externalRank/queryRank?clientInfo= { "deviceCode":"BOX", "rankConditions":[ {"code":"movie_list", "topN":5} ] }'
        res = requests.get(url)
        inp_str = res.json()
        result_bangming = []
        result_yingyongming = []
        result_yingyongtupian = []
        result_xiazaidizhi = []
        print(inp_str.items())
        for i, j in inp_str.items():
            if (i == 'content'):
                patten = re.compile(r'{"name":"(.*?)","code"')
                result_bangming = re.findall(patten, j)
                #print(result_bangming)

                patten = re.compile(r'{"name":"([\u4e00-\u9fa5_a-zA-Z0-9_]{1,10})","packageName"')
                result_yingyongming = re.findall(patten, j)
                print(result_yingyongming)

                patten = re.compile(r'"downloadUrl":"(http:.*?.apk)"')
                result_xiazaidizhi = re.findall(patten, j)
                #print(result_xiazaidizhi)

                patten = re.compile(r'"icon":"(.*?)"')
                result_yingyongtupian = re.findall(patten, j)
                print(result_yingyongtupian)
        return result_yingyongtupian,result_bangming,result_yingyongming,result_xiazaidizhi

    def createpage(self):
        result_bangming = []
        result_yingyongming = []
        result_yingyongtupian = []
        result_xiazaidizhi = []
        result_yingyongtupian,result_bangming,result_yingyongming,result_xiazaidizhi=self.get_memory()

        print(result_xiazaidizhi,result_yingyongtupian,result_yingyongming,result_bangming)

        # 主界面
        top_1 = PanedWindow(orient="vertical")
        top_1.pack(fill='both', expand=1)

        # 右边界面
        top_2 = PanedWindow(top_1)
        top_1.add(top_2)

        # 左边5项
        top_3 = PanedWindow(top_2, orient="vertical")
        top_2.add(top_3)

        # 右边图片
        top_4 = PanedWindow(top_2, orient="vertical")
        top_2.add(top_4)

        # 右边文字
        top_5 = PanedWindow(top_2, orient="vertical")
        top_2.add(top_5)

        # 下方两个按钮
        top_6 = PanedWindow(top_1, orient="horizontal")
        top_1.add(top_6)

        # 左边5标签
        left1 = Label(top_1, text="1", height=5, width=15)
        top_3.add(left1)
        left2 = Label(top_1, text="2", height=5, width=15)
        top_3.add(left2)
        left3 = Label(top_1, text="3", height=5, width=15)
        top_3.add(left3)
        left4 = Label(top_1, text="4", height=5, width=15)
        top_3.add(left4)
        left5 = Label(top_1, text="5", height=5, width=15)
        top_3.add(left5)

        pic_size = 93
        w_box = pic_size
        h_box = pic_size
        LP = [0, 0, 0, 0, 0]
        pil_image = [0, 0, 0, 0, 0]
        tk_image = [0, 0, 0, 0, 0]
        pil_image_resized = [0, 0, 0, 0, 0]
        k = 0
        for i in result_yingyongtupian:
            response = request.urlopen(i)
            cat_img = response.read()
            with open('C:\\Users\\jaska\\Desktop\\cat_500_600' + str(k) + '.jpg', 'wb') as f:
                f.write(cat_img)
                f.close()
            pil_image[k] = Image.open(r'C:\Users\jaska\Desktop\cat_500_600' + str(k) + '.jpg')
            w, h = pil_image[k].size
            pil_image_resized[k] = self.resize(w, h, w_box, h_box, pil_image[k])
            tk_image[k] = ImageTk.PhotoImage(pil_image_resized[k])
            print(tk_image)
            LP[k] = Label(top_4, image=tk_image[k], height=w_box, width=h_box)
            top_4.add(LP[k])
            k += 1

        def button_1():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[0])

        def button_2():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[1])

        def button_3():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[2])

        def button_4():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[3])

        def button_5():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[4])

        def button_6():
            top_1.destroy()
            Second(self.root)

        def button_7():
            top_1.destroy()
            Four(self.root)

        # 右边按钮
        button1_1 = Button(top_2, text=result_yingyongming[0], height=5, width=30, command=button_1, highlightcolor="blue",
                           activebackground="blue", justify="right", compound="right")
        top_5.add(button1_1)
        button1_2 = Button(top_2, text=result_yingyongming[1], height=5, width=30, command=button_2, highlightcolor="blue",
                           activebackground="blue", justify="right", compound="right")
        top_5.add(button1_2)
        button1_3 = Button(top_2, text=result_yingyongming[2], height=5, width=30, command=button_3, highlightcolor="blue",
                           activebackground="blue", justify="right", compound="right")
        top_5.add(button1_3)
        button1_4 = Button(top_2, text=result_yingyongming[3], height=5, width=30, command=button_4, highlightcolor="blue",
                           activebackground="blue", justify="right", compound="right")
        top_5.add(button1_4)
        button1_5 = Button(top_2, text=result_yingyongming[4], height=5, width=30, command=button_5, highlightcolor="blue",
                           activebackground="blue", justify="right", compound="right")
        top_5.add(button1_5)

        # 下方左右换页按钮
        button1_6 = Button(top_6, text="←", height=2, width=30, command=button_6, highlightcolor="blue",
                           activebackground="blue", justify="right", compound="right")
        top_6.add(button1_6)
        button1_7 = Button(top_6, text="→", height=2, width=30, command=button_7, highlightcolor="blue",
                           activebackground="blue", justify="right", compound="right")
        top_6.add(button1_7)
        root.mainloop()

    def resize(self,w,h,w_box,h_box,pil_image):
        f1 = 1.0 * w_box / w  # 1.0 forces float division in Python2
        f2 = 1.0 * h_box / h
        factor = min([f1, f2])
        # print(f1, f2, factor) # test
        # use best down-sizing filter
        width = int(w * factor)
        height = int(h * factor)
        return pil_image.resize((width, height), Image.ANTIALIAS)
class Four(object):
    def __init__(self, master=None):
        self.root=master
        self.root.geometry("500x600")
        self.createpage()

    def get_memory(self):
        url = 'https://gzgd.ams.ott.chinanetcenter.com:9912/ams/is/externalRank/queryRank?clientInfo= { "deviceCode":"BOX", "rankConditions":[ {"code":"education_list", "topN":5} ] }'
        res = requests.get(url)
        inp_str = res.json()
        result_bangming = []
        result_yingyongming = []
        result_yingyongtupian = []
        result_xiazaidizhi = []
        print(inp_str.items())
        for i, j in inp_str.items():
            if (i == 'content'):
                patten = re.compile(r'{"name":"(.*?)","code"')
                result_bangming = re.findall(patten, j)
                #print(result_bangming)

                patten = re.compile(r'{"name":"([\u4e00-\u9fa5_a-zA-Z0-9_]{1,10})","packageName"')
                result_yingyongming = re.findall(patten, j)
                print(result_yingyongming)

                patten = re.compile(r'"downloadUrl":"(http:.*?.apk)"')
                result_xiazaidizhi = re.findall(patten, j)
                #print(result_xiazaidizhi)

                patten = re.compile(r'"icon":"(.*?)"')
                result_yingyongtupian = re.findall(patten, j)
                print(result_yingyongtupian)
        return result_yingyongtupian,result_bangming,result_yingyongming,result_xiazaidizhi

    def createpage(self):
        result_bangming = []
        result_yingyongming = []
        result_yingyongtupian = []
        result_xiazaidizhi = []
        result_yingyongtupian,result_bangming,result_yingyongming,result_xiazaidizhi=self.get_memory()

        print(result_xiazaidizhi,result_yingyongtupian,result_yingyongming,result_bangming)

        # 主界面
        top_1 = PanedWindow(orient="vertical")
        top_1.pack(fill='both', expand=1)

        # 右边界面
        top_2 = PanedWindow(top_1)
        top_1.add(top_2)

        # 左边5项
        top_3 = PanedWindow(top_2, orient="vertical")
        top_2.add(top_3)

        # 右边图片
        top_4 = PanedWindow(top_2, orient="vertical")
        top_2.add(top_4)

        # 右边文字
        top_5 = PanedWindow(top_2, orient="vertical")
        top_2.add(top_5)

        # 下方两个按钮
        top_6 = PanedWindow(top_1, orient="horizontal")
        top_1.add(top_6)

        # 左边5标签
        left1 = Label(top_1, text="1", height=5, width=15)
        top_3.add(left1)
        left2 = Label(top_1, text="2", height=5, width=15)
        top_3.add(left2)
        left3 = Label(top_1, text="3", height=5, width=15)
        top_3.add(left3)
        left4 = Label(top_1, text="4", height=5, width=15)
        top_3.add(left4)
        left5 = Label(top_1, text="5", height=5, width=15)
        top_3.add(left5)

        pic_size = 93
        w_box = pic_size
        h_box = pic_size
        LP = [0, 0, 0, 0, 0]
        pil_image = [0, 0, 0, 0, 0]
        tk_image = [0, 0, 0, 0, 0]
        pil_image_resized = [0, 0, 0, 0, 0]
        k = 0
        for i in result_yingyongtupian:
            response = request.urlopen(i)
            cat_img = response.read()
            with open('C:\\Users\\jaska\\Desktop\\cat_500_600' + str(k) + '.jpg', 'wb') as f:
                f.write(cat_img)
                f.close()
            pil_image[k] = Image.open(r'C:\Users\jaska\Desktop\cat_500_600' + str(k) + '.jpg')
            w, h = pil_image[k].size
            pil_image_resized[k] = self.resize(w, h, w_box, h_box, pil_image[k])
            tk_image[k] = ImageTk.PhotoImage(pil_image_resized[k])
            print(tk_image)
            LP[k] = Label(top_4, image=tk_image[k], height=w_box, width=h_box)
            top_4.add(LP[k])
            k += 1

        def button_1():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[0])

        def button_2():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[1])

        def button_3():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[2])

        def button_4():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[3])

        def button_5():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[4])

        def button_6():
            top_1.destroy()
            Third(self.root)

        def button_7():
            messagebox.showinfo(title="往后",message="可惜是最后了哟！")

        # 右边按钮
        button1_1 = Button(top_2, text=result_yingyongming[0], height=5, width=30, command=button_1, highlightcolor="blue",
                           activebackground="blue", justify="right", compound="right")
        top_5.add(button1_1)
        button1_2 = Button(top_2, text=result_yingyongming[1], height=5, width=30, command=button_2, highlightcolor="blue",
                           activebackground="blue", justify="right", compound="right")
        top_5.add(button1_2)
        button1_3 = Button(top_2, text=result_yingyongming[2], height=5, width=30, command=button_3, highlightcolor="blue",
                           activebackground="blue", justify="right", compound="right")
        top_5.add(button1_3)
        button1_4 = Button(top_2, text=result_yingyongming[3], height=5, width=30, command=button_4, highlightcolor="blue",
                           activebackground="blue", justify="right", compound="right")
        top_5.add(button1_4)
        button1_5 = Button(top_2, text=result_yingyongming[4], height=5, width=30, command=button_5, highlightcolor="blue",
                           activebackground="blue", justify="right", compound="right")
        top_5.add(button1_5)

        # 下方左右换页按钮
        button1_6 = Button(top_6, text="←", height=2, width=30, command=button_6, highlightcolor="blue",
                           activebackground="blue", justify="right", compound="right")
        top_6.add(button1_6)
        button1_7 = Button(top_6, text="→", height=2, width=30, command=button_7, highlightcolor="blue",
                           activebackground="blue", justify="right", compound="right")
        top_6.add(button1_7)
        root.mainloop()

    def resize(self,w,h,w_box,h_box,pil_image):
        f1 = 1.0 * w_box / w  # 1.0 forces float division in Python2
        f2 = 1.0 * h_box / h
        factor = min([f1, f2])
        # print(f1, f2, factor) # test
        # use best down-sizing filter
        width = int(w * factor)
        height = int(h * factor)
        return pil_image.resize((width, height), Image.ANTIALIAS)


root=tkinter.Tk()
root.title('text')
First(root)


