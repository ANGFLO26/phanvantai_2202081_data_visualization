import streamlit as st # type: ignore
import yt_dlp # type: ignore
import time
import pandas as pd
import plotly.graph_objects as go # type: ignore
import os

# CSV file for storing data
CSV_FILE = "/home/phanvantai/Documents/THREE_YEARS/three_year_02/data visualization/midterm/data/youtube_video_data.csv"
# YouTube video URL to track
VIDEO_URL = "https://youtu.be/ESw0aKi8elE?si=pdo25fb6Cp6e-J-s"  # Replace with your video

# Read data from CSV file if it exists
if os.path.exists(CSV_FILE):
    df = pd.read_csv(CSV_FILE, parse_dates=["Timestamp"])
else:
    df = pd.DataFrame(columns=["Timestamp", "Views", "Likes", "Comments"])

def get_change(curr_value, prev_value):
    if prev_value is None:
        return "N/A"
    change = curr_value - prev_value
    if change > 0:
        return f"🔼 +{change:,}"
    elif change < 0:
        return f"🔽 {change:,}"
    else:
        return "➡ 0"

st.markdown("<h1 style='text-align: center;'>📊 Real-time Tracking of a YouTube Video</h1>", unsafe_allow_html=True)
placeholder = st.empty()

while True:
    try:
        with yt_dlp.YoutubeDL({"quiet": True, "skip_download": True}) as ydl:
            info = ydl.extract_info(VIDEO_URL, download=False)
        
        # Fetch new data
        timestamp = pd.Timestamp.now()
        views = info.get("view_count", 0)
        likes = info.get("like_count", 0)
        comments = info.get("comment_count", 0)

        # Get previous values if available
        prev_views = df["Views"].iloc[-1] if not df.empty else None
        prev_likes = df["Likes"].iloc[-1] if not df.empty else None
        prev_comments = df["Comments"].iloc[-1] if not df.empty else None

        # Calculate changes
        views_change = get_change(views, prev_views)
        likes_change = get_change(likes, prev_likes)
        comments_change = get_change(comments, prev_comments)

        # Append new data to DataFrame
        new_data = pd.DataFrame({
            "Timestamp": [timestamp],
            "Views": [views],
            "Likes": [likes],
            "Comments": [comments]
        })
        
        if df.empty:
            df = new_data
        else:
            df = pd.concat([df, new_data], ignore_index=True)

        # Check if data reaches 100 points, delete CSV file and create a new one
        if len(df) >= 100:
            os.remove(CSV_FILE)
            df = new_data  # Keep only the latest data

        # Save to CSV file
        df.to_csv(CSV_FILE, index=False)

        # Plot graph using Plotly
        fig = go.Figure()
        for key, name, color in zip(["Views", "Likes", "Comments"],
                                    ["Views", "Likes", "Comments"],
                                    ["blue", "red", "green"]):
            hover_texts = [
                f"<b>{name}</b>: {df[key][i]:,}<br>🔄 Change: {get_change(df[key][i], df[key][i-1] if i > 0 else None)}"
                for i in range(len(df["Timestamp"]))
            ]

            fig.add_trace(go.Scatter(
                x=df["Timestamp"], y=df[key],
                mode="lines+markers", name=f"{name} ({get_change(df[key].iloc[-1], df[key].iloc[-2] if len(df) > 1 else None)})",
                line=dict(color=color), marker=dict(size=8),
                hoverinfo="text",
                hovertext=hover_texts
            ))
        
        fig.update_layout(
            title="📊 Analyze a YouTube video based on views, likes, comments",
            xaxis_title="Time",
            yaxis_title="Count",
            hovermode="x unified"
        )

        # Display graph in Streamlit
        placeholder.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"❌ Error fetching data: {e}")

    # Wait 60 seconds before next update
    time.sleep(60)
