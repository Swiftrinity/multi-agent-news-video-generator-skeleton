import os
from datetime import datetime
from agents import news_fetcher,news_summarizer,script_generator,video_generator
from utils.file_utils import write_to_csv

# Step 1: Create a new timestamped run folder
timestamp = datetime.now().strftime("run_%Y-%m-%d_%H-%M-%S")
run_dir = os.path.join("runs", timestamp)
os.makedirs(run_dir, exist_ok=True)

# Step 2: Define input & output paths

news_data_path = os.path.join(run_dir, "news_data.csv")
summarized_news_data_path = os.path.join(run_dir, "summarized_news_data.csv")
video_script_path = os.path.join(run_dir, "video_script.csv")
generated_video_path = os.path.join(run_dir, "generated_video.csv")

## Step 3: Create the raw news data
#news_fetcher.run(news_data_path)


## Step 4: refine the news
#news_summarizer.run(news_data_path, summarized_news_data_path)


## Step 5: script generator make a good script for generating a video
#script_generator.run(summarized_news_data_path, video_script_path)


## Step 6: Trigger the video generator
#video_generator.run(video_script_path, generated_video_path)