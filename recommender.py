import pandas as pd          
import matplotlib.pyplot as plt  

print("=" * 50)
print("🎬  MOVIE RECOMMENDER")
print("=" * 50)



print("\n📂 Loading data...")

# Load ratings file
ratings = pd.read_csv(
    'data/ml-100k/u.data',     
    sep='\t',                  
    names=['user_id', 'movie_id', 'rating', 'timestamp'] 
)

movies = pd.read_csv(
    'data/ml-100k/u.item',    
    sep='|',                   
    encoding='latin-1',        
    usecols=[0, 1],           
    names=['movie_id', 'title'] 
)

print(f"✅ Loaded {len(ratings)} ratings")
print(f"✅ Loaded {len(movies)} movies")

print("\n" + "=" * 60)
print("📊 DATA SUMMARY")
print("=" * 60)

print(f"Total Ratings:  {len(ratings)}")
print(f"Total Movies:   {len(movies)}")
print(f"Total Users:    {ratings['user_id'].nunique()}")
print(f"Average Rating: {ratings['rating'].mean():.2f}")

print("\n" + "=" * 60)
print("🏆 TOP RATED MOVIES")
print("=" * 60)


movie_avg = ratings.groupby('movie_id')['rating'].mean()
movie_count = ratings.groupby('movie_id')['rating'].count()


movie_stats = pd.DataFrame({
    'avg_rating': movie_avg,
    'num_ratings': movie_count
})


movie_stats = movie_stats.join(movies.set_index('movie_id'), on='movie_id')


movie_stats = movie_stats[movie_stats['num_ratings'] >= 20]


top_movies = movie_stats.sort_values('avg_rating', ascending=False).head(10)

print("\n🎬 Top 10 Movies:")
for i, (idx, row) in enumerate(top_movies.iterrows(), 1):
    print(f"{i}. {row['title']} - ⭐ {row['avg_rating']:.2f} ({row['num_ratings']} ratings)")


print("\n" + "=" * 60)
print("🎯 RECOMMENDATIONS")
print("=" * 60)

def recommend_movies(user_id, num_recs=5):
    """Recommend movies for a user"""
    
    print(f"\n👤 User {user_id}")
    print("-" * 40)
    
   
    user_ratings = ratings[ratings['user_id'] == user_id]
    
    if len(user_ratings) == 0:
        print("❌ User not found!")
        return None
    
    
    print("📊 Movies you rated:")
    user_data = user_ratings.merge(movies, on='movie_id')
    user_data = user_data.sort_values('rating', ascending=False)
    
    for _, row in user_data.head(5).iterrows():
        print(f"   {row['title']} - ⭐ {row['rating']}")
    
  
    liked = user_ratings[user_ratings['rating'] >= 4]['movie_id'].tolist()
    
    if len(liked) == 0:
        print("\n💡 You haven't rated any movie highly.")
        print("   Showing most popular movies instead.")
        return get_popular_movies(num_recs)
    
    similar = ratings[ratings['movie_id'].isin(liked)]
    similar = similar[similar['user_id'] != user_id]
    
    # Count common movies
    similar_users = similar.groupby('user_id').size()
    similar_users = similar_users[similar_users >= 2].index.tolist()
    
    if len(similar_users) == 0:
        print("\n❌ No similar users found!")
        print("   Showing most popular movies instead.")
        return get_popular_movies(num_recs)
    
    print(f"\n👥 Found {len(similar_users)} similar users")
    
    
    similar_ratings = ratings[ratings['user_id'].isin(similar_users)]
    
   
    seen = user_ratings['movie_id'].tolist()
    similar_ratings = similar_ratings[~similar_ratings['movie_id'].isin(seen)]
    
  
    scores = similar_ratings.groupby('movie_id').agg({
        'rating': ['mean', 'count']
    })
    scores.columns = ['avg_rating', 'num_ratings']
    scores = scores[scores['num_ratings'] >= 2]
    
    if len(scores) == 0:
        print("\n❌ No recommendations found!")
        return get_popular_movies(num_recs)
    
    scores = scores.join(movies.set_index('movie_id'), on='movie_id')
    scores = scores.sort_values('avg_rating', ascending=False).head(num_recs)
    
 
    print(f"\n🎬 Top {num_recs} Recommendations:")
    for i, (idx, row) in enumerate(scores.iterrows(), 1):
        print(f"{i}. {row['title']} - ⭐ {row['avg_rating']:.2f}")
    
    return scores

def get_popular_movies(n=5):
    """Fallback: Show most popular movies"""
    
    popular = ratings.groupby('movie_id').size().sort_values(ascending=False).head(n)
    popular = popular.reset_index()
    popular.columns = ['movie_id', 'num_ratings']
    popular = popular.join(movies.set_index('movie_id'), on='movie_id')
    
    for i, (idx, row) in enumerate(popular.iterrows(), 1):
        avg = ratings[ratings['movie_id'] == row['movie_id']]['rating'].mean()
        print(f"{i}. {row['title']} - {row['num_ratings']} ratings (⭐ {avg:.2f})")
    
    return popular


test_users = [1, 100, 200]

for user in test_users:
    recommend_movies(user)
    print("\n" + "-" * 40)


print("\n" + "=" * 60)
print("📈 CREATING CHART")
print("=" * 60)

# Plot top 10 movies
plt.figure(figsize=(10, 6))
plt.barh(top_movies['title'], top_movies['avg_rating'], color='skyblue')
plt.xlabel('Average Rating')
plt.title('Top 10 Highest Rated Movies')
plt.tight_layout()
plt.savefig('top_movies.png')
print("✅ Chart saved as 'top_movies.png'")
plt.show()

print("\n" + "=" * 60)
print("💾 SAVING RESULTS")
print("=" * 60)

# Save top movies to CSV
top_movies.to_csv('top_movies.csv')
print("✅ Saved: top_movies.csv")

print("\n✅ ALL DONE!")
print("\n📁 Files created:")
print("   - top_movies.png (chart)")
print("   - top_movies.csv (data)")