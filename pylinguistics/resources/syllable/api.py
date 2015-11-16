class SyllableSeparator(object):
    """This class defines the basic interface for syllable separators.
    """
    def separate(self, word):
        """Separate a word in syllables.

        Required arguments:
        word -- the word to be separated.

        Returns:
        a list of strings, each one being a syllable of the word.
        """
        raise NotImplementedError("Don't instantiate this class. " +
                                  "Use one of its subclasses instead.")

    def test(self, words_file_path, syllables_file_path,
             encoding='utf-8', verbose=True):
        """Test the accuracy of the separation method.

        Required arguments:
        words_file_path -- path to a file containing one word per line.
        syllables_file_path -- path to a file containing the same words
            of words_file_path with the syllables separated by a -.

        Keyword arguments:
        encoding -- the encoding of the words and syllables files.
        verbose -- true for detailed message printing.
        """
        import codecs
        #import re
        with codecs.open(words_file_path, encoding=encoding, mode='r')\
                as content_file,\
            codecs.open(syllables_file_path, encoding=encoding, mode='r')\
                as syllables_file:

            words = map(str.strip, content_file.readlines())
            syllables = map(str.strip, syllables_file.readlines())

            accuracy = 0.0
            nwords = 0
            for word, separation in zip(words, syllables):
                nwords = nwords + 1
                try:
                    separated_word = '-'.join(self.separate(word.strip()))
                    #separated_word = re.sub(r"\-+", "-", separated_word)

                    if separated_word != separation:
                        if verbose:
                            print(("Word '%s' incorrectly separated.\n" +
                                   "\tCorrect form: %s.\n\tReturned form: %s")
                                  % (word, separation, separated_word))
                    else:
                        accuracy = accuracy + 1
                except Exception as e:
                    if verbose:
                        print("Word '%s' generated exception: %s" % (word, e))

            accuracy = accuracy * 100 / nwords
            if verbose:
                print('Accuracy: {0:.2f}%'.format(accuracy))

            return accuracy
