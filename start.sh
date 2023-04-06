if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Babukuruvila/SeriesXbot /SeriesXbot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /SeriesXbot
fi
cd /SeriesXbot
pip3 install -U -r requirements.txt
echo "Starting SeriesXbot...."
python3 bot.py
