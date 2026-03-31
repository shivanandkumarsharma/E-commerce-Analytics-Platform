# 🚀 E-commerce Analytics Platform

End-to-end E-commerce Analytics Platform using FastAPI, PostgreSQL, and Power BI, delivering real-time business insights through APIs and interactive dashboards.

## 📌 Overview
This project is an end-to-end data analytics platform built to extract, process, and visualize business insights from e-commerce data.

It integrates data engineering, backend development, and business intelligence into a single system.

---

## 🏗️ Architecture

Data Flow:
Raw Data → Data Cleaning (Python) → PostgreSQL → FastAPI → Power BI Dashboard

---

## 🛠️ Tech Stack

- Python
- FastAPI
- PostgreSQL
- Pandas
- SQLAlchemy
- Power BI

---

## ⚙️ Features

### 🔹 Backend APIs
- Total Revenue
- Top Product Categories
- Revenue by City (Dynamic)
- Revenue by Year (Filtered)

### 🔹 Data Pipeline
- Cleaned and transformed raw datasets
- Loaded into PostgreSQL using ETL scripts

### 🔹 Dashboard (Power BI)
- Revenue trends over time
- Category performance analysis
- City-level insights

---

## 📊 API Endpoints

| Endpoint | Description |
|--------|------------|
| `/total-revenue` | Get total revenue |
| `/top-categories` | Top 5 categories |
| `/revenue-by-city?limit=5` | Revenue by city |
| `/revenue-by-year?year=2017` | Revenue for a specific year |

---

## 📸 Dashboard Screenshots

### Revenue Insights

### Category Performance

### City Insights

---

## 🚀 How to Run

### 1. Clone Repo
```bash
git clone <repo-link>
cd ecommerce-analytics-platform
