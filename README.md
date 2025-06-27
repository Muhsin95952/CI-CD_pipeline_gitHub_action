# 🚀 Flask CI/CD Pipeline using GitHub Actions

This project demonstrates a basic CI/CD pipeline setup using **GitHub Actions** for a simple **Flask** web application. The pipeline builds a Docker image and pushes it to **Docker Hub** automatically upon every push to the `main` branch.

---

## 📁 Project Structure

flask-ci-cd-project/
├── app/
│ └── app.py
├── Dockerfile
├── requirements.txt
└── .github/
└── workflows/
└── ci-cd.yaml

yaml
Copy
Edit

---

## 🛠️ Technologies Used

- Python 3.10
- Flask
- Docker
- GitHub Actions
- Docker Hub

---

## 🚦 CI/CD Workflow Summary

1. Triggered on push to `main` branch.
2. Checks out the code.
3. Installs Python and dependencies.
4. Builds the Docker image.
5. Logs into Docker Hub using GitHub Secrets.
6. Pushes the image to Docker Hub.

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/flask-ci-cd-project.git
cd flask-ci-cd-project
2️⃣ Add Your Docker Hub Secrets in GitHub
Go to your GitHub repo:

Settings → Secrets and Variables → Actions → New Repository Secret

Add the following:

DOCKER_USERNAME → your Docker Hub username

DOCKER_PASSWORD → your Docker Hub password or access token

🐳 Run the App Locally Using Docker
After the GitHub Action has pushed the image to Docker Hub:

bash
Copy
Edit
docker pull yourdockerusername/flask-ci-cd:latest
docker run -d -p 5000:5000 yourdockerusername/flask-ci-cd:latest
Then visit: http://localhost:5000

✅ Output
csharp
Copy
Edit
Hello from Flask CI/CD pipeline!
📌 What You Learn
How to build and Dockerize a Flask app.

How to set up a GitHub Actions pipeline.

How to automate Docker image builds and pushes using CI/CD.

📷 Screenshot

📄 License
This project is licensed under the MIT License - feel free to use and modify!

💡 Next Step
Head over to Day 2: Dockerize a Node.js App and Push to Docker Hub →

yaml
Copy
Edit

---

Let me know if you'd like a logo or badge included too—or ready to continue to Day 2?









