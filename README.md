# Clickbait Headline Generator

A fun clickbait headline generator for generating humorous headlines for websites or content farms. Inspired by Al Sweigart's examples from "The Big Book of Small Python Projects".

## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## About the Project

The Clickbait Headline Generator uses a variety of pre-defined phrases and patterns to create engaging (and sometimes ridiculous) clickbait headlines. This project demonstrates basic Python programming skills, including working with random selection and string formatting, while producing fun, randomly generated headlines.

## Features

- Generates humorous clickbait headlines based on predefined templates.
- Uses a modular approach with classes and constants for easy modification and extension.
- Provides multiple headline types, such as "What You Don't Know", "Big Companies Hate Her", and "You Won't Believe".

## Requirements

- **Python**: 3.10 or higher
- See `requirements.txt` for other package dependencies if any.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YourUsername/Clickbait-Headline-Generator.git
   cd Clickbait-Headline-Generator
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python3.10 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**:
   Make sure you have Python 3.10 installed. Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main script to start the headline generator.

```bash
python main.py
```

1. Enter the number of headlines you want to generate.
2. Enjoy reading the generated clickbait headlines!

Example output:
```
Clickbait Headline Generator
By Al Sweigart al@inventwithpython.com

Our website needs to trick people into looking at ads!
Enter the number of clickbait headlines to generate:
> 3

Are Millennials Killing the Paper Industry?
What Scientists Don't Want You to Know About Bees
You Won't Believe What This Florida Man Found in His Backyard!
```

## Project Structure

- **main.py**: The main script to start the headline generator.
- **generators.py**: Contains the `Generator` class, which holds different methods for generating headline types.
- **constants.py**: Contains lists of words and phrases used for random selection in headlines.
- **requirements.txt**: Lists project dependencies and Python version.

## Contributing

Contributions are welcome! Feel free to fork the project and submit pull requests.

## License

This project is open-source and available under the MIT License.

