#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import subprocess
import psutil
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Handler:
    def main(self):
        builder = Gtk.Builder()
        builder.add_from_file("AboutMe.glade")
        builder.connect_signals(Handler())
        window = builder.get_object("window1")
        window.show_all()

        #####label change#####
        # label 
        cpu_name = (subprocess.Popen('cat /proc/cpuinfo | head -5 | tail -1 | cut -d: -f2 | tr -d "\n" ', stdout = subprocess.PIPE, shell = True).communicate()[0]).decode('utf-8')

        ram_totalsize = (subprocess.Popen(""" awk '{ printf"%.2f", $2/1024/1024 ; exit}' /proc/meminfo """, stdout = subprocess.PIPE, shell = True).communicate()[0]).decode('utf-8')

        rom_totalsize = str(round((psutil.disk_usage('/').total/1073741824), 2))
        rom_using = str(psutil.disk_usage('/').percent)

        os_name = (subprocess.Popen("""lsb_release -d | awk -F "\t" '{print $2}' | awk 'BEGIN{ORS = ""}{print $0}'""", stdout = subprocess.PIPE, shell = True).communicate()[0]).decode('utf-8')

        os_type = (subprocess.Popen("""uname -m | awk 'BEGIN{ORS = ""}{print $0}'""", stdout = subprocess.PIPE, shell = True).communicate()[0]).decode('utf-8')

        os_codename = (subprocess.Popen("""lsb_release -c | awk -F "\t" '{print $2}' | awk 'BEGIN{ORS = ""}{print $0}'""", stdout = subprocess.PIPE, shell = True).communicate()[0]).decode('utf-8')

        kernel_name = (subprocess.Popen("""uname | awk 'BEGIN{ORS = ""}{print $0}'""", stdout = subprocess.PIPE, shell = True).communicate()[0]).decode('utf-8')

        kernel_version = (subprocess.Popen("""uname --kernel-release | awk 'BEGIN{ORS = ""}{print $0}'""", stdout = subprocess.PIPE, shell = True).communicate()[0]).decode('utf-8')

        # cpu
        cpu_label = builder.get_object("cpu_label")
        cpu_label.set_label(cpu_name)

        # ram
        ram_label = builder.get_object("ram_label")
        ram_label.set_label('{0} GB'.format(ram_totalsize))

        # rom
        rom_label = builder.get_object("rom_label")
        rom_label.set_label('{0} GB (Using: {1} %)'.format(rom_totalsize,rom_using))

        # os
        os_label = builder.get_object("os_label")
        os_label.set_label(os_name)

        # os type
        ostype_label = builder.get_object("ostype_label")
        ostype_label.set_label(os_type)

        # codename
        codename_label = builder.get_object("codename_label")
        codename_label.set_label(os_codename)

        # kernel
        kernel_label = builder.get_object("kernel_label")
        kernel_label.set_label('{0} {1}'.format(kernel_name,kernel_version))

        Gtk.main()

    def onDestroy(self, *args):
        Gtk.main_quit()

app = Handler()
app.main()