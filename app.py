import streamlit as st
import requests

st.set_page_config(page_title="Segmind VEO-2 Generator", layout="centered")

st.title("🎥 Segmind VEO-2 Generator")
st.markdown("Generate videos with AI using Segmind's VEO-2 API")

# Sidebar: API Config
st.sidebar.header("🔑 API Configuration")
api_key = st.sidebar.text_input("API Key", type="password", placeholder="Enter your Segmind API key")
api_url = st.sidebar.text_input("API URL", "https://api.segmind.com/v1/veo-2")

# Only proceed if API key is provided
if api_key:
    headers = {"x-api-key": api_key}

    # Prompt Form
    with st.form("generate_form"):
        prompt = st.text_input("Prompt", "a red panda riding a skateboard")
        seed = st.number_input("Seed", min_value=0, max_value=9999999, value=965002)
        duration = st.selectbox("Duration (seconds)", ["3", "5", "10"], index=1)
        aspect_ratio = st.selectbox("Aspect Ratio", ["16:9", "9:16", "1:1"], index=0)
        submitted = st.form_submit_button("🎬 Generate")

    if submitted:
        with st.spinner("Generating video..."):
            payload = {
                "prompt": prompt,
                "seed": int(seed),
                "duration": duration,
                "aspect_ratio": aspect_ratio
            }

            response = requests.post(api_url, json=payload, headers=headers)

            if response.status_code == 200:
                try:
                    result = response.json()
                    video_url = result.get("video_url") or result.get("url")
                    if video_url:
                        st.video(video_url)
                    else:
                        st.success("API call succeeded, but no video URL found in response.")
                        st.json(result)
                except Exception as e:
                    st.error(f"Response parse error: {e}")
                    st.text(response.text)
            else:
                st.error(f"❌ Error {response.status_code}: {response.text}")
else:
    st.warning("Please enter your API key in the sidebar to proceed.")
