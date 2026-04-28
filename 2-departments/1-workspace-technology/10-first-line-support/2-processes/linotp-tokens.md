# 2.1.2. Managing LinOTP Tokens

LinOTP tokens are used for accessing VPNs and AWS (Amazon Web Services). Manage them via the self-service portal at https://selfservice2fa.visma.com/.

**Important:** Log in with the account that matches the service you need access to — use your internal account for VPN, and your CPA/dev_ account for AWS.

---

## Enrolling a New Token

1. Log in to https://selfservice2fa.visma.com/
2. Navigate to the **Enroll OATH soft token** tab.
3. Click **enroll your time based token**.
4. Open Google Authenticator on your phone, tap **+**, and select **Scan A QR code**.
5. Scan the QR code shown on screen.
6. Click **Ok**.

## Deleting an Existing Token

1. Go to the **delete Token** tab.
2. Select the token you want to remove.
3. Click **delete Token**.

## Resetting the Failcounter

The failcounter blocks login attempts after 10 consecutive failures (wrong password or token). To unblock:

1. Go to the **Reset Failcounter** tab.
2. Select the locked token.
3. Click **reset Failcounter**.

---

*Source: `_raw/Managing LinOTP Tokens.md`*
