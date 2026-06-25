# Deployment Guide

This guide explains how to deploy the Probability Paradoxes app to cloud platforms like Render.

## Prerequisites

- Git repository (GitHub, GitLab, or Bitbucket)
- Account on deployment platform (Render, Heroku, etc.)
- App code pushed to repository

## Deployment on Render

### Step 1: Prepare Your Repository

Ensure your repository has these files in the root:

```
✓ requirements.txt    # Python dependencies
✓ run_app.py         # Launcher script (optional)
✓ app/               # Application directory
  ✓ app.py          # Entry point
  ✓ pages/          # Page files
```

### Step 2: Create a New Web Service

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click **"New +"** → **"Web Service"**
3. Connect your Git repository
4. Select the repository containing your app

### Step 3: Configure Build Settings

**Basic Settings:**
- **Name:** `probability-paradoxes` (or your choice)
- **Region:** Choose closest to your users
- **Branch:** `main` (or your default branch)
- **Root Directory:** Leave blank (or specify if app is in subdirectory)

**Build Settings:**
- **Runtime:** `Python 3`
- **Build Command:**
  ```bash
  pip install -r requirements.txt
  ```

**Start Command:**
  ```bash
  streamlit run app/app.py --server.port=$PORT --server.address=0.0.0.0
  ```

**Instance Type:**
- **Free** (for testing)
- **Starter** or higher (for production)

### Step 4: Environment Variables (Optional)

If needed, add environment variables:
- Click **"Environment"** tab
- Add key-value pairs
- Example: `STREAMLIT_SERVER_HEADLESS=true`

### Step 5: Deploy

1. Click **"Create Web Service"**
2. Render will:
   - Clone your repository
   - Install dependencies
   - Start the app
3. Wait for deployment to complete (2-5 minutes)

### Step 6: Access Your App

Once deployed:
- Your app will be available at: `https://[your-app-name].onrender.com`
- Render provides a free `.onrender.com` subdomain
- You can add a custom domain in settings

---

## Alternative: Using `run_app.py`

If you prefer using the launcher script:

**Start Command:**
```bash
python run_app.py
```

**Note:** You'll need to modify `run_app.py` to accept Render's PORT:

```python
import subprocess
import sys
import os

def install_requirements():
    print("Installing requirements...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def run_app():
    print("Starting app...")
    port = os.environ.get("PORT", "8501")
    app_path = os.path.join("app", "app.py")
    
    subprocess.run([
        sys.executable, "-m", "streamlit", "run", app_path,
        f"--server.port={port}",
        "--server.address=0.0.0.0"
    ])

if __name__ == "__main__":
    if os.path.exists("requirements.txt"):
        install_requirements()
    run_app()
```

---

## Deployment on Other Platforms

### Heroku

**Procfile:**
```
web: streamlit run app/app.py --server.port=$PORT --server.address=0.0.0.0
```

**Commands:**
```bash
heroku create probability-paradoxes
git push heroku main
heroku open
```

### Streamlit Community Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click **"New app"**
3. Select repository, branch, and main file path: `app/app.py`
4. Click **"Deploy"**

**Advantages:**
- Free for public apps
- Automatic HTTPS
- Easy updates (push to Git)

### Railway

**Start Command:**
```bash
streamlit run app/app.py --server.port=$PORT --server.address=0.0.0.0
```

**Steps:**
1. Go to [railway.app](https://railway.app)
2. Click **"New Project"** → **"Deploy from GitHub repo"**
3. Select repository
4. Railway auto-detects Python and installs dependencies
5. Add start command in settings

### Google Cloud Run

**Dockerfile:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD streamlit run app/app.py --server.port=8080 --server.address=0.0.0.0
```

**Deploy:**
```bash
gcloud run deploy probability-paradoxes \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

---

## Configuration Tips

### Streamlit-Specific Settings

Create `.streamlit/config.toml` (already included):

```toml
[server]
headless = true
port = 8501
enableCORS = false
enableXsrfProtection = true

[browser]
gatherUsageStats = false

[client]
showSidebarNavigation = false

[theme]
base = "light"
primaryColor = "#6C63FF"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#31333F"
```

### Performance Optimization

**For Production:**

1. **Enable Caching:**
   ```python
   @st.cache_data
   def expensive_computation():
       ...
   ```

2. **Optimize Dependencies:**
   - Only include necessary packages in `requirements.txt`
   - Pin versions for reproducibility

3. **Resource Limits:**
   - Monitor memory usage
   - Upgrade instance if needed

### Security

**Best Practices:**

1. **Environment Variables:**
   - Never commit secrets to Git
   - Use platform's environment variable system

2. **HTTPS:**
   - Most platforms provide automatic HTTPS
   - Enforce HTTPS in production

3. **CORS:**
   - Configure `enableCORS` appropriately
   - Restrict origins if needed

---

## Troubleshooting

### Common Issues

**1. Port Binding Error**

**Problem:** App doesn't start, port error in logs

**Solution:** Ensure start command includes:
```bash
--server.port=$PORT --server.address=0.0.0.0
```

**2. Dependencies Not Installing**

**Problem:** Build fails, missing packages

**Solution:**
- Check `requirements.txt` is in root
- Verify all packages are spelled correctly
- Pin versions: `streamlit==1.49.1`

**3. App Crashes on Startup**

**Problem:** App starts but immediately crashes

**Solution:**
- Check logs for error messages
- Verify all imports work
- Test locally with same Python version

**4. Slow Performance**

**Problem:** App is slow or times out

**Solution:**
- Upgrade to paid tier (more resources)
- Optimize simulations (reduce iterations)
- Add caching with `@st.cache_data`

### Checking Logs

**Render:**
- Go to your service dashboard
- Click **"Logs"** tab
- View real-time logs

**Heroku:**
```bash
heroku logs --tail
```

**Streamlit Cloud:**
- Click **"Manage app"**
- View logs in dashboard

---

## Updating Your Deployment

### Automatic Updates

Most platforms support automatic deployment:

1. Push changes to Git:
   ```bash
   git add .
   git commit -m "Update app"
   git push origin main
   ```

2. Platform automatically:
   - Detects changes
   - Rebuilds app
   - Redeploys

### Manual Deployment

**Render:**
- Click **"Manual Deploy"** → **"Deploy latest commit"**

**Heroku:**
```bash
git push heroku main
```

---

## Monitoring

### Health Checks

**Render:**
- Automatic health checks
- Configure in service settings

**Custom Health Endpoint:**
```python
# Add to app.py
@st.cache_resource
def health_check():
    return {"status": "healthy"}
```

### Analytics

**Track Usage:**
- Render provides basic analytics
- Use Google Analytics for detailed tracking
- Monitor with Streamlit's built-in analytics

---

## Cost Optimization

### Free Tiers

**Render:**
- Free tier available
- Spins down after inactivity
- 750 hours/month free

**Streamlit Cloud:**
- Free for public apps
- Unlimited apps
- Community support

**Heroku:**
- Free tier discontinued
- Minimum $5/month

### Recommendations

**For Personal Projects:**
- Streamlit Community Cloud (free, easy)
- Render Free Tier (more control)

**For Production:**
- Render Starter ($7/month)
- Railway ($5/month)
- Heroku Standard ($25/month)

---

## Summary

### Quick Deployment Checklist

- [ ] Push code to Git repository
- [ ] Verify `requirements.txt` is complete
- [ ] Create account on deployment platform
- [ ] Create new web service
- [ ] Configure build command: `pip install -r requirements.txt`
- [ ] Configure start command: `streamlit run app/app.py --server.port=$PORT --server.address=0.0.0.0`
- [ ] Deploy and test
- [ ] Configure custom domain (optional)
- [ ] Set up monitoring

### Recommended Platform

**For this app:** **Render** or **Streamlit Community Cloud**

**Why:**
- Easy setup
- Free tier available
- Automatic HTTPS
- Good performance
- Simple Git integration

Your app should be live in under 10 minutes! 🚀
