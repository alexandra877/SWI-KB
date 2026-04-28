# 2.7.2. VPN — Cisco AnyConnect Installation on macOS

This guide is for Mac OS and might not be accurate for other operating systems.

> Additional info and guides for other systems: [Cisco AnyConnect Generic Info and Links to OS-specific User Guides](vpn-overview.md)

**Note:** Anyconnect VPN Client software is now renamed to **Cisco Secure Client VPN**.

Cisco Secure Client VPN might not work as intended if other 3rd party VPN clients are used/connected at the same time. We do not recommend nor support such use scenarios.

## Prerequisites

To get Cisco Secure Client VPN to work on Mac OS:

- You need to have all the OS updates installed and up-to-date.
- You need to have the **Firewall enabled** in OS Security Settings.
- You need up-to-date **AntiVirus and AntiMalware** (see Cisco.com site for supported versions to choose from).
- If you already have Cisco AnyConnect installed, we recommend removing/uninstalling it prior to starting this HowTo.
- At some points during install, you may need to provide one-time agreement on OS security side (you will be notified about this by the OS).
- We recommend having all the above requirements installed or set up prior to installing AnyConnect.

It is recommended to have your Mac OS machine **enrolled in Intune**, so it becomes a managed machine relating to OS upgrades, WiFi certificates, AntiVirus (SentinelOne Visma license), etc.

Without enrollment to Intune, you will have to manage OS upgrades and find suitable/working AntiVirus software yourself. You are also free to stop using Intune and un-enrol at any time.

For Intune enrollment, please contact our **Service Desk** team.

## Installation — Intune-Managed macOS PCs

If your macOS is managed via Intune, you can install the Cisco Secure Client VPN software and its components via the **Company Portal** app.

1. Open the **Company Portal** app.
2. Install **"Cisco Secure Client VPN"**.

> Note: The version of the client depicted in screenshots may be different/older than what you currently have available due to software upgrades and rollouts.

## Installation — Non-Managed macOS PCs

### Download Cisco Secure Client VPN

1. Go to [https://sites.google.com/visma.com/vpnclient](https://sites.google.com/visma.com/vpnclient).
   - You may be first prompted for authentication if you are not already connected to the Visma Mail account in the browser.
   - Log in with your Visma Google credentials (Visma e-mail address and corresponding password/Google Auth token).
   - **Please note:** Download might not work properly unless you use an **incognito/private browser tab/window**.
2. Choose **"Apple Mac OS X"**, then click **"Download"**.

> ISE Posture plugin is already included in the VPN Client install pack — make sure you have it selected during software install.
> ISECompliance is the definitions module for the ISE Posture plugin. You can download and install it separately, after VPN Client setup is completed.

### Software Installation

1. After the download is complete, go to the lower-right corner of your Mac OS Desktop and check the **Downloads** section.
2. Click on the downloaded **Cisco Secure Client DMG** file.
3. The DMG file will be mounted on your desktop and its content shown in a new window.
4. Double-click on **"Cisco Secure Client.pkg"** — the install wizard will start.
5. Click **"Continue"** (agree to license terms when prompted) until you reach the **"Installation Type"** section.
6. **Deselect all options except "VPN" and "ISE Posture"**.
7. Click **"Continue"**, then click **"Install"**.
8. The operating system will ask for installation approval — enter your **macOS user password** for confirmation and click **"Install Software"**.
9. Wait a few minutes for the installation to finish, then click **"Close"**.
10. You will be asked if you want to keep the VPN Client Installer or move it to Trash. Either option does not affect the already installed software.
11. Go to the "AnyConnect" or "Cisco Secure Client" image mount on your desktop, right-click and choose **"Eject"**.

During or at the end of the install process, you will be prompted to **enable access for VPN Client and related Network extensions**. Make sure to allow access when prompted by macOS Security settings and toggle those settings to **ON**.

This concludes the basic VPN client software installation.

You can now also install the separate ISECompliance module if, for some reason, it fails to be automatically downloaded by the VPN Client after initial VPN login.

## Client Setup and VPN Connection

1. Go to **LaunchPad**, or via Finder to **Applications**, find and start the **Cisco Secure Client VPN** software.
2. Allow system access for the Cisco Secure Client VPN software via macOS security settings if prompted. This may happen when running the software for the first time.
3. Make sure `access.visma.com` is in the address field.
4. Click **Connect**. You will be prompted for credentials.
5. Select the appropriate **Group** option:
   - Make sure you select `PersonalDevice` or `PersonalDevice-NoSplit` for the Group option, or you will not be able to connect.
   - If you own a macOS device issued by Visma and enrolled via/to Intune, you can also select one of the `CorporateDevice` profiles.
   - Personal/Corporate profiles define how the compliance-related system scan is done, not the access level (which is defined by the VPN group).

> **IMPORTANT:**
> We recommend using the normal `PersonalDevice` group option so that **only Visma office and DC-related traffic** flows through VPN.
> `*-NoSplit` group options will route **ALL traffic** via the VPN tunnel, including internet-related traffic.
> Please be aware of this and use them only when needed to access internet destinations that require you to be behind a trusted/known IP address.
> To save bandwidth, it is strongly recommended that YouTube or other similar streaming services should **not** be used while connected with the `*-NoSplit` options.

6. Enter your regular Visma username + password and click **"OK"**.
   - Example username: `john.doe` — no domain name before user or `@visma.com` at the end.

> **IMPORTANT:** If login fails at this point and you are sure the credentials are correct, most probably your user does not have any 2FA token assigned (SMS or Google Auth). Login does not work without a 2FA token. Please ask for support via **Visma ServiceDesk**.

7. When prompted, input the **OTP 2FA token** or **SMS code**.
   - SMS is sent to the phone number registered for your Visma AD user.
   - For enabling OTP 2FA token, please contact Visma ServiceDesk.
8. Allow system access for the AnyConnect software modules via macOS security settings if prompted.
9. **System scan will start.**
   - If it does not, uninstall any Cisco AnyConnect related software from your computer and restart from the beginning.
   - You will still need to have an active Firewall, up-to-date Anti-Virus and Anti-Malware tool, and up-to-date OS updates.
   - You have **15 minutes** to resolve any issues, then VPN will auto-disconnect. If the time is not enough, you can reconnect anytime and continue from where you left off.
10. After the scan is successful, you will reach **"compliant"** status and access to Visma resources is granted via VPN.

## Related Articles

- [Linux Ubuntu LTS — Installation and setup of Cisco AnyConnect](vpn-install-linux.md)
- [Mac OS X — Installation and setup of Cisco AnyConnect](vpn-install-macos.md)
- [MS Windows OS — Installation and setup of Cisco AnyConnect](vpn-install-windows.md)
- [Chrome OS — Installation and setup of Cisco AnyConnect](vpn-install-chrome.md)
