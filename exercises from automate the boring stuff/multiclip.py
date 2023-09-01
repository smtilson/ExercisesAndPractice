#! python3
# this is supposed to be a multi-clipboard program for storing canned responses.
# this isn't working the way it should.
#the main reasons seems to be I don't know how to make a bin or exe file properly
#so maybe figure that out.
#similarly, I can't execute from the terminal because I it isn't running in the virtual environment that
# has pyperclip installed, so that is an issue.
# here are some sample responses

import pyperclip
import sys

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}


if len(sys.argv) < 2:
        print('Usage: python mclip.py [keyphrase] - copy phrase text')
        sys.exit()

keyphrase = sys.argv[1]  # first command line arg is the keyphrase
if keyphrase in TEXT:
        pyperclip.copy(TEXT[keyphrase])
        print('Text for ' + keyphrase + ' copied to clipboard.')
else:
        print('There is no text for ' + keyphrase)
