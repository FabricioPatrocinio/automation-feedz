# External module
from alive_progress import alive_bar


def process_progress(number: int):
    '''Loading bar.'''

    def compute():
        for i in range(number):
            ...  # process an item
            yield  # insert this and you're done!

    with alive_bar(number) as bar:
        for i in compute():
            bar()
