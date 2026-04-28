# 2.7.2. VPN — Norway AnyConnect Access Instructions

The following instruction set covers the **Windows operating system** as an example, since the login info and profiles to choose from at connecting time are the same for all other supported AnyConnect client operating systems.

## Step-by-Step Guide

1. Start the **Norway AnyConnect Client** and make sure the correct server address is in the address field.

2. Click **Connect**. You will be prompted for credentials.

   - For **unmanaged devices** (not registered on Visma AD): select `PersonalDevice` or `PersonalDevice-NoSplit` for the Group option, or you will not be able to connect.
   - For **AD-registered Windows machines**: select `CorporateDevice` or `CorporateDevice-NoSplit` Group option.

   > **IMPORTANT:**
   > We recommend using the normal `PersonalDevice` or `CorporateDevice` group options so that **only Visma office and DC-related traffic** flows through VPN.
   > `*-NoSplit` group options will route **ALL traffic** via the VPN tunnel, including internet-related traffic.
   > Please be aware of this and use them only when needed to access internet destinations that require you to be behind a trusted/known IP address.
   > To save bandwidth, it is strongly recommended that YouTube or other similar streaming services should **not** be used while connected with the `*-NoSplit` options.

3. Enter your regular Visma username + password and click **"OK"**.
   - Example username: `john.doe` — no domain name before user or `@` at the end.

   > **IMPORTANT:** If login fails at this point and you are sure the credentials are correct, most probably your user does not have any 2FA token assigned (SMS or Google Auth). Login does not work without a 2FA token. Please ask for support via **Visma ServiceDesk**.

4. When prompted, input the **OTP 2FA token** or **SMS code**.
   - SMS is sent to the phone number registered for your Visma AD user.
   - For enabling OTP 2FA token, please contact Visma ServiceDesk.

5. The **system scan** will start.
   - If it does not, uninstall any Cisco AnyConnect related software from your computer and restart from the beginning. You might have had the AnyConnect client installed previously.
   - You will still need to have an active Firewall, up-to-date Anti-Virus and Anti-Malware tool, and up-to-date OS updates (usually provided by Windows or pre-installed on AD-registered PCs).
   - You have **15 minutes** to resolve any issues, then VPN will auto-disconnect. If the time is not enough, you can reconnect anytime and continue from where you left off.

6. After the scan is successful, you will get to **"compliant"** status and access to Visma resources is granted via VPN.

## Related Links

Cisco AnyConnect client software installation guides:

- [MS Windows OS — Installation and setup of Cisco AnyConnect](vpn-install-windows.md)
- [Mac OS X — Installation and setup of Cisco AnyConnect](vpn-install-macos.md)
- [Chrome OS — Installation and setup of Cisco AnyConnect](vpn-install-chrome.md)
- [Linux Ubuntu LTS — Installation and setup of Cisco AnyConnect](vpn-install-linux.md)
