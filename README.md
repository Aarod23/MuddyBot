
---

# Setting up and Running a Discord Bot Locally

This guide will walk you through setting up and running a Discord bot locally using Python and the Discord.py library.

## Prerequisites
1. Python installed on your system. You can download and install Python from [python.org](https://www.python.org/downloads/).
2. Basic understanding of Python programming language.
3. A text editor or an IDE like Visual Studio Code, PyCharm, or Sublime Text.

## Step 1: Clone the Repository
1. Open your terminal or command prompt.
2. Navigate to the directory where you want to store your project.
3. Clone the repository using the following command:
    ```
    git clone [<repository-url>](https://github.com/Aarod23/MuddyBot)
    ```
   
## Step 2: Install Dependencies
1. Navigate to the project directory.
2. Install the required Python packages using pip. Run the following command:
    ```
    pip install -r requirements.txt
    ```

## Step 3: Create a .env File
1. Create a file named `.env` in the project directory.
2. Add the following line to the `.env` file and replace `<your-token>` with your Discord bot token:
    ```
    TOKEN=<your-token>
    ```

## Step 4: Run the Bot
1. Open the `bot.py` file in your text editor or IDE.
2. Make sure the `bot.py` file contains the provided code.
3. Save the file.
4. In your terminal or command prompt, navigate to the project directory.
5. Run the bot using the following command:
    ```
    python bot.py
    ```

## Step 5: Test the Bot
1. Once the bot is running, open Discord.
2. Invite the bot to your server if you haven't already.
3. Interact with the bot using the provided commands (e.g., `/infract @user reason action`).

Congratulations! You have successfully set up and run a Discord bot locally.

---

Remember, this is a basic guide. Depending on your specific environment and setup, you may encounter additional steps or configurations. Feel free to explore the Discord.py documentation and resources for more advanced features and customization options.
