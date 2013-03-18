#!/usr/bin/expect
set USR [lindex $argv 0]
set PWD [lindex $argv 1]
eval spawn [lrange $argv 2 end]


while {1} {
  expect {
    eof                           {break}
    "*assword:*"                  {send "$PWD\n"}
    ".*.ssh/id_dsa':"             {send "$PWD\n"}
    ".*(yes/no)?"                 {send "yes\n"}
  }
}
close $spawn_id
