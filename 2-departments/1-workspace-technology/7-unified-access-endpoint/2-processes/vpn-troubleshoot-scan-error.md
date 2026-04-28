# 2.7.2. VPN — Troubleshoot: System Scan Error "Failed to Launch the Downloader"

| Field | Details |
|---|---|
| **Description** | System Scan is giving the error "Failed to launch the downloader" |
| **Purpose / Audience** | Assist anyone in Visma with the system scan error |
| **Scope** | For the recent problem where System Scan is giving the error "Failed to launch the downloader" |

## Resolution Steps

1. **Disconnect from the VPN.** Go to the Systray and close the application.

2. In the **Start menu**, type `Cisco` and choose **Open File Location**.

3. In the newly opened window, **right-click** on **"Cisco AnyConnect Secure Mobility Client"** and click **Properties**.

4. Go to the **Compatibility** tab, scroll down to **Settings**, and check (tick) the box **"Run this program as an administrator"**.

5. Click **OK**.

6. Reconnect to VPN and attempt the system scan again.
