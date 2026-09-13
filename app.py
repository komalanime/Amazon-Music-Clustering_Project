import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Amazon Music Clustering", page_icon="🎵", layout="wide")

st.title("🎵 Amazon Music Clustering")
st.write("Explore songs grouped by similar audio characteristics using K-Means clustering.")

@st.cache_data
def load_data():
    return pd.read_csv("amazon_music_clustered.csv")

try:
    df = load_data()
except FileNotFoundError:
    st.error("amazon_music_clustered.csv was not found. Run the Jupyter Notebook first and export the clustered CSV.")
    st.stop()

if "cluster" not in df.columns:
    st.error("The CSV does not contain the 'cluster' column.")
    st.stop()

st.success(f"Dataset loaded successfully: {len(df):,} songs")

st.sidebar.header("Filters")
clusters = sorted(df["cluster"].dropna().unique().tolist())
selected = st.sidebar.multiselect("Select Cluster(s)", clusters, default=clusters)
filtered = df[df["cluster"].isin(selected)].copy()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Songs", f"{len(filtered):,}")
c2.metric("Total Clusters", df["cluster"].nunique())

if "popularity_songs" in filtered.columns and len(filtered):
    c3.metric("Avg Popularity", f"{filtered['popularity_songs'].mean():.2f}")
else:
    c3.metric("Avg Popularity", "N/A")

if "danceability" in filtered.columns and len(filtered):
    c4.metric("Avg Danceability", f"{filtered['danceability'].mean():.2f}")
else:
    c4.metric("Avg Danceability", "N/A")

st.divider()

st.subheader("📊 Cluster Distribution")
counts = filtered["cluster"].value_counts().sort_index()
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(counts.index.astype(str), counts.values)
ax.set_xlabel("Cluster")
ax.set_ylabel("Number of Songs")
ax.set_title("Number of Songs in Each Cluster")
st.pyplot(fig)
plt.close(fig)

features = [
    "danceability", "energy", "loudness", "speechiness",
    "acousticness", "instrumentalness", "liveness",
    "valence", "tempo", "duration_ms"
]
available = [x for x in features if x in filtered.columns]

if available:
    st.subheader("🎚️ Cluster Audio Profile")
    profile = filtered.groupby("cluster")[available].mean()
    st.dataframe(profile.round(3), use_container_width=True)

    feature = st.selectbox("Select an audio feature", available)
    fig, ax = plt.subplots(figsize=(10, 5))
    profile[feature].plot(kind="bar", ax=ax)
    ax.set_title(f"Average {feature} by Cluster")
    ax.set_xlabel("Cluster")
    ax.set_ylabel(feature)
    ax.tick_params(axis="x", rotation=0)
    st.pyplot(fig)
    plt.close(fig)

if "popularity_songs" in filtered.columns:
    st.subheader("⭐ Most Popular Songs")
    cols = [x for x in ["name_song", "name_artists", "popularity_songs", "cluster", "genres"] if x in filtered.columns]
    n = st.slider("Number of songs", 5, 50, 10)
    st.dataframe(
        filtered.sort_values("popularity_songs", ascending=False).head(n)[cols],
        use_container_width=True
    )

st.subheader("📋 Clustered Dataset")
with st.expander("Show data"):
    st.dataframe(filtered.head(1000), use_container_width=True)

st.download_button(
    "⬇️ Download Filtered CSV",
    filtered.to_csv(index=False).encode("utf-8"),
    "amazon_music_clustered_filtered.csv",
    "text/csv"
)

st.sidebar.divider()
st.sidebar.info("Amazon Music Clustering | K-Means")
