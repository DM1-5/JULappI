# JULappI

This is a simple script that sends a WhatsApp message to a specific number. It is intended to be used as a cron job, so it can be used to send a message every day at a specific time.

## Installation

Install the required packages by running the following command:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```
The variables are hard-coded in the script, so you will need to change them to your own.

# To-Do

- [ ] Add a list of messages to be sent randomly.
- [ ] Add a list of word alredy sent to avoid repetition.
- [ ] Add a list of numbers to send the messages to.
- [ ] Cli arguments to change the variables.
- [ ] Use a database to store the messages. 