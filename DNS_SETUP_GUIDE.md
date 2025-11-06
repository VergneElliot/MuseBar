# 🌐 DNS Setup Guide for musebar.fr

## Quick Answer

**You only need to do ONE thing:** Update your nameservers at your domain registrar (where you bought `musebar.fr`).

**Everything else is automatic!** Once nameservers are updated, Cloudflare Pages will automatically create all the DNS records needed for your website.

---

## Step-by-Step Instructions

### Step 1: Find Your Domain Registrar

1. Go to: https://lookup.icann.org/
2. Enter: `musebar.fr`
3. Click "Lookup"
4. Look for "Registrar" - this tells you where you bought the domain

**Common registrars:**
- OVH (common for .fr domains)
- Gandi
- Namecheap
- GoDaddy
- Google Domains

### Step 2: Log Into Your Registrar

1. Go to your registrar's website
2. Log into your account
3. Find your domain: `musebar.fr`
4. Look for "DNS Settings", "Nameservers", or "DNS Management"

### Step 3: Update Nameservers

**IMPORTANT:** You need to replace your current nameservers with Cloudflare's nameservers.

**Cloudflare Nameservers (copy these):**
```
anirban.ns.cloudflare.com
dorthy.ns.cloudflare.com
```

**What to do:**
1. Find the nameserver/DNS section in your registrar's dashboard
2. **Delete** all existing nameservers
3. **Add** these two Cloudflare nameservers:
   - `anirban.ns.cloudflare.com`
   - `dorthy.ns.cloudflare.com`
4. **Save** your changes

**⚠️ Important Notes:**
- Make sure you add BOTH nameservers
- Delete any old nameservers (don't keep them)
- Save your changes

### Step 4: Turn Off DNSSEC (If Enabled)

1. In your registrar's dashboard, look for "DNSSEC" settings
2. If it's enabled, **turn it OFF**
3. You can re-enable it later in Cloudflare if needed
4. Save changes

### Step 5: Wait for Propagation

1. Go back to Cloudflare Dashboard
2. The "Invalid nameservers" warning should disappear within 5-30 minutes
3. Sometimes it can take up to 48 hours (but usually much faster)

**How to check if it worked:**
- Go to Cloudflare Dashboard → `musebar.fr` → Overview
- The "Invalid nameservers" badge should change to "Active" (green)

---

## What Happens Next (Automatic!)

Once Cloudflare detects the nameservers are updated:

1. ✅ **Cloudflare becomes your DNS provider** (automatic)
2. ✅ **Cloudflare Pages automatically creates DNS records** for your site (automatic)
3. ✅ **SSL certificate is automatically provisioned** (automatic)
4. ✅ **Your website goes live** at `musebar.fr` (automatic)

**You don't need to manually add any DNS records!** Cloudflare Pages will handle everything automatically.

---

## Connecting Your Pages Site to the Domain

After nameservers are updated:

1. Go to: Cloudflare Dashboard → **Pages** → Your Project (`muse-bar`)
2. Go to: **Custom domains** tab
3. Click: **"Set up a custom domain"**
4. Enter: `musebar.fr` (or `www.musebar.fr`)
5. Cloudflare will automatically:
   - Create the necessary DNS records
   - Provision SSL certificate
   - Connect your Pages site to the domain

---

## Common Questions

### Q: Do I need to manually add DNS records?
**A:** No! Once nameservers are updated and you connect the domain in Cloudflare Pages, all DNS records are created automatically.

### Q: Will my website go down during this process?
**A:** Usually no, but there might be a brief moment during the transition. The change is typically seamless.

### Q: How long does it take?
**A:** 
- Nameserver update: 5-30 minutes (sometimes up to 48 hours)
- DNS records creation: Automatic, happens immediately after nameservers are updated
- SSL certificate: 5-10 minutes after domain is connected

### Q: What if I can't find the nameserver settings?
**A:** 
- Check your registrar's help documentation
- Look for "DNS", "Nameservers", "DNS Management", or "Domain Settings"
- Contact your registrar's support if needed

### Q: Can I use both www and non-www?
**A:** Yes! After connecting `musebar.fr`, you can also add `www.musebar.fr` in the Cloudflare Pages custom domains section. Cloudflare will automatically create the DNS records for both.

---

## Troubleshooting

### "Invalid nameservers" still showing after 1 hour
- Double-check that you saved the changes at your registrar
- Verify you added BOTH nameservers correctly
- Make sure you deleted the old nameservers
- Wait a bit longer (can take up to 48 hours in rare cases)

### Can't find nameserver settings at registrar
- Try searching for "DNS" or "Nameservers" in the registrar's help section
- Contact your registrar's support
- Some registrars call it "Authoritative DNS" or "DNS Servers"

### Website not working after nameserver update
- Wait 10-15 minutes for DNS propagation
- Clear your browser cache
- Try accessing from a different network/device
- Check Cloudflare Pages deployment status

---

## Summary

**What you need to do (manual, one-time):**
1. ✅ Update nameservers at your registrar
2. ✅ Turn off DNSSEC (if enabled)

**What Cloudflare does automatically:**
1. ✅ Creates DNS records for your Pages site
2. ✅ Provisions SSL certificate
3. ✅ Routes traffic to your website
4. ✅ Provides CDN and security features

**Total manual work:** ~5 minutes at your registrar
**Everything else:** Automatic! 🎉

---

## Need Help?

If you're stuck:
1. Check your registrar's documentation for "changing nameservers"
2. Contact your registrar's support
3. Check Cloudflare's documentation: https://developers.cloudflare.com/dns/

Once nameservers are updated, come back and we'll connect your Pages site to the domain!

