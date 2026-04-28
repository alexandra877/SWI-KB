# 2.7.2. VPN — Cisco AnyConnect Installation on Chrome OS

This guide is for Chrome OS and might not be accurate for other operating systems.

> Additional info and guides for other systems: [Cisco AnyConnect Generic Info and Links to OS-specific User Guides](vpn-overview.md)

## Important Update — Updated ChromeOS Devices

If your ChromeOS device is more recent and updated to the latest ChromeOS version, the **Webstore variant** of the AnyConnect VPN Client app will **not work anymore** and will report errors or stay locked up in "initializing . . ." state.

For updated ChromeOS variants, please proceed as described below.

### Clean Up Old Webstore VPN Client (if installed)

If you still have the Webstore VPN client installed (the one from the Google Chrome Webstore), perform these clean-up steps:

1. Go to **ChromeOS settings** and remove all related VPN profiles under the network section, as well as related certificates, if any.
2. Go to the **Google Chrome Webstore** and remove/uninstall the AnyConnect VPN Client App.
   - Alternatively, go to **Chrome Browser settings → Manage extensions**, find and remove the AnyConnect VPN Client extension.

### Set Up the Google Play Store VPN Client

The new Google Play Store VPN Client is named **"Cisco Secure Client"** (currently at version 5.x.x).

The VPN Client can only be installed from the **Google Play Store** (similar to the app store available on Android devices).

1. If you do not have the Google Play Store on your Chromebook, see [how to enable it in the settings](https://www.google.com/chromebook/howto/enable-google-play-store/).
2. Open the **Google Play Store** app and search for **"Cisco Secure Client"** from Cisco Systems Inc., and install it.
3. Open the app and accept the license agreement by clicking **OK**.
4. Click on **Connections** — this will open a pop-up where the currently set up VPN connections are listed.
5. Click the **"+"** sign to add a new connection:
   - **Description**: anything you consider a useful name, e.g., "Visma VPN"
   - **Server address**: `access.visma.com`
   - **Advanced Preferences** do not have to be adjusted.
6. Click **"Done"** to create the VPN connection.

### Connecting to VPN

1. Make sure that the correct VPN connection is selected under **"Connections"**. If not, click on "Connections" and select it from the list.
2. Click on **"AnyConnect VPN"**.
3. Select the VPN profile from the dropdown — make sure you select a `PersonalDevice` profile for login to work. Access to VPN resources is not affected by this selection.
4. Enter your credentials (`user.name` and password) and hit **"connect"**.
5. When prompted, enter the **2FA code**.
6. Confirm the connection request with **"OK"**. If you do not agree, you will not be able to use the VPN service.
7. If successfully connected, you will see the coloured slider — **"AnyConnect VPN - connected"**.

---

## Step-by-Step Guide — Older ChromeOS Devices (Webstore VPN Client)

To get Cisco AnyConnect to work on Chromebook, some requirements apply — one of them is the Visma Wireless Certificate, which is the same certificate used for the VismaL3 wireless network.

Download the apps **Cisco AnyConnect** and **Certificate Enrolment for Chrome OS** from the Chrome Webstore.

### Obtaining the Required Visma Certificate

> **Important:** For some user/device combinations, the certificate enrollment might not work properly. If the steps below fail, continue to the next step — setup of profile in Cisco AnyConnect.

1. When you open Chrome on your Chromebook, you should have a small **blue shield** in the upper right corner where your extensions are visible.
   > **Note:** You will have to be at the office and connected to VismaL3/Wired network to be able to get the certificate!
2. Click the shield — you will be sent to a site asking for your AD username and password.
3. Enter your regular Visma username + password and click **"OK"**.
   - Example username: `john.doe` — no domain name before user or `@visma.com` at the end.
4. It will work for a few seconds before giving you a Success message if everything is correct.
5. Verify the certificate by typing `chrome://certificate-manager` in the address field.

### Set Up Profile in Cisco AnyConnect

The Cisco AnyConnect app is pushed to your Chromebook by policy. You can still go to the Webstore and search for the Cisco AnyConnect app and install it manually.

1. Open the **AnyConnect** app.
2. Click **"Add New Connection"** and enter:
   - **Name**: `Visma VPN`
   - **Server Address**: `access.visma.com`
3. Click on **"Select Certificate"** and click **OK**. *(This step is only needed when the certificate enrollment steps above worked for you.)*
4. Click **"Save Changes"**.
5. The setup of AnyConnect is done. Close the application.

### Connecting

1. Click on your **profile picture** in the lower right corner and select **VPN (Disconnected)**.
2. Select **Visma VPN (user)**.
3. Select `PersonalDevice` or `PersonalDevice-NoSplit` in the dropdown list for group.

> **Caution:** The NoSplit option will route ALL traffic via VPN, including normal internet traffic. Use of YouTube or other similar streaming services should be avoided while connected in this way to avoid constraining available VPN bandwidth at Oslo DC.

4. Enter your regular Visma username + password and click **"OK"**.
   - Example username: `john.doe` — no domain name before user or `@visma.com` at the end.

> **IMPORTANT:** If login fails at this point and you are sure the credentials are correct, most probably your user does not have any 2FA token assigned (SMS or Google Auth). Login does not work without a 2FA token. Please ask for support via **Visma ServiceDesk**.

5. When asked to enter your OTP value, this is the **2FA token code**. Click **Submit** to continue.
   - If you do not have a 2FA token set up, the prompt will ask you for an **SMS code** sent to your AD-registered phone number.
   - For setting up a 2FA token, contact [it-servicedesk@visma.com](mailto:it-servicedesk@visma.com).
6. When the connection is active, you can see it as **Connected** in the lower right corner menu.

## Support

For issues, contact via email or Support Portal:

- **Email**: [it-servicedesk@visma.com](mailto:it-servicedesk@visma.com)
- Visma ITC Local Support

## Related Articles

- [Linux Ubuntu LTS — Installation and setup of Cisco AnyConnect](vpn-install-linux.md)
- [Mac OS X — Installation and setup of Cisco AnyConnect](vpn-install-macos.md)
- [MS Windows OS — Installation and setup of Cisco AnyConnect](vpn-install-windows.md)
- [Chrome OS — Installation and setup of Cisco AnyConnect](vpn-install-chrome.md)
