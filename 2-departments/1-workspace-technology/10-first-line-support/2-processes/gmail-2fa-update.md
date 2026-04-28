---
data_status: verified
---

# Change Phone Number and Authenticator for Gmail 2FA

**Owner:** Unified Access & Endpoint (Identity Access Management)  
**Stakeholders:** All employees, IT Service Desk, 1st-line support  
**Last reviewed:** 2026-04-21  
**Review cadence:** Quarterly  
**Target audience:** Employees who need to update 2FA settings

---

## Purpose

Enable employees to securely update their phone number and authenticator (TOTP) token for Gmail/Google Account two-step verification (2FA). This process ensures continued access to company Google Workspace while maintaining security.

---

## Prerequisites

- Active Visma/Google Workspace account
- Access to current phone with authenticator app (Google Authenticator or Microsoft Authenticator)
- Access to backup codes (if phone is unavailable)

---

## Step-by-Step Instructions

### Phase 1: Obtain Backup Codes (Preparation)

1. **Create a support ticket:**
   - Go to https://jira.visma.com/servicedesk/customer/portal/8
   - Request a Google backup code for your account
   - Wait for IT support to provide you with 8-digit backup codes

### Phase 2: Sign In Using Backup Code

2. **Log in to Gmail:**
   - Go to https://mail.google.com
   - Enter your Visma email address and password

3. **If prompted for 2FA:**
   - Click "Can't use your phone?"
   - Click "Try another way"
   - Enter one of the 8-digit backup codes provided by support
   - **Note:** Backup codes are one-time use only

### Phase 3: Update Phone Number

4. **Access 2-step verification settings:**
   - Go to https://myaccount.google.com/signinoptions/twosv
   - Navigate to the "2-Step Verification Phones" section

5. **Update your phone:**
   - Delete the old phone number
   - Add your new phone number
   - Save the changes

### Phase 4: Update Authenticator Token

6. **Remove the old authenticator:**
   - In the 2-step verification settings, find the "Security keys" or "Authenticator app" section
   - Click the bin/delete icon next to your current token
   - Confirm deletion

7. **Enroll new authenticator:**
   - A prompt will appear to "Re-enroll" the authenticator
   - Click "Re-enroll"
   - A QR code will be displayed

8. **Scan the QR code:**
   - Open your authenticator app (Google Authenticator or Microsoft Authenticator) on your phone
   - Scan the QR code
   - A new 6-digit code should appear in the app for Gmail

### Phase 5: Verify and Complete

9. **Confirm the new setup:**
   - Return to the Google Account settings
   - You should see confirmation that the new authenticator has been enrolled
   - Try logging out and back in using your new phone's authenticator code

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Backup codes not received | Contact IT Service Desk; allow 1-2 hours for processing |
| QR code won't scan | Ensure good lighting; try a different phone camera; contact support |
| New authenticator code not appearing | Ensure time is synced on your phone; reinstall authenticator app; try again |
| Can't access Gmail at all | Use your backup code; if none available, escalate to Unified Access & Endpoint team |

---

## Escalation

| Scenario | Action | Owner |
|----------|--------|-------|
| Backup codes unavailable | Submit ticket to IT Service Desk | 1st-line support → Unified Access & Endpoint |
| Phone lost/unavailable | Contact IT Service Desk immediately; provide recovery info | Unified Access & Endpoint (IAM) |
| Account locked after failed attempts | Contact IT Service Desk; request account unlock | IT Service Desk |
| Technical issues with authenticator app | Contact 1st-line support or app vendor support | 1st-line support / Unified Access & Endpoint |

---

## Success Criteria

- [ ] Old phone number is removed from Google Account
- [ ] Old authenticator token is deleted
- [ ] New phone number is registered
- [ ] New authenticator token is enrolled and generating codes
- [ ] Successful test login using new authenticator code

---

## Related Documents

- `README.md` – Workspace Technology processes index
- [Unified Access & Endpoint team overview](../1-overview.md#4-unified-access--endpoint) – Team responsible for identity management
- Support portal: https://jira.visma.com/servicedesk/customer/portal/8

---

## How Employees Should Use This Document

1. Read through all steps before starting
2. Request backup codes first (Phase 1)
3. Follow each phase sequentially
4. Contact IT Service Desk if you get stuck at any step
5. Allow 15–30 minutes for the entire process

---

*Process published: 2026-04-21*
