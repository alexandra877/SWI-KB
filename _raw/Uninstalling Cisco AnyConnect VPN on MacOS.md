# How-To Guide - Uninstalling Cisco AnyConnect VPN on MacOS
Date: 13.03.2024
Tags: Uninstall, Cisco AnyConnect, VPN, MacOS, Guide
This guide provides step-by-step instructions on how to successfully uninstall the Cisco AnyConnect VPN Client on MacOS. The process can be completed using one of four methods, depending on the user’s preferences and the specific circumstances of their system.
## First Method: Using Finder
Open Finder.
Navigate to Applications and open the “Cisco” Folder. If the Cisco folder cannot be found/does not exist, please see the Second Method.
Double-click the “Uninstall AnyConnect” to start the uninstall process. If the uninstall app cannot be found, please see the Second Method.
Follow the instructions to uninstall Cisco AnyConnect.
## Second Method: Using Terminal
Open Terminal.
Change your directory to Cisco Anyconnect Bin using the following command: cd /opt/cisco/anyconnect/bin
List the files in the directory using the following command: ls
Check to see if there is a file named “vpn_uninstall.sh”. If the file exists, run the following command: sh vpn_uninstall.sh
If successful, you should receive this confirmation message in the Terminal: “Successfully removed Cisco AnyConnect Secure Mobility Client from the system.”
## Third Method: Using pkgutil
Open Terminal.
Run the following command: sudo pkgutil --forget com.cisco.pkg.anyconnect.vpn
## Fourth Method: Manual Uninstall
As a last resort, please follow the “rm -rf” commands found .
Please note that each method should be attempted in order, only proceeding to the next if the previous method was unsuccessful. Always ensure to follow the instructions carefully to avoid any potential issues.