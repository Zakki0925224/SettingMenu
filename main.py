#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Handler:

    def main(self):
        builder = Gtk.Builder()
        builder.add_from_file("SettingMenu.glade")
        builder.connect_signals(Handler())
        window = builder.get_object("window1")
        window.show_all()
        Gtk.main()

    # ウィンドウを閉じたとき
    def onDestroy(self, *args):
        Gtk.main_quit()

    # ボタン
    # def {設定したハンドラーの名前}(self, {接続したいウィジェットのID})
    def button1_clicked(self, button1):
        os.system('xfce4-display-settings')
    
    def button2_clicked(self, button2):
        os.system('xfce4-notifyd-config')

    def button3_clicked(self, button3):
        os.system('gnome-disks')

    def button4_clicked(self, button4):
        os.system('xfwm4-workspace-settings')

    def button5_clicked(self, button5):
        os.system('xfce4-power-manager-settings')

    # System About (original)
    def button6_clicked(self, button6):
        # よく分からないので一旦これで保留
        import about
        about.app.main()


    def button7_clicked(self, button7):
        os.system('system-config-printer')

    def button8_clicked(self, button8):
        os.system('xfce4-mouse-settings')

    def button9_clicked(self, button9):
        os.system('xfce4-keyboard-settings')

    def button10_clicked(self, button10):
        os.system('thunar-volman-settings')

    def button11_clicked(self, button11):
        os.system('software-properties-gtk --open-tab=4')

    def button12_clicked(self, button12):
        os.system('network-admin')

    def button13_clicked(self, button13):
        os.system('nm-connection-editor')

    def button14_clicked(self, button14):
        os.system('xfdesktop-settings')

    def button15_clicked(self, button15):
        os.system('xfce4-appearance-settings')

    # 起動せず
    def button16_clicked(self, button16):
        os.system('xfce4-panel')

    # xfce panel fetch
    def button17_clicked(self, button17):
        os.system('')

    def button18_clicked(self, button18):
        os.system('xfwm4-settings')

    def button19_clicked(self, button19):
        os.system('xfwm4-tweaks-settings')

    def button20_clicked(self, button20):
        os.system('/usr/lib/x86_64-linux-gnu/xfce4/exo-2/exo-helper-2 --configure')

    def button21_clicked(self, button21):
        os.system('xfce4-session-settings')

    def button22_clicked(self, button22):
        os.system('xfce4-mime-settings')

    # synaptic package manager
    def button23_clicked(self, button23):
        os.system('')

    def button24_clicked(self, button24):
        os.system('xfce4-terminal --preferences')

    # file manager
    def button25_clicked(self, button25):
        os.system('')

    # grub customizer
    def button26_clicked(self, button26):
        os.system('')

    # altermatives cunfigurator
    def button27_clicked(self, button27):
        os.system('')

    def button28_clicked(self, button28):
        os.system('users-admin')

    def button29_clicked(self, button29):
        os.system('/usr/bin/python3 /usr/bin/mugshot')

    def button30_clicked(self, button30):
        os.system('time-admin')

    # orage setting
    def button31_clicked(self, button31):
        os.system('')

    def button32_clicked(self, button32):
        os.system('/usr/bin/python3 /usr/bin/gnome-language-selector')
    
    def button33_clicked(self, button33):
        os.system('python3 /usr/share/ibus/setup/main.py')

    def button34_clicked(self, button34):
        os.system('/usr/lib/mozc/mozc_tool --mode=config_dialog')

    def button35_clicked(self, button35):
        os.system('fcitx-config-gtk3')

    def button36_clicked(self, button36):
        os.system('xfce4-accessibility-settings')

    # sudoが必要
    def button37_clicked(self, button37):
        os.system('python3 /usr/share/gufw/gufw/gufw.py')

    def button38_clicked(self, button38):
        os.system('/usr/bin/python3 /usr/bin/software-properties-gtk')
    
    def button39_clicked(self, button39):
        os.system('/usr/bin/python3 /usr/bin/update-manager')

    def button40_clicked(self, button40):
        os.system('xfce4-settings-editor')

app = Handler()
app.main()