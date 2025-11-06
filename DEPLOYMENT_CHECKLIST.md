# ✅ Cloudflare Pages Deployment Checklist

Use this checklist to ensure a smooth deployment process.

## Pre-Deployment

- [ ] Repository is pushed to GitHub
- [ ] All files are committed (check with `git status`)
- [ ] `index.html` is at the root of the repository
- [ ] All assets (CSS, JS, images) are in the repository
- [ ] Tested locally with `npm start` (site works on http://localhost:8000)

## Step 1: Cloudflare Pages Setup

- [ ] Logged into Cloudflare Dashboard
- [ ] Navigated to Pages section
- [ ] Clicked "Create a project" / "Connect to Git"
- [ ] Connected GitHub account
- [ ] Selected repository: `VergneElliot/MuseBar`
- [ ] Configured build settings:
  - [ ] Project name: `muse-bar` (or your choice)
  - [ ] Production branch: `main`
  - [ ] Build command: (leave empty)
  - [ ] Build output directory: `.` (dot/current directory)
- [ ] Clicked "Save and Deploy"
- [ ] Deployment completed successfully
- [ ] Preview URL works: `https://muse-bar.pages.dev` (or similar)

## Step 2: Custom Domain Configuration

- [ ] Have your domain name ready (e.g., `musebar.fr`)
- [ ] In Pages project, go to "Custom domains" tab
- [ ] Clicked "Set up a custom domain"
- [ ] Entered domain name
- [ ] DNS configured (automatic if domain on Cloudflare, or manual CNAME/A record)
- [ ] SSL/TLS certificate provisioned (check SSL/TLS tab)
- [ ] Waited 5-10 minutes for DNS propagation
- [ ] Tested custom domain in browser
- [ ] HTTPS works (green lock icon)

## Step 3: Testing

### Functionality Tests
- [ ] Homepage loads
- [ ] Navigation works
- [ ] Menu displays correctly
- [ ] All images load
- [ ] Google Maps embed works
- [ ] Fonts load correctly
- [ ] Icons display
- [ ] Smooth scrolling works
- [ ] Animations work

### Responsive Tests
- [ ] Mobile view (< 576px)
- [ ] Tablet view (768px - 991px)
- [ ] Desktop view (1200px+)

### Browser Tests
- [ ] Chrome/Edge
- [ ] Firefox
- [ ] Safari (if available)
- [ ] Mobile browser

### Performance Tests
- [ ] Page loads quickly
- [ ] No console errors (F12 → Console)
- [ ] No 404 errors (F12 → Network tab)
- [ ] HTTPS is active

## Step 4: Post-Deployment

- [ ] Bookmarked Cloudflare Pages dashboard
- [ ] Verified automatic deployments work (push to GitHub)
- [ ] Documented custom domain for future reference
- [ ] Shared site URL with team/stakeholders

## Troubleshooting

If something doesn't work:

1. **Check browser console** (F12 → Console) for errors
2. **Check Network tab** (F12 → Network) for failed requests
3. **Verify DNS** using `nslookup yourdomain.com` or online DNS checker
4. **Check Cloudflare Pages logs** in the dashboard
5. **Clear browser cache** (Ctrl+Shift+R)
6. **Wait for DNS propagation** (can take up to 48 hours, usually 5-10 minutes)

## Quick Commands

```bash
# Test locally
cd MuseBar
npm start

# Deploy (automatic via Git)
git add .
git commit -m "Update site"
git push origin main

# Check deployment status
# Visit: https://dash.cloudflare.com/ → Pages → Your Project
```

---

**Status**: ⬜ Not Started | 🟡 In Progress | ✅ Complete

