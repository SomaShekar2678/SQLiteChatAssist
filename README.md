# SQLite Chat Assistant

## 🔗 Deployed API
- **Base URL:** [https://sqlitechatassist.onrender.com](https://sqlitechatassist.onrender.com)
- **Test Query Endpoint:** `/query`

## 🛠️ Features
- Accepts natural language queries and converts them into SQL.
- Supports queries like:
  - `"Who is the manager of Sales?"`
  - `"List all employees hired after 2022-01-01"`
- Returns responses in JSON format.

## 🚀 How to Use
### **1️⃣ API Testing with cURL**
Run the following command:
```sh
curl -X POST https://sqlitechatassist.onrender.com/query -H "Content-Type: application/json" -d "{\"query\": \"Who is the manager of Sales?\"}"
