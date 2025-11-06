# 🔧 Deployment Troubleshooting Guide

## Issue: Cloudflare Pages Deploying Old Commit

If Cloudflare Pages is deploying an old commit instead of the latest one, follow these steps:

### Solution 1: Trigger Manual Redeployment (Recommended)

1. **Go to Cloudflare Pages Dashboard**
   - Visit: https://dash.cloudflare.com/
   - Navigate to: Pages → Your Project (`muse-bar`)

2. **Trigger New Deployment**
   - Click on the **"Deployments"** tab
   - Click **"Retry deployment"** on the failed deployment, OR
   - Click **"Create deployment"** → Select branch `main` → Click **"Deploy"**

3. **Verify Latest Commit**
   - The deployment should now use commit `0c0457e` (Optimize images)
   - Check the deployment logs to confirm

### Solution 2: Check Branch Configuration

1. **Verify Branch Settings**
   - Go to: Pages → Your Project → **Settings** → **Builds & deployments**
   - Ensure **Production branch** is set to: `main`
   - Ensure **Auto-deploy** is enabled

2. **Check Deployment Trigger**
   - Go to: Pages → Your Project → **Deployments**
   - Look for the latest deployment
   - Verify it's deploying from the correct commit

### Solution 3: Force Push (If Needed)

If the above doesn't work, you can create a small change to trigger a new deployment:

```bash
cd MuseBar
# Make a small change (like updating a comment)
echo "# Optimized for Cloudflare Pages" >> README.md
git add README.md
git commit -m "Trigger new deployment with optimized images"
git push origin main
```

This will trigger Cloudflare Pages to automatically deploy the latest code.

### Solution 4: Verify GitHub Repository

Check that the optimized images are actually in GitHub:

1. Visit: https://github.com/VergneElliot/MuseBar
2. Navigate to: `images/cavepv.png`
3. Check the file size (should be ~3.6 MB, not 36 MB)
4. Verify the latest commit is: `0c0457e Optimize images for Cloudflare Pages deployment`

### Solution 5: Clear Cloudflare Cache

If deployments are still using old files:

1. Go to: Cloudflare Dashboard → Your Domain → **Caching** → **Configuration**
2. Click **"Purge Everything"** (if available)
3. Or wait 5-10 minutes for cache to clear

---

## Current Status Check

To verify your repository is ready:

```bash
cd MuseBar

# Check latest commit
git log --oneline -1
# Should show: 0c0457e Optimize images for Cloudflare Pages deployment

# Check image sizes
ls -lh images/cavepv.png images/carrousel/cave.png
# Both should be under 4 MB

# Verify remote is correct
git remote -v
# Should show: https://github.com/VergneElliot/MuseBar.git
```

---

## Expected Deployment Log

After triggering a new deployment, you should see in the logs:

```
HEAD is now at 0c0457e Optimize images for Cloudflare Pages deployment
...
Success: Finished cloning repository files
...
Success: Deployed successfully
```

If you still see `7369340` in the logs, the deployment is using an old commit and you need to trigger a new one.

---

## Still Having Issues?

1. **Check Cloudflare Pages Logs**
   - Go to: Pages → Your Project → Deployments → Click on deployment → View logs
   - Look for the commit hash in the logs

2. **Verify GitHub Webhook**
   - Cloudflare Pages uses GitHub webhooks for auto-deployment
   - Check if webhooks are properly configured in GitHub repository settings

3. **Contact Support**
   - If none of the above works, there might be a Cloudflare Pages configuration issue
   - Check Cloudflare Pages documentation or support

---

## Quick Fix Command

If you want to quickly trigger a new deployment:

```bash
cd MuseBar
git commit --allow-empty -m "Trigger Cloudflare Pages redeployment"
git push origin main
```

This creates an empty commit that will trigger Cloudflare Pages to deploy the latest code (including the optimized images).

