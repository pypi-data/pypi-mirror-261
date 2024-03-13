import os
from PyPDF2 import PdfReader, PdfWriter
import PySimpleGUI as sg
import tkinter as tk
from tkinter import filedialog

def GetFileName():
    root = tk.Tk()
    root.withdraw()
    file_list = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    file_list = list(file_list)
    file_list.sort()
    return file_list


def MergePDF(file_list, output_dir, file_name):
    output = PdfWriter()
    outputPages = 0
    print(file_list)
    for pdf_file in file_list:
        print("文件：%s" % pdf_file.split('/')[-1], end=' ')
        # 读取PDF文件
        input = PdfReader(open(pdf_file, "rb"))
        # 获得源PDF文件中页面总数
        pageCount = len(input.pages)
        outputPages += pageCount
        print("页数：%d" % pageCount)
        # 分别将page添加到输出output中
        for iPage in range(pageCount):
            output.add_page(input.pages[iPage])
    print("\n合并后的总页数:%d" % outputPages)
    # 写入到目标PDF文件
    print("PDF文件正在合并，请稍等......")
    with open(os.path.join(output_dir, file_name + ".pdf"), "wb") as outputfile:
        output.write(outputfile)
    print("PDF文件合并完成")

# 创建GUI界面
layout = [
    [sg.Text('请选择要合并的多个PDF文件：')],
    [sg.Input(key='file_list'), sg.Button('浏览')],
    [sg.Text('请选择合并后的目标文件保存路径：')],
    [sg.Input(key='output_dir'), sg.FolderBrowse('浏览')],
    [sg.Text('请输入合并后的目标文件名前缀：')],
    [sg.Input(key='file_name'), sg.Text('.pdf', font=('Arial', 12))],
    [sg.Button('合并'), sg.Button('退出')]
]

window = sg.Window('PDF合并器', layout)

# 处理用户事件和输入
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == '退出':
        break
    elif event == '浏览':
        file_list = GetFileName()
        window['file_list'].update(';'.join(file_list))
    elif event == '合并':
        file_list = values['file_list'].split(';')
        output_dir = values['output_dir']
        file_name = values['file_name']
        if file_list and output_dir and file_name:
            try:
                MergePDF(file_list, output_dir, file_name)
                sg.popup('合并成功！')
            except Exception as e:
                sg.popup('合并失败！', str(e))
        else:
            sg.popup('请输入有效的路径和文件名！')

window.close()

