---
title: Toxic Tweets Milestone 2
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
</ol>

<h1>Motivation</h1>
<p>The internet has been converted from a tool offering unprecedented utility to mankind to a tool that can can destabilize societies and ven cause individuals to take their own lives.

Discussing things you care about can be difficult. The threat of abuse and harassment online means that many people stop expressing themselves and give up on seeking different opinions. Platforms struggle to effectively facilitate conversations, leading many communities to limit or completely shut down user comments.

The Conversation AI team, a research initiative founded by Jigsaw and Google (both a part of Alphabet) are working on tools to help improve online conversation. One area of focus is the study of negative online behaviors, like toxic comments (i.e. comments that are rude, disrespectful or otherwise likely to make someone leave a discussion). So far they’ve built a range of publicly available models served through the Perspective API, including toxicity. But the current models still make errors, and they don’t allow users to select which types of toxicity they’re interested in finding (e.g. some platforms may be fine with profanity, but not with other types of toxic content).</p>

<a href="https://pantelis.github.io/artificial-intelligence/aiml-common/projects/nlp/finetuning-language-models-tweets/index.html">Source</a>
<h1>Initial Setup</h1>

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

<h2></h2>


