# Prework: 10-Minute Environment Setup Walkthrough

In this course, we’ll be using Python. If you’ve never used Python before, don’t worry. We will provide most of the code you'll need. We use Python to provide a common place for all of us to work in during class. We will also be leveraging AI tools to help us develop code, so you don’t need to be expert or even be experienced in Python to get the most out of this course.

Outside of class, if you want to build AI apps using other languages, we will be providing extra code examples in JavaScript and Java for you to use. 

### 1. Setting Up Your IDE with Cursor
Cursor is an IDE with embedded AI tools. These tools increase development output and will expose you to good AI UX. We will discuss later in this course how to get the most out of Cursor and how it effects the development workflow. For now, let's just get it installed.

1. Go to https://www.cursor.com/
2. Click the download button, which will download the install package to your computer. Open the package to install Cursor.
3. Once installed, make sure you can open Cursor. 

### 2. Setting Up UV
UV is an extremely fast Python package and project manager, written in Rust. We’ll use this to install Python packages we need (including Python itself). 

1. Open your terminal and run the following command:
- Mac: `curl -LsSf https://astral.sh/uv/install.sh | sh` 
- Windows: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
2. Follow the instructions to add it to your PATH.
3. Restart your terminal.

### 3. Installing Python  
We'll use the latest Python version for this course. 
With UV, this one is easy. 
1. Run `uv python install` in your terminal. 

### 4. Installing Pip 
Pip is a Python package manager used to install Python libraries.

1. Pip is automatically included with Python. To check if it’s installed, open terminal/command prompt and type:
   ```bash
   pip --version
   ```

## Generate an Open AI Key
At MindBit, we prioritize protecting your intellectual property while ensuring a smooth and cost-effective learning experience. As part of our AI training, we ask each participant to sign up for their own OpenAI API account.

Here’s why:
- IP Protection: By using your own API key, any projects or work you create will remain entirely under your ownership and control.
- Minimal Costs: Our course only requires about $5 of token usage, so you’ll have full transparency and control over your API costs.

### API Cost-Literacy is Critical
Learning how to use OpenAI’s billing tools is very important for helping your company understand the costs of using AI. As you start advocating for AI projects, being able to clearly explain and predict expenses will make a huge difference. It shows that you’ve done your homework and can back up your ideas with real numbers, making it easier for your company to trust and support your AI plans. Plus, it helps make sure AI use stays within budget and delivers value. 

*We recommend you put $5 into your account* and closely monitor the spend as you go through your projects here to learn how much API usage costs as a hands-on way of learning how to navigate different models, token usage, etc. You can add in more money as you need or not depending on the scope of your project goals.

Seeing those tokens get used up, monitoring the throughput, and seeing all the dots connect is part of the magic that you will need to explain to your team or leaders.  

### 1: Create Your OpenAI Account
We are using OpenAI for the duration of this course as it is the most widely used platform in industry.  The same concepts we teach here will be applicable to all platforms.

1. Visit [OpenAI API website](https://platform.openai.com/) and sign up for an account if you don’t already have one.
2. Once you have signed up, log in and [navigate to the Billing section](https://platform.openai.com/settings/organization/billing/overview).
3. Add $5 to your account to cover API usage throughout the course. This amount should be sufficient for the duration of the program.

### 2: Generate Your API Key
Generating an API key is important because it securely lets your application access the OpenAI API, keeping your usage authorized and data protected.

1. In your OpenAI account, go to the [API Keys section](https://platform.openai.com/api-keys)
2. Generate a new API key and save it securely somewhere you won’t forget. You will use this key to access the API during the course.

### 3: Save the API key to an environment variable
Saving your API key to an environment variable keeps it secure and hidden from your code. It prevents accidentally sharing sensitive info and keeps your code clean and safe to share with others.

   <details>
   <summary>On Mac:</summary>

   - Open your `.bash_profile` file with a text editor: `open ~/.bash_profile`
   - Add the line `export OPENAI_API_KEY={your key}`
   - Save the file and close it

   </details>

   <details>
   <summary>On Windows:</summary>

   - Go to "Control Panel" > "System and Security" > "System"
   - Click "Advanced system settings"
   - Select the "Advanced" tab and click "Environment Variables"
   - Under "User variables", click "New"
   - Enter the variable name as "OPENAI_API_KEY" and the value as your key.
   - Click "OK" to save

   </details>

### Next Steps

You are on your way now!  Your environment is set up, you have your API key loaded up and ready to go, let's move on to [Prework 2: Creating our first AI Application in Python](prework_2.md)
