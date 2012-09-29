###Sublime Text 2 Color Console
This will allow you to see the output of Sublime Text 2's console in a (more-or-less) unified syntax highlighting scheme based on your current theme. It's based directly off of the Python and Django standard .tmLanguage files. I've found this to help find something visually much faster, since it mirrors the code it references.

![color console](https://github.com/ehamiter/ST2-Color-Console/raw/master/console.png)

###Caveats
I've removed any references to any deprecated, illegal, or invalid flags, so as not to completely red-line a text string that may not "look" right. This still needs work-- you'll notice if it encounters a multi-line string that does not terminate, the rest of the console will be highlighted with a string's set color. Also, a few "key" words have been added to attempt to unify common phrases used in the console, i.e. "Searching X files for 'word'" highlights the keyword "for", so I've added "Searching", "files", and "case sensitive" to maintain the coloring.

###Installation
------------
Install into your ST2 Packages folder as normal.  Then run **Color Console: Enable** from the command palette.  This will create a `Widget.sublime-settings` file that changes the console syntax hilighting to the current theme.  After creation, the settings file is opened, for if you would like to change the console to a different theme.

A shortcut to edit the `Widget.sublime-settings` file is available from **Preferences ->
Package Settings -> Color Console**.


**Optional:**
Select the color for the undefined console text in your current .tmTheme:

    <dict>
       <key>name</key>
       <string>Source</string>
       <key>scope</key>
       <string>source.console</string>
       <key>settings</key>
       <dict>
          <key>fontStyle</key>
          <string></string>
          <key>foreground</key>
          <string>#C5C8C6</string><!--console's non-defined text-->
       </dict>
    </dict>


Updated Sept 2012 by Charles Phillips

MIT Licensed. Use at your own risk.