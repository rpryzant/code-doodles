
#Notes because i need to get better at these types of problems...



#what actions does it need to support?
# forgot about requests! (sending, accepting, rejecting)

# what can we learn about tehse requirements?

# what are the core components of the system?
# - database, set of clients, set of servers
# - for databsae, a SQL server like SQLlite would work
#         could store user lists, chat transcripts, etc
# - if lots of data use HDFS or qfs
# - for communication, use XML
#      - XML is NOT compressed, but it's easy to understand, parse, and debug
# - server is a set of machines without single points of failure. so shard/replicate data



# things to worry bout
#  -dos attacks (clients can push data to you)
#  -scailabiltiy
#  -message ordinality for distributed threads
#  -auto signoff if user is afk?


# manages users. singleton class
class UserManager:
    self.instance
    self.usersById = {id : user}
    self.onlineUsers = {id : user}
    self.accountNameToId = {name : id}

    def getInstance(self):
    def addUser(self, ...):
    def approveAddRequest(self ...):
    def rejectAddRequest
    def userSignedOn
    def userSigenedOff


class User: 
    id, status, chats, sent requests, contacts
    
    methods for 
        -sending messages
        -setting status
        -sending and recieving (rejecting/accepting) requests
        -creating and deleting conversations

class thread:
    array (queue?) of messages
    
    methods for
        -adding messages
        -getting id, participants, messages
        
class groupchat (subclass of thread)
    remove/add participants

class chat (subclass of thread)
    get other participant

class message:
    content, date

    get content
    get date

class addRequest:
    simple class to group request data

class userStateus:
    same...type, message, get

