#!/usr/bin/env osascript
-- listName, reminderText, completed
on run argv
  set listName to item 1 of argv
  set reminderText to item 2 of argv
  set isItComplete to (item 3 of argv) as boolean

  tell application "Reminders"
    tell list listName
      make new reminder with properties {name: reminderText, completed: isItComplete}
    end tell
  end tell

  set output to "Set a reminder of \"" & reminderText & "\" on list \"" & listName & "\" "
  if isItComplete then
    set output to output & "as COMPLETED"
  else
    set output to output & "as NOT COMPLETED"
  end if
end run