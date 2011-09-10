## CLMailer

A simple command line emailing, with attachments and multiple email addresses support.
Use any smtp server, preferably gmail(just easier).

#### Instructions
1. Change the user_name and user_pwd variables to your own or you can just specify them with -u "user:pass" option
2. Change the default message and subject strings in the defMessage variable
3. Attachments are seperated with commas. Absolute paths only!

#### Usage Examples
*   Mailer.py [-smf] [Email Addresses]
*   Mailer.py -s "Hey whats up man" -m "How's it going...." "mail@mail.com"
*   Mailer.py -s "Hey whats up man" -m "How's it going...." -f "file1","file2" "mail@mail.com"
*   Mailer.py -s "Hey whats up man" -m "How's it going...." -f "file1","file2" -u "user:pass" "mail@mail.com" 

#### Prerequisites
*   Python 2.7
*   Python libraries:
    -   smtplib
    -   email

Developed and tested on Windows 7 and Python 2.7.
Since it's really the simplest form (with preinstalled libraries) no reason why it shouldn't work on other OSes


#### License is GPL
Copyright (C) 2011  Shlomi Zfira  sendanalert@gmail.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.