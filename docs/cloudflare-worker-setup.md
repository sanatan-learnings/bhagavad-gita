# Cloudflare Worker Setup Guide

This guide walks you through deploying the OpenAI API proxy worker to Cloudflare, eliminating the need for users to provide their own API keys.

## Why Use a Cloudflare Worker?

- **Better UX**: Users don't need to get/enter their own OpenAI API keys
- **Security**: Your API key stays secure on Cloudflare's edge
- **Cost Control**: You manage and monitor API usage centrally
- **Free Tier**: 100,000 requests/day on Cloudflare's free plan

## Prerequisites

1. **Cloudflare Account**: Sign up at https://cloudflare.com (free)
2. **OpenAI API Key**: Get from https://platform.openai.com/api-keys
3. **Node.js**: For Wrangler CLI (https://nodejs.org)

## Step 1: Install Wrangler CLI

```bash
npm install -g wrangler
```

Verify installation:
```bash
wrangler --version
```

## Step 2: Login to Cloudflare

```bash
wrangler login
```

This opens a browser window for authentication. Approve the access.

## Step 3: Get Your Account ID

1. Go to https://dash.cloudflare.com/
2. Click on "Workers & Pages" in the left sidebar
3. Your Account ID is displayed on the right side
4. Copy it

Edit `wrangler.toml` and add your account ID:
```toml
account_id = "your-account-id-here"
```

## Step 4: Set OpenAI API Key as Secret

```bash
wrangler secret put OPENAI_API_KEY
```

When prompted, paste your OpenAI API key. This stores it securely in Cloudflare (encrypted, never logged).

**Important**: Never commit your API key to Git! It's stored securely on Cloudflare.

## Step 5: Deploy the Worker

```bash
wrangler deploy
```

The output will show your worker URL:
```
Published bhagavad-gita-api (X.XX sec)
  https://bhagavad-gita-api.your-subdomain.workers.dev
```

**Copy this URL** - you'll need it in the next step.

## Step 6: Update Frontend Configuration

Edit `assets/js/guidance.js` and update the `WORKER_URL`:

```javascript
// Line ~30
const WORKER_URL = 'https://bhagavad-gita-api.your-subdomain.workers.dev';
```

Commit and push:
```bash
git add assets/js/guidance.js
git commit -m "Configure Cloudflare Worker URL"
git push
```

## Step 7: Test the Worker

1. Visit your site: https://sanatan-learnings.github.io/bhagavad-gita/guidance.html
2. Notice the API key section is now hidden
3. Type a question: "How do I overcome fear?"
4. You should receive a response without needing to enter an API key

## Monitoring Usage

Track your worker usage and costs:

1. **Worker Dashboard**: https://dash.cloudflare.com/ → Workers & Pages → bhagavad-gita-api
2. **OpenAI Usage**: https://platform.openai.com/usage

### Expected Costs

| Item | Cost |
|------|------|
| Cloudflare Worker | FREE (100k req/day) |
| OpenAI Query Embedding | ~$0.00002 per query |
| OpenAI Chat Completion | ~$0.01 per response |
| **Per User Query** | **~$0.01** |

For 1,000 daily queries: ~$10/month

## Troubleshooting

### Worker not found
```bash
wrangler whoami  # Check authentication
wrangler deploy  # Redeploy
```

### CORS errors
The worker is configured for `https://sanatan-learnings.github.io`. If testing locally, temporarily change CORS origin in `workers/cloudflare-worker.js`:

```javascript
const CORS_HEADERS = {
  'Access-Control-Allow-Origin': '*',  // Allow all for testing
  // ...
};
```

Don't forget to change it back to the production domain before deploying!

### API key errors
```bash
# Check if secret is set
wrangler secret list

# Update secret
wrangler secret put OPENAI_API_KEY
```

### Rate limiting
The worker includes rate limiting (10 requests/minute per IP). Adjust in `workers/cloudflare-worker.js`:

```javascript
const RATE_LIMIT = {
  requests: 10,    // Increase if needed
  per: 60 * 1000,  // Time window
};
```

## Local Development

Test the worker locally before deploying:

```bash
# Start local worker
wrangler dev

# Test with curl
curl -X POST http://localhost:8787 \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "Test"}]}'
```

For local dev, set OPENAI_API_KEY in `.dev.vars` file:
```bash
echo "OPENAI_API_KEY=sk-..." > .dev.vars
```

**Never commit .dev.vars!** (Already in .gitignore)

## Updating the Worker

After making changes to `workers/cloudflare-worker.js`:

```bash
wrangler deploy
```

No need to reset secrets - they persist across deployments.

## Security Best Practices

1. **Restrict CORS**: Set `Access-Control-Allow-Origin` to your domain only
2. **Monitor Usage**: Check Cloudflare & OpenAI dashboards regularly
3. **Rate Limiting**: Enabled by default, adjust as needed
4. **Rotate Keys**: Change OpenAI API key periodically
5. **Budget Alerts**: Set up billing alerts on OpenAI dashboard

## Alternative: User-Provided Keys

If you prefer users to bring their own API keys:

In `assets/js/guidance.js`, set:
```javascript
const WORKER_URL = '';  // Empty string
```

The frontend will fall back to user-provided API keys stored in localStorage.

## Undeploying

To remove the worker:

```bash
wrangler delete
```

## Support

- Cloudflare Docs: https://developers.cloudflare.com/workers/
- Wrangler Docs: https://developers.cloudflare.com/workers/wrangler/
- OpenAI API Docs: https://platform.openai.com/docs/
