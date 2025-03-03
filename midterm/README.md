                            #  YouTube Video Real-time Tracker

1. Introduction
This is a real-time tracking tool for YouTube video statistics. The tool displays an intuitive chart with three key metrics:
    - **Views**
    - **Likes**
    - **Comments**

2. System Requirements
- Operating Systems: Windows, Linux, macOS (compatible with all platforms)
- Python 3.8+

3. Installation
First, ensure that Python is installed on your system. Then, install the required libraries by running:

```bash
pip install -r requirements.txt
```

4. Usage Instructions
        a. Open a terminal or command prompt.
        b. Run the application using the command:
        ```bash
        streamlit run app.py
        ```
        c. To track a different YouTube video, replace the `VIDEO_URL` variable with the link of the desired video.

5. Key Features
- Displays a **line chart** to track video statistics.
- Updates data every **60 seconds**.
- Automatically saves data to a CSV file for later analysis.
- Shows the difference between old and new data for better tracking of video changes.

6. Data Storage
- Data is saved in a CSV file (`youtube_video_data.csv`).
- When the dataset reaches 100 entries, the file is deleted and reset.

7. Authors
**Phan Van Tai_ 2202081**  
**Nguyen Thanh Tuan_2202084**
