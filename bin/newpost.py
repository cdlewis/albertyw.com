#!/usr/bin/env python3

import calendar
import datetime
import os

current_time = datetime.datetime.utcnow()

current_directory = os.path.dirname(os.path.realpath(__file__))
notes_directory = os.path.join(
    current_directory, '..', 'albertyw.com', 'notes')
note_filename = current_time.strftime('%Y%m%d-%H%M')
note_path = os.path.join(notes_directory, note_filename)
note_path = os.path.normpath(note_path)

timestamp = calendar.timegm(current_time.utctimetuple())
note = "\n%s\n\n" % timestamp

with open(note_path, 'w') as note_handle:
    note_handle.write(note)

print('Note template written to %s' % note_path)
