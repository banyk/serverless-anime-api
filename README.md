# AniSearch – Serverless Anime Discovery Platform

AniSearch is a minimalist and serverless web application that allows users to search for anime titles and browse anime metadata — all powered by AWS Lambda, API Gateway, DynamoDB, and S3.

---

## ✨ Features

- 🔍 **Search Anime** by title using a simple search bar
- 📃 **View all Anime** in the database with one click
- ☁️ **Fully serverless** backend (Lambda + DynamoDB + API Gateway)
- 🖼️ **Anime covers stored in S3**, dynamically rendered in results
- ⚡ **Frontend hosted on S3**, styled in pure HTML + CSS + JavaScript
- 🌐 **CORS-enabled API** allows smooth browser interaction

---

## 🧱 Architecture

User (browser)

↓
Static Frontend (S3 Website Hosting)

↓
JavaScript fetch() requests (API calls)

↓
API Gateway (REST API)

↓
AWS Lambda (Python, boto3)

↓
DynamoDB (Anime metadata)

↓
S3 (Anime cover images)

---

## 🛠️ Technologies Used

- **AWS Lambda** – Python backend
- **API Gateway** – REST interface
- **DynamoDB** – Serverless NoSQL database for anime metadata
- **S3** – Static hosting + cover image storage
- **HTML + CSS + JavaScript** – Fully static frontend
- **boto3** – Python SDK for AWS

---

## 🚀 Live Demo

**Frontend (static website)**  
📍 `[http://anime-api-website.s3-website-us-east-1.amazonaws.com/](http://anime-api-website.s3-website-us-east-1.amazonaws.com/)`

**API endpoint**  
📍 `[https://448miw4o32.execute-api.us-east-2.amazonaws.com/prod/anime](https://448miw4o32.execute-api.us-east-2.amazonaws.com/prod/anime)`

> You can run a query like:  
> `[https://448miw4o32.execute-api.us-east-2.amazonaws.com/prod/anime?q=attack](https://448miw4o32.execute-api.us-east-2.amazonaws.com/prod/anime?q=attack)`

