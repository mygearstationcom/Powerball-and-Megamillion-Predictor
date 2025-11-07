# Powerball-and-Megamillion-Predictor
Thanks to LynxGeekNYC MegaMillion Predictor, AI and I created a predictor for Powerball and MegaMillions.

# Basically how I made it work for me
1 - Cloned their repository
2 - Creaated a venv: python3 -m venv .venv
3 - Activated the .venv: source .venv/bin/activate
4 - ran their program: python3 lotto-2024-v1.py
5 - spent a lot of time in the .venv to set up all the dependicies.
      This stuff is way above my heads so I used AI to assist and read all the many error codes to corectly set up the ,venv
      so the program would run.
6 - I finally developed 2 new programs for my purposes.
      powerball.py
      megamillions.py
7 - my ouput:
      python3 powerball.py
              Predicted numbers based on frequency (PowerBall):
              [37, 40, 50, 64, 68], PowerBall = 18
              Note: All white ball numbers 1-69 have been used. Choosing from the full range.
              
              Predicted numbers based on unused numbers (PowerBall):
              [4, 46, 50, 64, 64], PowerBall = 18
      ython3 megamillions.py
              Predicted numbers based on frequency (MegaMillions):
              [55, 56, 58, 60, 62], MegaBall = 24
              Note: All white ball numbers 1-70 have been used. Choosing from the full range.
              
              Predicted numbers based on unused numbers (MegaMillions):
              [16, 20, 24, 59, 60], MegaBall = 20

# How to set up your own adventure - I am using Python3.12
  1 - Clone my repository
  2 - Create a virtual environment:
      python3 -m venv .venv
  3 - Activate the .venv
      .venv/bin/activate
  4 - Make sure you have the necessary site packages installed.
      My system needed pandas, numpy, tensorflow==2.16.1 to work.
      Your system may need these and others
  4 - Run the programs
      python3 powerball.py
      and
      python3 megamillions.py

  # Good luck and DO NOT BLAME ME FOR ANY LOSSES! I AM NOT RESPONIBLE FOR YOUR ACTIONS AND ANY LOSSES or GAINS that YOU MIGHT INCUR.
