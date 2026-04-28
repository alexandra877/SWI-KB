# 2.7.2. VPN — Uninstalling Cisco AnyConnect on macOS

**Date:** 13.03.2024  
**Tags:** Uninstall, Cisco AnyConnect, VPN, MacOS, Guide

This guide provides step-by-step instructions on how to successfully uninstall the Cisco AnyConnect VPN Client on macOS. The process can be completed using one of four methods, depending on the user's preferences and the specific circumstances of their system.

> **Please note:** Each method should be attempted in order, only proceeding to the next if the previous method was unsuccessful. Always follow the instructions carefully to avoid any potential issues.

## Method 1: Using Finder

1. Open **Finder**.
2. Navigate to **Applications** and open the **"Cisco"** folder.
   - If the Cisco folder cannot be found or does not exist, proceed to Method 2.
3. Double-click **"Uninstall AnyConnect"** to start the uninstall process.
   - If the uninstall app cannot be found, proceed to Method 2.
4. Follow the instructions to uninstall Cisco AnyConnect.

## Method 2: Using Terminal

1. Open **Terminal**.
2. Change your directory to the Cisco AnyConnect bin folder:

   ```bash
   cd /opt/cisco/anyconnect/bin
   ```

3. List the files in the directory:

   ```bash
   ls
   ```

4. Check if there is a file named `vpn_uninstall.sh`. If the file exists, run:

   ```bash
   sh vpn_uninstall.sh
   ```

5. If successful, you should receive the following confirmation message in Terminal:

   ```
   Successfully removed Cisco AnyConnect Secure Mobility Client from the system.
   ```

## Method 3: Using pkgutil

1. Open **Terminal**.
2. Run the following command:

   ```bash
   sudo pkgutil --forget com.cisco.pkg.anyconnect.vpn
   ```

## Method 4: Manual Uninstall

As a last resort, please follow the `rm -rf` commands found in the internal documentation.
