# 🎬 Movie Recommendation System

> A simple AI-based recommendation system that suggests movies based on user interests and ratings.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.0.3-green)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7.2-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Features](#features)
- [Installation](#installation)
- [How It Works](#how-it-works)
- [Project Report](#project-report)
- [Workflow Explanation](#workflow-explanation)
- [Results](#results)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)

---

## 📖 Project Overview

This project builds a **Movie Recommendation System** using collaborative filtering. It analyzes user ratings to find similar users and recommends movies they liked but the target user hasn't seen yet.

### 🎯 What You'll Learn
- How to load and clean real-world datasets
- How to implement collaborative filtering
- How to analyze user behavior and movie trends
- How to create data visualizations

---

## 📊 Dataset

**Source:** [MovieLens 100K Dataset](https://grouplens.org/datasets/movielens/100k/)

| Feature | Details |
|---------|---------|
| **Total Ratings** | 100,000 |
| **Total Users** | 943 |
| **Total Movies** | 1,682 |
| **Rating Scale** | 1-5 stars |
| **Format** | TSV (Tab-Separated Values) |

### Dataset Files Used:
- `u.data` - User ratings (user_id, movie_id, rating, timestamp)
- `u.item` - Movie information (movie_id, title)

---

## ✨ Features

- ✅ **Data Loading** - Load MovieLens dataset from CSV/TSV files
- ✅ **Data Analysis** - View statistics, top movies, user activity
- ✅ **Recommendation Engine** - Collaborative filtering algorithm
- ✅ **User Recommendations** - Get personalized movie suggestions
- ✅ **Data Visualization** - Bar charts of top movies
- ✅ **Export Results** - Save results to CSV files

---

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender
### Step 2: Install Dependencies
pip install -r requirements.txt
Or install manually:
pip install pandas matplotlib
### Step 3: Download Dataset
# Download MovieLens 100K dataset
wget https://files.grouplens.org/datasets/movielens/ml-100k.zip
# Extract to data folder
unzip ml-100k.zip -d data/
### Step 4: Run the Program
bash
python movie_recommender.py
