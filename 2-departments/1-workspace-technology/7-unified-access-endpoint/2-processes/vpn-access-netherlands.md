# 2.7.2. VPN — Netherlands AnyConnect Access Instructions

This article provides a step-by-step guide on how to use the **Netherlands AnyConnect solution** to access customer "legacy networks". This solution was designed to meet the common requirement of all NL Visma onboarded companies.

The following instruction set covers the **Windows operating system** as an example, since the login info and profiles to choose from at connecting time are the same for all other supported AnyConnect client operating systems.

## Step-by-Step Guide

1. Start the **Netherlands AnyConnect Client**. Make sure the correct server address is in the address field.

2. Click **Connect**. You will be prompted for credentials.

3. Enter your regular Visma username + password and click **"OK"**.
   - Example username: `john.doe` — no domain name before user or `@` at the end.

   > **IMPORTANT:** If login fails at this point and you are sure the credentials are correct, most probably your user does not have any 2FA token assigned (SMS or Google Auth). Login does not work without a 2FA token. Please ask for support via **Visma ServiceDesk**.

4. When prompted, input the **OTP 2FA token** or **SMS code**.
   - SMS is sent to the phone number registered for your Visma AD user.
   - For enabling OTP 2FA token, please contact Visma ServiceDesk.

5. The **system scan** will start.
   - If it does not, uninstall any Cisco AnyConnect related software from your computer and restart from the beginning. You might have had the AnyConnect client installed previously.

6. After the scan is successful, you will get to **"compliant"** status and access to Visma resources is granted via VPN.

> **Important note:** When you connect for the first time to the NL AnyConnect solution, wait until you get the **"Network access allowed"** message and then verify that you get a client IP for the AnyConnect virtual NIC card from the correct IP pool.
>
> For this, compare the IP from `ipconfig` command output (for Windows) with the AnyConnect Company IP Pools list and ensure a match.
>
> If there is no match, you have to speak with the **VPN group owner** of your company (usually the IT manager) to put you in the correct group.
>
> Your company's AnyConnect VPN group name should be listed in the internal resources. If it isn't, then your company is not yet onboarded for AnyConnect access — you can request that by opening a ticket via ServiceDesk.

## AnyConnect Profiles Explained

| Profile | Description |
|---|---|
| `NL-Legacy-Split` | Allows dedicated/per-company access to their legacy networks and resources, while internet destinations are reachable outside the tunnel. |
| `NL-Legacy-NoSplit` | ALL traffic — dedicated/per-company legacy networks and internet access — is done via the tunnel. |
| `CorporateDevice-Split` | For users on a Visma (Intune) device whose company has migrated all legacy networks, services, and resources into NL Datacentre. Allows access to Datacentre hosted resources; internet destinations are reached outside the tunnel. |
| `CorporateDevice-NoSplit` | For users on a Visma (Intune) device whose company has migrated all legacy networks, services, and resources into NL Datacentre. Both Datacentre hosted resources and internet destinations are reached via the tunnel. |
| `PersonalDevice-Split` | For users on a personal device whose company has migrated all legacy networks, services, and resources into NL Datacentre. Allows access to Datacentre hosted resources; internet destinations are reached outside the tunnel. |
| `PersonalDevice-NoSplit` | For users on a personal device whose company has migrated all legacy networks, services, and resources into NL Datacentre. Both Datacentre hosted resources and internet destinations are reached via the tunnel. |

> **Note:** For reaching solutions that require whitelisting, you may need to whitelist the following public IP on the remote end side: `185.218.39.38`.

## Related Articles

- [Netherlands AnyConnect User Documentation and Access Instructions](vpn-access-netherlands.md)
- [Norway AnyConnect Access Instructions](vpn-access-norway.md)
- [Uninstalling Cisco AnyConnect VPN on macOS](vpn-uninstall-macos.md)
