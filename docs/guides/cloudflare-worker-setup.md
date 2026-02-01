# Cloudflare Worker Setup

Deploy the OpenAI API proxy to Cloudflare so users don't need their own API keys.

## Quick Deploy

If you have [verse-content-sdk](https://github.com/sanatan-learnings/verse-content-sdk) installed:

```bash
verse-deploy
```

Otherwise, follow the setup steps below.

## Why Use This?

- Users don't need to enter API keys
- Your API key stays secure on Cloudflare
- Free tier: 100,000 requests/day
- Cost: ~$0.01 per user query

## Setup

### 1. Install Wrangler

```bash
npm install -g wrangler
wrangler login
```

### 2. Configure Account

Get your account ID from https://dash.cloudflare.com/ → Workers & Pages

Edit `wrangler.toml`:
```toml
account_id = "your-account-id-here"
```

### 3. Set API Key

```bash
wrangler secret put OPENAI_API_KEY
# Paste your OpenAI API key when prompted
```

### 4. Deploy

```bash
wrangler deploy
```

Copy the worker URL from the output: `https://bhagavad-gita-api.your-subdomain.workers.dev`

### 5. Update Frontend

Edit `assets/js/guidance.js`:

```javascript
const WORKER_URL = 'https://bhagavad-gita-api.your-subdomain.workers.dev';
```

Commit and push:

```bash
git add assets/js/guidance.js
git commit -m "Configure Cloudflare Worker URL"
git push
```

### 6. Test

Visit your site's guidance page and ask a question. It should work without entering an API key.

## Monitor Usage

- **Cloudflare**: https://dash.cloudflare.com/ → Workers & Pages
- **OpenAI**: https://platform.openai.com/usage

Expected costs: ~$10/month for 1,000 daily queries.

## Troubleshooting

**Worker not found:**
```bash
wrangler whoami
wrangler deploy
```

**CORS errors (local testing):**

Edit `workers/cloudflare-worker.js` temporarily:
```javascript
const CORS_HEADERS = {
  'Access-Control-Allow-Origin': '*',  // Change back to your domain before deploying
  // ...
};
```

**API key errors:**
```bash
wrangler secret list           # Check if set
wrangler secret put OPENAI_API_KEY  # Update
```

**Rate limiting:**

Edit `workers/cloudflare-worker.js` to adjust:
```javascript
const RATE_LIMIT = {
  requests: 10,     // Increase if needed
  per: 60 * 1000,
};
```

## Local Development

Test locally before deploying:

```bash
# Create .dev.vars file
echo "OPENAI_API_KEY=sk-..." > .dev.vars

# Start local server
wrangler dev

# Test
curl -X POST http://localhost:8787 \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "Test"}]}'
```

## Update Worker

After editing `workers/cloudflare-worker.js`:

```bash
wrangler deploy
```

Secrets persist across deployments.

## Resources

- [Cloudflare Workers Docs](https://developers.cloudflare.com/workers/)
- [OpenAI API Docs](https://platform.openai.com/docs/)
