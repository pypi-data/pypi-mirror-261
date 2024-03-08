from .source import Source

if __name__ == '__main__':
    source = Source("https://www.google.com/")
    result = source.download()
