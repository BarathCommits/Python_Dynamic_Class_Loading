class Test2:
    print('Testing Outside')

    def __init__(self):
        print('Testing Inside def!!')
        self.execute()

    def execute(self):
        print('I am executing the')

class Test1:
    print('Call Test2')


