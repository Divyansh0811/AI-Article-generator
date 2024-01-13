# AI-Article-generator
Welcome to the AI Article Generator! 
The AI Article Generator is a powerful backend API designed to revolutionize content creation. With this innovative tool, users can effortlessly generate AI-written articles on any topic of their choice. Whether you're a content creator, developer, or researcher, our API offers a seamless way to access dynamically generated articles with just a few simple requests.
## Key Features:
 - **Topic-Agnostic Generation:** Enter any topic and let our AI-powered backend create informative and engaging articles tailored to your request.

 - **Quality Content:** Enjoy well-structured articles written in a natural language that mirrors human-like fluency and coherence.

 - **Versatile Integration:** Integrate the AI Article Generator into your applications, websites, or projects easily via a RESTful API.

# Getting Started

Kindly Follow these steps to quickly set up and use the API.

## Prerequisites

Make sure you have the following installed on your machine:

- [Python](https://www.python.org/) (version 3.7 or higher)
- [Git](https://git-scm.com/) (optional, for cloning the repository)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Divyansh0811/AI-Article-generator.git

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
3. **Activate the virtual Environment:**
   - On Windows
     ```bash
     .\venv\Scripts\activate
   - On MacOS/Linux
     ```bash
     source venv/bin/activate
4. **Install Dependencies:**
    ```bash
     pip install -r requirements.txt

## Usage
1. **Run the API:**
   ```bash
    uvicorn main:app --reload
2. **Generate an Article:**
   ```bash
     POST http://localhost:8000/generate_article BODY: { "topic" : "Your_Desired_Topic" }

## Example
![ai_article_generator](https://github.com/Divyansh0811/AI-Article-generator/assets/69900562/2e9b5527-22fd-445d-9db0-268e2073d3a9)




  
   
   

