from urllib import parse, request
import requests
import json
import os, re
from tkinter import messagebox, Canvas, PanedWindow, Label, Button, Frame, PhotoImage, Entry, StringVar
from tkinter.messagebox import showinfo
import tkinter
from PIL import Image, ImageTk

import text_pic, text_main


class show():
    def __init__(self):
        self.bangming = []
        self.biaoshi = []
        self.result_bangming = []
        self.result_yingyongming = []
        self.result_yingyongtupian = []
        self.result_xiazaidizhi = []
        self.real_biaoshi = []
        self.real_bangming = []
        self.bad = []
        self.biggest = []
        self.start()

    def Bcak_contral(self):

        def get_memory(name, biggest):
            patten = re.compile(r'(.*?)_list')
            bi_name = re.findall(patten, name)
            print(bi_name, name, biggest)
            url = 'https://gzgd.ams.ott.chinanetcenter.com:9912/ams/is/externalRank/queryRank?clientInfo= { "deviceCode":"BOX", "rankConditions":[ {"code":"' + str(
                bi_name[0]) + '_list", "topN":' + str(biggest) + '} ] }'
            res = requests.get(url)
            inp_str = res.json()

            for i, j in inp_str.items():
                if (i == 'content'):
                    patten = re.compile(r'{"name":"(.*?)","code"')
                    self.result_bangming = re.findall(patten, j)
                    # print(result_bangming)

                    patten = re.compile(r'{"name":"([\u4e00-\u9fa5_a-zA-Z0-9_]{1,10})","packageName"')
                    self.result_yingyongming = re.findall(patten, j)
                    # print(result_yingyongming)

                    patten = re.compile(r'"downloadUrl":"(http:.*?.apk)"')
                    self.result_xiazaidizhi = re.findall(patten, j)
                    # print(result_xiazaidizhi)

                    patten = re.compile(r'"icon":"(.*?)"')
                    self.result_yingyongtupian = re.findall(patten, j)
                    # print(result_yingyongtupian)

            return self.result_yingyongtupian, self.result_bangming, self.result_yingyongming, self.result_xiazaidizhi

        self.root = tkinter.Toplevel()

        top_1 = PanedWindow(self.root, orient="horizontal")
        top_1.pack(fill='both', expand=1)

        top_2 = PanedWindow(top_1, orient="vertical")
        top_1.add(top_2)

        top_3 = PanedWindow(top_1, orient="vertical")
        top_1.add(top_3)

        top_4 = PanedWindow(top_1, orient="vertical")
        top_1.add(top_4)

        top_5 = PanedWindow(top_1, orient="horizontal")
        top_4.add(top_5)

        top_6 = PanedWindow(top_1, orient="horizontal")
        top_4.add(top_6)

        top_7 = PanedWindow(top_1, orient="vertical")
        top_6.add(top_7)

        top_8 = PanedWindow(top_1, orient="horizontal")
        top_6.add(top_8)

        left1 = Label(top_2, text="排行榜名称", height=3, width=15).pack()

        LP = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        k = 0
        for i in self.real_bangming:
            LP[k] = Label(top_2, text=i, height=3, width=20).pack(pady=3, ipady=1)
            k += 1
            if (k > 10):
                break
        k = 0
        middle = Label(top_3, text="标识", height=3, width=15).pack()
        for i in self.real_biaoshi:

            LP[k] = Label(top_3, text=i, height=3, width=20).pack(pady=3, ipady=1)
            k += 1
            if (k > 10):
                break

        last = Label(top_5, text="操作", height=3, width=30).pack()

        def hand(fun, **kwds):
            '''''事件处理函数的适配器，相当于中介，那个event是从那里来的呢，我也纳闷，这也许就是python的伟大之处吧'''
            return lambda event, fun=fun, kwds=kwds: fun(event, **kwds)

        def button_(event, bangming, k):

            M = 0
            for i in self.bad:
                if (i == bangming):
                    M += 1
            # print(M, len(self.real_biaoshi), self.bad, bangming)
            if (M == 0):
                num = 0
                self.biaoshi = []
                print('biaoshi',self.biaoshi)
                self.bad.append(bangming)
                print("bad",self.bad,self.real_biaoshi)
                for i in self.real_biaoshi:
                   if i in self.bad:
                       continue
                   else:
                       self.biaoshi.append(i)
                print(self.biaoshi)
                messagebox.showinfo(title="提示", message="隐藏成功")
            else:
                self.biaoshi = []
                self.bad.remove(bangming)
                print('biaoshi', self.bad)
                for i in self.real_biaoshi:
                   if i in self.bad:
                       continue
                   else:
                       self.biaoshi.append(i)
                print(self.biaoshi)
                messagebox.showinfo(title="提示", message="取消隐藏成功")

        k = 0
        for i in self.real_biaoshi:
            LP[k] = Button(top_7, text="隐藏", height=3, width=20)
            LP[k].bind("<Button-1>", hand(button_, bangming=i, k=5))
            LP[k].pack()
            k += 1
            if (k > 10):
                break

        def button_delate(event, biaoshi,bangming,k):
            messagebox.showinfo(title="删除", message="确定删除嘛？")
            m = [999 for i in range(len(self.real_bangming) - 1)]
            k -= 1
            z = 0
            # for i in self.real_biaoshi:
            #     if (i == bangming):
            #         self.real_bangming[z] = 0
            #         self.real_biaoshi[z] = 0
            #     z += 1
            # print(self.real_biaoshi, self.real_bangming)
            # z = 0
            # for i in self.real_bangming:
            #     if (i != 0):
            #         m[z] = i
            #         z += 1
            # self.real_bangming = [998 for i in range(len(m))]
            # z = 0
            # for i in m:
            #     self.real_bangming[z] = i
            #     z += 1
            #
            # z = 0
            # for i in self.real_biaoshi:
            #     if (i != 0):
            #         m[z] = i
            #         z += 1
            # self.real_biaoshi = [999 for i in range(len(m))]
            # z = 0
            # for i in m:
            #     self.real_biaoshi[z] = i
            #     z += 1
            #
            # z = 0
            # for i in self.real_biaoshi:
            #     if (i == bangming):
            #         self.real_bangming[z] = 0
            #         self.real_biaoshi[z] = 0
            #     z += 1
            # print(self.real_biaoshi, self.real_bangming)
            # z = 0
            # for i in self.real_bangming:
            #     if (i != 0):
            #         m[z] = i
            #         z += 1
            # self.real_bangming = [998 for i in range(len(m))]
            # z = 0
            # for i in m:
            #     self.real_bangming[z] = i
            #     z += 1
            #
            # z = 0
            # for i in self.real_biaoshi:
            #     if (i != 0):
            #         m[z] = i
            #         z += 1
            # self.real_biaoshi = [999 for i in range(len(m))]
            # z = 0
            # for i in m:
            #     self.real_biaoshi[z] = i
            #     z += 1
            #
            # #########################################
            # z = 0
            # for i in self.biaoshi:
            #     if (i == bangming):
            #         self.bangming[z] = 0
            #         self.biaoshi[z] = 0
            #     z += 1
            # print(self.biaoshi, self.bangming)
            # z = 0
            # for i in self.bangming:
            #     if (i != 0):
            #         m[z] = i
            #         z += 1
            # self.bangming = [998 for i in range(len(m))]
            # z = 0
            # for i in m:
            #     self.bangming[z] = i
            #     z += 1
            #
            # z = 0
            # for i in self.biaoshi:
            #     if (i != 0):
            #         m[z] = i
            #         z += 1
            # self.biaoshi = [999 for i in range(len(m))]
            # z = 0
            # for i in m:
            #     self.biaoshi[z] = i
            #     z += 1

            self.real_biaoshi.remove(biaoshi)

            self.biaoshi.remove(biaoshi)

            self.real_bangming.remove(bangming)

            self.bangming.remove(bangming)

            print(self.real_bangming, self.real_biaoshi)
            self.root.destroy()
            self.Bcak_contral()

        k = 0
        for i in self.real_biaoshi:
            LP[k] = Button(top_8, text="删除", height=3, width=20)
            LP[k].bind("<Button-1>", hand(button_delate, biaoshi=i, bangming=self.real_bangming[k] ,k=k))
            LP[k].pack()
            k += 1
            if (k > 10):
                break

        def button_add():
            self.root.destroy()
            self.add()

        Add_but = Button(top_8, text="增加", height=3, width=30, command=button_add).pack()

    def add(self):
        root = tkinter.Toplevel()
        painame = StringVar()
        biaoname = StringVar()
        biggest = StringVar()

        def mit():
            while (1):
                p_name = painame.get()
                b_name = biaoname.get()
                big = biggest.get()
                num = 0
                for i in self.real_bangming:
                    if (i == p_name):
                        showinfo(title='错误', message='该排行榜已存在')
                        num = 1
                if (num == 1):
                    break
                patten = re.compile(r'(.*?)_list')
                bi_name = re.findall(patten, b_name)
                if (bi_name == []):
                    showinfo(title='错误', message='标识符错误')
                    break
                # print(bi_name, b_name)
                url = 'https://gzgd.ams.ott.chinanetcenter.com:9912/ams/is/externalRank' \
                      '/queryRank?clientInfo= { "deviceCode":"BOX", "rankConditions":' \
                      '[ {"code":"' + str(bi_name[0]) + '_list", "topN":' + str(1) + '} ] }'
                res = requests.get(url)
                res.keep_alive = False
                inp_str = res.json()
                result_bangming = []
                for i, j in inp_str.items():
                    if (i == 'content'):
                        patten = re.compile(r'{"name":"(.*?)","code"')
                        result_bangming = re.findall(patten, j)
                        # print(result_bangming)
                if (result_bangming == []):
                    showinfo(title='错误', message='标识符错误')
                else:
                    showinfo(title='提示', message='添加成功')
                    mp = self.real_bangming
                    mb = self.real_biaoshi
                    mbi = self.biggest
                    self.real_bangming = [998 for i in range(len(mp) + 1)]
                    self.real_biaoshi = [999 for i in range(len(mb) + 1)]
                    self.biggest.append(big)
                    k = 0
                    for i in mp:
                        self.real_bangming[k] = i
                        k += 1
                    self.real_bangming[k] = p_name
                    k = 0
                    for i in mb:
                        self.real_biaoshi[k] = i
                        k += 1
                    self.real_biaoshi[k] = b_name
                    ##################################
                    mp = self.bangming
                    mb = self.biaoshi
                    self.bangming = [998 for i in range(len(mp) + 1)]
                    self.biaoshi = [999 for i in range(len(mb) + 1)]
                    k = 0
                    for i in mp:
                        self.bangming[k] = i
                        k += 1
                    self.bangming[k] = p_name
                    k = 0
                    for i in mb:
                        self.biaoshi[k] = i
                        k += 1
                    self.biaoshi[k] = b_name
                    break

        def quit_():
            root.destroy()
            self.Bcak_contral()

        # 创建标签
        top_1 = PanedWindow()
        labelName = tkinter.Label(root, text='排行榜名称:', justify=tkinter.RIGHT, width=80)
        # 将标签放到窗口上
        labelName.place(x=10, y=8, width=80, height=20)
        # 创建文本框，同时设置关联的变量
        entryName = tkinter.Entry(root, width=80, textvariable=painame)
        entryName.place(x=100, y=5, width=80, height=30)
        labelPwd = tkinter.Label(root, text='标识符:', justify=tkinter.RIGHT, width=80)
        labelPwd.place(x=10, y=50, width=80, height=30)
        # 创建文本框
        entryPwd = tkinter.Entry(root, width=80, textvariable=biaoname)
        entryPwd.place(x=100, y=50, width=80, height=30)
        labelbig = tkinter.Label(root, text='获取应用数量:', justify=tkinter.RIGHT, width=80)
        labelbig.place(x=10, y=90, width=80, height=30)
        entryPwd = tkinter.Entry(root, width=80, textvariable=biggest)
        entryPwd.place(x=100, y=90, width=80, height=30)
        buttonOk = tkinter.Button(root, text='确定', command=mit)
        buttonOk.place(x=30, y=130, width=50, height=30)
        buttonCancel = tkinter.Button(root, text='返回', command=quit_)
        buttonCancel.place(x=130, y=130, width=50, height=30)
        # 取消按钮的事件处理函数
        root.mainloop()

    def chakan(self):
        root = tkinter.Toplevel()
        top_1 = PanedWindow(root, orient="vertical")
        top_1.pack(fill='both', expand=1)
        ttle = Label(top_1, text=self.bangming)
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

        def resize(w, h, w_box, h_box, pil_image):
            f1 = 1.0 * w_box / w  # 1.0 forces float division in Python2
            f2 = 1.0 * h_box / h
            factor = min([f1, f2])
            # print(f1, f2, factor) # test
            # use best down-sizing filter
            width = int(w * factor)
            height = int(h * factor)
            return pil_image.resize((width, height), Image.ANTIALIAS)

        pic_size = 93
        w_box = pic_size
        h_box = pic_size
        LP = [0, 0, 0, 0, 0]
        pil_image = [0, 0, 0, 0, 0]
        tk_image = [0, 0, 0, 0, 0]
        pil_image_resized = [0, 0, 0, 0, 0]
        k = 0
        for i in self.result_yingyongtupian:
            response = request.urlopen(i)
            cat_img = response.read()
            with open('C:\\Users\\jaska\\Desktop\\cat_500_600' + str(k) + '.jpg', 'wb') as f:
                f.write(cat_img)
                f.close()
            pil_image[k] = Image.open(r'C:\Users\jaska\Desktop\cat_500_600' + str(k) + '.jpg')
            w, h = pil_image[k].size
            pil_image_resized[k] = resize(w, h, w_box, h_box, pil_image[k])
            tk_image[k] = ImageTk.PhotoImage(pil_image_resized[k])
            print(tk_image)
            LP[k] = Label(top_4, image=tk_image[k], height=w_box, width=h_box)
            top_4.add(LP[k])
            k += 1

        def button_1():
            messagebox.showinfo(title="Download", message=self.result_xiazaidizhi[0])

        def button_2():
            messagebox.showinfo(title="Download", message=self.result_xiazaidizhi[1])

        def button_3():
            messagebox.showinfo(title="Download", message=self.result_xiazaidizhi[2])

        def button_4():
            messagebox.showinfo(title="Download", message=self.result_xiazaidizhi[3])

        def button_5():
            messagebox.showinfo(title="Download", message=self.result_xiazaidizhi[4])

        def button_6():
            root.destroy()
            self.Bcak_contral()

        # 右边按钮
        button1_1 = Button(top_2, text=self.result_yingyongming[0], height=5, width=30, command=button_1,
                           highlightcolor="blue",
                           activebackground="blue", justify="right", compound="right")
        top_5.add(button1_1)
        button1_2 = Button(top_2, text=self.result_yingyongming[1], height=5, width=30, command=button_2,
                           highlightcolor="blue",
                           activebackground="blue", justify="right", compound="right")
        top_5.add(button1_2)
        button1_3 = Button(top_2, text=self.result_yingyongming[2], height=5, width=30, command=button_3,
                           highlightcolor="blue",
                           activebackground="blue", justify="right", compound="right")
        top_5.add(button1_3)
        button1_4 = Button(top_2, text=self.result_yingyongming[3], height=5, width=30, command=button_4,
                           highlightcolor="blue",
                           activebackground="blue", justify="right", compound="right")
        top_5.add(button1_4)
        button1_5 = Button(top_2, text=self.result_yingyongming[4], height=5, width=30, command=button_5,
                           highlightcolor="blue",
                           activebackground="blue", justify="right", compound="right")
        top_5.add(button1_5)
        button1_6 = Button(top_6, text="返回", height=2, width=30, command=button_6, highlightcolor="blue",
                           activebackground="blue", justify="right", compound="right")
        top_6.add(button1_6)
        self.root.mainloop()

        def resize(self, w, h, w_box, h_box, pil_image):
            f1 = 1.0 * w_box / w  # 1.0 forces float division in Python2
            f2 = 1.0 * h_box / h
            factor = min([f1, f2])
            # print(f1, f2, factor) # test
            # use best down-sizing filter
            width = int(w * factor)
            height = int(h * factor)
            return pil_image.resize((width, height), Image.ANTIALIAS)

    def qianduan(self):
        room = tkinter.Toplevel()
        room.title("排行榜")
        p1 = PanedWindow(room, orient="horizontal")
        p1.pack(fill='both', expand=1)
        p2 = PanedWindow(p1, orient="vertical")
        p1.add(p2)
        p3 = PanedWindow(p1, orient="vertical")
        p1.add(p3)
        p4 = PanedWindow(p1, orient="vertical")
        p1.add(p4)
        p25 = PanedWindow(p1, orient="vertical")
        p1.add(p25)

        p17 = PanedWindow(p2, orient="horizontal")
        p2.add(p17)
        p18 = PanedWindow(p2, orient="horizontal")
        p2.add(p18)
        p19 = PanedWindow(p3, orient="horizontal")
        p3.add(p19)
        p20 = PanedWindow(p3, orient="horizontal")
        p3.add(p20)
        p21 = PanedWindow(p4, orient="horizontal")
        p4.add(p21)
        p22 = PanedWindow(p4, orient="horizontal")
        p4.add(p22)
        p23 = PanedWindow(p25, orient="horizontal")
        p25.add(p23)
        p24 = PanedWindow(p25, orient="horizontal")
        p25.add(p24)
        p27 = PanedWindow(p3, orient="horizontal")
        p3.add(p27)
        p28 = PanedWindow(p4, orient="horizontal")
        p4.add(p28)
        p29 = PanedWindow(p25, orient="horizontal")
        p25.add(p29)

        p5 = PanedWindow(p2, orient="vertical")
        p6 = PanedWindow(p2, orient="vertical")
        p7 = PanedWindow(p2, orient="vertical")
        p18.add(p5)
        p18.add(p6)
        p18.add(p7)
        p8 = PanedWindow(p3, orient="vertical")
        p9 = PanedWindow(p3, orient="vertical")
        p10 = PanedWindow(p3, orient="vertical")
        p27.add(p8)
        p27.add(p9)
        p27.add(p10)
        p11 = PanedWindow(p4, orient="vertical")
        p12 = PanedWindow(p4, orient="vertical")
        p13 = PanedWindow(p4, orient="vertical")
        p28.add(p11)
        p28.add(p12)
        p28.add(p13)
        p14 = PanedWindow(p25, orient="vertical")
        p15 = PanedWindow(p25, orient="vertical")
        p16 = PanedWindow(p25, orient="vertical")
        p29.add(p14)
        p29.add(p15)
        p29.add(p16)

        result_bangming = [0, 0, 0, 0]
        result_yingyongming = [0, 0, 0, 0]
        result_yingyongtupian = [0, 0, 0, 0]
        result_xiazaidizhi = [0, 0, 0, 0]
        g_yingyongtupian = [0, 0, 0, 0]
        g_yingyongming = [0, 0, 0, 0]
        k = 0
        for i in self.biaoshi:
            if (k > 4):
                break
            patten = re.compile(r'(.*?)_list')
            bi_name = re.findall(patten, i)
            url = 'https://gzgd.ams.ott.chinanetcenter.com:9912/ams/is/externalRank/queryRank?clientInfo= { "deviceCode":"BOX", "rankConditions":[ {"code":"' + str(
                bi_name[0]) + '_list", "topN":' + self.biggest[k] + '} ] }'
            res = requests.get(url)
            res.keep_alive = False
            inp_str = res.json()
            print(k)
            for i, j in inp_str.items():
                if (i == 'content'):
                    patten = re.compile(r'{"name":"(.*?)","code"')
                    result_bangming[k] = re.findall(patten, j)
                    print(result_bangming[k])

                    patten = re.compile(r'{"name":"([\u4e00-\u9fa5_a-zA-Z0-9_]{1,10})","packageName"')
                    result_yingyongming[k] = re.findall(patten, j)
                    self.result_yingyongming = result_yingyongming[:]
                    print(result_yingyongming[k])

                    patten = re.compile(r'"downloadUrl":"(http:.*?.apk)"')
                    result_xiazaidizhi[k] = re.findall(patten, j)
                    self.result_xiazaidizhi = result_xiazaidizhi[:]
                    print(result_xiazaidizhi[k])

                    patten = re.compile(r'"icon":"(.*?)"')
                    result_yingyongtupian[k] = re.findall(patten, j)
                    self.result_yingyongtupian = result_yingyongtupian[:]
                    print(result_yingyongtupian[k])
            k += 1

            def resize(w, h, w_box, h_box, pil_image):
                f1 = 1.0 * w_box / w  # 1.0 forces float division in Python2
                f2 = 1.0 * h_box / h
                factor = min([f1, f2])
                # print(f1, f2, factor) # test
                # use best down-sizing filter
                width = int(w * factor)
                height = int(h * factor)
                return pil_image.resize((width, height), Image.ANTIALIAS)

        pil_image = [0, 0, 0, 0, 0]
        tk_image = [0, 0, 0, 0, 0]
        pil_image_resized = [0, 0, 0, 0, 0]
        contral_num = 0

        for i in result_bangming:
            if (i == 0):
                break
            contral_num += 1

        def Label_():
            if (contral_num == 4):
                t1 = Label(p1, text=result_bangming[0], height=5, width=15)
                p17.add(t1)
                t2 = Label(p1, text=result_bangming[1], height=5, width=15)
                p19.add(t2)
                t3 = Label(p1, text=result_bangming[2], height=5, width=15)
                p21.add(t3)
                t4 = Label(p1, text=result_bangming[3], height=5, width=15)
                p23.add(t4)
                LP = [0, 0, 0, 0, 0]
                k = 0
                for i in range(5):
                    i = i + 1
                    LP[k] = Label(p1, text=i, height=5, width=15)
                    p5.add(LP[k])
                k = 0
                for i in range(5):
                    i = i + 1
                    LP[k] = Label(p1, text=i, height=5, width=15)
                    p8.add(LP[k])
                k = 0
                for i in range(5):
                    i = i + 1
                    LP[k] = Label(p1, text=i, height=5, width=15)
                    p11.add(LP[k])
                k = 0
                for i in range(5):
                    i = i + 1
                    LP[k] = Label(p1, text=i, height=5, width=15)
                    p14.add(LP[k])

            elif (contral_num == 3):
                t1 = Label(p1, text=result_bangming[0], height=5, width=15)
                p17.add(t1)
                t2 = Label(p1, text=result_bangming[1], height=5, width=15)
                p19.add(t2)
                t3 = Label(p1, text=result_bangming[2], height=5, width=15)
                p21.add(t3)
                LP = [0, 0, 0, 0, 0]
                k = 0
                for i in range(5):
                    i = i + 1
                    LP[k] = Label(p1, text=i, height=5, width=15)
                    p5.add(LP[k])
                k = 0
                for i in range(5):
                    i = i + 1
                    LP[k] = Label(p1, text=i, height=5, width=15)
                    p8.add(LP[k])
                k = 0
                for i in range(5):
                    i = i + 1
                    LP[k] = Label(p1, text=i, height=5, width=15)
                    p11.add(LP[k])
            elif (contral_num == 2):
                t1 = Label(p1, text=result_bangming[0], height=5, width=15)
                p17.add(t1)
                t2 = Label(p1, text=result_bangming[1], height=5, width=15)
                p19.add(t2)
                LP = [0, 0, 0, 0, 0]
                k = 0
                for i in range(5):
                    i = i + 1
                    LP[k] = Label(p1, text=i, height=5, width=15)
                    p5.add(LP[k])
                k = 0
                for i in range(5):
                    i = i + 1
                    LP[k] = Label(p1, text=i, height=5, width=15)
                    p8.add(LP[k])

            elif (contral_num == 1):
                t1 = Label(p1, text=result_bangming[0], height=5, width=15)
                p17.add(t1)
                LP = [0, 0, 0, 0, 0]
                k = 0
                for i in range(5):
                    i = i + 1
                    LP[k] = Label(p1, text=i, height=5, width=15)
                    p5.add(LP[k])
            else:
                print("contral_num=0")

        def button_0_1():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[0][0])

        def button_0_2():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[0][1])

        def button_0_3():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[0][2])

        def button_0_4():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[0][3])

        def button_0_5():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[0][4])

        def button_1_1():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[1][0])

        def button_1_2():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[1][1])

        def button_1_3():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[1][2])

        def button_1_4():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[1][3])

        def button_1_5():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[1][4])

        def button_2_1():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[2][0])

        def button_2_2():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[2][1])

        def button_2_3():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[2][2])

        def button_2_4():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[2][3])

        def button_2_5():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[2][4])

        def button_3_1():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[3][0])

        def button_3_2():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[3][1])

        def button_3_3():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[3][2])

        def button_3_4():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[3][3])

        def button_3_5():
            messagebox.showinfo(title="Download", message=result_xiazaidizhi[3][4])

        def gengduo(i):
            s_pic = 105
            gd_yingyongtupian = g_yingyongtupian[i]
            gd_yingyongming = result_yingyongming[i][5:]
            print('gd', gd_yingyongming[2:4], gd_yingyongtupian)

            def hand(fun, **kwds):
                '''''事件处理函数的适配器，相当于中介，那个event是从那里来的呢，我也纳闷，这也许就是python的伟大之处吧'''
                return lambda event, fun=fun, kwds=kwds: fun(event, **kwds)

            def button_(event, its, kts):
                messagebox.showinfo(title="Download", message='text')

            if (len(gd_yingyongtupian) == 0):
                messagebox.showinfo(title="Attacting", message="没有更多")
            elif (len(gd_yingyongtupian) <= 5):
                room = tkinter.Toplevel()
                room.title("排行榜")
                p1 = PanedWindow(room, orient="vertical")
                p1.pack(fill='both', expand=1)
                p2 = PanedWindow(p1, orient="horizontal")
                p1.add(p2)
                p3 = PanedWindow(p1, orient="horizontal")
                p1.add(p3)
                p4 = PanedWindow(p1, orient="horizontal")
                p1.add(p4)
                p5 = PanedWindow(p1, orient="horizontal")
                p1.add(p5)
                p6 = PanedWindow(p1, orient="horizontal")
                p1.add(p6)
                p7 = PanedWindow(p1, orient="horizontal")
                p1.add(p7)
                p8 = PanedWindow(p1, orient="horizontal")
                p1.add(p8)
                lp = [0, 0, 0, 0, 0]
                k = 0
                for i in gd_yingyongtupian:
                    lp[k] = Label(p1, image=i, height=s_pic, width=s_pic)
                    p2.add(lp[k])
                    lp[k] = Button(p3, text=gd_yingyongming[k], width=15, height=5)
                    lp[k].bind("<Button-1>", hand(button_, its=i, kts=k))
                    p3.add(lp[k])
                    k += 1
                room.mainloop()
            elif (len(gd_yingyongtupian) <= 10):
                room = tkinter.Toplevel()
                room.title("排行榜")
                p1 = PanedWindow(room, orient="vertical")
                p1.pack(fill='both', expand=1)
                p2 = PanedWindow(p1, orient="horizontal")
                p1.add(p2)
                p3 = PanedWindow(p1, orient="horizontal")
                p1.add(p3)
                p4 = PanedWindow(p1, orient="horizontal")
                p1.add(p4)
                p5 = PanedWindow(p1, orient="horizontal")
                p1.add(p5)
                p6 = PanedWindow(p1, orient="horizontal")
                p1.add(p6)
                p7 = PanedWindow(p1, orient="horizontal")
                p1.add(p7)
                p8 = PanedWindow(p1, orient="horizontal")
                p1.add(p8)
                lp = [0, 0, 0, 0, 0]
                k = 0
                newb = []
                newp = []
                newp = gd_yingyongtupian[0:4]
                newb = gd_yingyongming[0:4]
                for i in newp:
                    lp[k] = Label(p1, image=i, height=s_pic, width=s_pic)
                    p2.add(lp[k])
                    lp[k] = Button(p1, text=newb[k], width=15, height=5)
                    p3.add(lp[k])
                    k += 1
                k = 0
                newp = gd_yingyongtupian[5:]
                newb = gd_yingyongming[5:]
                for i in newp:
                    lp[k] = Label(p1, image=i, height=s_pic, width=s_pic)
                    p4.add(lp[k])
                    lp[k] = Button(p1, text=newb[k], width=15, height=5)
                    p5.add(lp[k])
                    k += 1
                room.mainloop()
            else:
                room = tkinter.Toplevel()
                room.title("排行榜")
                p1 = PanedWindow(room, orient="vertical")
                p1.pack(fill='both', expand=1)
                p2 = PanedWindow(p1, orient="horizontal")
                p1.add(p2)
                p3 = PanedWindow(p1, orient="horizontal")
                p1.add(p3)
                p4 = PanedWindow(p1, orient="horizontal")
                p1.add(p4)
                p5 = PanedWindow(p1, orient="horizontal")
                p1.add(p5)
                p6 = PanedWindow(p1, orient="horizontal")
                p1.add(p6)
                p7 = PanedWindow(p1, orient="horizontal")
                p1.add(p7)
                p8 = PanedWindow(p1, orient="horizontal")
                p1.add(p8)
                lp = [0, 0, 0, 0, 0]
                k = 0
                newb = []
                newp = []
                newp = gd_yingyongtupian[0:5]
                newb = gd_yingyongming[0:5]
                print("Test", newb, newp)
                for i in newp:
                    lp[k] = Label(p1, image=i, height=s_pic, width=s_pic)
                    p2.add(lp[k])
                    lp[k] = Button(p1, text=newb[k], width=15, height=5)
                    p3.add(lp[k])
                    k += 1
                k = 0
                print(gd_yingyongming, gd_yingyongtupian)
                newp = gd_yingyongtupian[6:11]
                newb = gd_yingyongming[6:11]
                for i in newp:
                    lp[k] = Label(p1, image=i, height=s_pic, width=s_pic)
                    p4.add(lp[k])
                    lp[k] = Button(p1, text=newb[k], width=15, height=5)
                    p5.add(lp[k])
                    k += 1
                k = 0
                n = 0
                if (len(gd_yingyongming) > 16):
                    n = 16
                else:
                    n = len(gd_yingyongming)
                newp = gd_yingyongtupian[12:n]
                newb = gd_yingyongming[12:n]
                for i in newp:
                    lp[k] = Label(p1, image=i, height=s_pic, width=s_pic)
                    p6.add(lp[k])
                    lp[k] = Button(p1, text=newb[k], width=15, height=5)
                    p7.add(lp[k])
                    k += 1
                room.mainloop()

        def button_9_0():
            gengduo(0)

        def button_9_1():
            gengduo(1)

        def button_9_2():
            gengduo(2)

        def button_9_3():
            gengduo(3)

        def Button_(contral_num):
            if (contral_num == 4):
                button9_0 = Button(p1, text='更多', width=15, height=5, command=button_9_0)
                p2.add(button9_0)
                button9_1 = Button(p1, text='更多', width=15, height=5, command=button_9_1)
                p3.add(button9_1)
                button9_2 = Button(p1, text='更多', width=15, height=5, command=button_9_2)
                p4.add(button9_2)
                button9_3 = Button(p1, text='更多', width=15, height=5, command=button_9_3)
                p25.add(button9_3)
                button0_1 = Button(p1, text=result_yingyongming[0][0], height=5, width=30, command=button_0_1,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button0_2 = Button(p1, text=result_yingyongming[0][1], height=5, width=30, command=button_0_2,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button0_3 = Button(p1, text=result_yingyongming[0][2], height=5, width=30, command=button_0_3,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button0_4 = Button(p1, text=result_yingyongming[0][3], height=5, width=30, command=button_0_4,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button0_5 = Button(p1, text=result_yingyongming[0][4], height=5, width=30, command=button_0_5,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")

                button1_1 = Button(p1, text=result_yingyongming[1][0], height=5, width=30, command=button_1_1,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button1_2 = Button(p1, text=result_yingyongming[1][1], height=5, width=30, command=button_1_2,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button1_3 = Button(p1, text=result_yingyongming[1][2], height=5, width=30, command=button_1_3,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button1_4 = Button(p1, text=result_yingyongming[1][3], height=5, width=30, command=button_1_4,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button1_5 = Button(p1, text=result_yingyongming[1][4], height=5, width=30, command=button_1_5,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")

                button2_1 = Button(p1, text=result_yingyongming[2][0], height=5, width=30, command=button_2_1,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button2_2 = Button(p1, text=result_yingyongming[2][1], height=5, width=30, command=button_2_2,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button2_3 = Button(p1, text=result_yingyongming[2][2], height=5, width=30, command=button_2_3,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button2_4 = Button(p1, text=result_yingyongming[2][3], height=5, width=30, command=button_2_4,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button2_5 = Button(p1, text=result_yingyongming[2][4], height=5, width=30, command=button_2_5,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")

                button3_1 = Button(p1, text=result_yingyongming[3][0], height=5, width=30, command=button_3_1,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button3_2 = Button(p1, text=result_yingyongming[3][1], height=5, width=30, command=button_3_2,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button3_3 = Button(p1, text=result_yingyongming[3][2], height=5, width=30, command=button_3_3,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button3_4 = Button(p1, text=result_yingyongming[3][3], height=5, width=30, command=button_3_4,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button3_5 = Button(p1, text=result_yingyongming[3][4], height=5, width=30, command=button_3_5,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")

                p7.add(button0_1)
                p7.add(button0_2)
                p7.add(button0_3)
                p7.add(button0_4)
                p7.add(button0_5)

                p10.add(button1_1)
                p10.add(button1_2)
                p10.add(button1_3)
                p10.add(button1_4)
                p10.add(button1_5)

                p13.add(button2_1)
                p13.add(button2_2)
                p13.add(button2_3)
                p13.add(button2_4)
                p13.add(button2_5)

                p16.add(button3_1)
                p16.add(button3_2)
                p16.add(button3_3)
                p16.add(button3_4)
                p16.add(button3_5)

            elif (contral_num == 3):
                button9_0 = Button(p1, text='更多', width=15, height=5, command=button_9_0)
                p2.add(button9_0)
                button9_1 = Button(p1, text='更多', width=15, height=5, command=button_9_1)
                p3.add(button9_1)
                button9_2 = Button(p1, text='更多', width=15, height=5, command=button_9_2)
                p4.add(button9_2)
                button0_1 = Button(p1, text=result_yingyongming[0][0], height=5, width=30, command=button_0_1,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button0_2 = Button(p1, text=result_yingyongming[0][1], height=5, width=30, command=button_0_2,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button0_3 = Button(p1, text=result_yingyongming[0][2], height=5, width=30, command=button_0_3,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button0_4 = Button(p1, text=result_yingyongming[0][3], height=5, width=30, command=button_0_4,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button0_5 = Button(p1, text=result_yingyongming[0][4], height=5, width=30, command=button_0_5,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")

                button1_1 = Button(p1, text=result_yingyongming[1][0], height=5, width=30, command=button_1_1,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button1_2 = Button(p1, text=result_yingyongming[1][1], height=5, width=30, command=button_1_2,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button1_3 = Button(p1, text=result_yingyongming[1][2], height=5, width=30, command=button_1_3,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button1_4 = Button(p1, text=result_yingyongming[1][3], height=5, width=30, command=button_1_4,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button1_5 = Button(p1, text=result_yingyongming[1][4], height=5, width=30, command=button_1_5,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")

                button2_1 = Button(p1, text=result_yingyongming[2][0], height=5, width=30, command=button_2_1,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button2_2 = Button(p1, text=result_yingyongming[2][1], height=5, width=30, command=button_2_2,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button2_3 = Button(p1, text=result_yingyongming[2][2], height=5, width=30, command=button_2_3,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button2_4 = Button(p1, text=result_yingyongming[2][3], height=5, width=30, command=button_2_4,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button2_5 = Button(p1, text=result_yingyongming[2][4], height=5, width=30, command=button_2_5,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")

                p7.add(button0_1)
                p7.add(button0_2)
                p7.add(button0_3)
                p7.add(button0_4)
                p7.add(button0_5)

                p10.add(button1_1)
                p10.add(button1_2)
                p10.add(button1_3)
                p10.add(button1_4)
                p10.add(button1_5)

                p13.add(button2_1)
                p13.add(button2_2)
                p13.add(button2_3)
                p13.add(button2_4)
                p13.add(button2_5)

            elif (contral_num == 2):
                button9_0 = Button(p1, text='更多', width=15, height=5, command=button_9_0)
                p2.add(button9_0)
                button9_1 = Button(p1, text='更多', width=15, height=5, command=button_9_0)
                p3.add(button9_1)

                button0_1 = Button(p1, text=result_yingyongming[0][0], height=5, width=30, command=button_0_1,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button0_2 = Button(p1, text=result_yingyongming[0][1], height=5, width=30, command=button_0_2,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button0_3 = Button(p1, text=result_yingyongming[0][2], height=5, width=30, command=button_0_3,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button0_4 = Button(p1, text=result_yingyongming[0][3], height=5, width=30, command=button_0_4,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button0_5 = Button(p1, text=result_yingyongming[0][4], height=5, width=30, command=button_0_5,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")

                button1_1 = Button(p1, text=result_yingyongming[1][0], height=5, width=30, command=button_1_1,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button1_2 = Button(p1, text=result_yingyongming[1][1], height=5, width=30, command=button_1_2,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button1_3 = Button(p1, text=result_yingyongming[1][2], height=5, width=30, command=button_1_3,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button1_4 = Button(p1, text=result_yingyongming[1][3], height=5, width=30, command=button_1_4,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button1_5 = Button(p1, text=result_yingyongming[1][4], height=5, width=30, command=button_1_5,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")

                p7.add(button0_1)
                p7.add(button0_2)
                p7.add(button0_3)
                p7.add(button0_4)
                p7.add(button0_5)

                p10.add(button1_1)
                p10.add(button1_2)
                p10.add(button1_3)
                p10.add(button1_4)
                p10.add(button1_5)

            elif (contral_num == 1):
                button9_0 = Button(p1, text='更多', width=15, height=5, command=button_9_0)
                p2.add(button9_0)

                button0_1 = Button(p1, text=result_yingyongming[0][0], height=5, width=30, command=button_0_1,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button0_2 = Button(p1, text=result_yingyongming[0][1], height=5, width=30, command=button_0_2,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button0_3 = Button(p1, text=result_yingyongming[0][2], height=5, width=30, command=button_0_3,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button0_4 = Button(p1, text=result_yingyongming[0][3], height=5, width=30, command=button_0_4,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")
                button0_5 = Button(p1, text=result_yingyongming[0][4], height=5, width=30, command=button_0_5,
                                   highlightcolor="blue", activebackground="blue", justify="right", compound="right")

                p7.add(button0_1)
                p7.add(button0_2)
                p7.add(button0_3)
                p7.add(button0_4)
                p7.add(button0_5)

            elif (contral_num == 0):
                print("contral_num = 0")

        def resize(w, h, w_box, h_box, pil_image):
            f1 = 1.0 * w_box / w  # 1.0 forces float division in Python2
            f2 = 1.0 * h_box / h
            factor = min([f1, f2])
            # print(f1, f2, factor) # test
            # use best down-sizing filter
            width = int(w * factor)
            height = int(h * factor)
            return pil_image.resize((width, height), Image.ANTIALIAS)

        def Photo_(contral_num):
            pic_size = 93
            w_box = pic_size
            h_box = pic_size
            LP = [0, 0, 0, 0, 0]
            pil_image = [0, 0, 0, 0, 0]
            tk_image = [0, 0, 0, 0, 0]
            pil_image_resized = [0, 0, 0, 0, 0]

            for i in range(5):
                LP[i] = [0 for i in range(100)]
                pil_image[i] = [0 for i in range(100)]
                tk_image[i] = [0 for i in range(100)]
                pil_image_resized[i] = [0 for i in range(100)]
            if (contral_num == 4):
                k = 0
                for i in result_yingyongtupian[0]:
                    if (k > 4):
                        # if (os.path.exists(r'C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(0) + '.jpg')):
                        #     pil_image[0][k] = Image.open(
                        #         r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(0) + '.jpg')
                        #     w, h = pil_image[0][k].size
                        #     pil_image_resized[0][k] = resize(w, h, w_box, h_box, pil_image[0][k])
                        #     tk_image[0][k] = ImageTk.PhotoImage(pil_image_resized[0][k])
                        #     print(tk_image)
                        #     k += 1
                        # else:
                        response = request.urlopen(i)
                        res.keep_alive = False
                        cat_img = response.read()
                        with open('C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(0) + '.jpg', 'wb') as f:
                            f.write(cat_img)
                            f.close()
                        pil_image[0][k] = Image.open(
                            r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(0) + '.jpg')
                        w, h = pil_image[0][k].size
                        pil_image_resized[0][k] = resize(w, h, w_box, h_box, pil_image[0][k])
                        tk_image[0][k] = ImageTk.PhotoImage(pil_image_resized[0][k])
                        print(tk_image)
                        k += 1
                    else:
                        # if (os.path.exists(r'C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(0) + '.jpg')):
                        #     pil_image[0][k] = Image.open(
                        #         r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(0) + '.jpg')
                        #     w, h = pil_image[0][k].size
                        #     pil_image_resized[0][k] = resize(w, h, w_box, h_box, pil_image[0][k])
                        #     tk_image[0][k] = ImageTk.PhotoImage(pil_image_resized[0][k])
                        #     print(tk_image)
                        #     LP[0][k] = Label(p1, image=tk_image[0][k], height=w_box, width=h_box)
                        #     p6.add(LP[0][k])
                        #     k += 1
                        # else:
                        response = request.urlopen(i)
                        cat_img = response.read()
                        with open('C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(0) + '.jpg', 'wb') as f:
                            f.write(cat_img)
                            f.close()
                        pil_image[0][k] = Image.open(
                            r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(0) + '.jpg')
                        w, h = pil_image[0][k].size
                        pil_image_resized[0][k] = resize(w, h, w_box, h_box, pil_image[0][k])
                        tk_image[0][k] = ImageTk.PhotoImage(pil_image_resized[0][k])
                        print(tk_image)
                        LP[0][k] = Label(p1, image=tk_image[0][k], height=w_box, width=h_box)
                        p6.add(LP[0][k])
                        k += 1
                g_yingyongtupian[0] = tk_image[0][5:]
                g_yingyongming[0] = result_yingyongming[0][5:]
                k = 0
                for i in result_yingyongtupian[1]:
                    if (k > 4):
                        # if (os.path.exists(r'C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(1) + '.jpg')):
                        #     pil_image[1][k] = Image.open(
                        #         r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(1) + '.jpg')
                        #     w, h = pil_image[1][k].size
                        #     pil_image_resized[1][k] = resize(w, h, w_box, h_box, pil_image[1][k])
                        #     tk_image[1][k] = ImageTk.PhotoImage(pil_image_resized[1][k])
                        #     print(tk_image)
                        #     k += 1
                        # else:
                        response = request.urlopen(i)
                        cat_img = response.read()
                        with open('C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(1) + '.jpg', 'wb') as f:
                            f.write(cat_img)
                            f.close()
                        pil_image[1][k] = Image.open(
                            r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(1) + '.jpg')
                        w, h = pil_image[1][k].size
                        pil_image_resized[1][k] = resize(w, h, w_box, h_box, pil_image[1][k])
                        tk_image[1][k] = ImageTk.PhotoImage(pil_image_resized[1][k])
                        print(tk_image)
                        k += 1
                    else:
                        # if (os.path.exists(r'C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(1) + '.jpg')):
                        #     pil_image[1][k] = Image.open(
                        #         r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(1) + '.jpg')
                        #     w, h = pil_image[1][k].size
                        #     pil_image_resized[1][k] = resize(w, h, w_box, h_box, pil_image[1][k])
                        #     tk_image[1][k] = ImageTk.PhotoImage(pil_image_resized[1][k])
                        #     print(tk_image)
                        #     LP[1][k] = Label(p1, image=tk_image[1][k], height=w_box, width=h_box)
                        #     p9.add(LP[1][k])
                        #     k += 1
                        # else:
                        response = request.urlopen(i)
                        cat_img = response.read()
                        with open('C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(1) + '.jpg', 'wb') as f:
                            f.write(cat_img)
                            f.close()
                        pil_image[1][k] = Image.open(
                            r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(1) + '.jpg')
                        w, h = pil_image[1][k].size
                        pil_image_resized[1][k] = resize(w, h, w_box, h_box, pil_image[1][k])
                        tk_image[1][k] = ImageTk.PhotoImage(pil_image_resized[1][k])
                        print(tk_image)
                        LP[1][k] = Label(p1, image=tk_image[1][k], height=w_box, width=h_box)
                        p9.add(LP[1][k])
                        k += 1
                g_yingyongtupian[1] = tk_image[1][5:]
                g_yingyongming[1] = result_yingyongming[1][5:]
                k = 0
                for i in result_yingyongtupian[2]:
                    if (k > 4):
                        # if (os.path.exists(r'C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(2) + '.jpg')):
                        #     pil_image[2][k] = Image.open(
                        #         r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(2) + '.jpg')
                        #     w, h = pil_image[2][k].size
                        #     pil_image_resized[2][k] = resize(w, h, w_box, h_box, pil_image[2][k])
                        #     tk_image[2][k] = ImageTk.PhotoImage(pil_image_resized[2][k])
                        #     print(tk_image)
                        #     k += 1
                        # else:
                        response = request.urlopen(i)
                        cat_img = response.read()
                        with open('C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(2) + '.jpg', 'wb') as f:
                            f.write(cat_img)
                            f.close()
                        pil_image[2][k] = Image.open(
                            r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(2) + '.jpg')
                        w, h = pil_image[2][k].size
                        pil_image_resized[2][k] = resize(w, h, w_box, h_box, pil_image[2][k])
                        tk_image[2][k] = ImageTk.PhotoImage(pil_image_resized[2][k])
                        print(tk_image)
                        k += 1
                    else:
                        # if (os.path.exists(r'C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(2) + '.jpg')):
                        #     pil_image[2][k] = Image.open(
                        #         r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(2) + '.jpg')
                        #     w, h = pil_image[2][k].size
                        #     pil_image_resized[2][k] = resize(w, h, w_box, h_box, pil_image[2][k])
                        #     tk_image[2][k] = ImageTk.PhotoImage(pil_image_resized[2][k])
                        #     print(tk_image)
                        #     LP[2][k] = Label(p1, image=tk_image[2][k], height=w_box, width=h_box)
                        #     p12.add(LP[2][k])
                        #     k += 1
                        # else:
                        response = request.urlopen(i)
                        cat_img = response.read()
                        with open('C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(2) + '.jpg', 'wb') as f:
                            f.write(cat_img)
                            f.close()
                        pil_image[2][k] = Image.open(
                            r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(2) + '.jpg')
                        w, h = pil_image[2][k].size
                        pil_image_resized[2][k] = resize(w, h, w_box, h_box, pil_image[2][k])
                        tk_image[2][k] = ImageTk.PhotoImage(pil_image_resized[2][k])
                        print(tk_image)
                        LP[2][k] = Label(p1, image=tk_image[2][k], height=w_box, width=h_box)
                        p12.add(LP[2][k])
                        k += 1
                g_yingyongtupian[2] = tk_image[2][5:]
                g_yingyongming[2] = result_yingyongming[2][5:]
                k = 0
                for i in result_yingyongtupian[3]:
                    if (k > 4):
                        # if (os.path.exists(r'C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(3) + '.jpg')):
                        #     pil_image[3][k] = Image.open(
                        #         r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(3) + '.jpg')
                        #     w, h = pil_image[3][k].size
                        #     pil_image_resized[3][k] = resize(w, h, w_box, h_box, pil_image[3][k])
                        #     tk_image[3][k] = ImageTk.PhotoImage(pil_image_resized[3][k])
                        #     print(tk_image)
                        #     k += 1
                        # else:
                        response = request.urlopen(i)
                        cat_img = response.read()
                        with open('C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(3) + '.jpg', 'wb') as f:
                            f.write(cat_img)
                            f.close()
                        pil_image[3][k] = Image.open(
                            r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(3) + '.jpg')
                        w, h = pil_image[3][k].size
                        pil_image_resized[3][k] = resize(w, h, w_box, h_box, pil_image[3][k])
                        tk_image[3][k] = ImageTk.PhotoImage(pil_image_resized[3][k])
                        print(tk_image)
                        k += 1
                    else:
                        # if (os.path.exists(r'C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(3) + '.jpg')):
                        #     pil_image[3][k] = Image.open(
                        #         r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(3) + '.jpg')
                        #     w, h = pil_image[3][k].size
                        #     pil_image_resized[3][k] = resize(w, h, w_box, h_box, pil_image[3][k])
                        #     tk_image[3][k] = ImageTk.PhotoImage(pil_image_resized[3][k])
                        #     print(tk_image)
                        #     LP[3][k] = Label(p1, image=tk_image[3][k], height=w_box, width=h_box)
                        #     p15.add(LP[3][k])
                        #     k += 1
                        # else:
                        response = request.urlopen(i)
                        cat_img = response.read()
                        with open('C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(3) + '.jpg', 'wb') as f:
                            f.write(cat_img)
                            f.close()
                        pil_image[3][k] = Image.open(
                            r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(3) + '.jpg')
                        w, h = pil_image[3][k].size
                        pil_image_resized[3][k] = resize(w, h, w_box, h_box, pil_image[3][k])
                        tk_image[3][k] = ImageTk.PhotoImage(pil_image_resized[3][k])
                        print(tk_image)
                        LP[3][k] = Label(p1, image=tk_image[3][k], height=w_box, width=h_box)
                        p15.add(LP[3][k])
                        k += 1
                g_yingyongtupian[3] = tk_image[3][5:]
                g_yingyongming[3] = result_yingyongming[3][5:]
            elif (contral_num == 3):
                k = 0
                for i in result_yingyongtupian[0]:
                    if (k > 4):
                        # if (os.path.exists(r'C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(0) + '.jpg')):
                        #     pil_image[0][k] = Image.open(
                        #         r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(0) + '.jpg')
                        #     w, h = pil_image[0][k].size
                        #     pil_image_resized[0][k] = resize(w, h, w_box, h_box, pil_image[0][k])
                        #     tk_image[0][k] = ImageTk.PhotoImage(pil_image_resized[0][k])
                        #     print(tk_image)
                        #     k += 1
                        # else:
                        response = request.urlopen(i)
                        res.keep_alive = False
                        cat_img = response.read()
                        with open('C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(0) + '.jpg', 'wb') as f:
                            f.write(cat_img)
                            f.close()
                        pil_image[0][k] = Image.open(
                            r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(0) + '.jpg')
                        w, h = pil_image[0][k].size
                        pil_image_resized[0][k] = resize(w, h, w_box, h_box, pil_image[0][k])
                        tk_image[0][k] = ImageTk.PhotoImage(pil_image_resized[0][k])
                        print(tk_image)
                        k += 1
                    else:
                        # if (os.path.exists(r'C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(0) + '.jpg')):
                        #     pil_image[0][k] = Image.open(
                        #         r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(0) + '.jpg')
                        #     w, h = pil_image[0][k].size
                        #     pil_image_resized[0][k] = resize(w, h, w_box, h_box, pil_image[0][k])
                        #     tk_image[0][k] = ImageTk.PhotoImage(pil_image_resized[0][k])
                        #     print(tk_image)
                        #     LP[0][k] = Label(p1, image=tk_image[0][k], height=w_box, width=h_box)
                        #     p6.add(LP[0][k])
                        #     k += 1
                        # else:
                        response = request.urlopen(i)
                        cat_img = response.read()
                        with open('C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(0) + '.jpg', 'wb') as f:
                            f.write(cat_img)
                            f.close()
                        pil_image[0][k] = Image.open(
                            r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(0) + '.jpg')
                        w, h = pil_image[0][k].size
                        pil_image_resized[0][k] = resize(w, h, w_box, h_box, pil_image[0][k])
                        tk_image[0][k] = ImageTk.PhotoImage(pil_image_resized[0][k])
                        print(tk_image)
                        LP[0][k] = Label(p1, image=tk_image[0][k], height=w_box, width=h_box)
                        p6.add(LP[0][k])
                        k += 1
                g_yingyongtupian[0] = tk_image[0][5:]
                g_yingyongming[0] = result_yingyongming[0][5:]
                k = 0
                for i in result_yingyongtupian[1]:
                    if (k > 4):
                    #     if (os.path.exists(r'C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(1) + '.jpg')):
                    #         pil_image[1][k] = Image.open(
                    #             r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(1) + '.jpg')
                    #         w, h = pil_image[1][k].size
                    #         pil_image_resized[1][k] = resize(w, h, w_box, h_box, pil_image[1][k])
                    #         tk_image[1][k] = ImageTk.PhotoImage(pil_image_resized[1][k])
                    #         print(tk_image)
                    #         k += 1
                    #     else:
                        response = request.urlopen(i)
                        cat_img = response.read()
                        with open('C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(1) + '.jpg', 'wb') as f:
                            f.write(cat_img)
                            f.close()
                        pil_image[1][k] = Image.open(
                            r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(1) + '.jpg')
                        w, h = pil_image[1][k].size
                        pil_image_resized[1][k] = resize(w, h, w_box, h_box, pil_image[1][k])
                        tk_image[1][k] = ImageTk.PhotoImage(pil_image_resized[1][k])
                        print(tk_image)
                        k += 1
                    else:
                        response = request.urlopen(i)
                        cat_img = response.read()
                        with open('C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(1) + '.jpg', 'wb') as f:
                            f.write(cat_img)
                            f.close()
                        pil_image[1][k] = Image.open(
                            r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(1) + '.jpg')
                        w, h = pil_image[1][k].size
                        pil_image_resized[1][k] = resize(w, h, w_box, h_box, pil_image[1][k])
                        tk_image[1][k] = ImageTk.PhotoImage(pil_image_resized[1][k])
                        print(tk_image)
                        LP[1][k] = Label(p1, image=tk_image[1][k], height=w_box, width=h_box)
                        p9.add(LP[1][k])
                        k += 1
                    # if (os.path.exists(r'C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(1) + '.jpg')):
                    #     pil_image[1][k] = Image.open(
                    #         r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(1) + '.jpg')
                    #     w, h = pil_image[1][k].size
                    #     pil_image_resized[1][k] = resize(w, h, w_box, h_box, pil_image[1][k])
                    #     tk_image[1][k] = ImageTk.PhotoImage(pil_image_resized[1][k])
                    #     print(tk_image)
                    #     LP[1][k] = Label(p1, image=tk_image[1][k], height=w_box, width=h_box)
                    #     p9.add(LP[1][k])
                    #     k += 1
                    # else:

                g_yingyongtupian[1] = tk_image[1][5:]
                g_yingyongming[1] = result_yingyongming[1][5:]
                k = 0
                for i in result_yingyongtupian[2]:
                    if (k > 4):
                        # if (os.path.exists(r'C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(2) + '.jpg')):
                        #     pil_image[2][k] = Image.open(
                        #         r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(2) + '.jpg')
                        #     w, h = pil_image[2][k].size
                        #     pil_image_resized[2][k] = resize(w, h, w_box, h_box, pil_image[2][k])
                        #     tk_image[2][k] = ImageTk.PhotoImage(pil_image_resized[2][k])
                        #     print(tk_image)
                        #     k += 1
                        # else:
                        response = request.urlopen(i)
                        cat_img = response.read()
                        with open('C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(2) + '.jpg', 'wb') as f:
                            f.write(cat_img)
                            f.close()
                        pil_image[2][k] = Image.open(
                            r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(2) + '.jpg')
                        w, h = pil_image[2][k].size
                        pil_image_resized[2][k] = resize(w, h, w_box, h_box, pil_image[2][k])
                        tk_image[2][k] = ImageTk.PhotoImage(pil_image_resized[2][k])
                        print(tk_image)
                        k += 1
                    else:
                        # if (os.path.exists(r'C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(2) + '.jpg')):
                        #     pil_image[2][k] = Image.open(
                        #         r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(2) + '.jpg')
                        #     w, h = pil_image[2][k].size
                        #     pil_image_resized[2][k] = resize(w, h, w_box, h_box, pil_image[2][k])
                        #     tk_image[2][k] = ImageTk.PhotoImage(pil_image_resized[2][k])
                        #     print(tk_image)
                        #     LP[2][k] = Label(p1, image=tk_image[2][k], height=w_box, width=h_box)
                        #     p12.add(LP[2][k])
                        #     k += 1
                        # else:
                        response = request.urlopen(i)
                        cat_img = response.read()
                        with open('C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(2) + '.jpg', 'wb') as f:
                            f.write(cat_img)
                            f.close()
                        pil_image[2][k] = Image.open(
                            r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(2) + '.jpg')
                        w, h = pil_image[2][k].size
                        pil_image_resized[2][k] = resize(w, h, w_box, h_box, pil_image[2][k])
                        tk_image[2][k] = ImageTk.PhotoImage(pil_image_resized[2][k])
                        print(tk_image)
                        LP[2][k] = Label(p1, image=tk_image[2][k], height=w_box, width=h_box)
                        p12.add(LP[2][k])
                        k += 1
                g_yingyongtupian[2] = tk_image[2][5:]
                g_yingyongming[2] = result_yingyongming[2][5:]
            elif (contral_num == 2):
                k = 0
                for i in result_yingyongtupian[0]:
                    if (k > 4):
                        # if (os.path.exists(r'C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(0) + '.jpg')):
                        #     pil_image[0][k] = Image.open(
                        #         r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(0) + '.jpg')
                        #     w, h = pil_image[0][k].size
                        #     pil_image_resized[0][k] = resize(w, h, w_box, h_box, pil_image[0][k])
                        #     tk_image[0][k] = ImageTk.PhotoImage(pil_image_resized[0][k])
                        #     print(tk_image)
                        #     k += 1
                        # else:
                        response = request.urlopen(i)
                        res.keep_alive = False
                        cat_img = response.read()
                        with open('C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(0) + '.jpg', 'wb') as f:
                            f.write(cat_img)
                            f.close()
                        pil_image[0][k] = Image.open(
                            r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(0) + '.jpg')
                        w, h = pil_image[0][k].size
                        pil_image_resized[0][k] = resize(w, h, w_box, h_box, pil_image[0][k])
                        tk_image[0][k] = ImageTk.PhotoImage(pil_image_resized[0][k])
                        print(tk_image)
                        k += 1
                    else:
                        # if (os.path.exists(r'C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(0) + '.jpg')):
                        #     pil_image[0][k] = Image.open(
                        #         r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(0) + '.jpg')
                        #     w, h = pil_image[0][k].size
                        #     pil_image_resized[0][k] = resize(w, h, w_box, h_box, pil_image[0][k])
                        #     tk_image[0][k] = ImageTk.PhotoImage(pil_image_resized[0][k])
                        #     print(tk_image)
                        #     LP[0][k] = Label(p1, image=tk_image[0][k], height=w_box, width=h_box)
                        #     p6.add(LP[0][k])
                        #     k += 1
                        # else:
                        response = request.urlopen(i)
                        cat_img = response.read()
                        with open('C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(0) + '.jpg', 'wb') as f:
                            f.write(cat_img)
                            f.close()
                        pil_image[0][k] = Image.open(
                            r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(0) + '.jpg')
                        w, h = pil_image[0][k].size
                        pil_image_resized[0][k] = resize(w, h, w_box, h_box, pil_image[0][k])
                        tk_image[0][k] = ImageTk.PhotoImage(pil_image_resized[0][k])
                        print(tk_image)
                        LP[0][k] = Label(p1, image=tk_image[0][k], height=w_box, width=h_box)
                        p6.add(LP[0][k])
                        k += 1
                g_yingyongtupian[0] = tk_image[0][5:]
                g_yingyongming[0] = result_yingyongming[0][5:]
                k = 0
                for i in result_yingyongtupian[1]:
                    if (k > 4):
                        # if (os.path.exists(r'C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(1) + '.jpg')):
                        #     pil_image[1][k] = Image.open(
                        #         r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(1) + '.jpg')
                        #     w, h = pil_image[1][k].size
                        #     pil_image_resized[1][k] = resize(w, h, w_box, h_box, pil_image[1][k])
                        #     tk_image[1][k] = ImageTk.PhotoImage(pil_image_resized[1][k])
                        #     print(tk_image)
                        #     k += 1
                        # else:
                        response = request.urlopen(i)
                        cat_img = response.read()
                        with open('C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(1) + '.jpg', 'wb') as f:
                            f.write(cat_img)
                            f.close()
                        pil_image[1][k] = Image.open(
                            r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(1) + '.jpg')
                        w, h = pil_image[1][k].size
                        pil_image_resized[1][k] = resize(w, h, w_box, h_box, pil_image[1][k])
                        tk_image[1][k] = ImageTk.PhotoImage(pil_image_resized[1][k])
                        print(tk_image)
                        k += 1
                    else:
                        # if (os.path.exists(r'C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(1) + '.jpg')):
                        #     pil_image[1][k] = Image.open(
                        #         r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(1) + '.jpg')
                        #     w, h = pil_image[1][k].size
                        #     pil_image_resized[1][k] = resize(w, h, w_box, h_box, pil_image[1][k])
                        #     tk_image[1][k] = ImageTk.PhotoImage(pil_image_resized[1][k])
                        #     print(tk_image)
                        #     LP[1][k] = Label(p1, image=tk_image[1][k], height=w_box, width=h_box)
                        #     p9.add(LP[1][k])
                        #     k += 1
                        # else:
                        response = request.urlopen(i)
                        cat_img = response.read()
                        with open('C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(1) + '.jpg', 'wb') as f:
                            f.write(cat_img)
                            f.close()
                        pil_image[1][k] = Image.open(
                            r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(1) + '.jpg')
                        w, h = pil_image[1][k].size
                        pil_image_resized[1][k] = resize(w, h, w_box, h_box, pil_image[1][k])
                        tk_image[1][k] = ImageTk.PhotoImage(pil_image_resized[1][k])
                        print(tk_image)
                        LP[1][k] = Label(p1, image=tk_image[1][k], height=w_box, width=h_box)
                        p9.add(LP[1][k])
                        k += 1
                g_yingyongtupian[1] = tk_image[1][5:]
                g_yingyongming[1] = result_yingyongming[1][5:]
                room.mainloop()
            elif (contral_num == 1):
                k = 0
                for i in result_yingyongtupian[0]:
                    if (k > 4):
                        # if (os.path.exists(r'C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(0) + '.jpg')):
                        #     pil_image[0][k] = Image.open(
                        #         r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(0) + '.jpg')
                        #     w, h = pil_image[0][k].size
                        #     pil_image_resized[0][k] = resize(w, h, w_box, h_box, pil_image[0][k])
                        #     tk_image[0][k] = ImageTk.PhotoImage(pil_image_resized[0][k])
                        #     print(tk_image)
                        #     k += 1
                        # else:
                        response = request.urlopen(i)
                        res.keep_alive = False
                        cat_img = response.read()
                        with open('C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(0) + '.jpg', 'wb') as f:
                            f.write(cat_img)
                            f.close()
                        pil_image[0][k] = Image.open(
                            r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(0) + '.jpg')
                        w, h = pil_image[0][k].size
                        pil_image_resized[0][k] = resize(w, h, w_box, h_box, pil_image[0][k])
                        tk_image[0][k] = ImageTk.PhotoImage(pil_image_resized[0][k])
                        print(tk_image)
                        k += 1
                    else:
                        # if (os.path.exists(r'C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(0) + '.jpg')):
                        #     pil_image[0][k] = Image.open(
                        #         r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(0) + '.jpg')
                        #     w, h = pil_image[0][k].size
                        #     pil_image_resized[0][k] = resize(w, h, w_box, h_box, pil_image[0][k])
                        #     tk_image[0][k] = ImageTk.PhotoImage(pil_image_resized[0][k])
                        #     print(tk_image)
                        #     LP[0][k] = Label(p1, image=tk_image[0][k], height=w_box, width=h_box)
                        #     p6.add(LP[0][k])
                        #     k += 1
                        # else:
                        response = request.urlopen(i)
                        cat_img = response.read()
                        with open('C:\\Users\\jaska\\Desktop\\cat_500_6' + str(k) + str(0) + '.jpg', 'wb') as f:
                            f.write(cat_img)
                            f.close()
                        pil_image[0][k] = Image.open(
                            r'C:\Users\jaska\Desktop\cat_500_6' + str(k) + str(0) + '.jpg')
                        w, h = pil_image[0][k].size
                        pil_image_resized[0][k] = resize(w, h, w_box, h_box, pil_image[0][k])
                        tk_image[0][k] = ImageTk.PhotoImage(pil_image_resized[0][k])
                        print(tk_image)
                        LP[0][k] = Label(p1, image=tk_image[0][k], height=w_box, width=h_box)
                        p6.add(LP[0][k])
                        k += 1
                g_yingyongtupian[0] = tk_image[0][5:]
                g_yingyongming[0] = result_yingyongming[0][5:]
            room.mainloop()

        Label_()
        Button_(contral_num)
        Photo_(contral_num)

    def start(self):

        def show1():
            print(self.biaoshi)
            self.qianduan()

        def show2():
            self.Bcak_contral()

        root = tkinter.Tk("200x200")
        b1 = tkinter.Button(root, text='前端', command=show1, width=50, height=5)
        b1.pack()
        b2 = tkinter.Button(root, text='后端', command=show2, width=50, height=5)
        b2.pack()
        root.mainloop()

show()
