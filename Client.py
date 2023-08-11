import requests
import tkinter.messagebox
import tkinter as tk
# # 定义请求的 URL
# url = 'http://127.0.0.1:5000/connection_test'

# # 定义要上传的数据，这里使用一个简单的 JSON 格式数据
# data = {
#     'name': 'value',
#     'a':1,
#     'b':0,
#     'c':1,
#     }

# # 发送请求
# response = requests.post(
#     'http://127.0.0.1:5000/upload_infomation', 
#     json=data
#     )
# # response = requests.get(url)

# # 打印响应内容
# print(response.text)

MAX_TIMEOUT = 1 # 最大超时时间(s)

CONNECTED = 0
DISCONNECTED = 1


class Client():
    def __init__(self):
        self.version = 'v1.0.0-alpha'
        
        self.window = tk.Tk()
        self.window.title(f"大学新生报到材料辅助收集系统客户端 {self.version}")
        self.window.geometry("420x600")  # 设置窗口初始大小
        self.window.resizable(False, False)  # 设置窗口不可改变大小
        
        self.connect_state = DISCONNECTED
        
        self.server_host = '127.0.0.1'
        self.server_host_n1 = tk.IntVar()
        self.server_host_n1.set(127)
        self.server_host_n2 = tk.IntVar()
        self.server_host_n2.set(0)
        self.server_host_n3 = tk.IntVar()
        self.server_host_n3.set(0)
        self.server_host_n4 = tk.IntVar()
        self.server_host_n4.set(1)
        self.server_port = 5000
        self.server_port_n = tk.IntVar()
        self.server_port_n.set(5000)
        
        self.choice_list = []
        
        self.CreateWidgets()
    
    
    def CreateWidgets(self):
        self.Frame_ServerInfomation = tk.LabelFrame(
            self.window,
            text="服务器信息",
            font=('微软雅黑',10),
            bd=2,
            relief="groove",
            )
        self.Frame_ServerInfomation.place(x=10, y=5, width=260, height=80)
        self.CreateWidgets_Frame_ServerInfomation()
        
        self.Frame_ConnectionTest = tk.LabelFrame(
            self.window,
            text="连接状态",
            font=('微软雅黑',10),
            bd=2,
            relief="groove",
            )
        self.Frame_ConnectionTest.place(x=270, y=5, width=140, height=80)
        self.CreateWidgets_Frame_ConnectionTest()
        
        self.Frame_OperationBar = tk.LabelFrame(
            self.window,
            text="操作栏",
            font=('微软雅黑',10),
            bd=2,
            relief="groove",
            )
        self.Frame_OperationBar.place(x=10, y=90, width=120, height=200)
        self.CreateWidgets_Frame_OperationBar()
        
        self.Frame_UploadInfomation = tk.LabelFrame(
            self.window,
            text="上传信息",
            font=('微软雅黑',10),
            bd=2,
            relief="groove",
            )
        self.Frame_UploadInfomation.place(x=140, y=90, width=270, height=500)
        self.CreateWidgets_Frame_UploadInfomation()


    def CreateWidgets_Frame_UploadInfomation(self):
        widget_width = 0
        widget_height = 20
        proportion = 1.1
        
        
        
        self.LabelPrompt_Name = tk.Label(#姓名提示
            self.Frame_UploadInfomation,
            text='姓名：',
            font=('微软雅黑',10),
            anchor='w',
            )
        self.LabelPrompt_Name.place(x=5, y=int(0*widget_height*proportion), width=100, height=widget_height)
        
        self.Entry_Name = tk.Entry(#姓名输入框
            self.Frame_UploadInfomation,
            font=('微软雅黑',10),
            )
        self.Entry_Name.place(x=70, y=int(0*widget_height*proportion), width=190, height=widget_height)
        
        self.LabelPrompt_IDNumber = tk.Label(#身份证提示
            self.Frame_UploadInfomation,
            text='身份证号：',
            font=('微软雅黑',10),
            anchor='w',
            )
        self.LabelPrompt_IDNumber.place(x=5, y=int(1*widget_height*proportion), width=100, height=widget_height)

        self.Entry_IDNumber = tk.Entry(#身份证输入框
            self.Frame_UploadInfomation,
            font=('微软雅黑',10),
            )
        self.Entry_IDNumber.place(x=70, y=int(1*widget_height*proportion), width=190, height=widget_height)

        self.LabelPrompt_StudentNumber = tk.Label(#学号提示
            self.Frame_UploadInfomation,
            text='学号：',
            font=('微软雅黑',10),
            anchor='w',
            )
        self.LabelPrompt_StudentNumber.place(x=5, y=int(2*widget_height*proportion), width=100, height=widget_height)

        self.Entry_StudentNumber = tk.Entry(#学号输入框
            self.Frame_UploadInfomation,
            font=('微软雅黑',10),
            )
        self.Entry_StudentNumber.place(x=70, y=int(2*widget_height*proportion), width=190, height=widget_height)

        #生成选择框
        for i in range(15):
            checkbox_pair = [
                tk.IntVar(),
                tk.Checkbutton(
                    self.Frame_UploadInfomation, 
                    text="",
                    font=('微软雅黑',12),
                    anchor='w',
                    )
                ]
            self.choice_list.append(checkbox_pair)
            self.choice_list[i][1].configure(variable=self.choice_list[i][0])
            self.choice_list[i][1].configure(state='disabled')
            self.choice_list[i][0].set(0)
            self.choice_list[i][1].place(
                x=5, 
                y=int((3+i)*26), 
                width=100, 
                height=30
                )


    def CreateWidgets_Frame_OperationBar(self):
        button_width = 105
        button_height = 30
        self.Button_UpdateNeedfulUploadInfomation = tk.Button(#更新需要上传的提交材料的信息按钮
            self.Frame_OperationBar,
            text='更新需求信息',
            font=('微软雅黑',10),
            command=self.Button_UpdateNeedfulUploadInfomation_Click,
            )
        self.Button_UpdateNeedfulUploadInfomation.place(x=5, y=0, width=button_width, height=button_height)
        
        self.Button_UploadInfomation = tk.Button(#上传的提交材料的信息的按钮
            self.Frame_OperationBar,
            text='上传到服务器',
            font=('微软雅黑',10),
            command=self.Button_UploadInfomation_Click,
            )
        self.Button_UploadInfomation.place(x=5, y=70, width=button_width, height=button_height)
        
        
    def CreateWidgets_Frame_ServerInfomation(self):
        self.LabelPrompt_ServerHost = tk.Label(#服务器IP地址提示
            self.Frame_ServerInfomation,
            text='服务器IP地址：',
            font=('微软雅黑',10),
            anchor='w',
            )
        self.LabelPrompt_ServerHost.place(x=5, y=0, width=100, height=20)
        
        self.Entry_ServerHost_n1 = tk.Entry(#服务器IP地址第1部分
            self.Frame_ServerInfomation,
            textvariable=self.server_host_n1,
            font=('微软雅黑',10),
            justify='center',
            )
        self.Entry_ServerHost_n1.place(x=100, y=0, width=30, height=20)
        self.Entry_ServerHost_n1.bind('<MouseWheel>', self.Entry_ServerHost_n1_MouseWheel)
        
        self.Entry_ServerHost_n2 = tk.Entry(#服务器IP地址第2部分
            self.Frame_ServerInfomation,
            textvariable=self.server_host_n2,
            font=('微软雅黑',10),
            justify='center',
            )
        self.Entry_ServerHost_n2.place(x=140, y=0, width=30, height=20)
        self.Entry_ServerHost_n2.bind('<MouseWheel>', self.Entry_ServerHost_n2_MouseWheel)
        
        self.Entry_ServerHost_n3 = tk.Entry(#服务器IP地址第3部分
            self.Frame_ServerInfomation,
            textvariable=self.server_host_n3,
            font=('微软雅黑',10),
            justify='center',
            )
        self.Entry_ServerHost_n3.place(x=180, y=0, width=30, height=20)
        self.Entry_ServerHost_n3.bind('<MouseWheel>', self.Entry_ServerHost_n3_MouseWheel)
        
        self.Entry_ServerHost_n4 = tk.Entry(#服务器IP地址第4部分
            self.Frame_ServerInfomation,
            textvariable=self.server_host_n4,
            font=('微软雅黑',10),
            justify='center',
            )
        self.Entry_ServerHost_n4.place(x=220, y=0, width=30, height=20)
        self.Entry_ServerHost_n4.bind('<MouseWheel>', self.Entry_ServerHost_n4_MouseWheel)
        
        self.LabelPrompt_ServerPort = tk.Label(#服务器端口提示
            self.Frame_ServerInfomation,
            text='服务器端口：',
            font=('微软雅黑',10),
            anchor='w',
            )
        self.LabelPrompt_ServerPort.place(x=5, y=25, width=100, height=20)
        
        self.Entry_ServerPort = tk.Entry(#服务器端口
            self.Frame_ServerInfomation,
            textvariable=self.server_port_n,
            font=('微软雅黑',10),
            justify='center',
            )
        self.Entry_ServerPort.place(x=100, y=25, width=70, height=20)
        self.Entry_ServerPort.bind('<MouseWheel>', self.Entry_ServerPort_MouseWheel)
        
        
    def CreateWidgets_Frame_ConnectionTest(self):
        self.Label_ConnectionTestSignal = tk.Label(#用于显示是否连接到服务器的信号灯
            self.Frame_ConnectionTest,
            background="red",
            )
        self.Label_ConnectionTestSignal.place(x=5, y=0, width=20, height=20)
        
        self.Label_ConnectionTest = tk.Label(#显示是否连接到服务器的文字
            self.Frame_ConnectionTest,
            text='未连接到服务器',
            font=('微软雅黑',10),
            anchor='w',
            )
        self.Label_ConnectionTest.place(x=30, y=0, width=95, height=20)
        
        self.Button_ConnectToServer = tk.Button(#用于连接到服务器的按钮
            self.Frame_ConnectionTest,
            text='连接服务器',
            font=('微软雅黑',10),
            command=self.Button_ConnectToServer_Click,
            )
        self.Button_ConnectToServer.place(x=5, y=25, width=90, height=26)
    
    
    def Button_UploadInfomation_Click(self):
        '''TODO : 添加将提交的材料信息打包成json格式的代码'''
        if self.connect_state == CONNECTED:
            json_data = {
                '姓名':self.Entry_Name.get(),
                '身份证号':self.Entry_IDNumber.get(),
                '学号':self.Entry_StudentNumber.get(),
            }
            for i,pair in enumerate(self.choice_list):
                checkbox_state = pair[1].cget("state")
                if checkbox_state == 'normal':
                    info_name = pair[1].cget("text")
                    json_data[info_name] = str(pair[0].get())
                elif checkbox_state == 'disbled':
                    pass
            try:
                response = requests.post(
                    f'http://{self.server_host}:{self.server_port}/upload_infomation',
                    timeout=MAX_TIMEOUT,
                    json=json_data
                    )
                if response.status_code==200:
                    tkinter.messagebox.showinfo('提示','信息上传成功！')
                else:
                    tkinter.messagebox.showerror('错误','信息上传失败！')
            except:
                self.Button_ConnectToServer_Click()
                tkinter.messagebox.showerror('错误','信息上传失败！')
                
        elif self.connect_state == DISCONNECTED:
            tkinter.messagebox.showerror('错误','未连接到服务器')
        
        
    def Button_UpdateNeedfulUploadInfomation_Click(self):
        '''当更新需要提交的材料类型的按钮点击时执行'''
        if self.connect_state == CONNECTED:
            response = requests.get(
                f'http://{self.server_host}:{self.server_port}/get_needful_upload_infomation',
                timeout=MAX_TIMEOUT
                )
            needful_info = response.json()
            for i,pair in enumerate(self.choice_list):
                info_text = needful_info.get(f"info{i}",None)
                if info_text == None:
                    pair[1].configure(text='')
                    pair[1].configure(state='disabled')
                else:
                    pair[1].configure(text=info_text)
                    pair[1].configure(state='normal')
        elif self.connect_state == DISCONNECTED:
            tkinter.messagebox.showerror('错误','未连接到服务器')
        
        
    def Entry_ServerPort_MouseWheel(self, event):
        self.server_port_n.set(self.server_port_n.get() + event.delta//120)
    
    
    def Entry_ServerHost_n1_MouseWheel(self, event):
        self.server_host_n1.set(self.server_host_n1.get() + event.delta//120)
        if self.server_host_n1.get() > 255:
            self.server_host_n1.set(255)
        elif self.server_host_n1.get()< 0:
            self.server_host_n1.set(0)
            
        
    def Entry_ServerHost_n1_Change(self, *args):
        '''DEPRECATED(小企鹅)'''
        raise RuntimeError('该方法已弃用')
        try:
            if self.server_host_n1.get() > 255:
                self.server_host_n1.set(255)
            elif self.server_host_n1.get()< 0:
                self.server_host_n1.set(0)
        except:
            pass
    
    def Entry_ServerHost_n2_MouseWheel(self, event):
        self.server_host_n2.set(self.server_host_n2.get() + event.delta//120)
        if self.server_host_n2.get() > 255:
            self.server_host_n2.set(255)
        elif self.server_host_n2.get()< 0:
            self.server_host_n2.set(0)
                
        
    def Entry_ServerHost_n2_Change(self, *args):
        '''DEPRECATED(小企鹅)'''
        raise RuntimeError('该方法已弃用')
        try:
            if self.server_host_n2.get() > 255:
                self.server_host_n2.set(255)
            elif self.server_host_n2.get()< 0:
                self.server_host_n2.set(0)
        except:
            pass
    
    
    def Entry_ServerHost_n3_MouseWheel(self, event):
        self.server_host_n3.set(self.server_host_n3.get() + event.delta//120)
        if self.server_host_n3.get() > 255:
            self.server_host_n3.set(255)
        elif self.server_host_n3.get()< 0:
            self.server_host_n3.set(0)
        
        
    def Entry_ServerHost_n3_Change(self, *args):
        '''DEPRECATED(小企鹅)'''
        raise RuntimeError('该方法已弃用')
        try:
            if self.server_host_n3.get() > 255:
                self.server_host_n3.set(255)
            elif self.server_host_n3.get()< 0:
                self.server_host_n3.set(0)
        except:
            pass
        
        
    def Entry_ServerHost_n4_MouseWheel(self, event):
        self.server_host_n4.set(self.server_host_n4.get() + event.delta//120)
        if self.server_host_n4.get() > 255:
            self.server_host_n4.set(255)
        elif self.server_host_n4.get() < 0:
            self.server_host_n4.set(0)
        
        
    def Entry_ServerHost_n4_Change(self, *args):
        '''DEPRECATED(小企鹅)'''
        raise RuntimeError('该方法已弃用')
        try:
            print(self.server_host_n4.get())
            if self.server_host_n4.get() > 255:
                self.server_host_n4.set(255)
            elif self.server_host_n4.get() < 0:
                self.server_host_n4.set(0)
        except:
            pass
        
    
    def Button_ConnectToServer_Click(self):
        try:
            response = requests.get(
                f'http://{self.server_host}:{self.server_port}/connection_test',
                timeout=MAX_TIMEOUT
                )
            if response.status_code==200:
                if response.text=='connected':
                    self.connect_state = CONNECTED
            else:
                self.connect_state = DISCONNECTED
        except:
            self.connect_state = DISCONNECTED
        self.SetConnectState()
    
    
    def SetConnectState(self):
        if self.connect_state == CONNECTED:
            self.Label_ConnectionTestSignal['background'] = 'green'
            self.Label_ConnectionTest['text'] = '已连接到服务器'
        elif self.connect_state == DISCONNECTED:
            self.Label_ConnectionTestSignal['background'] = 'red'
            self.Label_ConnectionTest['text'] = '未连接到服务器'
    
    
    def AutoConnectionTest(self):
        '''自动检测与服务器的连接状态'''
        if self.connect_state == DISCONNECTED:
            return
        self.Button_ConnectToServer_Click()
        self.window.after(1000, self.AutoConnectionTest)
    
    
    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    client = Client()
    client.run()