import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox as mbox


#Tk class generating
root = tk.Tk()

# screen size
root.geometry("700x110")

# screen title
root.title("QSO DB library 生成ツール")


# パラメータ
adif_file = tk.StringVar()
ask_adif_file = tk.StringVar()
QSO_DB = set()


#パラメータの初期化

def data_clear():

    ask_adif_file.set('')


# adif.adiファイル選択ボタンの動作

def ask_adif():   
    
    ask_adif_f = filedialog.askopenfilename(filetypes =  [('テキストファイル','*.adi')] , initialdir = './' )
    ask_adif_file.set(ask_adif_f)

#    print( "-------- ask_adif() " ) 
#    print( "adif_f   ; ", ask_adif_f )
#    print( "adif_file: ", ask_adif_file )


# ツールの終了

def closing():
    root.destroy()


def QSO_db_lib():

# tempファイルを削除するためにOSをインポートする
    import os

#------------------------------------------------------------------------
#
#   ファイルネーム（コールサイン）の入力
#

    forming_file =  "temp_forming.adi"
    file_name = ask_adif_file.get()
    
    adif_file = open(file_name,"r",encoding='utf-8')
    output_log = open(forming_file ,"w",encoding='utf-8')


#------------------------------------------------------------------------
#
# ADIFファイルが改行分割されたレコードを1レコードに編集
#
#

    data1 = ""

    lines = adif_file.readlines()

    for line in lines:
        
        if "<CALL:"  in line:
            
            if "<EOR>" in line:
                data1=line
                output_log.write(data1)
                continue
            
            data1=line.rstrip('\n')
            continue
        
        if "<CALL:" not in line:
            
            if "<EOR>" in line:
                data1=data1 + line
                output_log.write(data1)
                data1 = ""
                continue
            
            data1= data1 + line.rstrip('\n')
            continue


        output_log.write(line)
        
    adif_file.close()
    output_log.close()

#-----------------------------------------------------------------------------

    import pickle
    
    file_name = ""
    db_file = ""
    Callsign = ""

    #------------------------------------------------------------------------
    #
    #
    #


    temp_adif_file ="temp_forming.adi"
    db_file =  "Callsign_db.txt"

    #--------------------------------------------------------------------
    #
    #   ファイル名の定義
    #

    file_name=ask_adif_file.get()
#    adif_log = open( file_name ,"r",encoding='utf-8')
    adif_log = open( temp_adif_file ,"r",encoding='utf-8')
    qsodb_log = open( db_file ,"w",encoding='utf-8')

    logs = adif_log.readlines()

    #--------------------------------------------------------------------
    #
    #   変数宣言
    #

    data=""
    data1=""
    data2=""
    data3=""

    log = ""
    i=0

    a = ""
    b = ""
    c = ""

    CALL = ""
    FREQ = ""
    MODE = ""
    SUBMODE =""

    line = ""

#----------------------------------------------------------------------------

    #--------------------------------------------------
    #
    #   N1MM Logger+が出力しないADIFパラメータ対策
    #

    #line = "年月日" +" "+ "時分" +" "+ "バンド" +" "+ "モード" +" "+ "交信局" +" "+ "送信RST" +" "+ "送信ナンバー" +" "+ "受信RST" +" "+ "受信ナンバー" +" "+ "マルチ" +" "+ "得点"+ "\n"
     
    #logsheet.write(line)

    for log in logs:

        if "CALL:" not in log :
            CALL = " "

        if "GRIDSQUARE:" not in log :
            GRIDSQUARE = " "

        if "BAND:" not in log :
            BAND = " "

        if "CONTEST_ID:" not in log :
            CONTEST_ID = " "

        if "<MODE:" not in log :
            MODE = " "

        if "<SUBMODE:" not in log :
            SUBMODE = " "

            
    #--------------------------------------------------
    #
    #       JARL LOG作成　　ADIFフォーマットから要素抽出
    #
            
        log = log.replace(' "','')
        log = log.rstrip('\n')
        log = log.lstrip()
        log = log.split("<")

        for i in log:

            if "CALL:" in i :
                a = i
                b = a[5:7]
                b1= b.rstrip(">")
                b2 = len(b1)
                CALL = a[6+b2:7+b2+int(b1)]
                CALL = CALL.rstrip()


            if "BAND:" in i:
                a = i
                b = a[5:7]
                b1= b.rstrip(">")
                b2 = len(b1)
                BAND = a[6+b2:7+b2+int(b1)]
                BAND = BAND.rstrip()
                BAND = BAND.upper()

            if "CONTEST_ID:" in i:
                a = i
                b = a[11:13]
                b1= b.rstrip(">")
                b2 = len(b1)
                CONTEST_ID = a[12+b2:13+b2+int(b1)]
                CONTEST_ID = CONTEST_ID.rstrip()

                
# 2019/12/10 WSJTXのADIFファイルに対応するため、iの部分一致から特定文字の完全一致へ変更
                
            if "MODE:" == i[:5] :
                a = i
                b = a[5:7]
                b1= b.rstrip(">")
                b2 = len(b1)
                MODE = a[6+b2:7+b2+int(b1)]
                MODE = MODE.rstrip()
                
# 2019/12/10 WSJTXのADIFファイルに対応するため、SUBMODEを追加
# 2019/12/10 WSJTXのADIFファイルに対応するため、iの部分一致から特定文字の完全一致へ変更

            if "SUBMODE:" == i[:8] :
                a = i
                b = a[8:10]
                b1= b.rstrip(">")
                b2 = len(b1)
                SUBMODE = a[9+b2:10+b2+int(b1)]
                SUBMODE = SUBMODE.rstrip()             

    #--------------------------------------
    #
    #   QSO DBファィル出力
    #
    
        db_data = CALL+'-'+BAND+'-'+MODE+'\n'
        QSO_DB.add( db_data )

    for l in sorted( QSO_DB ) :
        qsodb_log.write( l )
        
    adif_log.close()
    qsodb_log.close()

#tempファイルの削除
    os.remove(temp_adif_file)

#「pickle」での書き出し
    f = open('QSO_DB_lib.txt', 'wb')
    pickle.dump(QSO_DB, f)
    f.close()

# ライブラリー作成完了の通知

    mbox.showinfo('作成状態', 'QSO_DB_libの作成完了' )
    
    return


# ウィジット作成（form.txtファイル）
form_label = tk.Label(root, text="ハムログADIFファイルの指定")
form_label.place(x=10, y=30)
form_box = tk.Entry(root, textvariable= ask_adif_file, width=80)
form_box.place(x=145, y=30)
form_btn = tk.Button(root, text="参照", command=ask_adif)
form_btn.place(x=650, y=30)

clear_Button = tk.Button(root,text='パラメータClear', command = data_clear )
clear_Button.place(x=40 , y=70)

okButton =tk.Button( root, text='ライブラリ作成', command = QSO_db_lib )
okButton.place(x=200 , y=70)

closeButton =tk.Button( root, text='Close', command = closing )
closeButton.place(x=400 , y=70)


root.mainloop()
