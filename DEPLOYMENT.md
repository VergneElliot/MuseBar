# 🚀 Deployment Guide - Muse Bar Website

This guide will walk you through deploying the Muse Bar website to Cloudflare Pages.

## Prerequisites

- ✅ Cloudflare account (you already have one)
- ✅ GitHub account with the repository
- ✅ Custom domain name (optional, but recommended)

---

## Step 1: Set Up Cloudflare Pages

### 1.1 Access Cloudflare Pages

1. Log in to your [Cloudflare Dashboard](https://dash.cloudflare.com/)
2. In the left sidebar, click on **"Pages"**
3. Click **"Create a project"** or **"Connect to Git"**

### 1.2 Connect Your GitHub Repository

1. Select **"GitHub"** as your Git provider
2. Authorize Cloudflare to access your GitHub account (if not already done)
3. Select the repository: **`VergneElliot/MuseBar`**
4. Click **"Begin setup"**

### 1.3 Configure Build Settings

Since this is a static site with no build process, use these settings:

- **Project name**: `muse-bar` (or your preferred name)
- **Production branch**: `main`
- **Build command**: Leave empty (or use: `echo "No build needed"`)
- **Build output directory**: `.` (current directory - the root of the repo)

**Important**: The build output directory should be `.` because `index.html` is at the root of the repository.

### 1.4 Environment Variables

No environment variables are needed for this static site. Click **"Save and Deploy"**.

### 1.5 Wait for Deployment

Cloudflare Pages will:
1. Clone your repository
2. Deploy the site (should take 1-2 minutes)
3. Provide you with a preview URL: `https://muse-bar.pages.dev` (or similar)

---

## Step 2: Configure Custom Domain

### 2.1 Add Custom Domain in Cloudflare Pages

1. In your Cloudflare Pages project, go to **"Custom domains"** tab
2. Click **"Set up a custom domain"**
3. Enter your domain name (e.g., `musebar.fr` or `www.musebar.fr`)
4. Click **"Continue"**

### 2.2 DNS Configuration

Cloudflare will automatically detect if your domain is already on Cloudflare:

#### If your domain is already on Cloudflare:
- DNS records will be automatically configured
- SSL/TLS certificate will be automatically provisioned
- Wait 1-2 minutes for DNS propagation

#### If your domain is NOT on Cloudflare:
You have two options:

**Option A: Transfer domain to Cloudflare (Recommended)**
1. Follow Cloudflare's domain transfer guide
2. Once transferred, DNS will be automatically configured

**Option B: Configure DNS manually**
1. In your domain registrar's DNS settings, add a CNAME record:
   - **Name**: `@` (or `www` for www subdomain)
   - **Type**: `CNAME`
   - **Value**: `muse-bar.pages.dev` (your Cloudflare Pages URL)
   - **TTL**: `3600` (or auto)

2. For the root domain (`@`), you may need to use an A record instead:
   - **Name**: `@`
   - **Type**: `A`
   - **Value**: `192.0.2.1` (Cloudflare will provide the exact IP)
   - **TTL**: `3600`

### 2.3 SSL/TLS Configuration

1. Go to **SSL/TLS** in your Cloudflare dashboard
2. Ensure SSL/TLS encryption mode is set to **"Full"** or **"Full (strict)"**
3. Cloudflare Pages automatically provisions SSL certificates (may take a few minutes)

### 2.4 Verify Domain

1. Wait 5-10 minutes for DNS propagation
2. Visit your custom domain in a browser
3. You should see your Muse Bar website!

---

## Step 3: Test the Deployment

### 3.1 Basic Functionality Tests

Test the following on your deployed site:

- [ ] **Homepage loads correctly**
  - Visit your domain and verify the page loads

- [ ] **Navigation works**
  - Click through all navigation links
  - Verify smooth scrolling works

- [ ] **Menu displays correctly**
  - Check that all menu items load
  - Verify menu tabs switch properly
  - Test on mobile and desktop

- [ ] **Images load**
  - Verify all images in the carousel display
  - Check logo and other images

- [ ] **External resources**
  - Google Maps embed should work
  - Google Fonts should load
  - Font Awesome icons should display

- [ ] **Responsive design**
  - Test on mobile (use browser dev tools)
  - Test on tablet
  - Test on desktop

- [ ] **Performance**
  - Check page load speed
  - Verify HTTPS is working (green lock icon)

### 3.2 Browser Testing

Test in multiple browsers:
- [ ] Chrome/Edge
- [ ] Firefox
- [ ] Safari (if available)
- [ ] Mobile browsers (iOS Safari, Chrome Mobile)

### 3.3 Common Issues & Solutions

#### Issue: HTML fragments not loading
**Solution**: This usually means the site isn't being served over HTTPS. Cloudflare Pages automatically provides HTTPS, so this shouldn't happen. If it does, check your SSL/TLS settings.

#### Issue: Images not displaying
**Solution**: 
- Check image paths are correct (relative paths should work)
- Verify images are committed to the repository
- Check browser console for 404 errors

#### Issue: Custom domain not working
**Solution**:
- Wait 24-48 hours for full DNS propagation
- Check DNS records are correct
- Verify SSL certificate is provisioned (may take a few minutes)

#### Issue: Styling looks broken
**Solution**:
- Clear browser cache (Ctrl+Shift+R or Cmd+Shift+R)
- Check that all CSS files are loading (browser dev tools → Network tab)
- Verify file paths are correct

---

## Step 4: Continuous Deployment (Automatic Updates)

Cloudflare Pages automatically deploys when you push to your `main` branch:

1. Make changes to your code
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Update menu items"
   git push origin main
   ```
3. Cloudflare Pages will automatically:
   - Detect the push
   - Deploy the new version
   - Update your live site (usually within 1-2 minutes)

### 4.1 Preview Deployments

Cloudflare Pages also creates preview deployments for pull requests:
- Each PR gets its own preview URL
- Perfect for testing changes before merging
- Preview URLs are automatically generated

---

## Step 5: Monitoring & Analytics (Optional)

### 5.1 Cloudflare Analytics

Cloudflare Pages provides basic analytics:
- Page views
- Bandwidth usage
- Request analytics

Access via: Your Pages project → **"Analytics"** tab

### 5.2 Custom Analytics

You can add Google Analytics or other tracking:
1. Add tracking code to `index.html` in the `<head>` section
2. Commit and push
3. Deploy automatically

---

## Quick Reference

### Cloudflare Pages Dashboard
- **URL**: https://dash.cloudflare.com/
- **Pages Section**: Left sidebar → "Pages"

### Your Project URLs
- **Preview URL**: `https://muse-bar.pages.dev` (or similar)
- **Custom Domain**: `https://yourdomain.com` (once configured)

### Useful Commands

```bash
# Test locally before deploying
cd MuseBar
npm start
# Visit http://localhost:8000

# Deploy (automatic via Git push)
git add .
git commit -m "Your commit message"
git push origin main
```

---

## Support & Resources

- **Cloudflare Pages Docs**: https://developers.cloudflare.com/pages/
- **Cloudflare Support**: https://support.cloudflare.com/
- **GitHub Repository**: https://github.com/VergneElliot/MuseBar

---

## Checklist

Before going live, ensure:

- [ ] Site deploys successfully on Cloudflare Pages
- [ ] Custom domain is configured and working
- [ ] SSL certificate is active (HTTPS works)
- [ ] All pages and sections load correctly
- [ ] Images and assets display properly
- [ ] Navigation and interactions work
- [ ] Site is responsive on mobile/tablet/desktop
- [ ] Performance is acceptable
- [ ] No console errors in browser dev tools

---

**🎉 Congratulations! Your Muse Bar website is now live!**

For updates, simply push to GitHub and Cloudflare Pages will automatically deploy.

