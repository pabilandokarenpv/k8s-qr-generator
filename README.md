# Kubernetes QR Code Generator with GitHub Codespaces

A hands-on project for learning Kubernetes by building and deploying a dynamic QR code generator microservice—entirely in your browser using GitHub Codespaces.

## What You'll Learn

- **Containers** - Packaging applications with Docker
- **Kubernetes Fundamentals** - Pods, Deployments, Services, and kubectl
- **Self-Healing** - Watch Kubernetes automatically restart failed Pods
- **Scaling** - Scale from 3 to 5 replicas with a single command
- **Load Balancing** - See traffic distributed across multiple Pods
- **Rolling Updates** - Update your app with zero downtime
- **GitHub Codespaces** - Cloud development without local setup

## What This App Does

Generates QR codes for:
- **URLs** - Share links
- **vCards** - Contact information (name, phone, email)
- **WiFi** - Auto-connect network credentials
- **Text** - Any message or data

## Quick Start

1. **Fork this repository**
2. Click **Code** → **Codespaces** → **Create codespace on main**
3. Wait 60 seconds for setup
4. Follow the tutorial in the article

## Project Structure
```
├── .devcontainer/
│   └── devcontainer.json    # Codespaces configuration
├── app/
│   ├── app.py               # Flask application
│   └── qr_types.py          # QR code formatters
├── k8s/
│   ├── deployment.yaml      # Kubernetes Deployment
│   └── service.yaml         # Kubernetes Service
├── requirements.txt         # Python dependencies
└── Dockerfile              # Container image
```

## Quick Test

Once deployed, generate a QR code:
```bash
curl -X POST http://localhost:8080/generate \
  -H "Content-Type: application/json" \
  -d '{
    "type": "url",
    "data": {"url": "https://tutorialsdojo.com"}
  }'
```

## Requirements

- GitHub account (free tier includes 60 hours/month of Codespaces)
- No local installation needed!

---

All the code from this article is available in this repository. Fork it, clone it to your Codespace, and start experimenting.

You now know more about Kubernetes than most developers who've never touched it. You've done what many put off for months because "it's too complicated."

The best part? You did it all in your browser, without filling your hard drive with Docker images or melting your laptop.

Kubernetes isn't scary anymore. It's just YAML files and kubectl commands. Keep experimenting, keep breaking things, fix them, and keep learning.

**Now go build something real.**

---

## Resources

- [Full Tutorial Article](YOUR_ARTICLE_LINK_HERE)
- [Kubernetes Documentation](https://kubernetes.io/docs/home/)
- [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
- [GitHub Codespaces Docs](https://docs.github.com/en/codespaces)

## License

MIT License - Feel free to use this for learning and experimentation.