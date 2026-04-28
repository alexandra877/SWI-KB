# 2.7.2. VPN — Cisco AnyConnect Installation on Linux Ubuntu LTS

This guide is for **Linux Ubuntu LTS (v22.04 and/or v24.04)** and does not apply to other operating systems/versions.

> Additional info and guides for other systems: [Cisco AnyConnect Generic Info and Links to OS-specific User Guides](vpn-overview.md)

**Note:** Anyconnect VPN Client software is now renamed to **Cisco Secure Client VPN**.

Cisco Secure Client VPN might not work as intended if other 3rd party VPN clients are used/connected at the same time. We do not recommend nor support such use scenarios.

**All requests need to go via Servicedesk.** Service Desk can be contacted at [https://jira.visma.com/servicedesk/customer/portal/8](https://jira.visma.com/servicedesk/customer/portal/8).

You are still required to read through this HowTo article to be informed about what is needed and under what conditions you can connect from a Linux machine.

## Steps Overview

Perform the following steps in order:

1. **Read through the prerequisites** below and make sure you have a supported Ubuntu OS version and that the proper AD groups are already added to your user. (Leave the SSM Agent part as the last step.)
2. **Download and install the VPN Client** following the steps below. After completing this, you will be able to connect to VPN but you will get disconnected every 10 minutes — SSM Agent and compliance is needed to fix that.
3. **Have SSM Agent set up on your PC** so that system scan and compliance status are reported, keeping your VPN connection up.
   - Do **not** try to install SSM Agent yourself from other sources, as it may lead to problems.
   - Contact ServiceDesk and ask them to assist you in SSM Agent installation and enrollment via AWS. They will provide you with the needed downloads, command lines, and activation codes.

> **Please note:** We do not recommend having two or more Linux machines enrolled per VPN username, as their alternate compliance reports will lead to confusion and VPN disconnects.

## Prerequisites

### At Username/AD Level

- Your **internal user** needs to be a member of your company's **VPN group**.
  - A list of onboarded companies and their VPN group name can be found in the linked internal resources.
  - If your company is not in the list, contact your IT manager to initiate onboarding via service management.
  - Access to VPN group can be requested via **MimPortal** (only accessible from internal Visma networks). HowTo instructions can be found in the linked internal resources.
- Additionally, your internal user needs to be a member of the **`VIT-S-VPN-LinuxEnabled`** AD group. This can be requested via ServiceDesk. Direct Manager approval is needed.
- Your internal user needs to have an **OTP SMS/GoogleAuth token** assigned, different from the token you use to sign in to Google with your Visma account.
  - SMS or GAuth (time-based) token can be enabled via [https://selfservice2fa.visma.com/](https://selfservice2fa.visma.com/) — log in with your internal username/password.
  - If you need help, please contact ServiceDesk.

### At OS Level

- Run **Ubuntu Linux LTS 22.04 or 24.04**. You will not be able to log in to VPN if using other Linux distributions.
- You must run **X-Window** (you can only use the VPN Client via GUI).
- Optional: if you already have Cisco AnyConnect VPN Client or Cisco Secure Client VPN installed, it is recommended to remove/uninstall it prior to starting this HowTo.
- All the **OS updates** installed and up-to-date.
- The **Firewall enabled** (UFW needs to run as a service and also be in "enabled" state).
- Up-to-date **AntiVirus and AntiMalware**:
  - For personal computers: install and use **ClamAV** (install instructions are provided below).
  - For Visma-issued PCs running Ubuntu Linux: use **SentinelOne** (see dedicated SentinelOne install instructions).
- You need to have the **SSM Agent installed**. Please contact ServiceDesk to set this up on your machine.

### SSM Agent — Description

SSM Agent is a service running on your system that checks for compliance (Firewall, Antivirus, OS updates). Compliance status is reported securely (at request or periodically) to the SSM server located in AWS Europe. The AWS server is polled periodically by the VPN system and non-compliant users are automatically disconnected from VPN.

## Download Cisco Secure Client VPN

1. Go to [https://sites.google.com/visma.com/vpnclient](https://sites.google.com/visma.com/vpnclient).
   - You may be first prompted for authentication if you are not already connected to the Visma Mail account in the browser.
   - It is recommended to use a **private/incognito window** while doing the download steps.
   - Log in with your Visma Google credentials (Visma e-mail address and corresponding password/Google Auth token).
2. Choose **"Linux Ubuntu LTS"**, then click **"Download"**.
   - If download does not work, please use a private/incognito browser window and log in using your Visma Google account.

## Software Installation

1. After download, go to your **Downloads** folder (or to the location where you saved the file).
2. Right-click on the downloaded **AnyConnect TAR.GZ** file and choose **"Extract here"**.
3. Open a **Terminal** window and navigate to the Downloads folder and then into the extracted sub-directories.
4. Execute the install script:

   ```bash
   sudo ./vpn_install.sh
   ```

   Enter your local system SUDO password when prompted.

5. Accept license terms by typing `y` when prompted.
6. VPN Client is now installed. The **Cisco Secure Client** app icon can now be found on the taskbar or in the Apps menu.

> You can now safely delete the extracted VPN Client folder in Downloads and the related TAR.GZ file. It is recommended to keep the TAR.GZ file in case you need to install or uninstall the VPN Client in the future.

## ClamAV Installation (Personal Computers)

> **Important:** If your PC running Ubuntu Linux was issued by Visma, please install **SentinelOne** as a solution for AntiVirus/AntiMalware instead.

For personal PCs, set up ClamAV:

1. Open **Terminal**.
2. Update package lists:

   ```bash
   sudo apt update
   ```

3. Install ClamAV and its daemon (both are needed for system compliance):

   ```bash
   sudo apt install clamav clamav-daemon -y
   ```

4. Download the latest signature database:

   ```bash
   sudo freshclam
   ```

5. Make sure the process is running:

   ```bash
   sudo systemctl restart clamav-daemon
   ```

6. You can now exit/close the Terminal window.

## Client Setup and VPN Connection

1. Start the **Cisco Secure Client VPN** by clicking on the icon in the taskbar or from the Apps menu.
2. Enter `access.visma.com` in the **Connect To** text box, then click the **"Connect"** button.
3. If you get a prompt with **"Certificate Validation Failure"**, please ignore it and click **"Close"**.
   - By default, the CorporateDevice Group is selected, which looks for an installed AD certificate. This does not apply to Linux.
4. Select **`PersonalDevice`** or **`PersonalDevice-NoSplit`** for the Group dropdown option to be able to connect.
   - Note: VPN access level for PersonalDevice or CorporateDevice is the same.

> **IMPORTANT:**
> It is recommended to use the normal `PersonalDevice` group option so that **only Visma office and DC-related traffic** flows through VPN.
> `*-NoSplit` group options will route **ALL traffic** via the VPN tunnel, including internet-related traffic.
> Please be aware of this and use them only when needed to access internet destinations that require you to be behind a trusted/known IP address.
> To save bandwidth, it is strongly recommended that YouTube or other similar streaming services should **not** be used while connected with the `*-NoSplit` options.

5. Enter your regular Visma username + password and click **"OK"**.
   - Username format: `user.name` (example: `john.doe`) — do **NOT** use `internal\` domain name before username or `@visma.com` at the end.

> **IMPORTANT:** If login fails at this point and you are sure the credentials are correct, most probably your user does not have any 2FA OTP token assigned (SMS or Google Auth). Login does not work without a 2FA OTP token. Please ask for support via **Visma ServiceDesk**.

6. When prompted, input the **OTP 2FA token** or **SMS code**.
   - SMS is sent to the phone number registered for your Visma AD user.
   - For enabling OTP 2FA token, please contact Visma ServiceDesk.
7. Click **"Continue"**.
8. You are now connected to VPN. Click on the application in the taskbar to show status.

## Related Articles

- [Linux Ubuntu LTS — Installation and setup of Cisco AnyConnect](vpn-install-linux.md)
- [Mac OS X — Installation and setup of Cisco AnyConnect](vpn-install-macos.md)
- [MS Windows OS — Installation and setup of Cisco AnyConnect](vpn-install-windows.md)
- [Chrome OS — Installation and setup of Cisco AnyConnect](vpn-install-chrome.md)
