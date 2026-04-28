# 2.7.2. VPN — Cisco AnyConnect Installation on Windows

This guide is for Microsoft Windows OS, including Windows on ARM64, and might not be accurate for other operating systems.

> Additional info and guides for other systems: [Cisco AnyConnect Generic Info and Links to OS-specific User Guides](vpn-overview.md)

**Note:** Anyconnect VPN Client software is now renamed to **Cisco Secure Client VPN**.

Cisco Secure Client VPN might not work as intended if other 3rd party VPN clients are used/connected at the same time. We do not recommend nor support such use scenarios.

## Prerequisites

To get Cisco Secure Client VPN to work on Microsoft Windows OS:

- We recommend that you upgrade your Windows 10 install to build **22H2** or later and Windows 11 to build **23H2** or later.
- You need to have all the OS updates installed and up-to-date.
- You need to have the **Firewall enabled** in OS Security Settings.
  - 3rd party vendors for OS Firewall (usually shipped with "Internet Security" software suites) do not usually play well with Anyconnect VPN.
  - We recommend having that 3rd party FW component disabled and using the default OS Windows Defender Firewall.
- You need up-to-date **AntiVirus and AntiMalware** (see Cisco.com site for supported versions to choose from).
  - If you are using a 3rd party vendor for Antivirus/AntiMalware, make sure that the default Windows Defender Antivirus is disabled in Windows security options/settings.
- If you already have Cisco AnyConnect installed, we recommend removing/uninstalling it prior to starting this HowTo.
- At some points during install, you may need to provide one-time agreement on OS security side (you will be notified about this by the OS).
- We recommend having all the above requirements installed or set up prior to installing Cisco Secure Client.

## Installation — Visma-Managed Windows PCs (Intune or SCCM)

> **Please note:** When the AD user is added to the VPN group (manually or via approved request in MimPortal), the needed software package is **automatically pushed** to managed Windows PCs via Intune/SCCM.
>
> The package contains Cisco Secure Client VPN, ISEPosture plugin, and DART tool.
>
> The below HowTo can still be done manually in case the above automation does not work for you, or for troubleshooting.

1. Open the **Software Center** app or, in case of Intune managed devices, the **Company Portal** app.
2. Install **"Cisco Secure Client VPN"**.

> Note: The version of the client depicted in screenshots may be different/older than what you currently have available due to software upgrades and rollouts.

## Installation — Non-Domain / Non-Managed Computers

> **Note:** Install procedure for Windows 32/64 or Windows on ARM64 is the same, but there are **different install packages** for the two variants. Make sure you download and install the packages suitable for your own Windows OS variant.

1. Go to [https://sites.google.com/visma.com/vpnclient](https://sites.google.com/visma.com/vpnclient).
   - You may be first prompted for authentication if you are not already connected to the Visma Mail account in the browser.
   - Log in with your Visma Google credentials (Visma e-mail address and corresponding password/Google Auth token).
   - **Please note:** Download might not work properly unless you use an **incognito/private browser tab/window**.
2. Choose the operating system — **"Microsoft Windows 32/64bit"** or **"Microsoft Windows on ARM"** — then click **"Download"**.
3. Use similar steps to download the matching **ISE Posture plugin** and **ISECompliance** (needed later).

## Client Setup and VPN Connection

1. Install the downloaded packages in order: **VPN Client** → **ISE Posture plugin** → **ISECompliance**.
2. Once install finishes, start **Cisco Secure Client**.
3. Make sure `access.visma.com` is in the address field.
4. Click **Connect**. You will be prompted for credentials.
5. Select the appropriate **Group** option:
   - For **unmanaged devices** (not registered on Visma AD): select `PersonalDevice` or `PersonalDevice-NoSplit`.
   - For **AD-registered Windows machines**: select `CorporateDevice` or `CorporateDevice-NoSplit`.

> **IMPORTANT:**
> We recommend using the normal `PersonalDevice` or `CorporateDevice` group options so that **only Visma office and DC-related traffic** flows through VPN.
> `*-NoSplit` group options will route **ALL traffic** via the VPN tunnel, including internet-related traffic.
> Please be aware of this and use them only when needed to access internet destinations that require you to be behind a trusted/known IP address.
> To save bandwidth, it is strongly recommended that YouTube or other similar streaming services should **not** be used while connected with the `*-NoSplit` options.

6. Enter your regular Visma username + password and click **"OK"**.
   - Example username: `john.doe` — no domain name before user or `@visma.com` at the end.

> **IMPORTANT:** If login fails at this point and you are sure the credentials are correct, most probably your user does not have any 2FA token assigned (SMS or Google Auth). Login does not work without a 2FA token. You can enrol a token yourself via the [Selfservice Portal](https://selfservice2fa.visma.com/) or ask for support via **Visma ServiceDesk** in the One Support Portal.

7. When prompted, input the **OTP 2FA token** or **SMS code**.
   - SMS is sent to the phone number registered for your Visma AD user.
   - For enabling OTP 2FA token, go to the Selfservice Portal or contact Visma ServiceDesk.
8. **System scan will start.**
   - If it does not, uninstall any Cisco AnyConnect or Cisco Secure Client related software from your computer and restart from the beginning. You might have had the AnyConnect client installed previously.
   - You will still need to have an active Firewall, up-to-date Anti-Virus and Anti-Malware tool, and up-to-date OS updates.
   - You have **15 minutes** to resolve any issues, then VPN will auto-disconnect. If the time is not enough, you can reconnect anytime and continue from where you left off.
9. After the scan is successful, you will reach **"compliant"** status and access to Visma resources is granted via VPN.

## Related Articles

- [Linux Ubuntu LTS — Installation and setup of Cisco AnyConnect](vpn-install-linux.md)
- [Mac OS X — Installation and setup of Cisco AnyConnect](vpn-install-macos.md)
- [MS Windows OS — Installation and setup of Cisco AnyConnect](vpn-install-windows.md)
- [Chrome OS — Installation and setup of Cisco AnyConnect](vpn-install-chrome.md)
