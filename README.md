# 💓 Civic Pulse

**An AI-powered, anonymous community reporting platform designed for the Google Solution Challenge 2026.**

## 📌 Problem Statement
Communities often face delayed resolutions to civic issues (infrastructure damage, environmental hazards, child welfare needs) due to fragmented reporting channels. Citizens fear retaliation or lack the time to navigate complex municipal portals, resulting in low reporting volumes and inefficient manual routing to the correct local NGOs.

## 💡 Solution Overview
Civic Pulse bridges the gap between citizens and NGOs. It provides a secure, 100% anonymous platform for citizens to report local issues. Utilizing an AI allocation engine, the platform instantly analyzes the problem description, categorizes it into specific niches, and directly alerts the most relevant local NGO to take action.

## ✨ Key Features
* **100% Anonymous Reporting:** Protects whistleblower identity automatically.
* **AI Smart Routing:** Automatically categorizes text descriptions into niche civic issues.
* **Community Voting:** Allows citizens to upvote pressing issues, automatically alerting NGOs to critical priorities.
* **Gamified Civic Hub:** Users earn "Pulse Points" and unlock badges (Citizen, Guardian, Legend) to encourage continuous community engagement.
* **NGO Live Dashboard:** A dedicated administrative view for NGOs to monitor smart-routed feeds and resource distribution metrics.

## 🛠 Tech Stack
* **Frontend:** HTML5, Tailwind CSS, Vanilla JavaScript, Chart.js
* **Backend:** Python, Flask
* **AI Engine:** Groq API (Llama-3-70b-versatile) for intelligent text classification.
* **Cloud & Database:** Firebase Realtime Database / Firebase Admin SDK (Google Cloud).

## ☁️ Google Cloud Integration
This project integrates **Google Cloud via Firebase**. The Firebase Admin SDK is utilized to securely manage backend administrative privileges and handle potential real-time synchronization of civic reports between the citizen client and the NGO dashboard. 

## 🚀 How to Run the Project Locally

### 1. Clone the repository
```bash
git clone [https://github.com/bhaveshksahu/civic-pulse.git](https://github.com/bhaveshksahu/civic-pulse.git)
cd civic-pulse