# AoC table generator

This is a simple script to generate a .md table for your AoC repository. It will generate a table looking just like [this one](https://github.com/Enailis/Advent-of-Code-2022/blob/master/README.md#solutions).

I used to manually update the table in my README.md file, but that was tedious and error-prone. So I wrote this script to do it for me.

The script will generate a table with the following columns:
    
    Day | Challenge | Part 1 | Part 2 | Rank Part 1 | Rank Part 2

The `Challenge` column will contain the name of the challenge and link to it on the AoC website.

The `Part 1` and `Part 2` columns will contain links to the solutions for each part of the challenge. (*This will work only if your repository is following the same folder organisation than mine. If you want to change this, change the 58th and 59th line of code.*)

The `Rank Part 1` and `Rank Part 2` columns will contain the global ranking you got for each part of the challenge.

## Usage

Clone this repository :

    git clone git@github.com:Enailis/AoC-table-generator.git

Install the requirements
    
    pip3 install -r requirements.txt
   
Run the script:

    python3 table_generator.py

## Configuration

To chose which year of AoC to generate the table for, copy the `.env-example` file to `.env` and change the `YEAR` variable to the desired year.

You'll need to get your session cookie from AoC to be able to generate the table. You can find it in your browser's developer tools.

In Firefox, open the developer tools, go to the `Storage` tab, and copy the value of the `session` cookie.

In Chromium, open the developer tools, go to the `Application` tab and copy the value of the `session` cookie.

## Known issue

The script should work flowlessly on Windows and MacOS. On Linux you might encounter an issue with the `pyperclip` module. If that's the case, it's probably because you don't have the `xclip` or `xsel` package installed. Install one of them and the script should work fine.