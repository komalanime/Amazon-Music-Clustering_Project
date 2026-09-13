# Amazon Music Clustering

## Project Overview
This project groups similar songs using K-Means clustering based on audio characteristics.
Amazon Music Customer Segmentation using K-Means ClusteringThis project segments Amazon Music listeners based on their listening behavior to identify distinct user groups for targeted recommendations.Tech Stack: Python, Pandas, Scikit-learn, Matplotlib, SeabornWorkflow:Data Cleaning & EDA on Amazon Music streaming dataFeature Scaling using StandardScalerOptimal K Selection using Elbow Method (Inertia) & Silhouette ScoreCustomer Segmentation using K-Means (K=3 Final)Cluster Profiling to understand listening patternsResult: Achieved a Silhouette Score of 0.236 with 3 well-separated clusters. The clustered dataset (amazon_music_clustered.csv) can be used for personalized marketing and recommendation systems.

## Dataset
`single_genre_artists.csv`

Main audio features:
- danceability
- energy
- loudness
- speechiness
- acousticness
- instrumentalness
- liveness
- valence
- tempo
- duration_ms

## Workflow
1. Data exploration
2. Data cleaning
3. Feature selection
4. Feature scaling with StandardScaler
5. Elbow Method
6. Silhouette Score
7. K-Means clustering
8. Cluster evaluation
9. Cluster profiling
10. PCA visualization
11. Song/artist analysis
12. CSV export

## Business Use Cases
- Personalized playlists
- Song discovery
- Artist analysis
- Music market segmentation

## Technologies
Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Streamlit.

## Run the Streamlit App

```bash
pip install -r requirements.txt
streamlit run app.py
```



## Project Files
```text
Amazon Music Clustering/
├── single_genre_artists.csv
├── Amazon_Music_Clustering.ipynb
├── app.py
├── requirements.txt
├── amazon_music_clustered.csv
├── cluster_profile.csv
└── k_evaluation_results.csv
```

## Conclusion

The project demonstrates how unsupervised machine learning can discover groups of songs with similar audio characteristics.
The project demonstrates how unsupervised machine learning can discover groups of songs with similar audio characteristics.

