# put your python code here
start_hour = int(input())
start_minute = int(input())
start_second = int(input())

end_hour = int(input())
end_minute = int(input())
end_second = int(input())

print((end_hour - start_hour) * 3600
      + (end_minute - start_minute) * 60
      + (end_second - start_second))