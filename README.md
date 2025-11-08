# Powerball-and-Megamillion-Predictor
Thanks to LynxGeekNYC MegaMillion Predictor, AI and I created a predictor for Powerball and MegaMillions.

# Basically how I made it work for me
1 - Cloned their repository:<br>&nbsp;&nbsp;&nbsp;&nbsp;git clone https://github.com/LynxGeekNYC/MegaMillions-Predictor.git<br>
2 - Created a venv:<br>&nbsp;&nbsp;&nbsp;&nbsp;python3 -m venv .venv<br>
3 - Activated the .venv:<br>&nbsp;&nbsp;&nbsp;&nbsp;<i><strong>source</strong></i> .venv/bin/activate<br>
4 - ran their program:<br>&nbsp;&nbsp;&nbsp;&nbsp;python3 lotto-2024-v1.py<br>
5 - spent a lot of time in the .venv to set up all the dependencies.<br>
     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<sub><i>---This stuff is way above my head so I used AI to assist and read all the many error codes to corectly set up the .venv so the program would run.</i></sub><br>
6 - I finally developed 2 new programs for my purposes:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;powerball.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;megamillions.py<br>
7 - my ouput:<br>
&nbsp;&nbsp;&nbsp;&nbsp;<b>python3 powerball.py</b><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Predicted numbers based on frequency (PowerBall):<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[37, 40, 50, 64, 68], PowerBall = 18<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Note: All white ball numbers 1-69 have been used. Choosing from the full range.<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Predicted numbers based on unused numbers (PowerBall):<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4, 46, 50, 64, 64], PowerBall = 18<br>
&nbsp;&nbsp;&nbsp;&nbsp;<b>python3 megamillions.py</b><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Predicted numbers based on frequency (MegaMillions):<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[55, 56, 58, 60, 62], MegaBall = 24<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Note: All white ball numbers 1-70 have been used. Choosing from the full range.<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Predicted numbers based on unused numbers (MegaMillions):<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[16, 20, 24, 59, 60], MegaBall = 20<br>

# How to set up your own adventure - I am using Python3.12
  1 - Clone my repository<br>
  2 - Create a virtual environment:<br>
      &nbsp;&nbsp;&nbsp;&nbsp;python3 -m venv .venv<br>
  3 - Activate the .venv<br>
      &nbsp;&nbsp;&nbsp;&nbsp;.venv/bin/activate<br>
  4 - Make sure you have the necessary site packages installed.<br>
      &nbsp;&nbsp;&nbsp;&nbsp; My system needed pandas, numpy, tensorflow==2.16.1 to work.<br>
      &nbsp;&nbsp;&nbsp;&nbsp;Your system may need these and others.<br>
  4 - Run the programs<br>
      &nbsp;&nbsp;&nbsp;&nbsp;python3 powerball.py<br>
      &nbsp;&nbsp;&nbsp;&nbsp;and<br>
      &nbsp;&nbsp;&nbsp;&nbsp;python3 megamillions.py<br>
# Note about updating the csv files
&nbsp;&nbsp;&nbsp;&nbsp;<b><i>---- How to update the powerball.csv ----</i></b><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Go to https://catalog.data.gov/dataset/  <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Search on megamillions then select the Title: Lottery Powerball Winning Numbers: Beginning *****<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Download the file  into your subdirectory<br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Open in your favorite spreadsheet program. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Highlight the data columns, copy to a new sheet, <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Click on the new sheet and save as powerball.csv<br>
&nbsp;&nbsp;&nbsp;&nbsp;<b><i>---- How to update the megamillions.csv ----</i></b><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Go to https://catalog.data.gov/dataset/  <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Search on megamillions then select the Title: Lottery Mega Millions Winning Numbers: Beginning *****<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Download the file  into your subdirectory<br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Open in your favorite spreadsheet program. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Highlight the data columns, copy to a new sheet, <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Click on the new sheet and save as megamillions.csv<br>


# Good luck and DO NOT BLAME ME FOR ANY LOSSES! I AM NOT RESPONSIBLE FOR YOUR ACTIONS and/or ANY LOSSES or GAINS that YOU MIGHT INCUR.
