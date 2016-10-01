"""
This is the file with your answer, do not rename or move it.
Write your code in it, and save it before submitting your answer.
"""
import re
import datetime
import pytz
from collections import defaultdict

# month name => month number map
MONTH_NAME_TO_NUM = {
        'Jan': 1,
        'Feb': 2,
        'Mar': 3,
        'Apr': 4,
        'May': 5,
        'Jun': 6,
        'Jul': 7,
        'Aug': 8,
        'Sep': 9,
        'Oct': 10,
        'Nov': 11,
        'Dec': 12,
        }

# number of back-to-back requests indicative of suspicous behavior
SUSPICION_THRESHOLD = 3

# resource that's being monitored for suspicious behavior
FLAGGED_RESOURCE = '/account/transfer'

class Request:
    """
    Object to store reconstructed request data from log files
    """
    def __init__(self, entry):
        entry = entry.split()
        self.ip = entry[0]
        self.user_id = entry[2]
        self.timestamp = self.__parse_timestamp(entry[3], entry[4])
        self.http_request = {
            'type': entry[5][1:],
            'resource': entry[6],
            'protocol': entry[7]
            }
        self.status_code = entry[8]
        self.size_in_bytes = entry[9]


    def __parse_timestamp(self, time_str, timezone_str):
        """
        Converts a log-formatted timestamp into timestamp.timestamp

        Args:
            time_str (str):
                raw timestamp from log
            timezone_str (str):
                raw timezone info from log
        """
        time_str = time_str[1:]
        timezone_str = timezone_str[:-1]

        day, month, year, hour, minute, second = re.split("\/|\:", time_str)
        timezone_offset = ((int(timezone_str) / 100) * 60) + (int(timezone_str) % 100)

        timestamp = datetime.datetime(
                year=int(year),
                day=int(day),
                month=MONTH_NAME_TO_NUM[month],
                hour=int(hour),
                minute=int(minute),
                second=int(second),
                tzinfo=pytz.utc             # keep all timestamps in UTC to stay sane
            )
        # apply log timezone as offset
        return timestamp + datetime.timedelta(minutes=timezone_offset)


def comb_for_suspects(prev_failures, cur_failures, time_delta):
    """
    Examines aggregate failed requests over a 1-second timewindow for suspicious behavior

    Args:
        prev_failures ( {str => int} ):
            mapping of ip's to number of failed requests in the previous time period
        cur_failures  ( {str => int} ):
            mapping of ip's to number of failed requests in the current time period
        time_delta (datetime.timedelta):
            difference in time between cur and prev failures
    """
    if time_delta > datetime.timedelta(0, 1):
        return [ip for ip, count in cur_failures.iteritems() if count >= 3]
    else:
        return [ip for ip, count in cur_failures.iteritems() if count + prev_failures[ip] >= 3]


def find_suspicious_ips(log_path):
    """Returns a list of IP addresses that are deemed suspicious. This function 
    declaration must be kept unmodified.
    
    Args:
        log_path: The full path of a log file.
    Returns:
        A list of IP addresses.
    """
    flagged_ips = []

    log_file = open(log_path)

    # keep track of prev and current failures to allow for a flagging window of 1 second
    prev_time = None
    prev_failed_requests = defaultdict(int)
    cur_time = None
    cur_failed_requests = defaultdict(int)

    for entry in log_file:
        request = Request(entry)
        # initialize timestamps on log entry
        if cur_time is None:
            cur_time = prev_time = request.timestamp
        # if we've hit a log entry with a new timestamp, save the old failed requests/timestamps
        # and restart failure counters
        #
        # NOTE: this assums that logs are sorted by timestamp (e.g. there won't be any  out-of-order 
        #       requests in the logs. I think that's a valid assumption assuming we have some kind 
        #       of sane consistancy guarentees on our logging
        elif request.timestamp != cur_time:
            flagged_ips += [
                ip for ip in comb_for_suspects(prev_failed_requests, cur_failed_requests, cur_time - prev_time)
                if ip not in flagged_ips
                ]

            prev_failed_requests = cur_failed_requests
            prev_time = cur_time
            
            cur_failed_requests = defaultdict(int)
            cur_time = request.timestamp

        if (400 <= request.status_code or request.status_code <= 499) and request.http_request['resource'] == FLAGGED_RESOURCE:
            cur_failed_requests[request.ip] += 1
    # add in any suspects that system may not have picked up on yet
    flagged_ips += [
        ip for ip in comb_for_suspects(prev_failed_requests, cur_failed_requests, cur_time - prev_time)
        if ip not in flagged_ips
        ]

    return flagged_ips

# This tests your code with the examples given in the question, 
# and is provided only for your convenience.
if __name__ == '__main__':
    print find_suspicious_ips('example.log')
#    print find_suspicious_ips('bank_logs.log')
