import glob

class Model:

    def __init__(self):
        # Eng carmodel db is hangman_words_en.db
        self.database_name = 'databases/hangman_words_ee.db'
        self.image_files = glob.glob('images/*.png')  # all hangman images
        # new game
        self.new_word = None  # random word from db
        self.user_word = []  # user found letters
        self.all_user_chars = []  # wrong letters entered
        self.counter = 0  # error counter (wrong letters)
        # Leaderboard
        self.player_name = 'UNKNOWN'  # unkown player name
        self.leaderboard_file = 'leaderboard.txt'
        self.score_data = []  # leaderboard file contents
