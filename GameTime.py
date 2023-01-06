from datetime import datetime


class GameTime:


    def __init__(self, label_time):
        self.label_time = label_time #  label where is time
        self.counter = 0 #  seconds
        self.running = False

        def update(self):
            if self.running:
                if self.counter == 0:
                    display = '0.00.00'
                else:
                    tt = datetime.utcfromtimestamp(self.counter)
                    string = tt.strftime('%t') #  eg %H:%M:%S
                    display = string
                self.label_time['text'] = display
                self.label_time.after(1000, self.update) # self.update without ( )'s
                self.counter += 1

    def start(self): #  Start time
        self.running = True
        self.update()

    def stop(self): # Stop time
        self.running = False

    def reset(self): #  Reset time
        self.counter = 0
        self.label_time['text'] = '0.00.00'