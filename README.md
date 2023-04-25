---
title: Toxic Tweets Milestone 4
emoji: 🐢
colorFrom: blue
colorTo: red
sdk: streamlit
sdk_version: 1.17.0
app_file: app.py
pinned: false
---

# Toxic-Tweets
<h3>Milestone Submissions</h3>
<ol>
    <li>Milestone 1: Setup Instructions</li>
    <li>Milestone 2: Hugging Face Space: <a href="https://huggingface.co/spaces/junming-qiu/toxic-tweets-milestone-2">Hugging Face Milestone 2 Demo</a></li>
    <li>Milestone 3: Fine Tuned Toxic Comment model: <a href="https://huggingface.co/spaces/junming-qiu/toxic-tweets-milestone-2">Hugging Face Milestone 3 Demo</a></li>
    <li>Milestone 4: Documentation</li>
</ol>

<h1>Motivation</h1>
<p>The internet has been converted from a tool offering unprecedented utility to mankind to a tool that can can destabilize societies and ven cause individuals to take their own lives.

Discussing things you care about can be difficult. The threat of abuse and harassment online means that many people stop expressing themselves and give up on seeking different opinions. Platforms struggle to effectively facilitate conversations, leading many communities to limit or completely shut down user comments.

The Conversation AI team, a research initiative founded by Jigsaw and Google (both a part of Alphabet) are working on tools to help improve online conversation. One area of focus is the study of negative online behaviors, like toxic comments (i.e. comments that are rude, disrespectful or otherwise likely to make someone leave a discussion). So far they’ve built a range of publicly available models served through the Perspective API, including toxicity. But the current models still make errors, and they don’t allow users to select which types of toxicity they’re interested in finding (e.g. some platforms may be fine with profanity, but not with other types of toxic content).</p>

<a href="https://pantelis.github.io/artificial-intelligence/aiml-common/projects/nlp/finetuning-language-models-tweets/index.html">Source</a>
<h1>Initial Setup (Milestone 1)</h1>

<p>For this project, I am using VSCode as my IDE with "Docker" and "Dev Containers" extensions installed. I will be creating a Docker dev envronment to build my project in, as it allows for standardization of libraries across machines.</p>

<h2>Docker Dev Environment Creation Instructions using Docker Desktop</h2>
<ol>
    <li>Download and install Docker <a href="https://www.docker.com/">client</a></li>
    <li>Open Docker client</li>
    <li>Click "Dev Environments" > "Create" > "Get Started" > "Choose Source" > <i>Link/Create a Git <a href="https://github.com/Junming-Qiu/Toxic-Tweets.git">repo</a></i> > "Continue"</li>
    <li>The environment is created and running</li>
    <li>In the "Dev Environments" tab, select the running container and click "OPEN IN VSCODE"</li>
</ol>
<img src="./Documentation/end_result.png"/>
<img src="./Documentation/step3.png"/>
<img src="./Documentation/config.png"/>
<p>Verify that the container is running by running "docker ps" in the command line</p>
<img src="./Documentation/terminal.png"/>
<p>Connect to docker container using CLI</p>
<img src="./Documentation/CLI_conn.png"/>
<p>For CLI creation of a dev environment, use this <a href="https://docs.docker.com/desktop/dev-environments/set-up/">resource</a></p>

<h1>HuggingFace Spaces Setup (Milestone 2)</h1>
<p>For this milestone, I will setup a HuggingFace Space where a user can select from a range of sentiment analysis models, enter a text, and get the sentiment of their input. This is the first step in allowing me to showcase my final fine tuned model after Milestone 3.</p>

<h2>Setting up HuggingFace Space</h2>
<ol>
    <li>Watch the video below to learn how to create a HuggingFace Space and implement CI functionality on Github.</li>
    <a href="https://www.youtube.com/embed/8hOzsFETm4I">HuggingFace Space Tutorial</a>
    <li>In HuggingFaces, go to "Spaces" > "Create new Space". Name the space and choose "Streamlit" as the Space SDK.</li>
    <li>Go to your HuggingFace Profile > "Settings" > "Access Tokens" > "New Token" > Create a new HuggingFace access token. Name the token and copy the token to somewhere secure.</li>
    <img width=50% src="./Documentation/HFAccess.jpg" />
</ol>
<h2>Setting up Github Action</h2>
<ol>
    <li>
        Go to your github repository > "Actions secrets and variables" > "Actions" > "New repository secret". Name the token "HF_TOKEN" and paste the HuggingFace token key.
    </li>
    <li>
        In github, got to "Actions" > "New workflow" > "set up a workflow yourself". Paste in the text below and fill out the appropriate fields with your HuggingFace info:
        <br/>
        <textarea rows="20" cols="70">      
name: Sync to Hugging Face hub
on:
push:
    branches: [main]
# to run this workflow manually from the Actions tab
workflow_dispatch:
jobs:
sync-to-hub:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
        with:
        fetch-depth: 0
    - name: Push to hub
        env:
        HF_TOKEN: ${{ secrets.HF_TOKEN }}
        run: git push --force https://Amrrs:$HF_TOKEN@huggingface.co/spaces/Amrrs/image-to-text-app main
</textarea>
    </li> 
    <li>Create a file called "app.py" and run "pip install streamlit". Follow this documentation to create a streamlit app: <a href="https://docs.streamlit.io/">Here</a></li>
    <li>Follow this documentation to load and use HuggingFace models: <a href="https://huggingface.co/docs/transformers/index">Here</a></li>
    <li>Once the app is created, push it or merge it to the main branch in github, and the app should automatically be uploaded into your HuggingFace space!</li>
</ol>

<h1>Fine Tuning (Milestone 3)</h1>
<p>For this milestone, I will pick a pretrained transformer model and fine tune it with the toxic-tweets dataset to create a multiheaded toxicity detection model.</p>
<ol>
    <li>Pick a model to fine tune on in HuggingFaces. In this case, I use BERT, as it is a reliable and complete model trained by Google.</li>
    <li>Follow this video tutorial on how to fine tune a model with the Trainer class</li>
    <a href="https://www.youtube.com/watch?v=GSt00_-0ncQ">HuggingFace Fine Tuning Tutorial</a>
    <li>
        For more detailed information on how I fine tuned my model, please check out my <a href="https://github.com/Junming-Qiu/Toxic-Tweets/blob/main/Final_Project_Fine_Tuning.ipynb">Jupyter notebook</a>
        <h3>Basic Fine Tuning Overview:</h3>
        <ul>
            <li>Load and clean data. Since the data is highly unbalanced, make sure that enough samples with unique combinations of toxicities are distributed in the training set</li>
            <li>Tokenize the input data and create a pytorch dataset with the data</li>
            <li>Initialize the HuggingFace Trainer and begin training!</li>
            <li>Evaluate the trainer and save the model</li>
        </ul>
    </li>
    <li>Upload the new model on HuggingFace space</li>
</ol>
<h1>Results and Conclusion (Milestone 4)</h1>
<h2>Deliverables:</h2>
<ol>
    <li>Documentation (Github)</li>
    <li>Project Launch Page</li>
    <li>Video Demonstration</li>
</ol>

