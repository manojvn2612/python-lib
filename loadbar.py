import time
import sys

def loading_bar(iterable, prefix='', length=40, fill='█', print_end='\r'):
    """
    Call in a loop to create a terminal loading bar.
    
    :param iterable: any iterable (e.g., range, list, etc.)
    :param prefix: string to be displayed before the loading bar
    :param length: length of the loading bar (number of characters in the bar)
    :param fill: character used to fill the loading bar
    :param print_end: what to print at the end (default is carriage return)
    """
    total = len(iterable)
    
    for i, item in enumerate(iterable, 1):
        percent = ("{0:.1f}").format(100 * (i / float(total)))
        filled_length = int(length * i // total)
        bar = fill * filled_length + '-' * (length - filled_length)
        sys.stdout.write(f'\r{prefix} |{bar}| {percent}% Complete')
        sys.stdout.flush()
        time.sleep(0.5)  # Simulating work being done
        
    sys.stdout.write(print_end)
    sys.stdout.flush()

# Example usage:
if __name__ == "__main__":
    items = range(100)
    loading_bar(items, prefix='Loading', length=50)
